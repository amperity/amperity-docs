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

A `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link| includes the information that allows Amperity to authorize to your |destination-name| account.


Settings
==================================================

**Connection string**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-connection-string-start
      :end-before: .. credential-azure-blob-storage-connection-string-end

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-connection-string-example-start
      :end-before: .. credential-azure-blob-storage-connection-string-example-end

**Container**
   **Required**

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-azure-blob-storage-container-start
      :end-before: .. credential-azure-blob-storage-container-end
