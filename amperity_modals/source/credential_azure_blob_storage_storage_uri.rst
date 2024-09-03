.. 
.. /markdown
.. 

.. |destination-name| replace:: Azure Blob Storage


Storage URI
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-azure-blob-storage-about-start
   :end-before: .. setting-azure-blob-storage-about-end

.. TODO: Hook this in from shared/credentials_settings.rst

Each |destination-name| resource has a `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#resource-uri-syntax>`__ |ext_link|, which contains the name of the account and the name of the container in which blob storage is located.


Settings
==================================================

**Container**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-container-start
      :end-before: .. credential-azure-blob-storage-container-end

**Storage URI**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-storage-uri-start
      :end-before: .. credential-azure-blob-storage-storage-uri-end
