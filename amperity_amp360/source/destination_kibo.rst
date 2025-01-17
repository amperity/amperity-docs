.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: Kibo
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **kibo**
.. |sftp-hostname| replace:: **sftp.monetate.net**
.. |file-format| replace:: CSV or TSV
.. |encoding-method| replace:: Encoding method options include "Zip" or "GZip".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Kibo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Kibo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Kibo

==================================================
Send query results to Kibo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-kibo-start
   :end-before: .. term-kibo-end

.. sendto-kibo-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-kibo-build-query>`
#. :ref:`Add orchestration <sendto-kibo-add-orchestration>`
#. :ref:`Run orchestration <sendto-kibo-run-orchestration>`

.. sendto-kibo-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-kibo-build-query:

Build query
==================================================

.. sendto-kibo-build-query-start

You may need to build a query that shapes the data so that fields in the output are mapped to the fields required by Monetate. Data shaping is typically required only one time.

.. sendto-kibo-build-query-end

.. include:: ../../amperity_datagrid/source/destination_kibo.rst
   :start-after: .. destination-kibo-get-details-note-start
   :end-before: .. destination-kibo-get-details-note-end


.. _sendto-kibo-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-kibo-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
