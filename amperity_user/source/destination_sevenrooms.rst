.. https://docs.amperity.com/user/


.. |destination-name| replace:: SevenRooms
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to SevenRooms.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to SevenRooms.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to SevenRooms

==================================================
Send query results to SevenRooms
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sevenrooms-start
   :end-before: .. term-sevenrooms-end

.. include:: ../../amperity_operator/source/destination_sevenrooms.rst
   :start-after: .. destination-sevenrooms-api-note-start
   :end-before: .. destination-sevenrooms-api-note-end

.. sendto-sevenrooms-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. sendto-sevenrooms-beta-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-sevenrooms-build-query>`
#. :ref:`Add orchestration <sendto-sevenrooms-add-orchestration>`
#. :ref:`Run orchestration <sendto-sevenrooms-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-sevenrooms-build-query:

Build query
==================================================

.. sendto-sevenrooms-build-query-start

You will need to build a query that outputs fields that can be sent to |destination-name|. The following example shows how to return email addresses from the **Customer 360** table:

.. code-block:: sql

   SELECT
     email
   FROM Customer_360
   WHERE email IS NOT NULL

The **email** field is required and is used to match guest profiles in |destination-name|. You may add other profile fields -- such as phone number, first name, and last name -- to the query, and Amperity writes them as attributes on the matching guest profile.

.. sendto-sevenrooms-build-query-end


.. _sendto-sevenrooms-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-sevenrooms-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
