.. https://docs.amperity.com/user/


.. |destination-name| replace:: Microsoft Dataverse
.. |what-send| replace:: table rows that match a table schema
.. |lambda-validate| replace:: validates that rows match the table schema


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Microsoft Dataverse.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Microsoft Dataverse.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Microsoft Dataverse

==================================================
Send query results to Microsoft Dataverse
==================================================

.. destination-microsoft-dataverse-howitworks-start

You can send data from Amperity to |destination-name|. First build a query that outputs a table with rows that match the schema of a table in |destination-name|. The column names, data types, and column order must match the schema that is defined in |destination-name|. Then use an orchestration to send that data from Amperity to |destination-name|.

.. destination-microsoft-dataverse-howitworks-end

.. image:: ../../images/sendto-microsoft-dataverse.png
   :width: 600 px
   :alt: Send data tables from Amperity to Microsoft Dataverse.
   :align: left
   :class: no-scaled-link

.. sendto-microsoft-dataverse-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-microsoft-dataverse-build-query>`
#. :ref:`Add orchestration <sendto-microsoft-dataverse-add-orchestration>`
#. :ref:`Run orchestration <sendto-microsoft-dataverse-run-orchestration>`

.. sendto-microsoft-dataverse-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-webhook-start
   :end-before: .. sendtos-ask-to-configure-webhook-end


.. _sendto-microsoft-dataverse-build-query:

Build query
==================================================

.. sendto-microsoft-dataverse-build-query-start

Build a query that returns rows that match the schema of a table in |destination-name|. For example, to send a list of first names, last names, and email addresses from Amperity to a table in |destination-name|, where all columns in that table have a **cr812_** column prefix and different column names from the ones in Amperity use a query similar to:

.. code-block:: sql
   :linenos:

   SELECT DISTINCT
     given_name AS cr812_firstname
     ,surname AS cr812_lastname
     ,email AS cr812_email_address
   FROM Merged_Customers

.. sendto-microsoft-dataverse-build-query-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-webhook-lambda-note-start
   :end-before: .. sendtos-build-query-webhook-lambda-note-end


.. _sendto-microsoft-dataverse-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-microsoft-dataverse-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
