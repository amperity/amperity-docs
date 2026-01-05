.. https://docs.amperity.com/user/


.. |destination-name| replace:: Persado
.. |what-send| replace:: marketing campaign engagement or segment data files
.. |sftp-type| replace:: **persado**
.. |sftp-hostname| replace:: **psftp.persado.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Persado.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Persado.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Persado

==================================================
Send query results to Persado
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-persado-start
   :end-before: .. term-persado-end

.. sendto-persado-about-start

Use data from Amperity in Persado to:

* Dynamically use segments to identify high value or high potential customers
* Generate personalized messaging using precise segments across channels, including email, web, short message service (SMS), push, paid media, and interactive voice response (IVR)
* Automatically track user-level data for conversions and revenue 

.. sendto-persado-about-end

.. sendto-persado-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-persado-build-query>`
#. :ref:`Add orchestration <sendto-persado-add-orchestration>`
#. :ref:`Run orchestration <sendto-persado-run-orchestration>`

.. sendto-persado-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-persado-build-query:

Build query
==================================================

.. sendto-persado-build-query-start

You may need to build queries that shape data into one of the following schemas:

* :ref:`Marketing engagement data <sendto-persado-build-query-marketing-enagement>`
* :ref:`Segment data <sendto-persado-build-query-segment>`

.. sendto-persado-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-persado-build-query-marketing-enagement:

Marketing engagement data
--------------------------------------------------

.. sendto-persado-build-query-marketing-enagement-start

Marketing engagement data should be sent every 24 hours and contain only data for the previous day. You must define a segment that maps columns to the :ref:`marketing engagement data schema <sendto-persado-data-columns-marketing-engagement>` using a query similar to:

.. code-block:: sql
   :linenos:

   SELECT
     LOWER(TO_HEX(MD5(CAST(LOWER(REGEXP_REPLACE(field_name, '\+.*@', '@')) AS varbinary)))) AS Hashed_Email
     ,field_name AS Campaign_Name
     ,field_name AS Subject_Line
     ,sendid_or_jobid AS Send_ID
     ,CAST(TO_UNIXTIME(MIN(field_name)) AS bigint) AS Sent_Timestamp
     ,CAST(TO_UNIXTIME(MIN(field_name)) AS bigint) AS Bounced_Timestamp
     ,CAST(TO_UNIXTIME(MIN(field_name)) AS bigint) AS Opened_Timestamp
     ,CAST(TO_UNIXTIME(MIN(field_name)) AS bigint) AS Clicked_Timestamp
     ,CAST(TO_UNIXTIME(MIN(field_name)) AS bigint) AS Unsubscribed_Timestamp
   FROM Marketing_Engagement_Table

.. note:: The **Marketing_Engagement_Table** from which you will map data to the Persado schema will vary. For example, if Salesforce Marketing Cloud is used as part of a combined marketing effort with Persado, some combination of tables from Salesforce is the source of this data.

.. sendto-persado-build-query-marketing-enagement-end


.. _sendto-persado-build-query-segment:

Segment data
--------------------------------------------------

.. sendto-persado-build-query-segment-start

Segment data should be sent weekly. You must define a segment that maps columns to the :ref:`segment data schema <sendto-persado-data-columns-segments>` using a query similar to:

.. code-block:: sql
   :linenos:

   SELECT
     LOWER(TO_HEX(MD5(CAST(LOWER(REGEXP_REPLACE(field_name, '\+.*@', '@')) AS varbinary)))) AS Hashed_Email
     ,MIN(field_name) AS birth_dt
     ,MAX(field_name) AS gender
     ,MAX(field_name) AS state_province_cd
     ,field_name AS anniversary
     ,field_name AS wedding_dt
     ,MAX(field_name) AS loyalty
     ,MAX(field_name) AS children_count
     ,MAX(field_name) AS registration_source
     ,MAX(field_name) AS profile_compl_flag
     ,field_name AS segment_name
     ,MAX(field_name) AS segmentation_tag
   FROM Weekly_Segment_Table

.. note:: The **Weekly_Segment_Table** from which you will map data to the Persado schema will vary.

.. sendto-persado-build-query-segment-end


.. _sendto-persado-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-persado-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _sendto-persado-data-columns:

Persado data schemas
==================================================

.. sendto-persado-data-columns-start

Persado supports the following schemas:

* :ref:`Marketing engagement data <sendto-persado-data-columns-marketing-engagement>`
* :ref:`Segment data <sendto-persado-data-columns-segments>`

.. sendto-persado-data-columns-end


.. _sendto-persado-data-columns-marketing-engagement:

for marketing engagement data
--------------------------------------------------

.. sendto-persado-data-columns-marketing-engagement-start

The marketing engagement data schema supports the following fields:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Persado Column
     - Description
   * - **Bounced_Timestamp**
     - The timestamp at which the email bounced. For example: "1614080616D".

   * - **Campaign_Name**
     - The name of a campaign. May be empty.

   * - **Clicked_Timestamp**
     - The timestamp at which the customer clicked an element in the email. For example: "1614080616D".

   * - **Hashed_Email**
     - The MD5 hash of the normalized email address. A normalized email address:

       #. Converts the characters to lower case
       #. Removes the **+** character, along with any characters between the **+** and the **@** symbol
       #. Uses the **VARCHAR** data type

   * - **Opened_Timestamp**
     - The timestamp at which the customer opened the email. For example: "1614080616D".

   * - **Send_ID**
     - An ID from Salesforce Marketing Cloud for the send. Also referred to as a jobID.

   * - **Sent_Timestamp**
     - The timestamp at which the email was sent. For example: "1614080616D".

   * - **Subject_Line**
     - The Persado ID.

   * - **Unsubscribed_Timestamp**
     - The timestamp at which the customer unsubscribed. For example: "1614080616D".

.. sendto-persado-data-columns-marketing-engagement-end


.. _sendto-persado-data-columns-segments:

for segment data
--------------------------------------------------

.. sendto-persado-data-columns-segments-start

The segment data schema supports the following fields:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Persado Column
     - Description

   * - **anniversary**
     - 

   * - **birth_dt**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-birthdate-start
          :end-before: .. term-birthdate-end

       .. caution:: This field contains PII data.

   * - **closest_mik_distance**
     - 

   * - **children_count**
     - Associated with the **loyalty**, **registration_source**, and **profile_compl_flag** columns.

   * - **gender**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-gender-start
          :end-before: .. term-gender-end

       .. caution:: This field contains PII data.

   * - **Hashed_Email**
     - The MD5 hash of the normalized email address. A normalized email address:

       #. Converts the characters to lower case
       #. Removes the **+** character, along with any characters between the **+** and the **@** symbol
       #. Uses the **VARCHAR** data type

   * - **loyalty**
     - Associated with the **children_count**, **registration_source**, and **profile_compl_flag** columns.

   * - **profile_compl_flag**
     - Associated with the **children_count**, **loyalty**, and **registration_source** columns.

   * - **registration_source**
     - Associated with the **children_count**, **loyalty**, and **profile_compl_flag** columns.

   * - **segment_name**
     - 

   * - **segmentation_tag**
     - 

   * - **state_province_cd**
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-state-start
          :end-before: .. term-state-end

       .. caution:: This field contains PII data.

   * - **wedding_dt**
     - 

.. sendto-persado-data-columns-segments-end
