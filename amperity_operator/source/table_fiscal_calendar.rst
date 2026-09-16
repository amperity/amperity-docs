.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Fiscal Calendar table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Fiscal Calendar table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Fiscal Calendar table

==================================================
Fiscal Calendar table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-fiscal-calendar-start
   :end-before: .. term-fiscal-calendar-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-454-calendar-start
   :end-before: .. term-454-calendar-end


.. _table-fiscal-calendar-add:

Add table
==================================================

.. table-fiscal-calendar-add-start

The **Fiscal Calendar** table is generated when fiscal calendar semantic tags are applied to a data source, after which it is available to your customer 360 database as a passthrough table.

.. table-fiscal-calendar-add-end

**To add the Fiscal Calendar table**

.. table-fiscal-calendar-add-steps-start

#. From the **Customer 360** page, select the **Databases** tab, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Fiscal_Calendar".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** dropdown, select the **Fiscal Calendar** table.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. From the **Table Semantics** dropdown, select **Fiscal Calendar**.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-fiscal-calendar-add-steps-end


.. _table-fiscal-calendar-extend:

Extend transactions
==================================================

.. table-fiscal-calendar-extend-start

Extend the **Unified Transactions** table by joining the **Fiscal Calendar** table using SQL similar to:

.. code-block:: sql
   :linenos:

   SELECT
     rollup_uit.*
     ,fc.fiscal_year AS fiscal_year
     ,fc.fiscal_quarter AS fiscal_quarter
     ,fc.fiscal_month AS fiscal_month
     ,fc.fiscal_week_number AS fiscal_week_number
     ,fc.fiscal_week_start AS fiscal_week_start
     ,fc.fiscal_week_end AS fiscal_week_end
     ,fc.day_of_week AS fiscal_day_of_week -- optional field 
     ,fc.holiday_sale_name AS holiday_sale_name -- optional field 
   FROM rollup_uit
   LEFT JOIN  fiscal_calendar fc
   ON fc.calendar_date = DATE(order_datetime)

.. table-fiscal-calendar-extend-end


.. _table-fiscal-calendar-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-fiscal-calendar-about-start
   :end-before: .. data-tables-fiscal-calendar-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-fiscal-calendar-table-start
   :end-before: .. data-tables-fiscal-calendar-table-end
