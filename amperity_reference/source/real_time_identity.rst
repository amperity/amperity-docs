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

Because recognition is a lookup against this materialized keychain, a customer is recognized in real time only once their identifiers are present in the keychain. A newly stitched identity is not recognizable in real time until the keychain reflects it.

.. real-time-identity-keychain-lookup-end

.. TODO: verify with <eng> -- when/how the keychain materialization task is (re)built and loaded into the live index (on Stitch completion? scheduled? on demand?), which determines the recognition latency between a newly stitched identity and real-time recognition (task/keychain.clj, keychain/sql.clj, link/sync.clj). Do not state a refresh cadence or a latency figure until confirmed (NC1).


.. _real-time-identity-anonymous:

Anonymous events and reconciliation
==================================================

.. real-time-identity-anonymous-start

When an event carries an identifier that is not in the keychain--a first-time visitor, or an identity Stitch has not yet resolved--the event cannot be resolved to a stitched customer. Amperity treats the event as anonymous and can provision a profile for it just in time, so that the activity is not lost.

Once that identifier becomes part of the stitched graph, later events that carry it resolve to the customer's stitched profile.

.. real-time-identity-anonymous-end

.. TODO: verify with <eng> -- the detail of how and when an anonymous (unclaimed/unlinked) profile's already-collected activity is reconciled into the stitched profile once the identifier appears in Stitch (auger.merge/resolve-profile-id>, auger.clj:217-261,250-261). Do not describe the merge/reconciliation mechanics until confirmed (NC2).
