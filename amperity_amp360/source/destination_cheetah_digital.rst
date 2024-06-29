.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Cheetah Digital
.. |what-send| replace:: customer profiles

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Cheetah Digital.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Cheetah Digital.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Cheetah Digital

==================================================
Send query results to Cheetah Digital
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-cheetah-digital-start
   :end-before: .. term-cheetah-digital-end

.. sendto-cheetah-digital-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-cheetah-digital-build-query>`
#. :ref:`Add orchestration <sendto-cheetah-digital-add-orchestration>`
#. :ref:`Run orchestration <sendto-cheetah-digital-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-cheetah-digital-build-query:

Build query
==================================================

.. sendto-cheetah-digital-build-query-start

Build a query that returns the customer profile data that you want to send to |destination-name|. For example:

.. code-block:: sql

   SELECT
     email AS "email"
     ,phone AS "phone"
     ,address AS "address"
     ,city AS "city"
     ,state AS "state"
     ,postal AS "zip"
   FROM Customer360

.. sendto-cheetah-digital-build-query-end


.. _sendto-cheetah-digital-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-cheetah-digital-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
