.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A profile collection turns inbound events into per-customer real-time profiles that you can read at request time.

.. meta::
    :content class=swiftype name=body data-type=text:
        A profile collection turns inbound events into per-customer real-time profiles that you can read at request time.

.. meta::
    :content class=swiftype name=title data-type=string:
        About profile collections and real-time profiles

==================================================
About profile collections and real-time profiles
==================================================

.. real-time-profiles-overview-start

A **profile collection** is where inbound events become per-customer state. A collection subscribes to :ref:`event streams <e-event-stream>`, resolves each event to a customer, and maintains a **real-time profile** for that customer: a set of attributes, keyed by a profile ID, that you can read back at request time. Profile collections and their profiles are the read side of the real-time pipeline--the audiences you build with :ref:`real-time segments <r-real-time-segment>` and act on with :ref:`real-time journeys <r-real-time-journey>` all read from them.

.. real-time-profiles-overview-end


.. include:: ../../amperity_reference/source/profiles.rst
   :start-after: .. profiles-intro-start
   :end-before: .. profiles-intro-end


.. _real-time-profiles-collections:

Profile collections
==================================================

.. real-time-profiles-collections-start

A profile collection is defined by:

* A **name** and title that identify the collection.
* A bound **identity graph**. The collection resolves customers against a :doc:`Stitch <page_stitch>` identity graph, which is what lets an inbound event's identifier map to a stitched customer.
* A set of **subscribed event streams**. The events on these streams are what update the collection's profiles.
* A set of **linking keys**, in priority order, that the collection uses to resolve an inbound event to a profile.
* A set of **attribute** definitions that every profile in the collection carries.

.. real-time-profiles-collections-end


.. _real-time-profiles-profiles:

Real-time profiles
==================================================

.. real-time-profiles-profiles-start

A real-time profile is the per-customer record a collection maintains. Each profile belongs to a tenant and a collection, is identified by its **profile ID**, and holds:

* The profile's **attributes**--the known, aggregated, and computed values the collection defines.
* The profile's **keychain**--the linking-key values that resolve to this profile.

As events arrive on the collection's subscribed streams, Amperity updates the matching profile's attributes in place, so a read of the profile reflects the customer's most recent recognized activity.

.. real-time-profiles-profiles-end


.. _real-time-profiles-profile-id:

Profile ID
==================================================

.. real-time-profiles-profile-id-start

Every real-time profile is keyed by a profile ID. The profile ID is the :ref:`Amperity ID <a-amperity-id>`--the stitched identifier that represents all of the records Amperity has resolved to a single customer. Because a collection keys profiles by the Amperity ID, each profile corresponds to one stitched customer, and the identifiers a customer is known by all resolve to that one profile.

.. real-time-profiles-profile-id-end

.. TODO: verify with <eng> -- the collection :profile-id is pinned to "amperity_id" (profile-rama/config.clj:731-733, ";; TODO: prototyping legacy, remove this special-casing"). Confirm no per-collection profile-id override ships before generalizing this wording (NC9).


.. _real-time-profiles-keychain:

Keychain and identity ordering
==================================================

.. real-time-profiles-keychain-start

A collection's linking keys form a :ref:`keychain <k-keychain>`: the key identifiers, in priority order, that map an inbound identifier to a profile. When Amperity resolves an event, it walks the keychain in priority order and returns the first profile a key resolves to. A keychain entry maps a linking-key value to a single Amperity ID; a value that would map to more than one Amperity ID is left out of the keychain rather than resolved ambiguously.

The keychain here is the collection-side view: the ordered keys a collection resolves against. How the keychain is built from Stitch outputs, and how an inbound event is recognized as a stitched customer end to end, is covered in real-time identity recognition.

.. real-time-profiles-keychain-end


.. _real-time-profiles-attributes:

Attributes
==================================================

.. real-time-profiles-attributes-start

A collection defines the attributes its profiles carry. Beyond known values brought in from customer 360 tables, two kinds of attribute are computed from a profile's real-time events:

* **Aggregate attributes** summarize a profile's events--a count, a sum, a maximum, the most recent value, and so on. Each aggregate declares a **scope** that determines which events it summarizes: a specific event type, every event on a stream, or all of the profile's events.
* **Computed attributes** derive a value from a profile's other attributes using an expression.

Both kinds are written in :doc:`Amperity's expression language <expressions>`, where the full set of functions--including the array functions used to work with event collections--is documented.

.. real-time-profiles-attributes-end


.. _real-time-profiles-inspect:

Inspect a profile
==================================================

.. real-time-profiles-inspect-start

To see what Amperity knows about a customer in real time, look up their profile by one of its identifiers--a linking-key value such as an email address. The lookup resolves the identifier through the collection's keychain to a profile and returns that profile's attributes and keychain.

A lookup behaves differently depending on whether the profile exists:

* If the identifier does not resolve to a profile, the lookup returns nothing--the profile is absent.
* If it resolves, the profile returns its full set of collection-defined attributes. Attributes that have not yet computed a value are filled with their defaults, so such an attribute reads as an empty or default value rather than being absent.

A profile's :ref:`real-time segment <r-real-time-segment>` memberships, and a collection's stats and history, are available through their own reads. Look up profiles programmatically through the `Real-time API <../api/endpoints_realtime.html>`__ or Amperity's `MCP tools <../api/mcp_tool_reference.html>`__.

.. real-time-profiles-inspect-end
