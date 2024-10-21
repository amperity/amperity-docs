.. 
.. /markdown
.. 

.. |destination-name| replace:: Oracle Eloqua
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|


Oracle Eloqua
==================================================

|destination-name| is an automation platform for email and SMS marketing. Use the Oracle Eloqua REST API to manage audiences in |destination-name|.

Send audiences from Amperity to manage |ext_oracle_eloqua_shared_lists|. Shared lists are static lists of contacts that can be used across |destination-name|. Each shared list should contain a list of contacts with a clearly defined relationship to the campaign or program that is managed from |destination-name|.

Amperity will add and remove audience members from a shared list, and then update any contact attributes that are associated with members of that shared list. The first audience that is sent from Amperity to |destination-name| should be to a new or empty shared list.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Username**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-username-start
   :end-before: .. credential-sftp-username-end

**Password**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-oracle-eloqua-password-start
   :end-before: .. credential-oracle-eloqua-password-end

**Company name**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-oracle-eloqua-company-name-start
   :end-before: .. credential-oracle-eloqua-company-name-end



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

**Shared list name**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-oracle-eloqua-shared-list-name-start
   :end-before: .. setting-oracle-eloqua-shared-list-name-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-oracle-eloqua-shared-list-name-caution-start
   :end-before: .. setting-oracle-eloqua-shared-list-name-caution-end

**Audience primary key**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-oracle-eloqua-audience-primary-key-start
   :end-before: .. setting-oracle-eloqua-audience-primary-key-end
