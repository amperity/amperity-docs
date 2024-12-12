.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Airship
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **Airship**
.. |sftp-hostname| replace:: **sftp.airship.com**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Airship.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Airship.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Airship

==================================================
Send query results to Airship
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-airship-start
   :end-before: .. term-airship-end

.. sendto-airship-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-airship-build-query>`
#. :ref:`Add orchestration <sendto-airship-add-orchestration>`
#. :ref:`Run orchestration <sendto-airship-run-orchestration>`

.. sendto-airship-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-airship-build-query:

Build query
==================================================

.. sendto-airship-build-query-start

You will need to build a query that shapes data to the fields required by an Airship audience list or attribute list.

You can do this in the following ways:

#. Add a SQL table (using |sql_spark|) to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or using the |sql_spark_cast| function to convert to a UUID.

#. Add a SQL query (using |sql_presto|) that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require using the |sql_presto_cast| function to convert to a UUID.

The correct approach here depends on the data and the desired use case (or cases) for downstream workflows.

.. sendto-airship-build-query-end


.. _sendto-airship-build-query-map-to-audience-lists:

Map to audience lists
--------------------------------------------------

.. sendto-airship-build-query-map-to-audience-lists-start

Airship `audience lists <https://docs.airship.com/guides/audience/audience-lists/>`__ |ext_link| are groups of devices, users, and addresses that can be targeted by channels and queries.

.. sendto-airship-build-query-map-to-audience-lists-end


.. _sendto-airship-build-query-map-to-attributes:

Map to attributes
--------------------------------------------------

.. sendto-airship-build-query-map-to-attributes-start

Airship `attributes <https://docs.airship.com/guides/audience/attributes/>`__ |ext_link| are key-value pairs that are associated with audiences for better message targeting.

.. sendto-airship-build-query-map-to-attributes-end


.. _sendto-airship-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. sendto-airship-add-orchestration-important-start

.. important:: Airship `audience lists <https://docs.airship.com/guides/audience/audience-lists/>`__ |ext_link| are groups of devices, users, and addresses that can be targeted by channels and queries and `attributes <https://docs.airship.com/guides/audience/attributes/>`__ |ext_link| are key-value pairs that are associated with audiences for better message targeting. Refer to the `SFTP tutorial <https://docs.airship.com/guides/messaging/user-guide/audience/segmentation/sftp-upload/>`__ |ext_link| for details about template patterns and file names.

.. sendto-airship-add-orchestration-important-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-airship-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
