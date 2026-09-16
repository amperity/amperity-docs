.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        A landing page for the collection of content about the Amperity Profile API.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the collection of content about the Amperity Profile API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Profile API endpoints

==================================================
Profile API
==================================================

.. endpoints-profile-api-about-start

The Amperity Profile API provides read-only access to indexes and the profiles within them. Use these endpoints to list the indexes in your tenant and to look up individual profiles.

.. endpoints-profile-api-about-end


.. _endpoints-profile-api-indexes:

Indexes
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /indexes
      :link-type: doc
      :link: endpoint_get_profile_index

      .. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
         :start-after: .. endpoint-get-profile-index-start
         :end-before: .. endpoint-get-profile-index-end

   .. grid-item-card:: GET /indexes/{id}
      :link-type: doc
      :link: endpoint_get_profile_index_id

      .. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
         :start-after: .. endpoint-get-profile-index-id-start
         :end-before: .. endpoint-get-profile-index-id-end


.. _endpoints-profile-api-profiles:

Profiles
==================================================

.. grid:: 1 1 1 1
   :gutter: 2
   :padding: 0
   :class-container: surface

   .. grid-item-card:: GET /indexes/{id}/profiles
      :link-type: doc
      :link: endpoint_get_profiles_list

      .. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
         :start-after: .. endpoint-get-profiles-list-start
         :end-before: .. endpoint-get-profiles-list-end

   .. grid-item-card:: GET /indexes/{id}/profiles/{id}
      :link-type: doc
      :link: endpoint_get_profile

      .. include:: ../../amperity_api/source/endpoint_get_profile.rst
         :start-after: .. endpoint-get-profile-start
         :end-before: .. endpoint-get-profile-end
