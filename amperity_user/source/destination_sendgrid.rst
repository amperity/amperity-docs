.. https://docs.amperity.com/user/


.. |destination-name| replace:: SendGrid
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to SendGrid.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to SendGrid.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to SendGrid

==================================================
Send query results to SendGrid
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sendgrid-start
   :end-before: .. term-sendgrid-end

.. include:: ../../amperity_operator/source/destination_sendgrid.rst
   :start-after: .. destination-sendgrid-api-note-start
   :end-before: .. destination-sendgrid-api-note-end

.. sendto-sendgrid-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. sendto-sendgrid-beta-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-sendgrid-build-query>`
#. :ref:`Add orchestration <sendto-sendgrid-add-orchestration>`
#. :ref:`Run orchestration <sendto-sendgrid-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-sendgrid-build-query:

Build query
==================================================

.. sendto-sendgrid-build-query-start

You will need to build a query that outputs fields that can be sent to |destination-name|. The following example shows how to return email addresses from the **Customer 360** table:

.. code-block:: sql

   SELECT
     email
   FROM Customer_360
   WHERE email IS NOT NULL

The **email** field is required, and email is the only field |destination-name| receives. The schema also accepts an **external_id** field, but it is not sent to |destination-name| in this phase.

.. sendto-sendgrid-build-query-end


.. _sendto-sendgrid-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-sendgrid-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
