.. 
.. /markdown
.. 

.. |destination-name| replace:: Amazon S3
.. |file-format| replace:: Apache Parquet, CSV, Custom delimiter, JSON, NDJSON, PSV, or TSV
.. |remote-folder| replace:: "/folder/name"


Amazon S3
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-s3-about-start
   :end-before: .. setting-amazon-s3-about-end


Requirements
==================================================

.. TODO: This destination has the following requirements.

#. An Amazon S3 bucket that is already configured to use credentials or cross-account role assumption.
#. The name of the S3 bucket to which Amperity will send data.
#. The Amazon S3 prefix for the location in the Amazon S3 bucket to which Amperity will send data.
#. The public key to use when Amperity is configured to send files to the bucket using Pretty Good Privacy (PGP) encryption.


Settings
==================================================

.. TODO: Configure the following settings.

**Compression**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-compression-start
      :end-before: .. setting-common-compression-end


**Escape character**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-escape-character-start
      :end-before: .. setting-common-escape-character-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-escape-character-unspecified-start
      :end-before: .. setting-common-escape-character-unspecified-end


**File format**

   **Required**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-file-format-start
      :end-before: .. setting-common-file-format-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-file-format-custom-delimiter-start
      :end-before: .. setting-common-file-format-custom-delimiter-end

   **Apache Parquet files only**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-file-format-apache-parquet-start
      :end-before: .. setting-common-file-format-apache-parquet-end


**Filename template**

   .. include:: ../../shared/terms.rst
      :start-after: .. term-filename-template-start
      :end-before: .. term-filename-template-end


**Header?**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-header-start
      :end-before: .. setting-common-header-end


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


**S3 prefix**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-amazon-s3-prefix-start
      :end-before: .. setting-amazon-s3-prefix-end


**Success file**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-success-file-start
      :end-before: .. setting-common-success-file-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-success-file-downstream-start
      :end-before: .. setting-common-success-file-downstream-end


**Use Zip64?**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-use-zip64-start
      :end-before: .. setting-common-use-zip64-end
