.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The real-time suite recognizes customers and reacts to their behavior as it happens, from an inbound event to an activated journey.

.. meta::
    :content class=swiftype name=body data-type=text:
        The real-time suite recognizes customers and reacts to their behavior as it happens, from an inbound event to an activated journey.

.. meta::
    :content class=swiftype name=title data-type=string:
        About real-time

==================================================
About real-time
==================================================

.. real-time-overview-start

Amperity's real-time suite recognizes your customers and reacts to their behavior as it happens. Inbound events flow through a pipeline of objects--from an event arriving on a stream, to the profile it updates, to the always-on audiences and journeys that act on it--so that your brand can respond to a customer in the moment rather than on a batch schedule.

.. real-time-overview-end


.. _real-time-pipeline:

The real-time pipeline
==================================================

.. real-time-pipeline-start

Data moves through the real-time suite in a fixed flow:

#. **Event streams and event types.** Customer events arrive on an :doc:`event stream <event_streams>`. The stream recognizes each event's :doc:`event type <event_streams>` and coerces its fields into a typed record.
#. **Identity recognition.** Amperity resolves the event's identifiers to the stitched customer they belong to, so the event updates the right person. See :doc:`real-time identity recognition <real_time_identity>`.
#. **Profile collections.** The event updates a :doc:`real-time profile <real_time_profiles>` in a profile collection--a per-customer record of attributes, keyed by the customer's Amperity ID.
#. **Attributes.** The collection maintains aggregate and computed :doc:`attributes <real_time_profiles>` from the profile's events, written in :doc:`Amperity's expression language <expressions>`.
#. **Real-time segments.** An always-on :doc:`real-time segment <real_time_segments>` continuously evaluates a predicate over the collection's profiles; a profile enters or exits the segment as its attributes change.
#. **Real-time journeys.** A :doc:`real-time journey <real_time_journeys>` that travelers enter by segment membership drives activations in real time--sending to a :doc:`destination <page_destinations>`--and records each traveler's path in a travel log.

.. real-time-pipeline-end

.. TODO: verify with <eng> -- the profile is keyed by the Amperity ID because the collection :profile-id is pinned to "amperity_id" (profile-rama/config.clj:731-733). Revisit if a per-collection profile-id override ships (NC9).

.. TODO: verify with Shawn -- the overview frames journey entry as real-time segment membership (the supported path). Event-triggered entry is built in the backend but not user-authorable (AMP-1633); per Q2 it is modeled as a segment with no availability label. Confirm this high-level framing.


.. _real-time-sandboxes:

Real-time in a sandbox
==================================================

.. real-time-sandboxes-start

Real-time features are inert by default in a :doc:`sandbox <sandboxes>`, so that you can build and test without sending live messages:

* **Real-time journeys do not send.** A real-time journey is off in a sandbox until you turn it on, so a sandbox journey does not activate to a destination on its own.
* **Profile collections do not run on a schedule.** Only an active collection runs automatically; in a sandbox you run a collection explicitly to test it.

.. real-time-sandboxes-end

.. TODO: verify with <eng> -- whether a sandbox automatically makes its event streams stop accepting events on creation. Stream auto-inert-on-sandbox-creation was not present in /app at discovery HEAD (NC4); the journeys/collections inert-by-default behavior is confirmed. Do not state that a sandbox's streams reject events by default until confirmed.


.. _real-time-api:

The Real-time API
==================================================

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-realtime-start
   :end-before: .. api-realtime-end
