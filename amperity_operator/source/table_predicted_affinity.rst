.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Predicted Affinity table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Predicted Affinity table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predicted Affinity table

==================================================
Predicted Affinity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-affinity-table-start
   :end-before: .. term-affinity-table-end

.. table-predicted-affinity-note-start

.. note:: The size of the **Predicted Affinity** table in your tenant is determined by the number of qualified products times the number of customers who have purchased a product within the previous 30 days.

.. table-predicted-affinity-note-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end


.. _table-affinity-about-predictions:

About predictions tables
==================================================

.. include:: ../../amperity_operator/source/add_predicted_models.rst
   :start-after: .. add-predicted-models-data-requirements-columns-and-tables-start
   :end-before: .. add-predicted-models-data-requirements-columns-and-tables-end


.. _table-affinity-add-table:

Add the Predicted Affinity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-affinity-table-start
   :end-before: .. term-affinity-table-end

.. table-affinity-add-table-about-start

To add a **Predicted Affinity** table you must extend the customer 360 database to add a table that joins the **Predicted Affinity ProductAttribute** passthrough table to the **Predicted Affinity Audience ProductAttribute** passthrough table.

.. table-affinity-add-table-about-end

**To add the Predicted Affinity table**

.. table-affinity-add-table-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Predicted Affinity" or some other name that identifies this table as the product affinity table for your tenant.
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

.. table-affinity-add-table-steps-end


.. _table-affinity-howto:

How to use the Predicted_Affinity table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-product-affinity-start
   :end-before: .. term-product-affinity-end

.. include:: ../../amperity_user/source/recommended_audiences.rst
   :start-after: .. recommended-audiences-howto-start
   :end-before: .. recommended-audiences-howto-end

.. table-affinity-refresh-frequency-note-start

Recommended audience sizes are refreshed on a weekly basis.

.. table-affinity-refresh-frequency-note-start


.. _table-affinity-howto-validate-campaigns:

Validate campaigns that use product affinity
--------------------------------------------------

.. include:: ../../amperity_user/source/recommended_audiences.rst
   :start-after: .. recommended-audiences-howto-validate-campaigns-start
   :end-before: .. recommended-audiences-howto-validate-campaigns-end


.. _table-affinity-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-affinity-table-about-start
   :end-before: .. data-tables-affinity-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-affinity-table-start
   :end-before: .. data-tables-affinity-table-end
