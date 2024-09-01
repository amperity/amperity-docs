.. 
.. /markdown
.. 

.. |destination-name| replace:: Azure Blob Storage


Azure Blob Storage
==================================================

Test link patterns.


Connection string
==================================================

.. destination-azure-blob-storage-credentials-connection-string-start

A `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link| includes the information that allows Amperity to authorize to your |destination-name| account.

.. destination-azure-blob-storage-credentials-connection-string-end


Shared acccess signature
==================================================

.. destination-azure-blob-storage-credentials-shared-access-signature-start

A `service-level shared access signature (SAS) <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>`__ |ext_link| specifies which resources in your brand's |destination-name| account can be accessed, what permissions that access allows on resources in the container, and the length of time for which the SAS is valid.

.. destination-azure-blob-storage-credentials-shared-access-signature-end


Storage URI
==================================================

.. destination-azure-blob-storage-credentials-storage-uri-start

Each |destination-name| resource has `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#resource-uri-syntax>`__ |ext_link|, which contains the name of the account and the name of the container in which blob storage is located.

.. destination-azure-blob-storage-credentials-storage-uri-end
