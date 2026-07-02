.. https://docs.amperity.com/user/


.. |destination-name| replace:: Bloomreach Engagement
.. |what-send| replace:: customer profiles


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Bloomreach

==================================================
Send query results to Bloomreach
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bloomreach-start
   :end-before: .. term-bloomreach-end

.. include:: ../../amperity_operator/source/destination_bloomreach.rst
   :start-after: .. destination-bloomreach-api-note-start
   :end-before: .. destination-bloomreach-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

.. sendto-bloomreach-steps-to-send-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - :ref:`Build a query <sendto-bloomreach-build-query>`

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - :ref:`Add orchestration <sendto-bloomreach-add-orchestration>`

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - :ref:`Run orchestration <sendto-bloomreach-run-orchestration>`

.. sendto-bloomreach-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-bloomreach-build-query:

Build query
==================================================

.. sendto-bloomreach-build-query-start

You will need to build a query that outputs the fields you want to send to |destination-name|. The query must include a Bloomreach hard identifier such as email, external ID, cookie, or Google Analytics ID. All other columns in your query results will be sent as customer properties.

.. sendto-bloomreach-build-query-end

.. sendto-bloomreach-build-query-example-start

The following example shows a query that returns customer profiles using email as the identifier:

.. code-block:: sql

   SELECT
     email
     ,given_name
     ,surname
     ,city
     ,state
     ,postal
     ,birthdate
     ,gender
   FROM Customer360
   WHERE email IS NOT NULL

.. sendto-bloomreach-build-query-example-end

.. sendto-bloomreach-build-query-example-external-id-start

You can also use the Amperity ID as an external identifier:

.. code-block:: sql

   SELECT
     amperity_id AS external_id
     ,email
     ,given_name
     ,surname
     ,phone
     ,lifetime_order_revenue
     ,lifetime_order_frequency
   FROM Customer360
   WHERE amperity_id IS NOT NULL

.. sendto-bloomreach-build-query-example-external-id-end

.. sendto-bloomreach-build-query-important-start

.. important:: The column you use for the Bloomreach identifier must match the **Identity source column** setting configured for the destination. Rows with blank values in the identity column will be skipped.

.. sendto-bloomreach-build-query-important-end


.. _sendto-bloomreach-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-bloomreach-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
