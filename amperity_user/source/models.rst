.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Predictive models for churn propensity, customer lifetime value, and product affinity may be enabled for use within Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Predictive models for churn propensity, customer lifetime value, and product affinity may be enabled for use within Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predictive models

==================================================
Predictive models
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-predictive-models-start
   :end-before: .. term-predictive-models-end

.. models-note-start

.. note:: Predictive models require at least four years of historical data (five years or more is recommended). You should have at least 100,000 customer transactions on an annual basis, with at least a 10% retention rate.

   The following tables must be configured in your customer 360 database prior to running predictive models:

   #. **Customer 360**
   #. **Merged Customers**
   #. **Transaction Attributes Extended**
   #. **Unified Itemized Transactions**. Updated to include product catalogs.
   #. **Unified Transactions**

.. models-note-end

.. models-learning-lab-start

.. admonition:: Amperity Learning Lab

   Amperity provides a set of predictive models.

   Churn propensity predicts the likelihood of customer activity. Predicted CLV predicts the order value for purchases made within the next year. Product affinity predicts who is likely to purchase.

   Open **Learning Lab** to learn more about how `predictive modeling <https://learn.amperity.com/predictive-course>`__ |ext_link| can help your brand. Registration is required.

.. models-learning-lab-end


.. _models-common-inputs:

Common inputs to models
==================================================

.. models-common-inputs-start

Columns from the **Merged Customers**, **Unified Transactions**, and **Unified Itemized Transactions**, including product catalogs, are used as inputs to predictive modeling. For multi-brand tenants, the **amperity_id** column from the **Customer 360** table is also used as an input to predictive modeling.

The following columns are common inputs to predictive models:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Source table
     - Input columns
   * - **Merged Customers**
     - The following columns are common inputs:

       * **amperity_id**
       * **birthdate**
       * **city**
       * **email**
       * **gender**
       * **given_name**
       * **phone**
       * **postal**
       * **state**
       * **surname**

   * - **Unified Itemized Transactions**
     - The following columns are common inputs:

       * **is_return**
       * **item_quantity**
       * **item_revenue**
       * **order_datetime**
       * **order_id**
       * **product_id**

   * - **Unified Transactions**
     - The following columns are common inputs:

       * **amperity_id**
       * **order_canceled_quantity**
       * **order_canceled_revenue**
       * **order_datetime**
       * **order_discount_amount**
       * **order_id**
       * **order_quantity**
       * **order_returned_quantity**
       * **order_returned_revenue**
       * **order_revenue**
       * **purchase_brand**
       * **purchase_channel**
       * **store_id**

.. models-common-inputs-end


.. _models-available:

Available models
==================================================

The following predictive models are available:

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: Churn propensity
      :link: model_predicted_churn.html

   .. grid-item-card:: Event propensity
      :link: model_event_propensity.html

   .. grid-item-card:: Predicted CLV
      :link: model_predicted_clv.html

   .. grid-item-card:: Product affinity
      :link: model_predicted_product_affinity.html


.. toctree::
   :caption: Destinations
   :maxdepth: 2
   :hidden:

   Churn propensity <model_predicted_churn>
   Event propensity <model_event_propensity>
   Predicted CLV <model_predicted_clv>
   Product affinity <model_predicted_product_affinity>
