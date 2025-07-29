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

For example, if the tenant ID is **acme** the base URL would be

::

   https://acme.amperity.com/api

.. api-amperity-base-url-end
