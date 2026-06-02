.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Stream events to Amperity and look up unified customer profiles using the Events API and Profile API v3.

.. meta::
    :content class=swiftype name=body data-type=text:
        Stream events to Amperity and look up unified customer profiles using the Events API and Profile API v3.

.. meta::
    :content class=swiftype name=title data-type=string:
        Real-time APIs


==================================================
Real-time APIs
==================================================

.. start-here-start

The Amperity real-time APIs enable event ingest and customer profile lookup at any touchpoint. Use the Events API to stream behavioral and transactional events from any upstream source. Use the Profile API v3 to look up a unified customer profile on demand using an identity key such as an email address or loyalty ID.

.. start-here-end


.. toctree::
   :caption: KEY CONCEPTS
   :maxdepth: 2
   :hidden:

   Identity recognition <identity_recognition>


.. toctree::
   :caption: USE CASES
   :maxdepth: 2
   :hidden:

   Anonymous-to-known <anonymous_to_known>


.. toctree::
   :caption: ABOUT THE APIs
   :maxdepth: 2
   :hidden:

   Overview <overview>
   Versioning <versioning>
   Authentication <authentication>
   Base URL <base_url>
   Requests <requests>
   Responses <responses>
   Pagination <pagination>
   Rate limits <rate_limits>
   Changelog <changelog>


.. toctree::
   :caption: EVENTS API ENDPOINTS
   :maxdepth: 2
   :hidden:

   GET /streams/{stream-id}/sample-events <endpoint_get_streams_streamid_sample_events>
   POST /events/{stream-id} <endpoint_post_events_streamid>
   Amperity expression language <ael>
   OpenAPI specification <https://docs.amperity.com/realtime/openapi-events.html>


.. toctree::
   :caption: PROFILE API V3 ENDPOINTS
   :maxdepth: 2
   :hidden:

   GET /collections/{collection-id}/stats <endpoint_get_collections_collection_stats>
   GET /lookup/{collection-id}/keychain <endpoint_get_lookup_collection_keychain>
   POST /lookup/{collection-id}/keychain <endpoint_post_lookup_collection_keychain>
   GET /profiles/{collection-id}/{profile-id} <endpoint_get_profiles_collection_profile>
   GET /profiles/{collection-id}/{profile-id}/segments <endpoint_get_profile_collection_profile_segments>
   GET /segments/{segment-id}/profiles <endpoint_get_segments_id_profiles>
   OpenAPI specification <https://docs.amperity.com/realtime/openapi-profile-v3.html>


.. toctree::
   :caption: MORE RESOURCES
   :hidden:

   Help Center <https://help.amperity.com>
   Learning Lab <https://amperity.com/learning-lab>
   System Status <https://status.amperity.com>
   Amperity.com <https://www.amperity.com>
