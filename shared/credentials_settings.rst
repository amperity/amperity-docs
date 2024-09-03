


**AZURE BLOB STORAGE**

This section contains credentials that are unique to Azure Blob Storage.

**Account name**

.. credential-azure-blob-storage-account-name-start

The name of your |destination-name| storage account.

.. credential-azure-blob-storage-account-name-end

**Connection string**

.. credential-azure-blob-storage-connection-string-start

A connection string allows access to a location within your |destination-name| storage account. A connection string is a combination of your storage account and your account access key.

.. credential-azure-blob-storage-connection-string-end

.. credential-azure-blob-storage-connection-string-overview-start

A `connection string <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account>`__ |ext_link| includes the information that allows Amperity to authorize to your |destination-name| account.

.. credential-azure-blob-storage-connection-string-overview-end

.. credential-azure-blob-storage-connection-string-example-start

A connection string is similar to:

::

   DefaultEndpointsProtocol=https;
   AccountName=name;AccountKey=key

.. credential-azure-blob-storage-connection-string-example-end






**Container**

.. credential-azure-blob-storage-container-start

A container organizes a set of blobs, similar to a directory in a file system. Your |destination-name| account can include an unlimited number of containers. Each container can store an unlimited number of blobs.

A container name must be a valid DNS name, as it forms part of the unique uniform resource identifier (URI) used to address the container or its blobs.

The value of the blob within the URI must be configured as the value for the **Container** setting within Amperity.

.. credential-azure-blob-storage-container-end

**Shared access signature**

.. credential-azure-blob-storage-shared-access-signature-start

A shared access signature (SAS) grants limited access to containers and blobs in your storage account. The value of a SAS is the URI for the resource to which the SAS delegates access, followed by the SAS token.

.. credential-azure-blob-storage-shared-access-signature-end

.. credential-azure-blob-storage-shared-access-signature-overview-start

A `service-level shared access signature (SAS) <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>`__ |ext_link| specifies which resources in your |destination-name| account can be accessed, what permissions that access allows on resources in the container, and the length of time for which the SAS is valid.

.. credential-azure-blob-storage-shared-access-signature-overview-end

.. credential-azure-blob-storage-shared-access-signature-permissions-start

When Microsoft Azure is configured to use a shared access signature (SAS) to grant restricted access rights to Microsoft Azure storage resources, be sure to use the correct SAS token string for credentials within Amperity and that the SAS is assigned the following permissions within Microsoft Azure: READ, ADD, CREATE, WRITE, DELETE, and LIST.

.. credential-azure-blob-storage-shared-access-signature-permissions-end

**Storage URI**

.. credential-azure-blob-storage-storage-uri-start

A URI for |destination-name| that contains the name of the account and the name of the container in which blob storage is located. For example:

::

   https://myaccount.blob.core.windows.net/mycontainer

.. credential-azure-blob-storage-storage-uri-end

.. credential-azure-blob-storage-storage-uri-overview-start

Each |destination-name| resource has a `storage URI <https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#resource-uri-syntax>`__ |ext_link|, which contains the name of the account and the name of the container in which blob storage is located.

.. credential-azure-blob-storage-storage-uri-overview-end
