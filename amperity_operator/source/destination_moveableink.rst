.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Movable Ink


.. meta::
    :description lang=en:
        Use Movable Ink to design dynamic creative for personalized content experiences that combine business logic with access to real-time customer profiles.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use Movable Ink to design dynamic creative for personalized content experiences that combine business logic with access to real-time customer profiles.

.. meta::
    :content class=swiftype name=title data-type=string:
        Make profiles available to Movable Ink

==================================================
Real-time datasets in Movable Ink Studio
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-moveable-ink-start
   :end-before: .. term-moveable-ink-end

.. destination-moveableink-intro-start

.. TODO: No inclusions. This is shared into the Database Profile API reference also.

Use the `Database Profile API <explorer-database-profile-api_>`__ to make real-time customer profile data available to Movable Ink Studio. Movable Ink Studio helps your brand scale 1:1 content personalization by automatically transforming data into personalized content unique to each customer at the moment of engagement.

Combine the `Database Profile API <explorer-database-profile-api_>`__ with Movable Ink Studio to design campaigns and customer interactions that access the most current customer profile details and generate personalized content at scale.

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

Review the following details before configuring `Database Profile API <explorer-database-profile-api_>`__ endpoints for use with |destination-name|. The `Database Profile API <explorer-database-profile-api_>`__ endpoint must be available before the integration can be configured in |destination-name|.

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
     - **To configure Database Profile API endpoints in Amperity**

       * :ref:`Build a query <destination-moveableink-configure-profile-api-query>`
       * :ref:`Add an API key for Movable Ink <destination-moveableink-configure-profile-api-key>`
       * :ref:`Generate an access token <destination-moveableink-configure-profile-api-token>`
       * :ref:`Add the Database Profile API index <destination-moveableink-configure-profile-api-index>`
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

       :ref:`Log in to Movable Ink and finish the steps <destination-moveableink-configure>` that are required for this integration.

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

An API key enables your downstream use cases to read data from the `Database Profile API <explorer-database-profile-api_>`__.

**To add an API key for the Database Profile API**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab. Under **API keys** click **Add API key**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - From the **Add API key** dialog, add the name for the API key, select the **Profile API Data Access** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-profile.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link


.. _destination-moveableink-configure-profile-api-token:

Generate an access token
==================================================

Access tokens that enable authentication to Amperity APIs are managed directly from the **Settings** page in Amperity.

**To generate access tokens**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Under **API keys** find the API key for which you want to generate an access token, and then from the **Actions** menu select **Get token**.

       .. image:: ../../images/api-keys-generate-access-token.png
          :width: 500 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Select the number of days this token allows access to the API, after which it will expire. For example, 3 days:

       .. image:: ../../images/api-keys-set-token-expiration.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       Use the **Rotate key secret** option to rotate an existing secret when generating an access token. This will force all previously provisioned tokens that are associated with the current API key to expire in 30 days.

       Click **Generate token**. The token is generated, and then is automatically copied to your clipboard.

       .. image:: ../../images/api-keys-token-saved-to-clipboard.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       .. important:: You are the only person who have access to the newly generated access key. Amperity does not save the access key anywhere and it will disappear when you close this dialog. Store the access key in a safe place.


.. _destination-moveableink-configure-profile-api-index:

Add the Database Profile API index
==================================================

.. api-profile-add-index-start

An index must be defined for each query that is used to generate an endpoint for the `Database Profile API <explorer-database-profile-api_>`__.

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

Filter fields are defined in the query that builds the index, and each filter field has the same name as its field in that query. For how requests filter on them, see the `Database Profile API reference <explorer-database-profile-api_>`__.


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

Configure Movable Ink Studio
==================================================

.. destination-moveableink-configure-start

After Amperity is configured with a query that makes results available from a `Database Profile API <explorer-database-profile-api_>`__ endpoint you can configure Movable Ink to connect to that endpoint. The user who configures the integration must be assigned to the **Manager** role in Movable Ink Studio.

**To add the Amperity integration to Movable Ink Studio**

.. list-table::
   :widths: 12 88
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Log in to Movable Ink.

       Expand **Data** and open the **Integrations Gallery**.

       Browse the integrations and choose **Amperity**. Click **Connect** to enable the **Profile API** integration.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - The following settings are required to configure a connection between Movable Ink Studio and a `Database Profile API <explorer-database-profile-api_>`__ endpoint:

       **Integration name**

          The name of the integration. For example: "Amperity customer profiels".

       **Bearer token**

          A :ref:`bearer token <destination-moveableink-configure-profile-api-token>` allows Movable Ink Studio access to `Database Profile API <explorer-database-profile-api_>`__ endpoints.

       **Tenant subdomain**

          The subdomain is part of the URL of your Amperity tenant. For example, "socktown":

          .. code-block:: none

             https://socktown.amperity.com/

       **Index ID**

          The index ID is a unique ID for each `Database Profile API <explorer-database-profile-api_>`__ endpoint to which Movable Ink Studio will make requests. For example: ``ix-2BmokYMVR``. This value can be copied from the Amperity user interface :ref:`after the Database Profile API endpoint has been created <destination-moveableink-configure-profile-api-index-id>`.

       **User ID**

          The user ID is a field within the `Database Profile API <explorer-database-profile-api_>`__ index that is configured as the :ref:`profile ID field <destination-moveableink-configure-profile-id-field>`.

       **Tenant ID**

          The tenant ID is the :ref:`unique ID for your Amperity tenant <destination-moveableink-configure-profile-api-tenant>`.

       When the settings are added correctly the Movable Ink Studio user interface will display a successful connection with a 200 OK response.

       .. image:: ../../images/moveable-ink-connection.png
          :width: 500 px
          :alt: Configure Movable Ink to connect to an Database Profile API endpoint.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Click **Next** and configure how the fields in the `Database Profile API <explorer-database-profile-api_>`__ index should be shown within Movable Ink Studio.

       .. image:: ../../images/moveable-ink-datafields.png
          :width: 500 px
          :alt: Configure how fields in an Database Profile API endpoint are shown to users in Moveabile Ink Studio.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Click **Save**. The integration is added to the list of active integrations and is available for use within Movable Ink Studio.

.. destination-moveableink-configure-end
