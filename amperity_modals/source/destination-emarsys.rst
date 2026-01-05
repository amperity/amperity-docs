.. /downloads/markdown/


.. |destination-name| replace:: SAP Emarsys
.. |audience-primary-key| replace:: "email" or "phone"
.. |what-send| replace:: contact lists
.. |where-send| replace:: |destination-name|


SAP Emarsys
==================================================

|destination-name| is an omnichannel customer engagement platform for personalizing customer interactions across channels to increase customer engagement and lifetime value.


Credentials
==================================================

**Client ID and secret**

A client ID and client secret with permission to access your instance of |destination-name|. These values are part of the `API credentials <https://help.sap.com/docs/SAP_EMARSYS/5d44574160f44536b0130abf58cb87cc/fdf4b58974c110149353957a3e7ef453.html?locale=en-US&state=PRODUCTION&version=CLOUD&q=client%20id>`__ |ext_link| configured for your instance of |destination-name|.

The OAuth user associated with the client ID and secret must have `contact, contactlist, and field <https://dev.emarsys.com/docs/emarsys-core-api-guides/ef41493bd7812-endpoint-permission-settings>`__ |ext_link| permissions to the SAP Emarsys Rest API.



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

**Contact identifier**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-sap-emarsys-contact-identifier-start
   :end-before: .. setting-sap-emarsys-contact-identifier-end

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
