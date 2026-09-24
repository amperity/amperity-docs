.. https://docs.amperity.com/user/


.. |destination-name| replace:: Airship Attributes
.. |what-send| replace:: attributes


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Airship Attributes.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Airship Attributes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Airship Attributes

==================================================
Send query results to Airship Attributes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-airship-attributes-start
   :end-before: .. term-airship-attributes-end

.. include:: ../../amperity_operator/source/destination_airship_attributes.rst
   :start-after: .. destination-airship-attributes-api-note-start
   :end-before: .. destination-airship-attributes-api-note-end

.. include:: ../../amperity_operator/source/destination_airship_attributes.rst
   :start-after: .. destination-airship-attributes-beta-start
   :end-before: .. destination-airship-attributes-beta-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

.. sendto-airship-attributes-steps-to-send-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - :ref:`Build a query <sendto-airship-attributes-build-query>`


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - :ref:`Add orchestration <sendto-airship-attributes-add-orchestration>`


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - :ref:`Run orchestration <sendto-airship-attributes-run-orchestration>`

.. sendto-airship-attributes-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-airship-attributes-build-query:

Build query
==================================================

.. sendto-airship-attributes-build-query-start

Build a query that returns the fields to send to |destination-name|. Rename the column that holds the Airship identifier to ``airship_identifier``; its contents must match the **Identifier type** configured on the destination (a named user ID, a channel ID, or an email address). Every other column is sent as an Airship attribute, and each column name must exactly match the ID of an attribute that already exists in your Airship project.

The following example returns an email identifier and two attribute columns from the **Customer 360** table. It assumes the destination's **Identifier type** is set to email address, and that ``loyalty_tier`` and ``lifetime_value`` already exist as attributes in the Airship project:

.. code-block:: sql

   SELECT
     email AS airship_identifier
     ,loyalty_tier
     ,lifetime_value
   FROM Customer_360

.. note:: Airship rejects the entire upload if any attribute column is not already an attribute in your Airship project. Create every attribute in the Airship dashboard, under **Audience > Attributes > Attribute List**, before running the orchestration.

.. sendto-airship-attributes-build-query-end


.. _sendto-airship-attributes-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-airship-attributes-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
