.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        About details that are common to files that can be pulled to or sent from Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        About details that are common to files that can be pulled to or sent from Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        About file formats

==================================================
About file formats
==================================================

.. format-common-start

Details that are common to files that can be pulled to or sent from Amperity using Amazon S3, Azure Blob Storage, Google Cloud Storage, or any SFTP site.

.. format-common-end

.. _format-common-pull:

Pull files to Amperity
==================================================

.. format-common-pull-start

The following sections apply to all files that are pulled to Amperity:

* :ref:`format-common-pull-credentials`
* :ref:`format-common-pull-files`
* :ref:`format-common-pull-date-formats`
* :ref:`format-common-pull-file-compression`

.. format-common-pull-end


.. _format-common-pull-credentials:

Connect to source
--------------------------------------------------

.. format-common-pull-credentials-start

Amperity requires the ability to connect to, and then read data from a filedrop location. The credentials that allow that connection and the permissions to read data are entered into the Amperity user interface while configuring a courier. These credentials are created and managed by the owner of the filedrop location, which is often external to Amperity (but is sometimes a system that is owned by Amperity). The customer may need to provide credentials to Amperity using SnapPass to complete the configuration.

.. format-common-pull-credentials-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-snappass-start
   :end-before: .. term-snappass-end


.. _format-common-pull-files:

Pull file formats
--------------------------------------------------

.. format-common-pull-files-start

Amperity supports the following file formats when using a filedrop location to pull data to Amperity:

* :doc:`Apache Avro <format_avro>`
* :doc:`Apache Parquet <format_parquet>`
* :doc:`CBOR <format_cbor>`
* :doc:`CSV <format_csv>`
* :doc:`JSON <format_json>`
* :doc:`NDJSON <format_ndjson>`
* :doc:`PSV <format_psv>`
* :doc:`Streaming JSON <format_json_streaming>`
* :doc:`TSV <format_tsv>`
* :doc:`XML <format_xml>`

.. format-common-pull-files-end

.. vale off

.. format-common-pull-files-note-start

.. note:: Amperity can ingest data from a wide variety of data sources, such as legacy data outputs like :ref:`AS/400 <format-csv-pull-couriers-as400>`. Ask your Amperity Support representative about formats that are not directly listed to determine if those data formats can be used as a way to provide data to Amperity.

.. format-common-pull-files-note-end

.. vale on


.. _format-common-pull-date-formats:

Date formats
--------------------------------------------------

.. vale off

.. format-common-pull-date-formats-start

Dates should be quoted and should be in the "yyyy-MM-dd HH:mm:ss.SSS" format. The time portion (":mm:ss.SSS") is optional. For example:

* 2019-01-28 18:32:05.123
* 2019-01-28 18:32:05
* 2019-01-28

When the date format is not similar to the expected date format, Amperity attempts to convert the date and time values. If date formats are mixed, Amperity uses the first date format that matches.

.. format-common-pull-date-formats-end

.. vale on

.. format-common-pull-date-formats-tip-start

.. tip:: Spark SQL may be used to transform source data into a supported date format prior to loading it to Amperity.

.. format-common-pull-date-formats-tip-end


.. _format-common-pull-date-formats-date-values:

Date values conversion order
++++++++++++++++++++++++++++++++++++++++++++++++++

.. vale off

.. format-common-pull-date-formats-date-values-start

Date values are converted in the following order of precedence:

.. list-table::
   :widths: 20 200 200
   :header-rows: 1

   * - --
     - Date type
     - Format
   * - 1
     - basic-date
     - "yyyyMMdd"
   * - 2
     - date
     - "yyyy-MM-dd"
   * - 3
     - slash-date
     - "yyyy/MM/dd"
   * - 4
     - us-date-4y
     - "MM/dd/yyyy"
   * - 5
     - us-date-2y
     - "MM/dd/yy"
   * - 6
     - date-month-4y
     - "dd-MMM-yyyy"
   * - 7
     - date-month-2y
     - "dd-MMM-yy"
   * - 8
     - date-month-4y-spaced
     - "dd MMM yyyy"
   * - 9
     - date-month-4y-no-space
     - "ddMMMyyyy"

.. format-common-pull-date-formats-date-values-end

.. vale on


.. _format-common-pull-date-formats-time-values:

Time values conversion order
++++++++++++++++++++++++++++++++++++++++++++++++++

.. vale off

.. format-common-pull-date-formats-time-values-start

Time values, when present, are converted in the following order of precedence:

.. list-table::
   :widths: 20 200 200
   :header-rows: 1

   * - --
     - Date type
     - Format
   * - 1
     - basic-time-Z
     - "HHmmssZ"
   * - 2
     - basic-time
     - "HHmmss"
   * - 3
     - basic-time-millis-Z
     - "HHmmss.SSSSSSSSSZ"
   * - 4
     - basic-time-millis
     - "HHmmss.SSSSSSSSS"
   * - 5
     - 24-hour-minute-second-millis-zone
     - "HH:mm:ss.SSS z"
   * - 6
     - 24-hour-minute-second-millis-Z
     - "HH:mm:ss.SSSSSSSSSZ"
   * - 7
     - 24-hour-minute-second-millis
     - "HH:mm:ss.SSSSSSSSS"
   * - 8
     - 24-hour-minute-second-Z
     - "HH:mm:ssZ"
   * - 9
     - 24-hour-minute-second
     - "HH:mm:ss"
   * - 10
     - 24-hour-minute
     - "HH:mm"
   * - 11
     - 24-hour
     - "HH"
   * - 12
     - 12-hour-minute-second
     - "hh:mm:ss a"
   * - 13
     - 12-hour-minute
     - "hh:mm a"
   * - 14
     - 12-hour-minute-zone
     - "hh:mma z"

.. format-common-pull-date-formats-time-values-end

.. vale on


.. _format-common-pull-file-compression:

File compression / archive
--------------------------------------------------

.. format-common-pull-file-compression-start

Amperity supports the following compression and archiving formats:

* Tar
* Tgz
* Zip
* GZip

.. format-common-pull-file-compression-end


.. _format-common-pull-file-compression-large-datasets:

Large datasets
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-large-dataset-start
   :end-before: .. term-large-dataset-end

.. format-common-pull-file-compression-large-datasets-start

Amperity recommends that large datasets:

* Be provided to Amperity using Amazon S3, Azure Blob Storage, or Google Cloud Storage to use their massively parallel I/O capabilities
* Use compression to reduce file sizes
* In certain cases, may use the Amperity Streaming Ingest API to avoid batched data drops

.. format-common-pull-file-compression-large-datasets-end


.. _format-common-send-input-examples:

Input examples
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-common-send-input-examples-start

The following examples show how files input to Amperity are unpacked, depending on various combinations of encryption, compression type, and file format. All examples use ``yyyy_MM_dd`` for the date format.

.. format-common-send-input-examples-end


.. _format-common-send-input-examples-single:

for single files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-common-send-input-examples-single-start

**PGP, TGZ, CSV**

#. Input to Amperity: *table_name_yyyy_MM_dd.tgz.pgp*
#. After decryption: *table_name_yyyy_MM_dd.tgz*
#. After decompression: *table_name_yyyy_MM_dd.csv*

**PGP, GZip, TAR, CSV**

#. Input to Amperity: *table_name_yyyy_MM_dd.csv.tar.gz.pgp*
#. After decryption: *table_name_yyyy_MM_dd.csv.tar.gz*
#. After decompression: *table_name_yyyy_MM_dd.csv.tar*
#. After the archive is opened: *table_name_yyyy_MM_dd.csv*

**PGP, TAR, Apache Parquet**

#. Input to Amperity: *table_name_yyyy_MM_dd.tar.pgp*
#. After decryption: *table_name_yyyy_MM_dd.tar*
#. After decompression: *table_name_yyyy_MM_dd.parquet*, with 1 to n Apache Parquet part files within the directory.

.. format-common-send-input-examples-single-end


.. _format-common-send-input-examples-multiple:

for multiple files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-common-send-input-examples-multiple-start

**PGP, TAR, Apache Parquet**

#. Input to Amperity: *input_name_yyyy_MM_dd.parquet.tar.pgp*
#. After decryption: *input_name_yyyy_MM_dd.parquet.tar*
#. After decompression: *table_name_yyyy_MM_dd.parquet*, where, for each table, 1 to n Apache Parquet files will be located within a single directory.

**PGP, TGZ, CSV**

#. Input to Amperity: *input_name_yyyy_MM_dd.csv.tgz.pgp*
#. After decryption: *input_name_yyyy_MM_dd.csv.tgz*
#. After decompression: *table_name.csv*, where all tables that were input are located within a single directory.

.. format-common-send-input-examples-multiple-end


.. _format-common-send:

Send files from Amperity
==================================================

.. format-common-send-start

The following sections apply to all files that are sent from Amperity:

* :ref:`format-common-send-credentials`
* :ref:`format-common-send-files`
* :ref:`format-common-send-file-template-patterns`
* :ref:`format-common-send-file-compression`

.. format-common-send-end


.. _format-common-send-credentials:

Connect to destination
--------------------------------------------------

.. format-common-send-credentials-start

Amperity requires the ability to connect, and then write data to the location in which files will be dropped. The credentials that allow Amperity to write data to that location are configured in Amperity. If this location is not managed by Amperity, the customer need to provide these credentials to Amperity using SnapPass to complete the configuration.

.. format-common-send-credentials-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-snappass-start
   :end-before: .. term-snappass-end


.. _format-common-send-files:

Send file formats
--------------------------------------------------

.. format-common-pull-files-start

Amperity supports the following file formats when sending files from Amperity:

* :ref:`Apache Parquet <format-parquet-destination>`
* :ref:`CSV <format-csv-destination>`
* :ref:`JSON <format-json-destination>`
* :ref:`NDJSON <format-ndjson-destination>`
* :ref:`PSV <format-psv-destination>`
* :ref:`TSV <format-tsv-destination>`

.. format-common-send-files-end


.. _format-common-send-file-template-campaigns:

Campaign template patterns
--------------------------------------------------

.. TODO: Deprecate this when campaign revamp is complete.

.. include:: ../../legacy/source/data_templates.rst
   :start-after: .. data-templates-campaigns-start
   :end-before: .. data-templates-campaigns-end


.. _format-common-send-file-template-campaign-name:

Campaign names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../legacy/source/data_templates.rst
   :start-after: .. data-templates-campaigns-campaign-name-start
   :end-before: .. data-templates-campaigns-campaign-name-end


.. _format-common-send-file-template-group-name:

Group names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../legacy/source/data_templates.rst
   :start-after: .. data-templates-campaigns-group-name-start
   :end-before: .. data-templates-campaigns-group-name-end


.. _format-common-send-file-template-list-name:

List names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../legacy/source/data_templates.rst
   :start-after: .. data-templates-campaigns-list-name-start
   :end-before: .. data-templates-campaigns-list-name-end


.. _format-common-send-file-template-patterns:

Filename template patterns
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-filename-template-start
   :end-before: .. term-filename-template-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-joda-time-start
   :end-before: .. term-joda-time-end


.. _format-common-send-file-compression:

File compression
--------------------------------------------------

.. format-common-send-file-compression-start

Amperity supports the following compression and archiving formats:

* Tar
* Tgz
* Zip
* GZip

When Tar or Zip options are not specified, a folder is created using the name filename template specified for the orchestration. This folder contains one or more files, each of which have generated names.

.. tip:: Compression and archive file extensions are not added to the filename template automatically. These may be added while configuring an orchestration. To add the file compression format to the output filename, append .tar, .tgz, .zip, or .gz after the file format extension in the filename template. For example: parquet.tar, csv.zip, or tsv.gz.

.. format-common-send-file-compression-end


.. _format-common-send-output-examples:

Output examples
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-common-send-output-examples-start

The following examples show how files output by Amperity are named depending on the various combination of options for file format, compression type, and encryption that are available. All examples use ``yyyy_MM_dd`` for the date format.

.. format-common-send-output-examples-end


.. _format-common-send-output-examples-queries:

for queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-common-send-output-examples-queries-start

**Apache Parquet, TAR, PGP**

#. Output from Amperity: *query_name_yyyy_MM_dd.tar.pgp*
#. After decryption: *query_name_yyyy_MM_dd.tar*
#. After decompression: *query_name_yyyy_MM_dd.parquet*, with 1 to n Apache Parquet part files within the directory.

**CSV, TGZ, PGP**

#. Output from Amperity: *query_name_yyyy_MM_dd.tgz.pgp*
#. After decryption: *query_name_yyyy_MM_dd.tgz*
#. After decompression: *query_name_yyyy_MM_dd.csv*

**CSV, GZip, PGP**

#. Output from Amperity: *query_name_yyyy_MM_dd.csv.gz.pgp*
#. After decryption: *query_name_yyyy_MM_dd.csv.gz*
#. After decompression: *query_name_yyyy_MM_dd.csv*

.. format-common-send-output-examples-queries-end


.. _format-common-send-output-examples-single:

for single tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-common-send-output-examples-single-start

**Apache Parquet, TAR, PGP**

#. Output from Amperity: *table_name_yyyy_MM_dd.tar.pgp*
#. After decryption: *table_name_yyyy_MM_dd.tar*
#. After decompression: *table_name_yyyy_MM_dd.parquet*, with 1 to n Apache Parquet part files within the directory.

**CSV, TGZ, PGP**

#. Output from Amperity: *table_name_yyyy_MM_dd.tgz.pgp*
#. After decryption: *table_name_yyyy_MM_dd.tgz*
#. After decompression: *table_name_yyyy_MM_dd.csv*

**CSV, GZip, PGP**

#. Output from Amperity: *table_name_yyyy_MM_dd.csv.gz.pgp*
#. After decryption: *table_name_yyyy_MM_dd.csv.gz*
#. After decompression: *table_name_yyyy_MM_dd.csv*

.. format-common-send-output-examples-single-end


.. _format-common-send-output-examples-multiple:

for multiple tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-common-send-output-examples-multiple-start

**Apache Parquet, TAR, PGP**

#. Output from Amperity: *output_name_yyyy_MM_dd.parquet.tar.pgp*
#. After decryption: *output_name_yyyy_MM_dd.parquet.tar*
#. After decompression: *table_name_yyyy_MM_dd.parquet*, where, for each table, 1 to n Apache Parquet files will be located within a single directory.

**CSV, TGZ, PGP**

#. Output from Amperity: *output_name_yyyy_MM_dd.csv.tgz.pgp*
#. After decryption: *output_name_yyyy_MM_dd.csv.tgz*
#. After decompression: *table_name.csv*, where all tables that were output are located within a single directory.

.. format-common-send-output-examples-multiple-end


.. _format-common-ssh-and-encryption:

SFTP and encryption
==================================================

.. format-common-encryption-start

You must use encryption when using Secure File Transfer Protocol (SFTP) to transfer files to and from Amperity. Encryption protects the information in the files and requires the use of secure protocols and encryption programs:

* :ref:`Secure Shell (SSH) <format-common-ssh>` is a secure protocol that protects your files as they are transferred to and from Amperity
* :ref:`Pretty Good Privacy (PGP) <format-common-pgp>` is an encryption program that signs, encrypts, and decrypts files, protecting your files while they are at rest

.. format-common-encryption-end


.. _format-common-ssh:

Secure Shell (SSH)
--------------------------------------------------

.. format-common-ssh-start

Secure Shell (SSH) is a secure protocol that protects your files while they are transferred to and from Amperity.

.. format-common-ssh-end

.. format-common-ssh-rsa-preferred-start

.. important:: Amperity prefers using RSA as the encryption format for `generating SSH keys <https://www.ssh.com/academy/ssh/keygen>`__ |ext_link| that are used by SFTP connections to pull data to or send data from Amperity. Amperity prefers the size of the SSH key to be 4096 bits.

   Amperity also supports the ECDSA and EC25519 encryption formats.

.. format-common-ssh-rsa-preferred-end


.. _format-common-public-key-for-sftp:

Generate SSH keypairs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-rsa-start
   :end-before: .. term-rsa-end

**To generate SSH keypairs**

.. format-common-pull-credentials-sftp-steps-start

#. Run the following command to generate an RSA key pair:

   .. code-block:: console

      $ ssh-keygen -t rsa -m PEM -f generated-key

   This writes two files: generated-key (the private key) and generated-key.pub (the public key).

#. The location in which the public and private keys should be placed depends on the location to which data is transferred.
#. Add the public key to the SFTP location from which data is sent to Amperity.
#. Add the private key to the Amperity SFTP courier.

.. format-common-pull-credentials-sftp-steps-end


.. _format-common-pgp:

Pretty Good Privacy (PGP)
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pgp-start
   :end-before: .. term-pgp-end

.. format-common-pgp-start

PGP helps protect your files while they are at rest. Amperity recommends to use:

* 4096-bit keys
* A strong passphrase
* One PGP key per-tenant (minimum). One PGP key per system (recommended)

Files that are encrypted using PGP are appended with the .pgp extension.

.. format-common-pgp-end

.. format-common-pgp-important-subkeys-start

.. important:: PGP public keys have two types: a primary key and a subkey. Amperity does not allow the use of a primary key for public-private key encryption. If you attempt to use a primary key you will see an error similar to "Destination failed validation: PGP public key is a primary key. Please provide a subkey or a keyring with exactly one subkey."

.. format-common-pgp-important-subkeys-end


.. _format-common-pgp-encryption:

Encrypt files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-common-pgp-encryption-start

Any tool that is compliant with the OpenPGP standard, as defined by `RFC 4880 <https://tools.ietf.org/html/rfc4880>`__ |ext_link| may be used for PGP encryption. For example:

* GNU Privacy Guard. Available from `https://www.gnupg.org/ <https://www.gnupg.org/>`__ |ext_link|. Instructions for how to use GNU Privacy Guard are from that site.
* GPG Tools. Available from `https://gpgtools.org/ <https://gpgtools.org/>`__ |ext_link|. Instructions for how to use GPG Tools are from that site.

.. format-common-pgp-encryption-end

**Use PGP encryption with destinations**

.. format-common-pgp-sources-start

To use PGP encryption with data sources use the **PGP credentials** setting to select a PGP credential. For new keys, use the **PGP credentials** setting to assign the credential a name and description, a passphrase, and then the public key that is used to encrypt data.

.. caution:: Be sure to include the ``BEGIN PGP PUBLIC KEY BLOCK`` and ``END PGP PUBLIC KEY BLOCK`` header and footer in the key. Only users and systems with access to the private key is able to decrypt this data. Use Snappass to share the public key.

.. format-common-pgp-sources-end

.. TODO: Saving this, for now.
.. 
.. .. tip:: Use the following command to encrypt a file:
.. 
..    ::
.. 
..       $ gpg --encrypt --recipient s3@acme.amperity.com data.csv
.. 
..    This will encrypt a file named "data.csv" and will output a file named "data.csv.gpg". Change ``data.csv`` to the name of the file to be encrypted. Change ``s3@acme.amperity.com`` to the location in Amperity to which the data is sent.
.. 


.. _format-common-pgp-decryption:

Decrypt files
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-common-pgp-decryption-start

Any tool that is compliant with the OpenPGP standard, `as defined by RFC4880 <https://tools.ietf.org/html/rfc4880>`__ may be used for PGP decryption. For example:

* GNU Privacy Guard. Available from https://www.gnupg.org/. Instructions for how to use GNU Privacy Guard are from that site.
* GPG Tools. Available from https://gpgtools.org/. Instructions for how to use GPG Tools are from that site.

.. format-common-pgp-decryption-end

**Add PGP decryption to data sources**

.. format-common-pgp-sources-start

To use PGP decryption with data sources use the **PGP credentials** setting to select a PGP credential. For new keys, use the **PGP credentials** setting to assign the credential a name and description, a passphrase, and then the private key that is used to decrypt data.

.. note:: Some data sources require you to switch to the legacy editor before you can configure PGP credentials. This link is at the top of the page when you are creating a courier and is named "Switch to legacy editor".

.. caution:: Be sure to include the ``BEGIN PGP PRIVATE KEY BLOCK`` and ``END PGP PRIVATE KEY BLOCK`` header and footer in the key.

   Anyone with access to the decryption key is capable of decrypting data that has been encrypted with the corresponding public key. Please keep both public and private keys confidential. Use Snappass to share the private key.

.. format-common-pgp-sources-end

.. TODO: Saving this, for now
.. 
.. .. tip:: Use the following command to `decrypt a file <https://www.gnupg.org/gph/en/manual/x110.html>`__:
.. 
..    ::
.. 
..       $ gpg --decrypt --recipient [location]@acme.amperity.com data.csv.gpg
.. 
..    This will decrypt a file named "data.csv.gpg" and will output a file named "data.csv". Change ``data.csv`` to the name of the file to be decrypted. Change ``[location]`` to the parameter that indicates the cloud platform to which the data is sent.
.. 


.. _format-common-transfer-data:

About data transfers
--------------------------------------------------

.. format-common-transfer-data-start

You must use encryption while transferring files to and from Amperity. SSH protects your files as they are transferred to and from Amperity. PGP protects your files while they are at rest.

The combination of public and private keys that are used for a specific workflow depends on if data is being :ref:`pulled to Amperity from an upstream system <format-common-pull-files-to-amperity>` or if data is being :ref:`sent from Amperity to a downstream system <format-common-send-files-from-amperity>`.

.. format-common-transfer-data-end


.. _format-common-pull-files-to-amperity:

Pull files to Amperity
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-common-pull-files-to-amperity-start

When Amperity pulls files from upstream systems using SFTP, use the following combinations for SSH and PGP keys:

**for SSH**

#. The owner of the upstream system creates the SSH keypair and will maintain the private SSH key.

#. The public SSH key is configured in Amperity. You may send the public SSH key to your Amperity representative using SnapPass.


**for PGP**

#. Amperity Support creates the PGP keypair and will maintain the private PGP key.

#. Amperity Support sends you the public PGP key using SnapPass. The owner of the upstream system will encrypt files using the public PGP key prior to adding the files to the location from which Amperity will pull data.

   .. tip:: Use :ref:`file compression <format-common-pull-file-compression>` *before* encrypting files. Compression applied *after* encryption will not reduce the size of the file.

#. Amperity uses the private PGP key to decrypt files pulled from the upstream system.

.. format-common-pull-files-to-amperity-end


.. _format-common-send-files-from-amperity:

Send files from Amperity
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-common-send-files-from-amperity-start

When Amperity sends files to downstream systems using SFTP, use the following combinations for SSH and PGP keys:

**for SSH**

#. Amperity Support creates the SSH keypair and will maintain the private SSH key

#. Amperity Support sends you the public SSH key using SnapPass. Add the public SSH key to the downstream system to which Amperity is configured to send data

**for PGP**

#. The owner of the downstream system creates the PGP keypair and maintains the private PGP key. You may send the public PGP key to your Amperity representative using SnapPass

#. Amperity uses the public PGP key to encrypt files before sending them to the downstream system.

#. The downstream system uses the private PGP key to decrypt files sent from Amperity

.. format-common-send-files-from-amperity-end


.. _format-common-pgp-key-rotations:

Key rotations
--------------------------------------------------

.. format-common-pgp-key-rotations-start

Amperity performs key rotations on a periodic basis as a best practice. Key rotations are sometimes necessary in situations where a key may have been compromised. When a key rotation happens, Amperity will:

#. Generate a key pair
#. Create a keyring file that contains the old and new private keys and uses the same passphrase
#. Install the keyring file to the courier
#. Share the new public key with the customer using SnapPass
#. Wait for confirmation from the customer that the public key is updated
#. Create a keyring file that contains *only* the updated private key
#. Install the keyring file that contains *only* the updated private key to the courier

.. format-common-pgp-key-rotations-end
