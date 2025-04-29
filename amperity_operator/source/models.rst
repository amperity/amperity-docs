.. https://docs.amperity.com/operator/


    :description lang=en:
        Amperity predictive modeling is built from your brand's customer profiles and behavioral history to give you insights into customer purchasing behavior.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity predictive modeling is built from your brand's customer profiles and behavioral history to give you insights into customer purchasing behavior.

.. meta::
    :content class=swiftype name=title data-type=string:
        Predictive models


==================================================
About predictive models
==================================================

.. models-start

Amperity predictive modeling is based on your brand's customer profiles and behavioral history to give you insights into customer purchasing behavior. Amperity combs through hundreds of features to yield a state of the art adaptive ensemble model. Amperity layers on a rigorous MLOps infrastructure to continually monitor prediction accuracy and stability.

.. models-end

.. TODO: For more information on our models for churn and customer lifetime value, please see https://link.springer.com/article/10.1007/s11129-023-09272-x.


.. _models-list:

Available models
==================================================

.. models-list-start

The following out-of-the-box models are configurable directly within Amperity by a user who is assigned the **DataGrid Operator** or **DataGrid Administrator** policies:

* :ref:`Churn propensity <model-churn-propensity>`
* :ref:`Event propensity (EPM) <model-event-propensity>`
* :ref:`Predicted CLV <model-predicted-clv>`
* :ref:`Product affinity <model-product-affinity>`

.. tip:: When building models there is a tradeoff between speed and accuracy.

   When optimizing for speed the default models are often accurate enough with the default set of input fields. Your brand can revisit the inputs at a later point in time.

   When optimizing for accuracy you should include all possible fields that are relevant for modeling, including required and optional fields in **Unified Transactions**. This may require using SQL to extend the table to support these additional features.

   Review the list of fields that are used by :ref:`churn propensity, predicted CLV, and product affinity modeling <models-fields-used-by-all-models>` and by :ref:`event propensity modeling <models-fields-used-by-epm>` to determine what features may be required for :ref:`additional model accuracy <models-extend>`.

.. models-list-end

.. TODO: The following sections have "-about-" start/end blocks that are pulling from the individual model topics. These should act as the more detailed intros to the models, describe the use cases, etc. Customers will want to link to the more detailed topics.


.. _model-churn-propensity:

Churn propensity
--------------------------------------------------

.. model-churn-propensity-about-start

Use :doc:`churn propensity <model_churn_propensity>` scores to churn prevention campaigns. Every customer has a unique purchase history. Instead of relying on hard-coded RFM analyses, Amperity's model uncovers each user's underlying purchase patterns and makes predictions about their likelihood to re-engage with your brand, whether they're a daily, monthly, or seasonal shopper.

* Identify customers who are likely to churn
* Provide better insights about the root causes of customer churn to help you determine what will compel them to stay with right-timed messaging and relevant products
* Support a churn prevention campaign that contains a series of escalating win-back offers
* Optimize suppression and spend

By leveraging churn propensity modeling, you can take a proactive approach to customer retention, reduce churn rates, and improve overall customer satisfaction.

.. model-churn-propensity-about-end


.. _model-event-propensity:

Event propensity
--------------------------------------------------

.. model-event-propensity-about-start

Use :doc:`event propensity <model_event_propensity>` modeling to associate individual customers to specific events that, depending on the type of event, are most likely to lead to engagement with your brand. Customers are grouped by audience size and by ranking.

.. model-event-propensity-about-end


.. _model-predicted-clv:

Predicted CLV
--------------------------------------------------

.. model-predicted-clv-about-start

Amperity models :doc:`predicted customer lifetime value (CLV) <model_predicted_clv>` by fitting observed spend against hundreds of behavioral and demographic inputs in a patented approach, and then predicts for each customer their:

#. Probability of purchase
#. Number of orders
#. Average order value

You can use predicted CLV modeling to build high-value audiences that identify:

* Which customers have the highest predicted value?
* Which customers will respond better to special offers and perks?
* What are the best personalized experiences for your top customers, such as personalized rewards, offers, and content?
* Which customers have individual price preferences?

.. model-predicted-clv-about-end


.. _model-product-affinity:

Product affinity
--------------------------------------------------

.. model-product-affinity-about-start

Amperity models :doc:`product affinity <model_product_affinity>` for any product taxonomy that contains between 20 and 2000 unique values, such as brand, category, subcategory, color, size, season, and style. Product affinity modeling analyzes:

* Historical data to identify customers who have purchased a product in the past and are likely to do so again.
* Lookalike audiences to identify customers who have not purchased a product, but are likely to buy because they are similar to customers who have purchased.

.. model-product-affinity-about-end


.. _models-fields-used-by-all-models:

Fields used by all models (except EPM)
==================================================

.. models-fields-used-by-all-models-start

The churn, pCLV, and affinity models start with a set of fields from the **Merged_Customers**, **Unified_Itemized_Transactions**, and **Unified_Transactions** tables from the database in which the model is built. EPM uses fields from **Merged Customers**, as well as the custom input tables selected during configuration.

.. note::
  The churn and pCLV models now support custom input tables for transactions and transaction items. These tables should have the same field names as **Unified_Transactions** and **Unified_Itemized_Transactions**, but can have custom logic, such as filtering or aliasing, depending on the data your brand wants to use to model churn and pCLV.

You may further customize predictive models, such as excluding certain types of customers and adding custom features that support your brand's use cases. Customer exlusions are based off of the **Customer_Attributes** table, and custom features are based off of additional fields that may exist on **Unified_Itemized_Transactions**.

You do not need to configure the following fields:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Table
     - Fields
   * - **Merged Customers**
     - Predictive models always use the following fields in the **Merged Customers** table:

       * **Amperity ID**
       * **Birthdate**
       * **City**
       * **Email**
       * **Gender**
       * **Given name**
       * **Phone**
       * **Postal**
       * **State**
       * **Surname**

   * - **Unified Transactions**
     - Predictive models always use the following fields in the **Unified Transactions** table:

       * **Amperity ID**
       * **Order datetime**
       * **Order ID**
       * **Order quantity**
       * **Order revenue**

       The following fields, when they are available in the **Unified Transactions** table, will also be used:

       * **Order cancelled quantity**
       * **Order cancelled revenue**
       * **Order discount amount**

         If your tenant does not have order-level discount data, define order-level discounts to equal the the sum of item-level discount amounts. This will ensure that predictive modeling will be able to incorporate signals for discount shoppers.

       * **Order returned quantity**
       * **Order returned revenue**
       * **Purchase brand**
       * **Purchase channel**
       * **Store ID**

   * - **Unified Itemized Transactions**
     - Predictive models always use the following fields in the **Unified Itemized Transactions** table:

       * **Amperity ID**
       * **Is return**
       * **Item quantity**
       * **Item revenue**
       * **Order datetime**
       * **Order ID**
       * **Product ID**

.. models-fields-used-by-all-models-end


.. _models-fields-used-by-epm:

Fields used by event propensity
==================================================

.. models-fields-used-by-epm-start

EPM is highly configurable, with the only table used by default being **Merged_Customers**. The model requires that you select two other data assets with event-level data: one containing the target event, and one containing a revenue generating event.

The target event is the event we want to model, e.g. loyalty program signups, credit card signups, repeat bookings. The data asset should have one row per event, and **must have a field for the event's date or timestamp**.

A revenue generating event is an event in which a customer spends money with your brand, e.g. a retail transaction or a booking. The data asset should also have one row per event, and **must have fields for an event's date or timestammp and revenue amount**. You may also select other fields from the revenue generating event that you think would be helpful for modeling (e.g. purchase or booking channel)

Additionally, you may configure custom events as further inputs to the model. Custom event data assets are also expected to be one row per event.

For revenue generating events and custom events, there are configuration options for the event's timestamp, and also the event's **realization date**. For events, such as bookings, where a customer pays money at one point in time, but then "realizes" or consumes the good or service at another point in time, we strongly recommend supplying both fields to the model.

.. models-fields-used-by-epm-end


.. _models-extend:

Extending models
==================================================

.. models-extend-start

You can build predictive models from the **Customer 360** page. Each database that contains the **Merged Customers**, **Unified Itemized Transactions**, and **Unified Transactions** tables may be configured for predictive modeling. You can only activate one churn/pCLV model per database, but you may have any number of product affinity and event propensity models.

.. warning:: Currently, even if your brand wants to use a custom transactions or transactions item table for churn and pCLV modeling, you must have tables named **Merged_Customers**, **Unified_Itemized_Transactions**, and **Unified_Transactions** in your database due to automated back-end validations.

Each predictive model allows for additional fields to be added to support your brand's use cases. There are two approaches:

#. Optimize for implementation speed.

   If your brand wants to optmize for implementation speed the default fields, along with any required extensions, are accurate enough to start with.

   You can revisit a model that was optimized for implementation speed at a later time, and then make changes to extend them for model accuracy later.

#. :bdg-success:`Recommended` Optimize for model accuracy.

   If your brand wants to optimize for model accuracy you should plan to extend each model as much as possible.

   This includes adding fields and features to the model configuration, and also ensuring that the database tables that contain those fields and features are available within the database in which the model is built.

   Add all possible fields that are relevant for modeling, including all optional fields are available from the **Unifie_Itemized_Transactions** table.

   Ensure that the **Customer Attributes** table contains all possible exceptions that your brand may want to use.

   Ensure that custom features your brand wants to use in predictive models are largely populated (i.e. small percentage of nulls) and reliable (values don't change much day-to-day).

.. models-extend-end


.. _models-build:

Build a model
==================================================

.. models-build-start

Predictive models are configurable in Amperity:

* :ref:`Build a churn propensity model <model-churn-propensity-configure>`
* :ref:`Build a event propensity model <model-event-propensity-configure>`
* :ref:`Build a predicted CLV <model-predicted-clv-configure>`
* :ref:`Build a product affinity model <model-product-affinity-configure>`

.. models-build-end


.. _models-howtos:

How-tos
==================================================

.. models-howtos-start

This section describes individual tasks that are related to building predictive models:

.. models-howtos-end


.. _models-howtows-activate:

Activate a model
--------------------------------------------------

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to edit, from the |fa-kebab| menu, select **Edit**.
#. This opens page for selected model in edit mode.
#. Press **Activate** at top right-hand-size of the model configuration page
#. Select a courier group. The model will run at the same frequency as the courier group.


.. _models-howtows-add:

Add a model
--------------------------------------------------

These are captured in the "Build a model" section for each of the five model-specific pages. Links for now:

#. :ref:`model-churn-propensity-configure`
#. :ref:`model-event-propensity-configure`
#. :ref:`model-predicted-clv-configure`
#. :ref:`model-product-affinity-configure`


.. _models-howtows-delete:

Delete a model
--------------------------------------------------

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to delete, from the |fa-kebab| menu, select **Delete**. Confirm by clicking **Delete**.


.. _models-howtows-edit:

Edit a model
--------------------------------------------------

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to edit, from the |fa-kebab| menu, select **Edit**.
#. This opens page for selected model in edit mode.


.. _models-howtows-pause:

Pause a model
--------------------------------------------------

A paused model will not run as part of a courier group workflow, even if that workflow is scheduled. You may activate a paused workflow without redefining the schedule (if a schedule exists).

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to pause, from the |fa-kebab| menu, select **Pause**. Confirm that you want to pause the model by clicking **Pause**.


.. _models-howtows-promote-from-sandbox:

Promote from a sandbox
--------------------------------------------------

.. TODO: ROUGH NOTES

The following steps are needed to prepare a model for sandbox promotion.

#. Create a sandbox
#. Run the database(s) in which your brand intends to activate models
#. :ref:`Add models <models-howtows-add>`
#. Kick off a model validations in the lower left-hand-side of the page. When complete, confirm that validation metrics are passing.
#. :ref:`Kick off training jobs <models-howtows-view-jobs>`
#. :ref:`When the training jobs are complete, kick off inference jobs <models-howtows-view-jobs>`
#. When the inference job is complete, re-run the database to populate the predictive data asset.
#. :ref:`Active the model <models-howtows-activate>`
#. Promote the sandbox.


.. _models-howtows-schedule:

Schedule a model
--------------------------------------------------

A model must be associated with a scheduled courier group workflow.

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to schedule, from the |fa-kebab| menu, select **Schedule workflow**. This opens the **Model schedule** dialog.
#. The **Training job cadence** is the frequency at which additional data is made available to the model to improve accuracy. The default is every two weeks.
#. The **Inference job cadence** is the frequency at which predictions are generated. The default is daily.
#. Click **Save**.


.. _models-howtows-view-jobs:

View jobs
--------------------------------------------------

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to schedule, from the |fa-kebab| menu, select **Jobs**. This opens the **Jobs** page.
#. You can run the full predictive workflow or individual jobs by type.
#. The results for each job are shown on the right side, including past run dates, run status, and the number of records in the results.


.. _models-howtows-view-model-configuration:

View model configuration
--------------------------------------------------

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to schedule, from the |fa-kebab| menu, select **View**. This opens the page for selected model.


.. _models-howtows-view-model-versions:

View model versions
--------------------------------------------------

#. From the **Customer 360** page, open the **Databases** tab.
#. Choose a database, and then from the |fa-kebab| menu, select **Predictive models**. This opens the **Predictive models** page.
#. In the row with the model you want to schedule, from the |fa-kebab| menu, select **View**. This opens the page for selected model.
#. A dropdown menu at top of the page lists the current configuration as the default. Earlier configurations are available from the same dropdown.
