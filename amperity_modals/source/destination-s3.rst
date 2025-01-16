.. /downloads/markdown/


.. |destination-name| replace:: Amazon S3
.. |file-format| replace:: Apache Parquet, CSV, Custom delimiter, JSON, NDJSON, PSV, or TSV
.. |remote-folder| replace:: "/folder/name"
.. |what-send| replace:: Apache Parquet, CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any Amazon S3 bucket


Amazon S3
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-s3-about-start
   :end-before: .. setting-amazon-s3-about-end


Credentials
==================================================

**IAM role-to-role** credentials require the name of the Amazon S3 bucket and the target role ARN. Amperity will provide the values for the Amperity role ARN and the external ID.

**IAM** credentials require the name of the Amazon S3 bucket, the IAM access key, and the IAM secret key. An IAM role ARN is optional.


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

**S3 prefix**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-s3-prefix-start
   :end-before: .. setting-amazon-s3-prefix-end

**File format**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-start
   :end-before: .. setting-common-file-format-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-custom-delimiter-start
   :end-before: .. setting-common-file-format-custom-delimiter-end

*Apache Parquet files only*

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
