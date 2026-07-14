.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        A landing page for the collection of content about the Amperity Real-time API.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the collection of content about the Amperity Real-time API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Real-time API endpoints

==================================================
Real-time API
==================================================

.. endpoints-realtime-about-start

Use the Real-time API to stream customer events into Amperity and to look up unified customer profiles on demand. Send events, such as page views, purchases, and loyalty actions, to an event stream, then look up profiles by identity key, retrieve profiles by ID, query segment membership, and retrieve profile store statistics. The Real-time API supports low-latency use cases such as personalization, decisioning, and in-session activation.

.. endpoints-realtime-about-end

.. note:: The Real-time API is an unstable API. Its endpoints do not require an ``api-version`` header, may change, and are offered without a guarantee of support or advance notice of breaking changes.

.. note:: Creating a profile store is not a self-service API operation. To set up a profile store, an event stream, or a real-time segment, contact your Amperity representative.


.. _endpoints-realtime-events:

Events
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: POST /events/{stream-id}
      :link-type: doc
      :link: endpoint_post_profile_store_events

      .. include:: ../../amperity_api/source/endpoint_post_profile_store_events.rst
         :start-after: .. endpoint-post-profile-store-events-start
         :end-before: .. endpoint-post-profile-store-events-end


.. _endpoints-realtime-lookup:

Lookup
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /lookup/{collection-id}/keychain
      :link-type: doc
      :link: endpoint_get_profile_store_lookup

      .. include:: ../../amperity_api/source/endpoint_get_profile_store_lookup.rst
         :start-after: .. endpoint-get-profile-store-lookup-start
         :end-before: .. endpoint-get-profile-store-lookup-end

   .. grid-item-card:: POST /lookup/{collection-id}/keychain
      :link-type: doc
      :link: endpoint_post_profile_store_lookup

      .. include:: ../../amperity_api/source/endpoint_post_profile_store_lookup.rst
         :start-after: .. endpoint-post-profile-store-lookup-start
         :end-before: .. endpoint-post-profile-store-lookup-end


.. _endpoints-realtime-profiles:

Profiles
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /profiles/{collection-id}/{profile-id}
      :link-type: doc
      :link: endpoint_get_profile_store_profile

      .. include:: ../../amperity_api/source/endpoint_get_profile_store_profile.rst
         :start-after: .. endpoint-get-profile-store-profile-start
         :end-before: .. endpoint-get-profile-store-profile-end


.. _endpoints-realtime-segments:

Segments
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /segments/{segment-id}/profiles
      :link-type: doc
      :link: endpoint_get_profile_store_segment_profiles

      .. include:: ../../amperity_api/source/endpoint_get_profile_store_segment_profiles.rst
         :start-after: .. endpoint-get-profile-store-segment-profiles-start
         :end-before: .. endpoint-get-profile-store-segment-profiles-end


.. _endpoints-realtime-profile-stores:

Profile stores
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /collections/{collection-id}/stats
      :link-type: doc
      :link: endpoint_get_profile_store_stats

      .. include:: ../../amperity_api/source/endpoint_get_profile_store_stats.rst
         :start-after: .. endpoint-get-profile-store-stats-start
         :end-before: .. endpoint-get-profile-store-stats-end

   .. grid-item-card:: GET /collections/{collection-id}/history
      :link-type: doc
      :link: endpoint_get_profile_store_history

      .. include:: ../../amperity_api/source/endpoint_get_profile_store_history.rst
         :start-after: .. endpoint-get-profile-store-history-start
         :end-before: .. endpoint-get-profile-store-history-end
