.. /downloads/markdown/


.. |destination-name| replace:: Azure Blob Storage
.. |file-format| replace:: Apache Parquet, CSV, Custom delimiter, JSON, NDJSON, PSV, or TSV
.. |remote-folder| replace:: "/folder/name"
.. |what-send| replace:: Apache Parquet, CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any Azure Blob Storage container


Azure Blob Storage
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-azure-blob-storage-about-start
   :end-before: .. setting-azure-blob-storage-about-end


Credentials
==================================================

**Connection string** credentials a connection string and the name of the Azure Blob Storage container.

**Shared access signature** credentials require the account name, a shared access signature, and the name of the Azure Blob Storage container.

**Storage URI** credentials require a storage URI and the name of the Azure Blob Storage container.


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

**File format**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-start
   :end-before: .. setting-common-file-format-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-custom-delimiter-start
   :end-before: .. setting-common-file-format-custom-delimiter-end

Apache Parquet files only:

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-apache-parquet-start
   :end-before: .. setting-common-file-format-apache-parquet-end

**Escape character**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-escape-character-start
   :end-before: .. setting-common-escape-character-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-escape-character-unspecified-start
   :end-before: .. setting-common-escape-character-unspecified-end

**Filename template**

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end

**Line ending**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-line-ending-start
   :end-before: .. setting-common-line-ending-end

**Compression**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-compression-start
   :end-before: .. setting-common-compression-end

**PGP public key**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-pgp-public-key-start
   :end-before: .. setting-common-pgp-public-key-end

**Quote mode**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-quote-mode-start
   :end-before: .. setting-common-quote-mode-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-quote-mode-none-start
   :end-before: .. setting-common-quote-mode-none-end

**Parquet extension**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-parquet-extension-start
   :end-before: .. setting-common-parquet-extension-end

**Success file**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-success-file-start
   :end-before: .. setting-common-success-file-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-success-file-downstream-start
   :end-before: .. setting-common-success-file-downstream-end

**Header**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-header-start
   :end-before: .. setting-common-header-end

**Row number**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-row-number-start
   :end-before: .. setting-common-row-number-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-row-number-column-name-start
   :end-before: .. setting-common-row-number-column-name-end

**Use Zip64?**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-use-zip64-start
   :end-before: .. setting-common-use-zip64-end
