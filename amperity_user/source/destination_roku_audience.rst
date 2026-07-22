.. https://docs.amperity.com/user/


.. |destination-name| replace:: Roku Audience
.. |what-send| replace:: audiences


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Roku Audience.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Roku Audience.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Roku Audience

==================================================
Send query results to Roku Audience
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-roku-audience-start
   :end-before: .. term-roku-audience-end

.. include:: ../../amperity_operator/source/destination_roku_audience.rst
   :start-after: .. destination-roku-audience-api-note-start
   :end-before: .. destination-roku-audience-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

.. sendto-roku-audience-steps-to-send-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - :ref:`Build a query <sendto-roku-audience-build-query>`


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - :ref:`Add orchestration <sendto-roku-audience-add-orchestration>`


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - :ref:`Run orchestration <sendto-roku-audience-run-orchestration>`

.. sendto-roku-audience-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-roku-audience-build-query:

Build query
==================================================

.. sendto-roku-audience-build-query-start

Build a query that returns the fields that are required by |destination-name|. The **email** field is required. You can optionally include **phone**, **maid** (mobile advertiser ID), and **ip** fields to improve match rates.

The following example shows a query that returns email addresses from the **Customer 360** table:

.. code-block:: sql

   SELECT
     email
   FROM Customer_360

The following example shows a query that returns email addresses and device identifiers to improve match rates:

.. code-block:: sql

   SELECT
     email
     ,phone
     ,mobile_advertiser_id AS maid
     ,ip
   FROM Customer_360

.. note:: Roku matches audiences using email as the primary identifier. Phone numbers, mobile advertiser IDs, and IP addresses are optional and can improve match rates when included.

.. sendto-roku-audience-build-query-end


.. _sendto-roku-audience-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-roku-audience-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
