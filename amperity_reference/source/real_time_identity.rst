.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Real-time identity recognition resolves an inbound event's identifier to the stitched customer it belongs to.

.. meta::
    :content class=swiftype name=body data-type=text:
        Real-time identity recognition resolves an inbound event's identifier to the stitched customer it belongs to.

.. meta::
    :content class=swiftype name=title data-type=string:
        About real-time identity recognition

==================================================
About real-time identity recognition
==================================================

.. real-time-identity-overview-start

Real-time identity recognition is how Amperity decides *which customer* an inbound event belongs to. When an event arrives carrying an identifier--an email address, a loyalty ID, a device identifier--Amperity resolves that identifier to the stitched customer it represents and updates that customer's :doc:`real-time profile <real_time_profiles>`. Recognition is what connects an anonymous-looking event to the unified customer Amperity already knows.

.. real-time-identity-overview-end


.. _real-time-identity-two-kinds:

Two kinds of recognition
==================================================

.. real-time-identity-two-kinds-start

An inbound event goes through two distinct recognitions; keep them separate:

* **Event-type recognition** decides *what kind of event* a payload is, so that Amperity can apply the right event type and coerce the event's fields.
* **Identity recognition** decides *which customer* the event belongs to, by resolving the event's identifiers to a stitched customer.

This page is about the second. Event-type recognition is covered in :doc:`About event streams and event types <event_streams>`.

.. real-time-identity-two-kinds-end


.. _real-time-identity-chain:

From an inbound event to a stitched customer
==================================================

.. real-time-identity-chain-start

Once an event has been recognized as a type and coerced, Amperity resolves it to a customer:

#. **Extract the linking keys.** Amperity reads the event's linking keys--the fields the event type designates as identifiers, such as an email address.
#. **Route to collections.** The event is routed to the :ref:`profile collections <p-profile-collection>` that subscribe to its stream.
#. **Resolve to a profile.** Within each collection, Amperity resolves the linking keys against the collection's :ref:`keychain <real-time-profiles-keychain>`, in priority order, to at most one profile. That profile is keyed by the customer's :ref:`Amperity ID <a-amperity-id>`.
#. **Update the profile.** The event updates the attributes of the profile it resolved to.

The result is that an event arriving with, say, an email address updates the single stitched customer that email belongs to, without the sender needing to know that customer's Amperity ID.

.. real-time-identity-chain-end

.. TODO: verify with <eng> -- the profile is keyed by the Amperity ID because the collection :profile-id is pinned to "amperity_id" (profile-rama/config.clj:731-733). Revisit if a per-collection profile-id override ships (NC9).


.. _real-time-identity-keychain-lookup:

The keychain is a lookup, not live stitching
==================================================

.. real-time-identity-keychain-lookup-start

Real-time recognition does not re-run :doc:`Stitch <page_stitch>` on each event. It is a lookup against a **keychain that is materialized from Stitch's output**. Stitch resolves your customer records into stitched customers, each identified by an Amperity ID; the keychain is built from that output, mapping each linking-key value to the single Amperity ID it resolves to. A value that Stitch associates with more than one Amperity ID is left out of the keychain rather than resolved ambiguously.

After each Stitch run, Amperity applies the changes in Stitch's output to the keychain, so that newly stitched identities become recognizable in real time. Between runs, the keychain also grows in real time as events arrive, as described in the next section.

.. real-time-identity-keychain-lookup-end


.. _real-time-identity-real-time:

Identity changes in real time
==================================================

.. real-time-identity-real-time-start

Recognition does not wait for the next Stitch run to learn about new customers and identifiers. As events arrive, Amperity updates identity in real time:

* **New profiles.** When an event's identifiers match nothing in the keychain--a first-time visitor, or a customer Stitch has not seen--Amperity assigns a new Amperity ID and creates a profile for it within seconds, so that the activity is not lost and the visitor can be recognized on their next event.
* **New identifiers.** When an event resolves to a known profile and also carries an identifier that is not yet in the keychain--a new device, a second email address--Amperity adds that identifier to the profile's keychain.
* **Anonymous to known.** When an event links an anonymous profile to a known customer--for example, a login event that carries both a cookie ID and an email address--Amperity merges the anonymous profile's history into the known customer's profile.

.. real-time-identity-real-time-end


.. _real-time-identity-stitch:

Real-time identity and Stitch
==================================================

.. real-time-identity-stitch-start

Real-time identity and Stitch keep each other up to date:

* **Events feed Stitch.** Every event type is saved to a table in your tenant's events dataset. Stitch reads those tables as source data, so identifiers seen in real-time events take part in identity resolution on the next Stitch run. The identifiers of profiles created in real time also flow back to Stitch, which keeps their Amperity IDs.
* **Stitch corrects real time.** When a Stitch run merges, splits, adds, or removes customers, Amperity applies those changes to every affected profile collection: it recalculates the affected profiles' attributes from their full event history and re-evaluates their segment membership.

Real-time profiles are always the best available answer, and each Stitch run trues them up. Expect some Amperity IDs to change between runs as Stitch refines its results.

.. real-time-identity-stitch-end

.. TODO: verify with <eng> -- whether real-time anonymous-to-known merges are sent back to Stitch. Per the feature context, merge feedback to Stitch is off by default, so the batch identity graph reflects a merge only when Stitch reaches the same conclusion from the underlying data. Do not state that real-time merges update Stitch until confirmed.
