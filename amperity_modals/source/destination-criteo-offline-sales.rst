.. /downloads/markdown/


.. |destination-name| replace:: Criteo
.. |what-send| replace:: offline sales
.. |where-send| replace:: |destination-name|


Criteo Offline Sales
==================================================

Send offline sales to |destination-name| to attribute in-store purchases back to the ads that |destination-name| served, and to inform ad targeting. Amperity sends transaction data at the line-item level: each row returned by your query is one product within a purchase, grouped by transaction and then by shopper. Amperity hashes email addresses before sending them; a shopper can also be identified by a customer ID or a retailer visitor ID.

.. events-criteo-offline-sales-modal-beta-start

.. admonition:: Beta

   The |destination-name| Offline Sales connector is currently in beta. Contact your Amperity representative to learn more.

.. events-criteo-offline-sales-modal-beta-end


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Account ID**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-criteo-offline-sales-account-id-start
   :end-before: .. credential-criteo-offline-sales-account-id-end

**Log label**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-criteo-offline-sales-log-label-start
   :end-before: .. credential-criteo-offline-sales-log-label-end


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
