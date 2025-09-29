.. /downloads/markdown/


.. |destination-name| replace:: Listrak SMS
.. |audience-primary-key| replace:: "phone" 
.. |what-send| replace:: SMS profiles
.. |where-send| replace:: |destination-name|


Listrak
==================================================

Use the `Listrak SMS REST API <https://api.listrak.com/sms>`__ |ext_link| to manage SMS profiles in |destination-name|.

`Custom SMS profile attributes <https://help.listrak.com/en/articles/1852936-sms-profile-fields-and-personalization-guide>`__ |ext_link| must be created in |destination-name| before Amperity can send custom attributes.



Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**SMS client ID and client secret**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-listrak-sms-client-id-secret-start
   :end-before: .. credential-listrak-sms-client-id-secret-end


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

**SMS list ID**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-phone-list-id-start
   :end-before: .. setting-listrak-sms-phone-list-id-end

**Sender code ID**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-sender-code-id-start
   :end-before: .. setting-listrak-sms-sender-code-id-end

**Audience primary key**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-audience-primary-key-start
   :end-before: .. setting-common-audience-primary-key-end

**Include attributes that match custom profile fields**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-enable-segmentation-start
   :end-before: .. setting-listrak-sms-enable-segmentation-end

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
