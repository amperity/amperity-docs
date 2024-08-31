.. 
.. /markdown
.. 

.. |destination-name| replace:: SFTP
.. |file-format| replace:: Apache Parquet, CSV, Custom delimiter, JSON, NDJSON, PSV, or TSV
.. |sftp-hostname| replace:: "sftp.acme.com"
.. |remote-folder| replace:: "/folder/name"
.. |sftp-port| replace:: "22"
.. |what-send| replace:: Apache Parquet, CSV, JSON, NDJSON, PSV, or TSV files
.. |where-send| replace:: any SFTP site


SFTP
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-sftp-about-start
   :end-before: .. setting-sftp-about-end


Requirements
==================================================

.. TODO: This destination has the following requirements.

.. setting-sftp-requirements-start

#. The hostname and port for the SFTP site to which data will be sent. For example, |sftp-hostname| (hostname) and |sftp-port| (port).
#. A username and passphrase.
#. The host public key when encryption is configured.
#. The name of the remote folder to which Amperity will send data. This must begin with a forward slash ("/"). For example: |remote-folder|.
#. The public key to use when Amperity is configured to send files to the bucket using Pretty Good Privacy (PGP) encryption.
#. The private key if the "private-key" credential type is selected.

.. setting-sftp-requirements-end


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


**Header**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-header-start
      :end-before: .. setting-common-header-end


**Line ending**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-line-ending-start
      :end-before: .. setting-common-line-ending-end


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


**Remote folder**

   **Required**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-remote-folder-start
      :end-before: .. setting-common-remote-folder-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-remote-folder-forward-slash-start
      :end-before: .. setting-common-remote-folder-forward-slash-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-remote-folder-spaces-start
      :end-before: .. setting-common-remote-folder-spaces-end


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
