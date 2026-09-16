.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Learn about the Event Propensity table produced by an event propensity model.

.. meta::
    :content class=swiftype name=body data-type=text:
        Learn about the Event Propensity table produced by an event propensity model.

.. meta::
    :content class=swiftype name=title data-type=string:
        Event Propensity table

==================================================
Event Propensity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-event-propensity-table-start
   :end-before: .. term-event-propensity-table-end

.. table-event-propensity-note-start

.. note:: The size of the **Event Propensity** table in your tenant is determined by the number of customers who are associated with events in the table.

.. table-event-propensity-note-end


.. _table-event-propensity-add-table:

How the Event Propensity table is created
==================================================

.. table-event-propensity-add-table-about-start

Amperity creates the **Event Propensity** table automatically when you build and activate an event propensity model. You do not need to add the table by hand or write any SQL.

Each active event propensity model produces its own output table, named ``Predicted_Propensity_{EventName}`` after the target event name provided during model setup. The table contains one row per customer per event, along with the customer's score, ranking, and recommended audience-size flags. See the :ref:`column reference <table-event-propensity-reference>` for details.

.. table-event-propensity-add-table-about-end

To start producing an **Event Propensity** table, build an event propensity model and then activate it:

* :ref:`Build an event propensity model <model-event-propensity-configure>`
* :ref:`Predictive model how-tos <models-howtos>` for the steps to activate a model.


.. _table-event-propensity-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-event-propensity-table-about-start
   :end-before: .. data-tables-event-propensity-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-event-propensity-table-start
   :end-before: .. data-tables-event-propensity-table-end
