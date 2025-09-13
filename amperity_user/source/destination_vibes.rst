.. https://docs.amperity.com/user/


.. |destination-name| replace:: Vibes
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **vibes**
.. |sftp-hostname| replace:: **upload.vibes.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Vibes.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Vibes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Vibes

==================================================
Send query results to Vibes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-vibes-start
   :end-before: .. term-vibes-end

.. sendto-vibes-start

You can use a flat-file (CSV) batch process to send query results from Amperity to |destination-name| to update recipient list data. This process supports downstream workflows, such as for:

* Users who interact with campaigns from mobile devices
* Interactive campaigns, including incentives, contents, and info-on-demand
* Loyalty programs and offers

Files that are sent to |destination-name| are routed based on a required filename pattern. After the files are processed, an SMS message or push notification is sent to the recipient list from the |destination-name| platform.

.. sendto-vibes-end

.. sendto-vibes-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-vibes-build-query>`
#. :ref:`Add orchestration <sendto-vibes-add-orchestration>`
#. :ref:`Run orchestration <sendto-vibes-run-orchestration>`

.. sendto-vibes-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-vibes-build-query:

Build query
==================================================

.. sendto-vibes-build-query-start

You will need to build a query that shapes data to the fields required by a |destination-name| recipient list. A recipient list is customizable, which may require a unique query for each recipient list.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to build a SQL query to filter within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

Choose the approach that works best for your use cases and downstream workflows.

.. sendto-vibes-build-query-end


.. _sendto-vibes-build-query-map-to-recipient-list:

Map to Recipient List
--------------------------------------------------

.. sendto-vibes-build-query-map-to-recipient-list-start

A `recipient list <https://developer-platform.vibes.com/docs/recipient-list-import>`__ |ext_link| is a collection of references used as a target filter for messages. A recipient list must include one of the following fields that acts as the unique ID:

#. **person_id**; must be lowercase
#. **person_key**; must be lowercase
#. **external_person_id**; a unique ID that exists in an external system
#. **mdn**; the mobile directory number (MDN)

   .. important:: The mobile directory number for phone numbers in the USA may use the 10-digit MDN format.

      The MDN for international numbers must be in E.164 format, which is a plus symbol ( + ) followed by the country code and phone number without spaces. For example: "+12205551234".

The unique ID acts as the row identifier and rows may include additional columns that act as message variables.

A SQL query built using Presto SQL can return results for use with any Vibes recipient list. For a recipient list with custom fields, add a SQL table with a **SELECT** statement similar to:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS "external_person_id"
     phone AS "mdn"
     given_name AS "first_name"
     surname AS "last_name"
     loyalty_points as "points"
   FROM customer360
   LIMIT 2000

For a recipient list that applies personalization for first name and city:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS "external_person_id"
     phone AS "mdn"
     given_name AS "personalization_1"
     city AS "personalization_2"
   FROM customer360
   LIMIT 2000

For a recipient list that only requires a mobile device number:

.. code-block:: sql
   :linenos:

   SELECT
     phone-mobile AS "mdn"
   FROM customer360
   LIMIT 2000

.. sendto-vibes-build-query-map-to-recipient-list-end


.. _sendto-vibes-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. sendto-vibes-add-orchestration-important-start

.. important:: Refer to the |destination-name| documentation if you plan to import a `recipient list <https://developer-platform.vibes.com/docs/recipient-list-import>`__ |ext_link| with included headers.

.. sendto-vibes-add-orchestration-important-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-vibes-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
