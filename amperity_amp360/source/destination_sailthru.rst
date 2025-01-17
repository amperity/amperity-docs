.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: Sailthru
.. |what-send| replace:: email address lists


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Sailthru.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Sailthru.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Sailthru

==================================================
Send query results to Sailthru
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sailthru-start
   :end-before: .. term-sailthru-end

.. sendto-sailthru-start

Use Amperity to manage |what-send| in Sailthru. Build a query using the **email** field and then send the results of that query to Sailthru. The audience list will be updated to match the query.

.. sendto-sailthru-end

.. sendto-sailthru-api-note-start

.. note:: This destination uses the `Sailthru API <https://getstarted.sailthru.com/developers/api-basics/introduction/>`__ |ext_link|.

.. sendto-sailthru-api-note-end

.. sendto-sailthru-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-sailthru-build-query>`
#. :ref:`Add orchestration <sendto-sailthru-add-orchestration>`
#. :ref:`Run orchestration <sendto-sailthru-run-orchestration>`

.. sendto-sailthru-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-sailthru-extended-profile-attributes:

Extended profile attributes
==================================================

.. include:: ../../amperity_datagrid/source/destination_sailthru.rst
   :start-after: .. destination-sailthru-extended-profile-attributes-start
   :end-before: .. destination-sailthru-extended-profile-attributes-end


.. _sendto-sailthru-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end


.. _sendto-sailthru-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-sailthru-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
