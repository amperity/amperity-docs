.. https://docs.amperity.com/internal/


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
   :start-after: .. term-affinity-table-start
   :end-before: .. term-affinity-table-end

.. table-event-propensity-note-start

.. note:: The size of the **Event Propensity** table in your tenant is determined by the number of customers who are associated with events in the table.

.. table-event-propensity-note-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end


.. _table-affinity-add-table:

Add the Event Propensity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-event-propensity-table-start
   :end-before: .. term-event-propensity-table-end

.. table-affinity-add-table-about-start

To add a **Event Propensity** table you must extend the customer 360 database to add a table that joins the **Event Propensity ProductAttribute** passthrough table to the **Event Propensity Audience ProductAttribute** passthrough table.

.. table-affinity-add-table-about-end

**To add the Event Propensity table**

.. table-affinity-add-table-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Event Propensity" (or some other name that clearly identifies this table as the product affinity table for your tenant).
#. Set the build mode to **SQL**.
#. Add the following SQL:

   .. code-block:: sql

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

.. table-affinity-add-table-steps-end


.. _table-affinity-howto:

How to use the Predicted Affinity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-product-affinity-start
   :end-before: .. term-product-affinity-end

.. TODO: Re-hook this to the amperity_ampiq/recommended_audiences page after moving it to amperity-docs

.. recommended-audiences-howto-start

Use fields in the product affinity table to build segments that contain the right list of customers for your campaigns and are aligned to recommended audience sizes.

#. Start by associating product affinity to a smaller audience size, and then, depending on the goals of your campaign, increase the audience size until you have reached your campaign's circulation size and/or revenue goals.
#. For further refinement you can compare the audience size to customer ranking. Increase or decrease the audience size by small amounts until the list of customers that fall within the desired ranking also matches the circulation size and/or revenue goals.

You may also use audience size and customer ranking independently of each other, depending on what types of segments you want to build and what types of campaigns those segments will be associated with. For example, you can build a segment that uses ranking *or* audience size and not both.

.. recommended-audiences-howto-end

.. table-affinity-refresh-frequency-note-start

Recommended audience sizes are refreshed on a weekly basis.

.. table-affinity-refresh-frequency-note-start


.. _table-affinity-howto-validate-campaigns:

Validate campaigns that use product affinity
--------------------------------------------------

.. TODO: Re-hook this to the amperity_ampiq/recommended_audiences page after moving it to amperity-docs

.. recommended-audiences-howto-validate-campaigns-start

The best approach to validate the successful use of product affinity modeling in a campaign is to use two segment and campaign pairs. The first pair is based on product affinity and the other pair is not. Configure each campaign for a 30% hold-out, and then send the same campaign message to both lists.

You should expect to see more revenue from a campaign that is based on product affinity.

You may observe a lower unsubscribe rate with a campaign that is based on product affinity (if you have access to a data source that can provide email response statistics). A lower unsubscribe rate on a more targeted section of your customer base can reduce the overall unsubscribe rate among your larger set of customers.

For example:

* Unsubscribe rates without product affinity is ~5%. If you send 120k emails at a 5% unsubscribe rate, that's 6k unsubscribes.
* Unsubscribe rates with product affinity is ~3%. If you send 60k emails at a 3% unsubscribe rate, that's 1800 unsubscribes and 4200 fewer than the list without product affinity.

.. recommended-audiences-howto-validate-campaigns-end


.. _table-affinity-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-event-propensity-table-about-start
   :end-before: .. data-tables-event-propensity-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-event-propensity-table-start
   :end-before: .. data-tables-event-propensity-table-end
