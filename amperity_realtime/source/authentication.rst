.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        All requests that are made to Amperity API endpoints must be authenticated using an API key.

.. meta::
    :content class=swiftype name=body data-type=text:
        All requests that are made to Amperity API endpoints must be authenticated using an API key.

.. meta::
    :content class=swiftype name=title data-type=string:
        Authentication

==================================================
Authentication
==================================================

.. authentication-start

All requests that are made to Amperity API endpoints must be authenticated using an API key.

.. authentication-end

.. api-authenticate-start

Authenticate to Amperity APIs by including the following line in the request:

::

   -H "Authorization: Bearer ${access-token}"

After the token passes validation, the request will look up any access policies attached to the API key, and then determine whether the requested operation is permitted.

.. api-authenticate-end

.. api-keys-important-start

.. important:: A user must be assigned the **Allow API key administration** policy before they can manage API keys and access tokens required by Amperity APIs.

   A user who is assigned the **Allow user administration** policy can assign the **Allow API key administration** policy to individual users within your tenant.

.. api-keys-important-end


.. _authentication-sandboxes:

Authentication for sandboxes
==================================================

.. api-keys-sandboxes-start

API keys are tenant-specific and are not pulled to a sandbox or promoted from a sandbox to production. API keys must be created in a sandbox to send events to the Events API or access data using the Profile API.

.. api-keys-sandboxes-end


.. _authentication-api-keys:

API keys
==================================================

.. authentication-api-keys-start

Amperity API keys are synthetic identities that are bound to your tenant and enable programmatic access to Amperity.

.. authentication-api-keys-end


.. _authentication-api-keys-add:

Add API key
--------------------------------------------------

.. api-keys-api-token-add-start

Each API key has a unique internal secret that is signed into the claims of all access tokens issued for that API key. This secret is one of the validation checks that occurs during authentication.

.. api-keys-api-token-add-end

.. api-keys-api-token-add-datagrid-start

An API key with the **Real-time API data access** policy enables upstream sources to send events to the Events API.

**To add an API key for the Events API**

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
     - From the **Add API key** dialog, add the name for the API key, select the **Real-time API data access** option, and then click **Save**.

.. api-keys-api-token-add-datagrid-end


.. _authentication-api-keys-rotate:

Rotate API key
--------------------------------------------------

.. api-keys-api-token-rotate-start

You can rotate the internal secrets used by access tokens to ensure that previously issued access tokens cannot authenticate to the Events API.

When an API key is rotated a new internal secret is generated, after which it becomes the active secret for that API key. The previously issued access token is deposed, which allows existing relay configurations to remain valid for 30 days while the new token is distributed. A deposed access token may be explicitly dropped at any time.

If an access token already has a deposed token, that deposed token is dropped and the previously issued token takes its place as the deposed token.

.. api-keys-api-token-rotate-end

**To rotate API keys**

.. api-keys-api-token-rotate-steps-start

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
     - Under **API keys** find the API key, and then from the **Actions** menu select **Get token**.

       Set the token expiration length. Enable the **Rotate key secret** option to rotate the existing secret when generating the token. This forces all previously provisioned tokens associated with the API key to expire in 30 days.

       Click **Generate token**. The token is generated and automatically copied to your clipboard.

       .. important:: Store the token in a secure secrets manager before closing this dialog. Amperity does not save the token and it will not be shown again.

.. api-keys-api-token-rotate-steps-end


.. _authentication-access-tokens:

Access tokens
==================================================

.. authentication-access-tokens-start

Access to the Amperity API requires using `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| access tokens that are signed by Amperity-managed API keys.

.. authentication-access-tokens-end


.. _authentication-access-token-generate:

Generate access token
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-jwt-start
   :end-before: .. term-jwt-end

.. api-keys-access-tokens-start

Amperity uses a `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| for authentication. Access tokens are issued from API keys that are authorized to send events to the Events API or read data from the Profile API.

Access tokens are managed directly from the Amperity UI.

.. api-keys-access-tokens-end

.. api-keys-access-tokens-about-jwt-start

Programmatic workflows should authenticate to Amperity APIs using JWT access tokens as the bearer token within the header of a request.

.. api-keys-access-tokens-about-jwt-end

.. api-keys-access-tokens-generate-start

Access tokens that enable authentication to the Events API are managed from the **Settings** page.

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

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Select the number of days this token allows access, after which it will expire.

       Click **Generate token**. The token is generated and automatically copied to your clipboard.

       .. important:: Store the token in a secure secrets manager before closing this dialog. Amperity does not save the token and it will not be shown again.

.. api-keys-access-tokens-generate-end


.. _authentication-access-token-oauth:

Get OAuth credentials
--------------------------------------------------

.. api-keys-api-token-oauth-start

Every configured API key has OAuth credentials that enable OAuth-based authentication workflows.

.. api-keys-api-token-oauth-end

**To get OAuth credentials for an API key**

.. api-keys-api-token-oauth-steps-start

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
     - Under **API keys** find the API key, and then from the **Actions** menu select **Get OAuth credentials**.

       The **OAuth credentials** dialog shows the following:

       #. Client ID.
       #. Client secret.
       #. Token endpoint.

       Use these values to configure automated workflows to authenticate using OAuth.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Use the client ID and client secret to send an HTTP POST request to the token endpoint. This returns an access token.

       **Example request**

       .. code-block:: none

          POST /api/v0/oauth2/token HTTP/1.1
          Host: acme.amperity.com
          Content-Type: application/x-www-form-urlencoded
          X-Amperity-Tenant: acme

          grant_type=client_credentials
          &client_id=ClientId
          &client_secret=ClientSecret

       **Example response**

       .. code-block:: json

          {
            "access_token": "N88Du6L1xsmA5DRZrtxSGYmbHP",
            "expires_in": 3600,
            "token_type": "Bearer"
          }

       Use the ``access_token`` value in the ``Authorization`` header. The token expires after the number of seconds specified by ``expires_in``.

.. api-keys-api-token-oauth-steps-end


.. _authentication-access-token-revoke:

Revoke access token
--------------------------------------------------

.. api-keys-access-tokens-revoke-start

You can revoke credentials associated with an API key by opening the **Actions** menu for an API key and choosing **Revoke credentials**. Do one of the following:

#. Revoke all credentials issued prior to the last rotation.
#. Revoke all credentials immediately.

The selected action cannot be undone.

.. api-keys-access-tokens-revoke-end

**To revoke access tokens**

.. api-keys-access-tokens-revoke-steps-start

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
     - Under **API keys** find the API key for which you want to revoke credentials, and then from the **Actions** menu select **Revoke credentials**.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - From the **Revoke credentials** dialog, choose one of the following options:

       Use **Revoke old credentials** to revoke only credentials issued before the last rotation. Active credentials remain valid.

       Use **Revoke all credentials** to immediately revoke all credentials, including active ones. Any relay function using this API key will stop sending events until it is updated with a new token.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Click **Revoke credentials**, and then confirm. This action cannot be undone.

.. api-keys-access-tokens-revoke-steps-end
