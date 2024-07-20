.. 
.. https://docs.amperity.com/api/
..

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

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-authenticate-start
   :end-before: .. api-authenticate-end

.. api-authenticate-start

Authenticate to Amperity APIs by including the following line in the request:

::

   -H "Authorization: Bearer ${access-token}"

After the token passes validation, the request will look up any access policies attached to the API key, and then determine whether the requested operation is permitted.

.. api-authenticate-end

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-important-start
   :end-before: .. api-keys-important-end


.. _authentication-api-keys:

API keys
==================================================

.. authentication-api-keys-start

Amperity API keys are synthetic identities that are bound to your tenant and enable programmatic access to Amperity.

.. authentication-api-keys-end


.. _authentication-api-keys-add:

Add API key
--------------------------------------------------

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-add-start
   :end-before: .. api-keys-api-token-add-end

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-add-datagrid-start
   :end-before: .. api-keys-api-token-add-datagrid-end


.. _authentication-api-keys-rotate:

Rotate API key
--------------------------------------------------

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-rotate-start
   :end-before: .. api-keys-api-token-rotate-end

**To rotate API keys**

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-rotate-steps-start
   :end-before: .. api-keys-api-token-rotate-steps-end


.. _authentication-access-tokens:

Access tokens
==================================================

.. authentication-access-tokens-start

Access to the Amperity API requires using |ext_jwt| access tokens that are signed by Amperity-managed API keys.

.. authentication-access-tokens-end


.. _authentication-access-token-generate:

Generate access token
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-jwt-start
   :end-before: .. term-jwt-end

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-start
   :end-before: .. api-keys-access-tokens-end

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-about-jwt-start
   :end-before: .. api-keys-access-tokens-about-jwt-end

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-generate-start
   :end-before: .. api-keys-access-tokens-generate-end


.. _authentication-access-token-revoke:

Revoke access token
--------------------------------------------------

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-revoke-start
   :end-before: .. api-keys-access-tokens-revoke-end

**To revoke access tokens**

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-revoke-steps-start
   :end-before: .. api-keys-access-tokens-revoke-steps-end
