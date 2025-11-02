.. 
.. xxxxx
..



.. vale off

**SECTIONS FOR SHARED FILE FORMATS**

.. vale on


.. formats-filedrop-common-start

You may reference the following sections while configuring this data source:

* Using credentials that |format_common_allow_access| from this location
* Adding an optional |format_common_rsa_keys|
* Ensuring files are provided in a |format_common_file_formats|
* Ensuring files are provided with the correct |format_common_date_formats|
* Supporting the desired |format_common_file_compression_archive| method
* Encrypting files before they are added to the location using |format_common_pgp|. An encryption key must be configured so that files can be decrypted by Amperity prior to loading them

  .. tip:: Use SnapPass to securely share your organization's credentials and encryption keys with your Amperity representative.

.. formats-filedrop-common-end


.. formats-json-rfc-8259-start

JSON files that are used as source data with Amperity must follow `RFC 8259 <https://datatracker.ietf.org/doc/html/rfc8259>`__ |ext_link|, which requires using, at a minimum, the UTF-8 encoding format.

.. formats-json-rfc-8259-end
