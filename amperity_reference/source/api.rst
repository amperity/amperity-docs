.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About the APIs that may be used with Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About the APIs that may be used with Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity APIs

==================================================
Amperity APIs
==================================================

.. api-overview-start

Amperity has the following APIs:

* :ref:`Amperity API <api-amperity>`
* :ref:`Profile API <api-profile>`
* :ref:`Streaming Ingest API <api-streaming-ingest>`

.. api-overview-end


.. _api-amperity:

Amperity API
==================================================

.. api-amperity-start

The |amperity_api| enables programmatic access to your Amperity tenant through a collection of RESTful endpoints that support API-first use cases for integrations, applications, and custom workflows. Use Amperity API endpoints to streamline workflows, enhance marketing strategies, and unlock the value of your brand's customer data.

.. include:: ../../shared/api_amperity.rst
   :start-after: .. term-http-methods-start
   :end-before: .. term-http-methods-end

.. api-amperity-end


.. _api-profile:

Profile API
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-profile-api-start
   :end-before: .. term-profile-api-end

.. api-profile-about-start

The |api_profile| is unique to your tenant. The endpoints that are enabled for your use cases do not exist until the results of queries that have been defined by your brand have been published to the Profile API as an index. A :ref:`set of actions are available <api-profile-actions>` for each endpoint that your brand enables when using the Profile API.

.. warning:: The Profile API is currently in a closed beta. Ask your Amperity representative about potential use cases that are enabled by the Profile API and for information about how (and when) your brand can get access to the Profile API.

.. api-profile-about-start

.. api-keys-important-profile-api-start

.. note::

   .. include:: ../../shared/terms.rst
      :start-after: .. term-profile-api-administrator-policy-start
      :end-before: .. term-profile-api-administrator-policy-end

   A user must be assigned the **Allow Profile API administration** policy before they can manage endpoints that are enabled by the Profile API.

   A user who is assigned the **Allow user administration** policy can assign the **Allow Profile API administration** policy to individual users within your tenant.

.. api-keys-important-profile-api-end


.. _api-streaming-ingest:

Streaming Ingest API
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-streaming-ingest-api-start
   :end-before: .. term-streaming-ingest-api-end

.. api-streaming-ingest-start

The |api_streaming_ingest| is designed for streaming events and profile updates. It is a low latency, high throughput REST API, designed to accept billions of records per day.

.. api-streaming-ingest-end


.. _api-authenticate:

Authenticate to Amperity APIs
==================================================

.. api-authenticate-start

Authenticate to Amperity APIs by including the following line in the request:

::

   -H "Authorization: Bearer ${access-token}"

After the token passes validation, the request will look up any access policies attached to the API key, and then determine whether the requested operation is permitted.

.. api-authenticate-end


.. _api-keys:

About Amperity API keys
==================================================

.. api-keys-start

Amperity API keys are synthetic identities that are bound to your tenant and enable programmatic access to Amperity.

Access to the Amperity API requires using `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| access tokens that are signed by Amperity-managed API keys.

.. api-keys-end

.. api-keys-sandboxes-start

API keys are tenant-specific and are neither pulled nor promoted in the sandbox experience.

.. api-keys-sandboxes-end

.. api-keys-important-start

.. important:: A user must be assigned the **Allow API key administration** policy before they can manage API keys and access tokens that are required by Amperity APIs.

   A user who is assigned the **Allow user administration** policy can assign the **Allow API key administration** policy to individual users within your tenant.

.. api-keys-important-end


.. _api-keys-api-tokens:

About API keys
--------------------------------------------------

.. api-keys-api-tokens-start

API keys are managed directly from the Amperity UI.

* :ref:`Add API keys <api-keys-api-token-add>`
* :ref:`Delete API keys <api-keys-api-token-delete>`
* :ref:`Rotate API keys <api-keys-api-token-rotate>`

.. api-keys-api-tokens-end


.. _api-keys-api-token-add:

Add API keys
--------------------------------------------------

.. api-keys-api-token-add-start

Each API key has a unique internal secret that is signed into the claims of all access tokens that are issued for that API key. This secret is one of the validation checks that occurs during authentication to the Amperity API.

.. api-keys-api-token-add-end

.. api-keys-api-token-add-list-start

You can create the following types of API tokens for the Amperity API:

* :ref:`api-keys-api-token-add-issuer`
* :ref:`api-keys-api-token-add-datagrid`
* :ref:`api-keys-api-token-add-profile`
* :ref:`api-keys-api-token-add-streaming-ingest`

.. api-keys-api-token-add-list-end


.. _api-keys-api-token-add-issuer:

API token issuer
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-api-token-add-issuer-start

An API issuer token enables your downstream workflow to programmatically issue new access tokens for API keys.

**To add an issuer token**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab. Under **API keys** click **Add API key**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - From the **Add API key** dialog, add the name for the API key, select the **API Token Issuer** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-issuer.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link

.. api-keys-api-token-add-issuer-end


.. _api-keys-api-token-add-datagrid:

Amperity API data access
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-api-token-add-datagrid-start

An API key enables your downstream use cases to interact with the Amperity API.

**To add an API key for the Amperity API**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab. Under **API keys** click **Add API key**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - From the **Add API key** dialog, add the name for the API key, select the **DataGrid Operator** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-datagrid.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link

.. api-keys-api-token-add-datagrid-end


.. _api-keys-api-token-add-profile:

Profile API data access
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-api-token-add-profile-start

An API key enables your downstream use cases to read data from the Profile API.

**To add an API key for the Profile API**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab. Under **API keys** click **Add API key**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - From the **Add API key** dialog, add the name for the API key, select the **Profile API Data Access** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-profile.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link

.. api-keys-api-token-add-profile-end


.. _api-keys-api-token-add-streaming-ingest:

Streaming Ingest API write access
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-api-token-add-streaming-ingest-start

A write access token enables your upstream use cases to write data to the Streaming Ingest API.

**To add an access token for the Streaming Ingest API**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab. Under **API keys** click **Add API key**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - From the **Add API key** dialog, add the name for the API key, select the **Streaming Ingest Write Access** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-streaming.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link

.. api-keys-api-token-add-streaming-ingest-end


.. _api-keys-api-token-delete:

Delete API keys
--------------------------------------------------

.. api-keys-api-token-delete-start

In situations where rotating an access key isn't enough, you can delete an API key.

**To delete API tokens**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Under **API keys** find the index, and then from the **Actions** menu select "Delete".

       .. image:: ../../images/api-keys-delete-access-token.png
          :width: 500 px
          :alt: Delete an API token.
          :align: left
          :class: no-scaled-link

.. api-keys-api-token-delete-end


.. _api-keys-api-token-rotate:

Rotate API keys
--------------------------------------------------

.. api-keys-api-token-rotate-start

You can rotate the internal secrets used by access tokens to ensure that previously-issued access tokens cannot authenticate to the Amperity API.

When an API key is rotated a new internal secret is generated, after which it becomes the active secret for that API key. The previously-issued access token is deposed, which allows the previous code to remain valid for a short period of time to allow for distribution of the new access token. A deposed access token will remain valid for 30 days, or may be explicitly dropped.

If an access token already has a deposed token, that deposed token is dropped and the previously-issued access token will take its place as the deposed token.

This process may be used to invalidate outstanding tokens issued without expiry times. Clients should be careful not to rotate too often (e.g. on every issue call), or they will be surprised when their existing tokens stop working suddenly.

.. note:: If you rotate your tokens too quickly you may run into issues where previously-issued access tokens are not deposed for a long enough time, which prevents newly-issued tokens from being distributed.

API tokens can be rotated directly from Amperity.

.. api-keys-api-token-rotate-end

**To rotate API keys**

.. api-keys-api-token-rotate-steps-start


.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Under **API keys** find the index, and then from the **Actions** menu select "Rotate API token".

       .. image:: ../../images/api-keys-rotate-api-token.png
          :width: 500 px
          :alt: Rotate an API token.
          :align: left
          :class: no-scaled-link

.. api-keys-api-token-rotate-steps-end


.. _api-keys-access-tokens:

About access tokens
==================================================

.. api-keys-access-tokens-start

Amperity uses a `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| for authentication to the Amperity API. These access tokens are issued from API keys which are authorized to perform certain actions with Amperity.

Because a JWT access token automatically expires, tokens should be refreshed on a regular basis.

Access tokens are managed directly from the Amperity UI.

.. api-keys-access-tokens-end

.. api-keys-access-tokens-list-start

* :ref:`Generate access tokens <api-keys-access-tokens-generate>`
* :ref:`Refresh access tokens <api-keys-access-tokens-refresh>`

.. api-keys-access-tokens-list-end


.. _api-keys-access-tokens-about-jwt:

About JWT
--------------------------------------------------

.. term-jwt-start

A JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.

.. term-jwt-end

.. api-keys-access-tokens-about-jwt-start

Programmatic workflows should authenticate to Amperity APIs using JWT access tokens as the bearer token within the header of a request.

.. api-keys-access-tokens-about-jwt-end


.. _api-keys-access-tokens-generate:

Generate access tokens
--------------------------------------------------

.. api-keys-access-tokens-generate-start

Access tokens that enable authentication to the Amperity API are managed directly from the **Users & Activity** page in Amperity.

**To generate access tokens**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Under **API keys** find the API key for which you want to generate an access token, and then from the **Actions** menu select "Generate access token".

       .. image:: ../../images/api-keys-generate-access-token.png
          :width: 500 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Select the number of days this token will allow access to the API, after which it will expire. For example, 3 days:

       .. image:: ../../images/api-keys-set-token-expiration.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       Use the **Rotate key secret** option to rotate an existing secret when generating an access token. This will force all previously-provisioned tokens that are associated with the current API key to expire in 30 days.

       Click **Generate token**. The token is generated, and then is automatically copied to your clipboard.

       .. image:: ../../images/api-keys-token-saved-to-clipboard.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       .. important:: You are the only person who will have access to the newly-generated access key. Amperity does not save the access key anywhere and it will disappear when you close this dialog. Store the access key in a safe place.

.. api-keys-access-tokens-generate-end


.. _api-keys-access-tokens-refresh:

Refresh access tokens
--------------------------------------------------

.. api-keys-access-tokens-refresh-start

Access tokens may be :ref:`refreshed directly (using an issuer token) <api-keys-access-tokens-refresh-api-issuer>`, and by using :ref:`HTTP <api-keys-access-tokens-refresh-http>` or :ref:`cURL <api-keys-access-tokens-refresh-curl>`.

.. api-keys-access-tokens-refresh-end


.. _api-keys-access-tokens-refresh-api-issuer:

using API issuer tokens
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-access-tokens-refresh-api-issuer-start

Use :ref:`API issuer tokens <api-keys-api-token-add-issuer>` to enable a downstream workflow to programmatically refresh access tokens. :ref:`Generate an access token for the issuer token <api-keys-access-tokens-generate>`, and then use the issuer token as part of the programmatic workflow.

.. api-keys-access-tokens-refresh-api-issuer-end


.. _api-keys-access-tokens-refresh-curl:

using cURL
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-access-tokens-refresh-curl-start

To refresh an access token using cURL, submit a request similar to:

.. code-block:: none

   curl -XPOST \
   -H "Content-Type: application/json" \
   -H "X-Amperity-Tenant: <tenant-name>" \
   -H "Authorization: Bearer <token-refresher token>" \
   https://<tenant-name>.amperity.com/api/v0/admin/api-keys/<api-key-id>/tokens \
   -d '{"expires-at": "2020-06-16T00:24:16Z"}'

.. api-keys-access-tokens-refresh-curl-end


.. _api-keys-access-tokens-refresh-http:

using HTTP
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-access-tokens-refresh-http-start

To refresh an access token using HTTP, submit a request similar to:

.. code-block:: none

   POST /api/v0/admin/api-keys/<api-key-id>/tokens HTTP/1.1
   Host: https://<tenant-name>.amperity.com
   Content-Type: application/json
   X-Amperity-Tenant: <tenant-name>
   Authorization: Bearer <token-refresher token>

   {"expires-at": "2020-06-16T00:24:16Z"}

.. api-keys-access-tokens-refresh-http-end


.. _api-keys-access-tokens-refresh-postman:

using Postman
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-access-tokens-refresh-postman-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-postman-start
   :end-before: .. term-postman-end

Amperity provides complete details for refreshing an API token using a |ext_download_postman_api_refresh|. Use this collection as the starting point for testing your refresh token workflow.

.. api-keys-access-tokens-refresh-postman-end


.. _api-keys-access-tokens-refresh-generate-token:

when generating an access token
++++++++++++++++++++++++++++++++++++++++++++++++++

.. api-keys-access-tokens-refresh-generate-token-start

Use the **Rotate key secret** option to rotate an existing secret when :ref:`generating an access token <api-keys-access-tokens-generate>`. This will force all previously-provisioned tokens that are associated with the current API key to expire in 30 days.

.. api-keys-access-tokens-refresh-generate-token-end


.. _api-keys-access-tokens-revoke:

Revoke access tokens
--------------------------------------------------

.. api-keys-access-tokens-revoke-start

You may revoke access tokens associated with an API key by opening the **Actions** menu for an API key, and then choosing **Revoke tokens**. There are two options:

#. Revoke all tokens that were issued prior to the last rotation.
#. Revoke all tokens immediately.

The selected action cannot be undone.

.. api-keys-access-tokens-revoke-end

**To revoke access tokens**

.. api-keys-access-tokens-revoke-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Under **API keys** find the API key for which you want to revoke tokens, and then from the **Actions** menu select "Revoke token".


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - From the **Revoke tokens** dialog, choose one of the following options:

       .. image:: ../../images/api-keys-revoke-access-token.png
          :width: 340 px
          :alt: Revoke an access token.
          :align: left
          :class: no-scaled-link

       Use **Revoke old tokens** to revoke only tokens that were created prior to the last rotation.

       Use **Revoke all tokens** to immediately revoke all tokens.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Click **Revoke tokens**, and then confirm that you want to revoke the selected tokens. This action cannot be undone.

.. api-keys-access-tokens-revoke-steps-end


.. _api-profile-actions:

About Profile API actions
==================================================

.. api-profile-actions-start

The following actions are available for each endpoint that your brand enables in the Profile API:

* :ref:`api-profile-action-copy-url`
* :ref:`api-profile-action-copy-index-id`
* :ref:`api-profile-action-delete`
* :ref:`api-profile-action-edit`
* :ref:`api-profile-action-run`
* :ref:`api-profile-action-view`

.. api-profile-actions-end


.. _api-profile-action-copy-url:

Copy endpoint URL
--------------------------------------------------

.. api-profile-action-copy-url-start

Use this to get the full URL for your tenant, including the ID for the endpoint. Use this URL in the requests your brand makes to the profile API.

.. important:: Each request to a profile API endpoint **MUST** have the correct URL for that endpoint. The URL for an endpoint is similar to:

   ::

      https://{tenant-domain}/attribute/v0/indexes/{index-id}

.. api-profile-action-copy-url-end

**To copy the URL for an endpoint**

.. api-profile-action-copy-url-steps-start

#. Open the **Destinations** page.
#. Under **Profile API**, select |fa-kebab| from a row within the list of endpoints, and then select **Copy URL**.

   .. image:: ../../images/api-profile-endpoint-copy-url.png
      :width: 500 px
      :alt: Copy the URL for an endpoint in the Amperity Profile API.
      :align: left
      :class: no-scaled-link

   This copies the full URL to the clipboard on your computer, after which you can use it to configure requests that are made to that endpoint.

.. api-profile-action-copy-url-steps-end


.. _api-profile-action-copy-index-id:

Copy index ID
--------------------------------------------------

.. api-profile-action-copy-index-id-start

The index ID is a unique identifier for an endpoint. To make a request to any Profile API endpoint you must include the index ID in the URL for the request.

::

   https://{tenant-domain}/attribute/v0/indexes/{index-id}

.. api-profile-action-copy-index-id-end

**To copy the index ID for an endpoint**

.. api-profile-action-copy-index-id-steps-start

#. Open the **Destinations** page.
#. Under **Profile API**, select |fa-kebab| from a row within the list of endpoints, and then select **Copy index ID**.

   .. image:: ../../images/api-profile-endpoint-copy-index-id.png
      :width: 500 px
      :alt: Copy the index ID for an endpoint in the Amperity Profile API.
      :align: left
      :class: no-scaled-link

   This copies the index ID to the clipboard on your computer, after which it can be added to a request that is made to that Profile API endpoint.

.. api-profile-action-copy-index-id-steps-end


.. _api-profile-action-delete:

Delete endpoint
--------------------------------------------------

.. api-profile-action-delete-start

If your tenant is not using an endpoint, it may be deleted from the Profile API.

.. api-profile-action-delete-end

**To delete an endpoint**

.. api-profile-action-delete-steps-start

#. Open the **Destinations** page.
#. Under **Profile API**, select the elipses icon for an endpoint, and then select **Delete**.

   .. image:: ../../images/api-profile-endpoint-delete.png
      :width: 500 px
      :alt: Delete and endpoint from the Amperity Profile API.
      :align: left
      :class: no-scaled-link

#. Click the **Delete** button to confirm that you want to delete the endpoint.

.. api-profile-action-delete-steps-end


.. _api-profile-action-edit:

Edit endpoint settings
--------------------------------------------------

.. api-profile-action-edit-start

You can update the settings for any endpoint in the Profile API.

.. api-profile-action-edit-end

**To edit the settings for an endpoint**

.. api-profile-action-edit-steps-start

#. Open the **Destinations** page.
#. Under **Profile API**, select |fa-kebab| from a row within the list of endpoints, and then select **Edit**.

   .. image:: ../../images/api-profile-endpoint-edit.png
      :width: 500 px
      :alt: Edit the settings for an endpoint in the Amperity Profile API.
      :align: left
      :class: no-scaled-link

#. Make your changes.
#. Click **Save**.

.. api-profile-action-edit-steps-end


.. _api-profile-action-run:

Generate endpoint
--------------------------------------------------

.. api-profile-action-run-start

Run a query to generate the data that will be available from an endpoint. The **Run** action does one of the following:

* Generates the index if it was not generated on save.
* Regenerates the index and refreshes the data that is available at that endpoint.

.. api-profile-action-run-end

**To run an endpoint**

.. api-profile-action-run-steps-start

#. Open the **Destinations** page.
#. Under **Profile API**, select |fa-kebab| from a row within the list of endpoints, and then select **Run**.

   .. image:: ../../images/api-profile-endpoint-run.png
      :width: 500 px
      :alt: Generate the index for an endpoint in the Amperity Profile API.
      :align: left
      :class: no-scaled-link

   This action will generate the index if it does not already exist **OR** this action will regenerate the index and refresh the data that is available from the endpoint.

.. api-profile-action-run-steps-end


.. _api-profile-action-view:

View endpoint settings
--------------------------------------------------

.. api-profile-action-view-start

You may view the settings for any configured endpoint.

.. api-profile-action-view-end

**To view the settings for an endpoint**

.. api-profile-action-view-steps-start

#. Open the **Destinations** page.
#. Under **Profile API**, select the elipses icon for an endpoint, and then select **View**.

.. api-profile-action-view-steps-end
