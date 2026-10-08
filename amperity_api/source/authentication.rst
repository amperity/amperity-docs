.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        All requests that are made to Amperity APIs must be authenticated using an API key.

.. meta::
    :content class=swiftype name=body data-type=text:
        All requests that are made to Amperity APIs must be authenticated using an API key.

.. meta::
    :content class=swiftype name=title data-type=string:
        How to authenticate with Amperity APIs

==================================================
How to authenticate with Amperity APIs
==================================================

.. authentication-start

All requests that are made to Amperity APIs must be authenticated using an API key.

.. authentication-end

Authenticate to Amperity APIs by including the following line in the request:

::

   -H "Authorization: Bearer ${access-token}"

After the token passes validation, the request will look up any access policies attached to the API key, and then determine whether the requested operation is permitted.

.. api-authenticate-start

Authenticate to Amperity APIs by including the following line in the request:

::

   -H "Authorization: Bearer ${access-token}"

After the token passes validation, the request will look up any access policies attached to the API key, and then determine whether the requested operation is permitted.

.. api-authenticate-end

.. important:: A user must be assigned the **Allow API key administration** policy before they can manage API keys and access tokens that are required by Amperity APIs.

   A user who is assigned the **Allow user administration** policy can assign the **Allow API key administration** policy to individual users within your tenant.


.. _authentication-sandboxes:

Authentication for sandboxes
==================================================

API keys are tenant-specific and are not pulled to a sandbox *or* promoted from a sandbox to production. API keys must be created in a sandbox to use a Tenant API endpoint, stream data using the Streaming API, or access `Database Profile API <explorer-database-profile-api_>`__ indexes.


.. _authentication-tenant-id:

Find your tenant ID
==================================================

.. authentication-tenant-id-start

Requests to Amperity APIs name the tenant they are for. To find your tenant ID, open the **Settings** page and select the **Security** tab. Under **API keys**, in the row for an API key, open the |fa-kebab| menu and select **Copy tenant ID**.

* **Sandboxes.** A sandbox has its own tenant ID, such as **socktown-sb-12345**. Use the sandbox's tenant ID for requests to that sandbox. The base URL stays the same as production.
* **Microsoft Azure.** For tenants hosted in Microsoft Azure, the tenant ID is also part of the base URL. For example, the tenant **socktown** uses the base URL ``https://socktown.amperity.com/api``.

For the base URL and the header that carries the tenant ID for each API, see the :doc:`Amperity APIs <explorer>` page.

.. authentication-tenant-id-end


.. _authentication-api-keys:

API keys
==================================================

.. authentication-api-keys-start

Amperity API keys are synthetic identities that are bound to your tenant and enable programmatic access to Amperity.

.. authentication-api-keys-end


.. _authentication-api-keys-add:

Add API key
--------------------------------------------------

Each API key has a unique internal secret that is signed into the claims of all access tokens that are issued for that API key. This secret is one of the validation checks that occurs during authentication to Amperity APIs.

An API key enables your downstream use cases to interact with Amperity APIs.

**To add an API key for Amperity APIs**

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
     - From the **Add API key** dialog, add the name for the API key, select the **DataGrid Operator** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-datagrid.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link


.. _authentication-api-keys-rotate:

Rotate API key
--------------------------------------------------

You can rotate the internal secrets used by access tokens to ensure that previously issued access tokens cannot authenticate to Amperity APIs.

When an API key is rotated a new internal secret is generated, after which it becomes the active secret for that API key. The previously issued access token is deposed, which allows the previous code to remain valid for a short period of time to allow for distribution of the new access token. A deposed access token will remain valid for 30 days, or may be explicitly dropped.

If an access token already has a deposed token, that deposed token is dropped and the previously issued access token takes its place as the deposed token.

This process may be used to invalidate outstanding tokens issued without expiry times. Clients should be careful not to rotate too often, such as to not rotate on every issue call, or they will be surprised when their existing tokens stop working.

.. note:: If you rotate your tokens too often you may run into issues where previously issued access tokens are not deposed for a long enough time, which prevents newly issued tokens from being distributed.

**To rotate API keys**

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
     - Under **API keys** find the index, and then from the **Actions** menu select **Generate token**.

       Set the token expiration length. Enable the **Rotate key secret** option to rotate an existing secret when generating an access token. This will force all previously provisioned tokens that are associated with the current API key to expire in 30 days.


.. _authentication-access-tokens:

Access tokens
==================================================

.. authentication-access-tokens-start

Access to Amperity APIs requires using `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| access tokens that are signed by Amperity-managed API keys.

.. authentication-access-tokens-end


.. _authentication-access-token-generate:

Generate access token
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-jwt-start
   :end-before: .. term-jwt-end

Amperity uses a `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| for authentication to Amperity APIs. These access tokens are issued from API keys which are authorized to perform certain actions with Amperity.

Because a JWT access token automatically expires, tokens should be refreshed on a regular basis.

Access tokens are managed directly from the Amperity UI.

Programmatic workflows should authenticate to Amperity APIs using JWT access tokens as the bearer token within the header of a request.

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


.. _authentication-access-token-oauth:

Get OAuth credentials
--------------------------------------------------

Every configured API token has an access token to enable using OAuth.

**To get OAuth credentials for an API key**

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
     - Under **API keys** find the index, and then from the **Actions** menu select **Get OAuth credentials**.

       The **OAuth credentials** dialog box opens and shows the following credential details:

       #. Client ID.
       #. Client secret.
       #. Token endpoint.

       Use these values to configure automated workflows to use OAuth when accessing the API for which this token allows access.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Use the client ID and client secret to send an HTTP POST request to the token endpoint. This will return an access token.

       **Example request details**

       .. code-block:: none

          POST /api/v0/oauth2/token HTTP/1.1
          Host: acme.amperity.com
          Content-Type: application/x-www-form-urlencoded
          X-Amperity-Tenant: acme2

          grant_type=client_credentials
          &client_id=ClientId
          &client_secret=ClientSecret

       The 200 OK response will be similar to

       .. code-block:: json

          {
            "access_token": "N88Du6L1xsmA5DRZrtxSGYmbHP",
            "expires_in": 3600,
            "token_type": "Bearer"
          }

       Where:

       * ``access_token`` is an access token that can authenticate requests to Amperity APIs. Use this access token in the HTTP Authorization header.
       * ``expires_in`` is the amount of time, after which, the access token expires.
       * ``token_type`` should always be set to "Bearer".


.. _authentication-access-token-revoke:

Revoke access token
--------------------------------------------------

You may revoke access tokens associated with an API key by opening the **Actions** menu for an API key, and then choosing **Revoke tokens**. Do one of the following:

#. Revoke all tokens that were issued before the last rotation.
#. Revoke all tokens immediately.

The selected action cannot be undone.

**To revoke access tokens**

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
     - Under **API keys** find the API key for which you want to revoke tokens, and then from the **Actions** menu select **Revoke token**.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - From the **Revoke tokens** dialog, choose one of the following options:

       .. image:: ../../images/api-keys-revoke-access-token.png
          :width: 340 px
          :alt: Revoke an access token.
          :align: left
          :class: no-scaled-link

       Use **Revoke old tokens** to revoke only tokens that were created before the last rotation.

       Use **Revoke all tokens** to immediately revoke all tokens.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Click **Revoke tokens**, and then confirm that you want to revoke the selected tokens. This action cannot be undone.
