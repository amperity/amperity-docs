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


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Hostname**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-hostname-start
   :end-before: .. credential-sftp-hostname-end

**Port**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-port-start
   :end-before: .. credential-sftp-port-end

**Username**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-username-start
   :end-before: .. credential-sftp-username-end

**Host public key**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-host-public-key-start
   :end-before: .. credential-sftp-host-public-key-end

**Private key**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-private-key-start
   :end-before: .. credential-sftp-private-key-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-private-key-required-start
   :end-before: .. credential-sftp-private-key-required-end

**Passphrase**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-passphrase-start
   :end-before: .. credential-sftp-passphrase-end


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

**Remote folder**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-remote-folder-start
   :end-before: .. setting-common-remote-folder-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-remote-folder-forward-slash-start
   :end-before: .. setting-common-remote-folder-forward-slash-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-remote-folder-spaces-start
   :end-before: .. setting-common-remote-folder-spaces-end

**File format**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-start
   :end-before: .. setting-common-file-format-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-file-format-custom-delimiter-start
   :end-before: .. setting-common-file-format-custom-delimiter-end

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

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-vibes-filename-template-pattern-start
   :end-before: .. setting-vibes-filename-template-pattern-end

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
