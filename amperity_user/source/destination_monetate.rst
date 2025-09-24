.. https://docs.amperity.com/user/


.. |destination-name| replace:: Monetate
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **kibo**
.. |sftp-hostname| replace:: **sftp.monetate.net**
.. |file-format| replace:: CSV or TSV
.. |encoding-method| replace:: Encoding method options include "Zip" or "GZip".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Monetate.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Monetate.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Monetate

==================================================
Send query results to Monetate
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-monetate-start
   :end-before: .. term-monetate-end

.. sendto-monetate-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-monetate-build-query>`
#. :ref:`Add orchestration <sendto-monetate-add-orchestration>`
#. :ref:`Run orchestration <sendto-monetate-run-orchestration>`

.. sendto-monetate-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-monetate-build-query:

Build query
==================================================

.. sendto-monetate-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Monetate. Data shaping is typically required only one time.

.. sendto-monetate-build-query-end

.. destination-monetate-get-details-note-start

.. note:: Files sent to |destination-name| must:

   * Not exceed 10 GB uncompressed or 100 million rows
   * Contain at least one column and may not contain more than 30
   * Include a single row per unique identifier
   * Use double quotes around fields that include a comma
   * Include a header row for new datasets

   Review the `customer dataset upload requirements <https://docs.kibocommerce.com/114237-customer-data/631062-customer-dataset-upload-requirements>`__ |ext_link| for additional information. 

.. destination-monetate-get-details-note-end


.. _sendto-monetate-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-monetate-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
