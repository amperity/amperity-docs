.. /downloads/markdown/


.. |destination-name| replace:: Microsoft Advertising
.. |what-send| replace:: conversion events
.. |where-send| replace:: |destination-name|


Microsoft Ads Conversions API
==================================================

Send conversion events to |destination-name| using the Conversions API (CAPI) to attribute conversions that happen away from the browser — in-store purchases, CRM events, phone orders, and other server-side transactions — back to your |destination-name| campaigns, and to build audiences for remarketing. Each row returned by your query is sent as a single custom conversion event, matched by a hashed customer identifier, a Microsoft click ID, or another identifier.

.. events-microsoft-ads-conversions-modal-beta-start

.. admonition:: Beta

   The Microsoft Ads Conversions API connector is currently in beta. Contact your Amperity representative to learn more.

.. events-microsoft-ads-conversions-modal-beta-end


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API token**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-microsoft-ads-conversions-api-token-start
   :end-before: .. credential-microsoft-ads-conversions-api-token-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-microsoft-ads-conversions-api-token-find-start
   :end-before: .. credential-microsoft-ads-conversions-api-token-find-end


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Business user access**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-allow-start
   :end-before: .. setting-common-business-user-access-allow-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-restrict-pii-start
   :end-before: .. setting-common-business-user-access-restrict-pii-end

**UET Tag ID**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-microsoft-ads-conversions-tag-id-start
   :end-before: .. setting-microsoft-ads-conversions-tag-id-end
