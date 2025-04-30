.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: Criteo
.. |what-send| replace:: audiences


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Criteo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Criteo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Criteo

==================================================
Send query results to Criteo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-start
   :end-before: .. term-criteo-end

.. sendto-criteo-api-note-start

.. note:: This destination uses the `Criteo API <https://developers.criteo.com/marketing-solutions/docs>`__ |ext_link|.

.. sendto-criteo-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

.. sendto-criteo-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-criteo-build-query>`
#. :ref:`Add orchestration <sendto-criteo-add-orchestration>`
#. :ref:`Run orchestration <sendto-criteo-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-criteo-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end

**Example**

.. sendto-criteo-build-query-example-start

.. code-block:: sql

   SELECT 
     amperity_id AS "Amperity ID"
     ,email AS Email
   FROM Merged_Customers
   WHERE email IS NOT NULL

.. sendto-criteo-build-query-example-end


.. _sendto-criteo-send-transactions:

Send transactions data
--------------------------------------------------

.. include:: ../../amperity_ampiq/source/events_criteo.rst
   :start-after: .. events-criteo-overview-start
   :end-before: .. events-criteo-overview-end

.. include:: ../../amperity_ampiq/source/events_criteo.rst
   :start-after: .. events-criteo-build-query-start
   :end-before: .. events-criteo-build-query-end


.. _sendto-criteo-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-criteo-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
