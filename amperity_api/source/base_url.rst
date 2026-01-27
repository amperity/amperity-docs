.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        All requests to the Amperity API use 'https://{tenant-id}.amperity.com/api' as the base URL.

.. meta::
    :content class=swiftype name=body data-type=text:
        All requests to the Amperity API use 'https://{tenant-id}.amperity.com/api' as the base URL.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity API base URL

==================================================
Base URL
==================================================

.. api-amperity-base-url-start

All requests made to Amperity API endpoints should be directed to the following base URL:

::

   https://{tenant-id}.amperity.com/api


You can find the tenant ID from the Amperity user interface. From the **Users and Activity** page, select the **Actions** menu for an API key, and then click **Copy tenant ID**.

For example, if the tenant ID is **socktown** the base URL would be

::

   https://socktown.amperity.com/api

.. api-amperity-base-url-end


.. _api-amperity-base-url-sandboxes:

Base URLs and sandboxes
==================================================

.. api-amperity-base-url-sandboxes-start

The base URL for a sandbox is the same as the base URL for production:

::

   https://socktown.amperity.com/api

Use the **amperity-tenant** header to specify the name of the sandbox.

.. code-block:: rest

   curl --request POST \
          'https://socktown.amperity.com/api/workflow/runs' \
        --header 'amperity-tenant: socktown-sb-a12bcd34' \
        --header 'api-version: 2024-04-01' \
        --header 'Authorization: Bearer REDACTED' \
        --header 'Content-Type: application/json' \
        --data '{"config_id":"cg-1abc2D34E"}'

.. api-amperity-base-url-sandboxes-end
