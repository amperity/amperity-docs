.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Event Propensity table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Event Propensity table.

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

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end


.. _table-event-propensity-add-table:

Add the Event Propensity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-event-propensity-table-start
   :end-before: .. term-event-propensity-table-end

.. table-event-propensity-add-table-about-start

To add a **Event Propensity** table you must extend the customer 360 database to add a table that joins the **Event Propensity ProductAttribute** passthrough table to the **Event Propensity Audience ProductAttribute** passthrough table.

.. table-event-propensity-add-table-about-end

**To add the Event Propensity table**

.. table-event-propensity-add-table-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Event Propensity" or some other name that clearly identifies this table as the event propensity table for your tenant.
#. Set the build mode to **SQL**.
#. Add the following SQL:

   .. code-block:: sql
      :linenos:

      SELECT 
        r.product_attribute AS `product_sub_category`
        ,r.amperity_id
        ,r.score
        ,r.ranking
        ,r.ranking <= s.audience_size_small AS audience_size_small
        ,r.ranking <= s.audience_size_medium AS audience_size_medium
        ,r.ranking <= s.audience_size_large AS audience_size_large
      FROM Predicted_Affinity_ProductAttribute AS r
      LEFT JOIN Predicted_Affinity_Audience_ProductAttribute AS s
      ON r.product_attribute = s.product_attribute

#. Click **Validate** to verify the SQL runs without error.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that the **db/required** and **db/unique** database field semantics were applied to the **amperity_id** column.
#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-event-propensity-add-table-steps-end


.. _table-event-propensity-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-event-propensity-table-about-start
   :end-before: .. data-tables-event-propensity-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-event-propensity-table-start
   :end-before: .. data-tables-event-propensity-table-end
