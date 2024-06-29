.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Throtle
.. |plugin-name| replace:: Amazon S3
.. |what-send| replace:: customer profile data

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Throtle.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Throtle.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Throtle

==================================================
Send query results to Throtle
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-throtle-start
   :end-before: .. term-throtle-end

.. sendto-throtle-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-throtle-build-query>`
#. :ref:`Add orchestration <sendto-throtle-add-orchestration>`
#. :ref:`Run orchestration <sendto-throtle-run-orchestration>`

.. sendto-throtle-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-throtle-build-query:

Build query
==================================================

.. sendto-throtle-build-query-start

You will need to build a query that returns the correct set of matching keys as required by |destination-name|.

.. sendto-throtle-build-query-end


.. _sendto-throtle-build-query-matching-keys:

Throtle matching keys
--------------------------------------------------

.. sendto-throtle-build-query-matching-keys-start

Throtle uses precision-level matching at an individual level for its matching process. The following identifiers are used as matching keys in |destination-name|:

#. Email address fields ("Email 1", "Email 2", "Email 3", ...)
#. First Name, Last Name, and full postal address ("Street Address 1", "Street Address 2", "City", "State", and "Zip Code")
#. Phone numbers ("Telephone") 
#. Mobile advertising IDs ("MAID 1", "MAID 2", "MAID 3", ...); examples of a mobile advertising ID include Identifier for Advertisers (IDFA) and Google Advertising ID (GAID) 
#. IP addresses in either IPv4 or IPv6 format ("IP Address")

.. sendto-throtle-build-query-matching-keys-end


.. _sendto-throtle-build-query-matching-keys-email:

Email addresses
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sendto-throtle-build-query-matching-keys-email-start

You may send email addresses using SHA-256 hashing. That said, sending email addresses as clear text allows |destination-name| to use its full set of email standardization and validation tools, which lead to higher match rates within |destination-name|. If you choose to send email addresses to |destination-name| using clear text, be sure to use PGP encryption on the file.

.. note:: Clear text email addresses should be avoided if using |destination-name| for safe haven data processing.

.. sendto-throtle-build-query-matching-keys-email-end


.. _sendto-throtle-build-query-matching-keys-privacy-safe:

Privacy Safe data processing
++++++++++++++++++++++++++++++++++++++++++++++++++

.. sendto-throtle-build-query-matching-keys-privacy-safe-start

The following identifiers are used as matching keys in |destination-name| for Privacy Safe data processing:

#. Email address fields ("Email 1", "Email 2", "Email 3", ...)

   .. important:: Email addresses must be hashed using SHA-256 when sending results for Privacy Safe data processing; clear text should be avoided.

      .. include:: ../../amperity_reference/source/sql_presto.rst
         :start-after: .. sql-presto-style-guide-one-way-sha256-hashes-start
         :end-before: .. sql-presto-style-guide-one-way-sha256-hashes-end

      .. include:: ../../amperity_reference/source/sql_presto.rst
         :start-after: .. sql-presto-style-guide-one-way-sha256-hash-syntax-start
         :end-before: .. sql-presto-style-guide-one-way-sha256-hash-syntax-end

      .. include:: ../../amperity_reference/source/sql_presto.rst
         :start-after: .. sql-presto-function-to-hex-example-one-way-hash-start
         :end-before: .. sql-presto-function-to-hex-example-one-way-hash-end

#. "First Name", "Last Name", and full postal address ("Street Address 1", "Street Address 2", "City", "State", and "Zip Code")

.. sendto-throtle-build-query-matching-keys-privacy-safe-end


.. _sendto-throtle-build-query-sql:

Define a query
--------------------------------------------------

.. sendto-throtle-build-query-sql-start

The following **SELECT** statement maps customer profile data to the set of matching key formats that are accepted by |destination-name|, including all required field names.

::

   SELECT
     amperity_id AS ID
     ,given_name AS "First Name"
     ,surname AS "Last Name"
     ,address AS "Street Address 1"
     ,address2 AS "Street Address 2"
     ,city AS "City"
     ,state AS "State"
     ,postal AS "Zip Code"
     ,phone AS "Telephone"
     ,email AS "Email 1"
     ,email_x AS "Email x" # replace "x" with 1, 2, 3, etc.
     ,mobile_advertising_id AS "MAID 1"
     ,mobile_advertising_id_x AS "MAID x" # replace "x" with 1, 2, 3, etc.
     ip_address AS "IP" # use either IPv4 or IPv6 address formats
     ,SN.Segment_Name
     ,SN.Segment_Name
     ,SN.Segment_Name
     ...
   FROM Customer_360

where **SN** represents the source name for each segment.

.. note:: There are many ways to build a **SELECT** statement that maps data from tables in Amperity to fields in |destination-name|. Refer to your specific |destination-name| field requirements, and then build your query to return the matching results. The only absolute requirement is to map an ID that is not the Amperity ID to the **customerID** field in |destination-name|. Attributes from tables in Amperity that you want to send to |destination-name| must be mapped to the field names as they are defined in |destination-name|, but there is no requirement to map to any particular attribute.

.. sendto-throtle-build-query-sql-end


.. _sendto-throtle-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-throtle-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
