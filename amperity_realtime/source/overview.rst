.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        The Amperity Real-time APIs provide programmatic access to event streams and real-time customer profiles.

.. meta::
    :content class=swiftype name=body data-type=text:
        The Amperity Real-time APIs provide programmatic access to event streams and real-time customer profiles.

.. meta::
    :content class=swiftype name=title data-type=string:
        Overview

==================================================
About real-time APIs
==================================================

.. api-amperity-start

The Amperity real-time APIs provide programmatic access to event streams and real-time customer profiles in your Amperity tenant. Two APIs are available.

* :doc:`Versioning <versioning>`
* :doc:`Authentication <authentication>`
* :doc:`Base URL <base_url>`
* :doc:`Requests <requests>`
* :doc:`Responses <responses>`
* :doc:`Pagination <pagination>`
* :doc:`Rate limits <rate_limits>`

.. api-amperity-end


.. _overview-events-api:

Events API
==================================================

.. overview-events-api-start

Use the Events API to send customer events—page views, purchases, loyalty actions, and other behavioral signals—directly into an Amperity event stream. Events are processed in real time and can trigger identity resolution, profile updates, and downstream activation.

* :doc:`GET /streams/{stream-id}/sample-events <endpoint_get_streams_streamid_sample_events>`
* :doc:`POST /events/{stream-id} <endpoint_post_events_streamid>`
* :doc:`Amperity expression language <ael>`
* `OpenAPI specification <https://docs.amperity.com/realtime/openapi-events.html>`__

.. overview-events-api-end


.. _overview-profile-api-v3:

Profile API v3
==================================================

.. overview-profile-api-v3-start

Use the Profile API v3 to look up real-time customer profiles, query segment membership, and retrieve collection statistics. Profile lookups return live data from the profile store and support low-latency use cases such as personalization, decisioning, and in-session activation.

* :doc:`GET /collections/{collection-id}/stats <endpoint_get_collections_collection_stats>`
* :doc:`GET /lookup/{collection-id}/keychain <endpoint_get_lookup_collection_keychain>`
* :doc:`POST /lookup/{collection-id}/keychain <endpoint_post_lookup_collection_keychain>`
* :doc:`GET /profiles/{collection-id}/{profile-id} <endpoint_get_profiles_collection_profile>`
* :doc:`GET /profiles/{collection-id}/{profile-id}/segments <endpoint_get_profile_collection_profile_segments>`
* :doc:`GET /segments/{segment-id}/profiles <endpoint_get_segments_id_profiles>`
* `OpenAPI specification <https://docs.amperity.com/realtime/openapi-profile-v3.html>`__

.. overview-profile-api-v3-end
