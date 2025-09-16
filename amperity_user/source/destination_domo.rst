.. https://docs.amperity.com/user/


.. |destination-name| replace:: Domo
.. |what-send| replace:: data
.. |allow-for-duration| replace:: up to one hour


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Domo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Domo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Domo

==================================================
Send query results to Domo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-domo-start
   :end-before: .. term-domo-end

.. include:: ../../amperity_operator/source/destination_domo.rst
   :start-after: .. destination-domo-context-start
   :end-before: .. destination-domo-context-end

.. destination-domo-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <destination-domo-build-query>`
#. :ref:`Add orchestration <destination-domo-add-orchestration>`
#. :ref:`Run orchestration <destination-domo-run-orchestration>`

.. destination-domo-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _destination-domo-build-query:

Build query
==================================================

.. destination-domo-build-query-start

You need to build a query that outputs the data that you want to use within |destination-name|.

.. destination-domo-build-query-end


.. _destination-domo-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _destination-domo-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
