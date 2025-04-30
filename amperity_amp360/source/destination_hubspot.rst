.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: HubSpot
.. |what-send| replace:: contact list updates


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to HubSpot.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to HubSpot.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to HubSpot

==================================================
Send query results to HubSpot
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-hubspot-start
   :end-before: .. term-hubspot-end

.. sendto-hubspot-start

Use Amperity to manage contact lists in |destination-name|. Build a query using the **email** field and send the results of that query to |destination-name|. Amperity will update contacts that already exist in |destination-name|; Amperity does not create contacts.

.. sendto-hubspot-end

.. include:: ../../amperity_operator/source/destination_hubspot.rst
   :start-after: .. destination-hubspot-contain-only-numbers-letters-underscores-start
   :end-before: .. destination-hubspot-contain-only-numbers-letters-underscores-end

.. sendto-hubspot-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-hubspot-build-query>`
#. :ref:`Add orchestration <sendto-hubspot-add-orchestration>`
#. :ref:`Run orchestration <sendto-hubspot-run-orchestration>`

.. sendto-hubspot-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-hubspot-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end

.. include:: ../../amperity_operator/source/destination_hubspot.rst
   :start-after: .. destination-hubspot-build-query-start
   :end-before: .. destination-hubspot-build-query-end


.. _sendto-hubspot-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-hubspot-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
