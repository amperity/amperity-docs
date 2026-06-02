.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        All requests to the Amperity Real-time API have a base URL.

.. meta::
    :content class=swiftype name=body data-type=text:
        All requests to the Amperity Real-time API have a base URL.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Real-time API base URL

==================================================
Base URL
==================================================

.. api-amperity-base-url-start

The Events API and Profile API v3 use different base URLs.

.. api-amperity-base-url-end


.. _base-url-events:

Events API
==================================================

.. base-url-events-start

Use the following base URLs for Events API endpoints.

**Amazon AWS**

.. code-block:: none

   https://app.amperity.com

**Microsoft Azure**

.. code-block:: none

   https://{tenant-id}.amperity.com

**Australia**

.. code-block:: none

   https://app-aws-apse2.amperity.com

.. base-url-events-end


.. _base-url-profile:

Profile API v3
==================================================

.. base-url-profile-start

Use the following base URLs for Profile API v3 endpoints.

**Amazon AWS**

.. code-block:: none

   https://app.amperity.com/prof

**Microsoft Azure**

.. code-block:: none

   https://{tenant-id}.amperity.com/prof

.. note:: The tenant ID must be in the base URL *and* in the **Amperity-Tenant** header.

   For example, if the tenant ID is **socktown** the base URL is:

   .. code-block:: none

      https://socktown.amperity.com/prof

   with

   .. code-block:: none

      --header 'Amperity-Tenant: socktown'

**Australia**

.. code-block:: none

   https://app-aws-apse2.amperity.com/prof

.. base-url-profile-end

.. base-url-tenant-id-start

You can find the tenant ID from the Amperity user interface. From the **Settings** page and select the **Security** tab. Under **API keys**, in the row for an API key, open the |fa-kebab| menu and select **Copy tenant ID**.

.. base-url-tenant-id-end


.. _api-amperity-base-url-sandboxes:

Base URL and sandboxes
==================================================

.. api-amperity-base-url-sandboxes-start

The base URL for a sandbox is the same as the base URL for production.

Use the tenant ID for the sandbox for all requests made to a sandbox. The tenant ID is unique to the sandbox. For example, if the tenant ID for a sandbox is **socktown-sb-12345** the base URL is the same as the base URL for production and the **Amperity-Tenant** header is:

.. code-block:: none

   --header 'Amperity-Tenant: socktown-sb-12345'

.. api-amperity-base-url-sandboxes-end
