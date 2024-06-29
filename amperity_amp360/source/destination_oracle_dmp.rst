.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Oracle DMP
.. |what-send| replace:: delimited files (CSV, PSV, and TSV)
.. |sftp-type| replace:: **passphrase or **private-key**
.. |sftp-hostname| replace:: **sftp.bluekai.com**
.. |file-format| replace:: CSV, TSV, or PSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Oracle DMP (BlueKai).

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Oracle DMP (BlueKai).

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Oracle DMP (BlueKai)

==================================================
Send query results to Oracle DMP (BlueKai)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-dmp-start
   :end-before: .. term-oracle-dmp-end

.. sendto-oracle-dmp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-oracle-dmp-build-query>`
#. :ref:`Add orchestration <sendto-oracle-dmp-add-orchestration>`
#. :ref:`Run orchestration <sendto-oracle-dmp-run-orchestration>`

.. sendto-oracle-dmp-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-oracle-dmp-build-query:

Build query
==================================================

.. sendto-oracle-dmp-build-query-start

You may need to build a query that shapes the data so that fields in the output can be mapped to the fields required by Oracle DMP.

.. sendto-oracle-dmp-build-query-end


.. _sendto-oracle-dmp-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-oracle-dmp-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
