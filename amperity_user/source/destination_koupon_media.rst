.. https://docs.amperity.com/user/


.. |destination-name| replace:: Koupon Media
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **koupon-media**
.. |sftp-hostname| replace:: **sftp.kouponmedia.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Koupon Media.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Koupon Media.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Koupon Media

==================================================
Send query results to Koupon Media
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-koupon-media-start
   :end-before: .. term-koupon-media-end

.. sendto-koupon-media-channel-types-start

You can associate records in Amperity to the following `Koupon Media channel types <https://www.kouponmedia.com/creating-channel>`__ |ext_link|:

#. Web application channels
#. Mobile application channels
#. SMS channels
#. Email channels
#. Social channels

.. sendto-koupon-media-channel-types-end

.. sendto-koupon-media-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-koupon-media-build-query>`
#. :ref:`Add orchestration <sendto-koupon-media-add-orchestration>`
#. :ref:`Run orchestration <sendto-koupon-media-run-orchestration>`

.. sendto-koupon-media-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-koupon-media-build-query:

Build query
==================================================

.. sendto-koupon-media-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Koupon Media. Data shaping is typically required only one time.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to add a SQL query that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use cases for downstream workflows.

.. sendto-koupon-media-build-query-end


.. _sendto-koupon-media-build-query-map-to-channel:

Map to channel
--------------------------------------------------

.. sendto-koupon-media-build-query-map-to-channel-start

.. important:: The output sent to Koupon Media can vary, depending on the channel for which the data is being used and if any data from other data sources are appended or joined to the output.

A query sent to Koupon Media will result in defining a mapping of fields in Amperity to the fields required by the channel to which the query is sent. These mappings are similar to:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS ROW_ID
     ,given_name AS FST_NAME
     ,surname AS LST_NAME
     ,address AS ADDR_LINE_1
     ,address2 AS ADDR_LINE_2
     ,city AS CITY_NAME
     ,state AS STATE_PROVINCE_CD
     ,postal AS POSTAL_CD
     ,phone_mobile AS CELLNAME
     ,'' AS CUSTOMFIELD1
     ,'' AS CUSTOMFIELD2
     ,'' AS CUSTOMFIELD3
     ,'' AS CUSTOMFIELD4
     ,'' AS CUSTOMFIELD5
     ,'' AS CUSTOMFIELD6
     ,'' AS CUSTOMFIELD7
     ,'' AS CUSTOMFIELD8
     ,'' AS CUSTOMFIELD9
     ,'' AS CUSTOMFIELD10
     ,'' AS CUSTOMFIELD11
     ,'' AS CUSTOMFIELD12
     ,'' AS CUSTOMFIELD13
     ,'' AS CUSTOMFIELD14
     ,'' AS CUSTOMFIELD15
     ,'' AS CUSTOMFIELD16
     ,loyalty_id AS CUSTOMFIELD17
     ,'' AS CUSTOMFIELD18
     ,'' AS CUSTOMFIELD19
     ,'' AS CUSTOMFIELD20
   from TableName

where **'' AS CUSTOMFIELDx** adds the field required by the Koupon Media data structure, but without mapping it to a field and where, for example, **loyalty_id AS CUSTOMFIELD17** shows mapping the loyalty ID for customers to a field in Koupon Media.

.. tip:: The types of data that may be sent to Koupon Media from Amperity include, but are not limited to, any of the types of data that are listed in the `Koupon Media privacy policy <https://www.koupon.com/privacy>`__ |ext_link|, such as phone numbers, email addresses, clickstream data, and so on. As a general guideline, data sent from Amperity should comply with this policy.

.. sendto-koupon-media-build-query-map-to-channel-end


.. _sendto-koupon-media-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-koupon-media-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
