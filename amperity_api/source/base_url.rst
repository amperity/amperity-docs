.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        All requests to the Amperity API have a base URL.

.. meta::
    :content class=swiftype name=body data-type=text:
        All requests to the Amperity API have a base URL.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity API base URL

==================================================
Base URL
==================================================

.. api-amperity-base-url-start

All requests made to Amperity API endpoints should be directed to the base URL.

.. api-amperity-base-url-end


.. _base-url-aws:

Amazon AWS
==================================================

.. base-url-aws-start

Tenants hosted in Amazon AWS have the following base URL:

::

   https://app.amperity.com/api

Use the **amperity-tenant** header to provide the tenant ID.

.. base-url-aws-end

.. base-url-tenant-id-start

You can find the tenant ID from the Amperity user interface. From the **Settings** page and select the **Security** tab. Under **API keys**, in the row for an API key, open the |fa-kebab| menu and select **Copy tenant ID**.

.. base-url-tenant-id-end


.. _base-url-azure:

Microsoft Azure
==================================================

.. base-url-azure-start

Tenants hosted in Amazon AWS have the following base URL:

::

   https://{tenant-id}.amperity.com/api

.. note:: The tenant ID must be in the base URL *and* in the **amperity-tenant** header.

   You can find the tenant ID from the Amperity user interface. From the **Settings** page and select the **Security** tab. Under **API keys**, in the row for an API key, open the |fa-kebab| menu and select **Copy tenant ID**.

   For example, if the tenant ID is **socktown** the base URL is:

   ::

      https://socktown.amperity.com/api

   with

   ::

      --header 'amperity-tenant: socktown'

.. base-url-azure-end


.. _api-amperity-base-url-sandboxes:

Base URL and sandboxes
==================================================

.. api-amperity-base-url-sandboxes-start

The base URL for a sandbox is the same as the base URL for production.

Use the tenant ID for the sandbox for all requests made to a sandbox. unique to the sandbox. For example, if the tenant ID for a sandbox is **socktown-sb-12345** the base URL is the same as the base URL for production and the **amperity-tenant** header is:

::

   --header 'amperity-tenant: socktown-sb-12345'

.. api-amperity-base-url-sandboxes-end
