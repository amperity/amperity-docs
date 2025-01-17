.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: Azure Blob Storage
.. |what-send| replace:: files


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Azure Blob Storage.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Azure Blob Storage.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Azure Blob Storage

==================================================
Send query results to Azure Blob Storage
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-azure-blob-storage-start
   :end-before: .. term-azure-blob-storage-end

.. sendto-azure-blob-storage-important-start

.. important:: Use this destination to send data from Amperity to Azure Data Lake Storage Gen1 or Azure Data Lake Storage Gen2.

.. sendto-azure-blob-storage-important-end

.. sendto-azure-blob-storage-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-azure-blob-storage-build-query>`
#. :ref:`Add orchestration <sendto-azure-blob-storage-add-orchestration>`
#. :ref:`Run orchestration <sendto-azure-blob-storage-run-orchestration>`

.. sendto-azure-blob-storage-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-azure-blob-storage-build-query:

Build query
==================================================

.. sendto-azure-blob-storage-build-query-start

You will need to build a query, and then send the results to Azure Blob Storage.

.. sendto-azure-blob-storage-build-query-end


.. _sendto-azure-blob-storage-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-azure-blob-storage-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
