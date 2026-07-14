.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        A landing page for the collection of content about the Amperity Real-time Events API.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the collection of content about the Amperity Real-time Events API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Real-time Events API endpoints

==================================================
Real-time Events API
==================================================

.. endpoints-realtime-events-about-start

Use the Real-time Events API to send customer events, such as page views, purchases, and loyalty actions, directly into an Amperity event stream. Events are processed in real time and can trigger identity resolution, profile updates, and downstream activation.

.. endpoints-realtime-events-about-end

.. note:: The Real-time Events API is an unstable API. Its endpoints do not require an ``api-version`` header, may change, and are offered without a guarantee of support or advance notice of breaking changes.

.. note:: Setting up an event stream is not a self-service API operation. To set up a profile store and its event streams, contact your Amperity representative.


.. _endpoints-realtime-events-events:

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
