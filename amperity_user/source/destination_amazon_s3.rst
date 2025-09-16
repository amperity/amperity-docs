.. https://docs.amperity.com/user/


.. |destination-name| replace:: Amazon S3
.. |what-send| replace:: files


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to any Amazon S3 bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to any Amazon S3 bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Amazon S3

==================================================
Send query results to Amazon S3
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-s3-start
   :end-before: .. term-amazon-s3-end

.. sendto-amazon-s3-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-amazon-s3-build-query>`
#. :ref:`Add orchestration <sendto-amazon-s3-add-orchestration>`
#. :ref:`Run orchestration <sendto-amazon-s3-run-orchestration>`

.. sendto-amazon-s3-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-amazon-s3-build-query:

Build query
==================================================

.. sendto-amazon-s3-build-query-start

You need to build a query, and then send the results to Amazon S3.

.. sendto-amazon-s3-build-query-end


.. _sendto-amazon-s3-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-amazon-s3-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
