.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: AWS Connect
.. |what-send| replace:: customer profiles
.. |lambda-validate| replace:: phone numbers

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to AWS Connect.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to AWS Connect.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to AWS Connect

==================================================
Send query results to AWS Connect
==================================================

.. sendto-aws-connect-howitworks-start

You can send phone numbers and SMS message strings from Amperity to |destination-name|. First build a query that outputs customer profiles. Then use an orchestration to send that data from Amperity to |destination-name|.

.. sendto-aws-connect-howitworks-end

.. image:: ../../images/sendto-aws-connect.png
   :width: 600 px
   :alt: Send customer profiles from Amperity to AWS Connect.
   :align: left
   :class: no-scaled-link

.. sendto-aws-connect-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-aws-connect-build-query>`
#. :ref:`Add orchestration <sendto-aws-connect-add-orchestration>`
#. :ref:`Run orchestration <sendto-aws-connect-run-orchestration>`

.. sendto-aws-connect-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-webhook-start
   :end-before: .. sendtos-ask-to-configure-webhook-end


.. _sendto-aws-connect-build-query:

Build query
==================================================

.. sendto-aws-connect-build-query-start

Build a query that returns customer profiles and custom values. For example:

.. code-block:: sql

   SELECT
     given_name AS "First Name"
     surname AS "Last Name"
     postal AS "Zip Code"
     email AS "Email Address"
     phone AS "Phone Number"
   FROM Merged_Customers

.. sendto-aws-connect-build-query-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-webhook-lambda-note-start
   :end-before: .. sendtos-build-query-webhook-lambda-note-end


.. _sendto-aws-connect-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-aws-connect-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
