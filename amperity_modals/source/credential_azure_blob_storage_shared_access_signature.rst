.. 
.. /markdown
.. 

.. |destination-name| replace:: Azure Blob Storage


Shared access signature
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-azure-blob-storage-about-start
   :end-before: .. setting-azure-blob-storage-about-end

.. TODO: Hook this in from shared/credentials_settings.rst

A `service-level shared access signature (SAS) <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>`__ |ext_link| specifies which resources in your |destination-name| account can be accessed, what permissions that access allows on resources in the container, and the length of time for which the SAS is valid.


Settings
==================================================

**Account name**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-account-name-start
      :end-before: .. credential-azure-blob-storage-account-name-end

**Container**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-container-start
      :end-before: .. credential-azure-blob-storage-container-end

**Shared access signature**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-shared-access-signature-start
      :end-before: .. credential-azure-blob-storage-shared-access-signature-end
