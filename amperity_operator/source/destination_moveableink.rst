.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Moveable Ink


.. meta::
    :description lang=en:
        Use Moveable Ink to design dynamic creative for personalized content experiences that combine business logic with access to real-time customer profiles.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use Moveable Ink to design dynamic creative for personalized content experiences that combine business logic with access to real-time customer profiles.

.. meta::
    :content class=swiftype name=title data-type=string:
        Make profiles available to Moveable Ink

==================================================
Real-time datasets in Moveable Ink Studio
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-moveable-ink-start
   :end-before: .. term-moveable-ink-end

.. destination-moveableink-intro-start

.. TODO: No inclusions. This is shared into the Profile API reference also.

Use the Profile API to make real-time customer profile data available to Moveable Ink Studio. Moveable Ink Studio helps your brand scale 1:1 content personalization by automatically transforming data into personalized content unique to each customer at the moment of engagement.

Combine the Profile API with Moveable Ink Studio to design campaigns and customer interactions that access the most current customer profile details and generate personalized content at scale.

* Automatically transform data into unique composite images for each customer in real-time
* Streamline steps in onboarding processes
* Personalize monthly recaps and year-in-review use cases with real-time customer data
* Target or segment creative based on profile attributes
* Create long-lasting loyalty experiences for your customers

.. destination-moveableink-intro-end


.. _destination-moveableink-get-details:

Get details
==================================================

.. destination-moveableink-get-details-start

Review the following details before configuring Profile API endpoints for use with |destination-name|. The Profile API endpoint must be available before the integration can be configured in |destination-name|.

.. destination-moveableink-get-details-end

.. destination-moveableink-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **To configure Profile API endpoints in Amperity**

       * :ref:`Build a query <destination-moveableink-configure-profile-api-query>`
       * :ref:`Add an API key for Moveable Ink <destination-moveableink-configure-profile-api-key>`
       * :ref:`Generate an access token <destination-moveableink-configure-profile-api-token>`
       * :ref:`Add the Profile API index <destination-moveableink-configure-profile-api-index>`
       * :ref:`Copy the profile ID field <destination-moveableink-configure-profile-id-field>`
       * :ref:`Copy the index ID <destination-moveableink-configure-profile-api-index-id>`
       * :ref:`Generate the endpoint <destination-moveableink-configure-profile-api-generate>`
       * :ref:`Copy the tenant ID <destination-moveableink-configure-profile-api-tenant>`


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **To configure MoveableInk**

       A user with access to |destination-name| and who is assigned to the **Manager** role is required to configure the Amperity integration with |destination-name|.

       :ref:`Log in to Moveable Ink and finish the steps <destination-moveableink-configure>` that are required for this integration.

.. destination-moveableink-get-details-table-end


.. _destination-moveableink-configure-profile-api-query:

Build a query
==================================================

.. destination-moveableink-configure-profile-api-query-start

Use the **Query Editor** to build a query that returns customer profiles for use in |destination-name| Studio.

.. destination-moveableink-configure-profile-api-query-end


.. _destination-moveableink-configure-profile-api-key:

Add an API key
==================================================

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-add-profile-start
   :end-before: .. api-keys-api-token-add-profile-end


.. _destination-moveableink-configure-profile-api-token:

Generate an access token
==================================================

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-generate-start
   :end-before: .. api-keys-access-tokens-generate-end


.. _destination-moveableink-configure-profile-api-index:

Add the Profile API index
==================================================

.. api-profile-add-index-start

An index must be defined for each query that is used to generate an endpoint for the Profile API.

.. api-profile-add-index-end

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-howitworks-indexes-start
   :end-before: .. profile-api-howitworks-indexes-end


.. _destination-moveableink-configure-profile-id-field:

Copy the profile ID field
==================================================

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-howitworks-profile-id-field-start
   :end-before: .. profile-api-howitworks-profile-id-field-end

**Verify the list of filter fields**

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-howitworks-filter-fields-start
   :end-before: .. profile-api-howitworks-filter-fields-end


.. _destination-moveableink-configure-profile-api-index-id:

Copy the index ID
==================================================

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-howitworks-index-ids-start
   :end-before: .. profile-api-howitworks-index-ids-end


.. _destination-moveableink-configure-profile-api-generate:

Generate the endpoint
==================================================

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-enable-copy-tenant-id-start
   :end-before: .. profile-api-enable-copy-tenant-id-end


.. _destination-moveableink-configure-profile-api-tenant:

Copy the tenant ID
==================================================

.. include:: ../../amperity_operator/source/api_profile.rst
   :start-after: .. profile-api-enable-copy-tenant-id-start
   :end-before: .. profile-api-enable-copy-tenant-id-end


.. _destination-moveableink-configure:

Configure Moveable Ink Studio
==================================================

.. destination-moveableink-configure-start

After Amperity is configured with a query that makes results available from a Profile API endpoint you can configure Moveable Ink to connect to that endpoint. The user who configures the integration must be assigned to the **Manager** role in Moveable Ink Studio.

**To add the Amperity integration to Moveable Ink Studio**

.. list-table::
   :widths: 12 88
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Log in to Moveable Ink.

       Expand **Data** and open the **Integrations Gallery**.

       Browse the integrations and choose **Amperity**. Click **Connect** to enable the **Profile API** integration.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - The following settings are required to configure a connection between Moveable Ink Studio and a Profile API endpoint:

       **Integration name**

       The name of the integration. For example: "Amperity customer profiels".

       **Bearer token**

       A :ref:`bearer token <destination-moveableink-configure-profile-api-token>` allows Moveable Ink Studio access to Profile API endpoints.

       **Tenant subdomain**

       The subdomain is part of the URL for your Amperity tenant. For example, "socktown":

       .. code-block:: none

          https://socktown.amperity.com/

       **Index ID**

       The index ID is a unique ID for each Profile API endpoint to which Moveable Ink Studio will make requests. For example: "ix-2BmokYMVR". This value can be copied from the Amperity user interface :ref:`after the Profile API endpoint has been created <destination-moveableink-configure-profile-api-index-id>`.

       **User ID**

       The user ID is a field within the Profile API index that is configured as the :ref:`profile ID field <destination-moveableink-configure-profile-id-field>`.

       **Tenant ID**

       The tenant ID is the :ref:`unique ID for your Amperity tenant <destination-moveableink-configure-profile-api-tenant>`.

       When the settings are added correctly the Moveable Ink Studio user interface will display a successful connection with a 200 OK response.

       .. image:: ../../images/moveable-ink-connection.png
          :width: 500 px
          :alt: Configure Moveable Ink to connect to an Amperity Profile API endpoint.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Click **Next** and configure how the fields in the Profile API index should be shown within Moveable Ink Studio.

       .. image:: ../../images/moveable-ink-datafields.png
          :width: 500 px
          :alt: Configure how fields in an Amperity Profile API endpoint are shown to users in Moveabile Ink Studio.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Click **Save**. The integration is added to the list of active integrations and is available for use within Moveable Ink Studio.

.. destination-moveableink-configure-end
