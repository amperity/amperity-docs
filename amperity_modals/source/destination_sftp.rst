.. 
.. /markdown
.. 

.. |destination-name| replace:: SFTP
.. |file-format| replace:: Apache Parquet, CSV, Custom delimiter, JSON, NDJSON, PSV, or TSV


SFTP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sftp-start
   :end-before: .. term-sftp-end


Requirements
==================================================

.. TODO: This destination has the following requirements.

#. The hostname and port for the SFTP site to which data will be sent. For example, "sftp.acme.com" and "20".
#. The username and passphrase.
#. The host public key (if encryption is configured).
#. A private key when the "private-key" credential type is selected.
#. The name of the remote folder to which Amperity will send data.
#. The public key to use for PGP encryption.


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


**Filename template**

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end


**Header?**

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
