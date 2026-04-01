.. https://docs.amperity.com/reference/


==================================================
Lab 04: Modifying databases
==================================================

Combining implementation specific data that has been ingested or transformed with these core data assets form the building blocks for your organization's reporting and analytics view. A complete view of the customer helps organizations make more informed decisions about their customers. In this lab you will explore a common scenario of changing the PII displayed about customers. You will also add additional attributes about the customer, both attributes pre-built by Amperity and custom attributes.

.. admonition:: Reference materials

   * `Core tables <../reference/databases.html#core-tables>`__ |ext_link|
   * `Customer_360 <../reference/data_tables.html#customer-360>`__ |ext_link|
   * `Unified Coalesced <../reference/data_tables.html#unified-coalesced>`__ |ext_link|
   * `Unified_Customer <../reference/data_tables.html#unified-customer>`__ |ext_link|
   * `Merged Customers <../reference/data_tables.html#merged-customers>`__ |ext_link|
   * `Unified Transactions <../reference/data_tables.html#unified-transactions>`__ |ext_link|
   * `Transaction Attributes Extended <../reference/data_tables.html#transaction-attributes-extended>`__ |ext_link|

   **Related to sources**

   * `Semantic Tags <../reference/semantics.html>`__ |ext_link|
   * `Custom Domain Tables <../reference/domain_tables.html#custom-domain-tables>`__ |ext_link|
   * `Foreign keys (fk) <../reference/semantics.html#foreign-keys-fk>`__ |ext_link|


Objective
==================================================

In this lab exercise you will learn about building and configuring Databases to build off the data assets you have ingested and stitched in the training tenant:

#. Modify the PII attributes of the **Customer 360** table.
#. Add pre-built transaction attributes to the **Customer 360** table.


Create a new sandbox for the exercise
==================================================

#. Log into your production training tenant at https://app.amperity.com.

#. Navigate to the **Settings** page and locate the **Sandboxes** subtab on this page.

#. Create a new sandbox using the following information:

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Amperity field
        - Value to enter
      * - **Sandbox Name**
        - TET-YourName-Lab3-SB
      * - **Sandbox Description**
        - A sandbox to update the database configuration

#. Use the tenant dropdown or the **Actions** to select the **Go to sandbox** button to switch to the sandbox you just created.

#. Ensure you are in the sandbox training tenant. Sandbox tenants utilize the teal blue navigation color scheme. Sandboxes also display the sandbox status banner. You can quickly switch between tenants by clicking on the tenant selection menu in the top-right corner of the screen.

   .. image:: /_images/ex04_open_training_tenant.png
      :width: 300 px
      :alt: Open training tenant
      :align: left
      :class: no-scaled-link

#. Navigate to the **Quick start** page and click on **View details** to the right of **Identity resolution**.

   .. image:: /_images/ex04_quickstart_idres.png
      :width: 500 px
      :alt: Quick start identity resolution
      :align: left
      :class: no-scaled-link

#. Click **Edit** on **Identify your fields**.

   .. image:: /_images/ex04_identify_fields.png
      :width: 500 px
      :alt: Identity fields
      :align: left
      :class: no-scaled-link

#. With the **online_customers_out** table selected in the top left-hand corner, enter the semantic tag for the **cust_id** semantic field as **fk-onlinecustomerid** and click on **Add fk-onlinecustomerid** and then click **Save & Close**.

   This will automatically update Stitch rules.

   .. image:: /_images/ex04_update_stitch_rules.png
      :width: 500 px
      :alt: Update Stitch rules
      :align: left
      :class: no-scaled-link

#. Return to the **Quick start** page, and click on **View details**. In the **Datasources** tile, click on "Training Data Bridge", and then on **Edit selections**.

   .. image:: /_images/ex04_return_to_quickstart.png
      :width: 500 px
      :alt: Return to quick start
      :align: left
      :class: no-scaled-link

#. Select **online_itemized_out** and **product_catalog** and click on **Next**.

   .. image:: /_images/ex04_training_data_bridge.png
      :width: 400 px
      :alt: Training data bridge
      :align: left
      :class: no-scaled-link

#. Click on **Save and sync**.

   .. image:: /_images/ex04_save_and_sync.png
      :width: 400 px
      :alt: Save and sync
      :align: left
      :class: no-scaled-link

#. From the **Sources** page in the **Custom domain tables** section, select **Add table**.

   .. image:: /_images/ex04_custom_domain_tables.png
      :width: 400 px
      :alt: Custom domain tables
      :align: left
      :class: no-scaled-link

#. Name the table **online_itemized_transactions_CDT** and click **Save**.

   .. image:: /_images/ex04_create_custom_domain_table.png
      :width: 500 px
      :alt: Create custom domain tables
      :align: left
      :class: no-scaled-link

#. Paste in the following SQL and click **Next**.

   .. code-block:: sql
      :linenos:

      SELECT
        CONCAT(
          OT.cust_id
          ,OT.order_id
          ,OT.order_datetime
          ,PC.product_id
          ,PC.product_subcategory
          ,OT.code
        ) AS PrimaryKey
        ,OT.cust_id AS `customer_id`
        ,OT.order_id AS `order_id`
        ,OT.order_datetime AS `order_datetime`
        ,CASE
          WHEN OT.code = 'return' THEN null
          WHEN OT.code = 'cancellation' THEN null
          ELSE COALESCE(OT.item_discount/OT.item_revenue, 0)
        END AS discount_percent_calculated
        ,OT.item_discount
        ,OT.item_revenue AS `item_revenue`
        ,OT.item_quantity AS `item_quantity`
        ,OT.code AS `code`
        ,CASE
          WHEN OT.code = 'return' THEN true
          ELSE false
        END AS is_return
        ,CASE
          WHEN OT.code = 'cancellation' THEN true
          ELSE false
        END AS is_cancellation
        ,OT.purchase_brand
        ,OT.purchase_channel
        ,0 as store_id
        ,PC.product_id AS `product_id`
        ,PC.product_category
        ,PC.product_subcategory
      FROM online_itemized_out AS OT
      LEFT JOIN product_catalog AS PC ON PC.product_id = OT.product_id

#. Update the semantic tags using the following table and click **Activate**.

   .. list-table::
      :widths: 40 20 40
      :header-rows: 1

      * - Field name
        - Data type
        - Semantics
      * - **PrimaryKey**
        - String
        - pk
      * - **customer_id**
        - String
        - fk-onlinecustomerid
      * - **order_id**
        - String
        - txn-item/order-id
      * - **order_datetime**
        - Datetime
        - txn-item/order-datetime
      * - **discount_percent_calculated**
        - Float
        - txn-item/item-discount-percent
      * - **item_discount**
        - Integer
        - txn-item/item-discount-amount
      * - **item_revenue**
        - Float
        - txn-item/item-revenue
      * - **item_quantity**
        - Integer
        - txn-item/item-quantity
      * - **code**
        - String
        - Set semantics...
      * - **is_return**
        - Boolean
        - txn-item/is-return
      * - **is_cancellation**
        - Boolean
        - txn-item/is-cancellation
      * - **purchase_brand**
        - String
        - txn-item/purchase-brand
      * - **purchase_channel**
        - String
        - txn-item/purchase-channel
      * - **store_id**
        - Integer
        - txn-item/store-id
      * - **product_id**
        - String
        - txn-item/product-id
      * - **product_category**
        - String
        - txn-item/product-category
      * - **product_subcategory**
        - String
        - txn-item/product-subcategory

   .. image:: /_images/ex04_update_semantic_tags.png
      :width: 500 px
      :alt: Update semantic taggs
      :align: left
      :class: no-scaled-link

#. Navigate to the **Customer 360** page, select the kebab menu |fa-kebab| next to the existing **Customer Profiles** database and select **Delete**. Follow the prompt to delete the database.

   .. image:: /_images/ex04_navigate_to_c360.png
      :width: 340 px
      :alt: Navigate to Customer 360 page
      :align: left
      :class: no-scaled-link

#. Click **Create Database** and in the prompt type **Customers Profiles** for the name and select the **Customer 360** template. Leave the permissions as **Admin only** and click **Create** to create the new database with all the transaction tables.

   .. image:: /_images/ex04_create_database.png
      :width: 340 px
      :alt: Create database
      :align: left
      :class: no-scaled-link

#. After the database is created you will be automatically dropped into the **Edit** interface for the database. To reach this at any time click the kebab menu |fa-kebab| and select **Edit**.

#. Click **Add table** to add the **Has_Purchased_Brand** table. In the top left corner of the screen, rename the table to **Has_Purchased_Brand** then select **Build Mode** of **Custom SQL**, and then paste in the following SQL then click on **Next**.

   .. image:: /_images/ex04_add_table_to_database.png
      :width: 400 px
      :alt: Add table to database
      :align: left
      :class: no-scaled-link

   .. code-block:: sql
      :linenos:

      SELECT
        amperity_id
        ,MAX(
          CASE WHEN purchase_brand = 'TrendyBear' THEN true ELSE false
          END
        ) AS Is_Trendy_Bear_Customer
        ,MAX(
          CASE WHEN purchase_brand = 'FoxEssentials' THEN true ELSE false
          END
        ) AS Is_Fox_Essentials_Customer
        ,MAX(
          CASE WHEN purchase_brand = 'GoldenSwan' THEN true ELSE false
          END
        ) AS Is_Golden_Swan_Customer
      FROM Unified_Itemized_Transactions
      GROUP BY 1

#. In the screen that comes up, click **Generate field descriptions** and then **Save**.

   .. image:: /_images/ex04_generate_field_descriptions.png
      :width: 500 px
      :alt: Generate field descriptions
      :align: left
      :class: no-scaled-link

#. Click on the kebab menu |fa-kebab| to the right of the **Customer 360** table and select **Edit** to update the table.

   .. image:: /_images/ex04_edit_to_update_table.png
      :width: 500 px
      :alt: Edit to update table
      :align: left
      :class: no-scaled-link

#. In the screen that comes up, replace the existing SQL by pasting in the following SQL, then click on **Next**.

   .. image:: /_images/ex04_replace_sql.png
      :width: 500 px
      :alt: Replace SQL
      :align: left
      :class: no-scaled-link

   .. code-block:: sql
      :linenos:

      SELECT
        mc.amperity_id AS `amperity_id`
        ,mc.given_name AS `given_name`
        ,mc.surname AS `surname`
        ,mc.full_name AS `full_name`
        ,mc.address AS `address`
        ,mc.city AS `city`
        ,mc.state AS `state`
        ,mc.postal AS `postal`
        ,mc.email AS `email`
        ,mc.phone AS `phone`
        ,mc.birthdate AS `birthdate`
        ,mc.gender AS `gender`
        ,ta.multi_purchase_brand AS `multi_purchase_brand`
        ,ta.multi_purchase_channel AS `multi_purchase_channel`
        ,ta.one_and_done AS `one_and_done`
        ,ta.early_repeat_purchaser AS `early_repeat_purchaser`
        ,ta.first_order_id AS `first_order_id`
        ,ta.first_order_datetime AS `first_order_datetime`
        ,ta.first_order_revenue AS `first_order_revenue`
        ,ta.first_order_total_items AS `first_order_total_items`
        ,ta.first_order_is_retained AS `first_order_is_retained`
        ,ta.second_order_id AS `second_order_id`
        ,ta.second_order_datetime AS `second_order_datetime`
        ,ta.second_order_revenue AS `second_order_revenue`
        ,ta.second_order_total_items AS `second_order_total_items`
        ,ta.second_order_is_retained AS `second_order_is_retained`
        ,ta.latest_order_id AS `latest_order_id`
        ,ta.latest_order_datetime AS `latest_order_datetime`
        ,ta.latest_order_revenue AS `latest_order_revenue`
        ,ta.latest_order_total_items AS `latest_order_total_items`
        ,ta.lifetime_preferred_purchase_brand AS `lifetime_preferred_purchase_brand`
        ,ta.lifetime_preferred_purchase_channel AS `lifetime_preferred_purchase_channel`
        ,ta.lifetime_order_revenue AS `lifetime_order_revenue`
        ,ta.lifetime_order_frequency AS `lifetime_order_frequency`
        ,ta.lifetime_total_items AS `lifetime_total_items`
        ,ta.lifetime_largest_order_value AS `lifetime_largest_order_value`
        ,ta.lifetime_average_order_value AS `lifetime_average_order_value`
        ,ta.lifetime_average_item_price AS `lifetime_average_item_price`
        ,ta.lifetime_average_num_items AS `lifetime_average_num_items`
        ,HPB.Is_Trendy_Bear_Customer
        ,HPB.Is_Golden_Swan_Customer
        ,HPB.Is_Fox_Essentials_Customer
      FROM Merged_Customers mc
      LEFT JOIN Transaction_Attributes_extended ta ON mc.amperity_id = ta.amperity_id
      LEFT JOIN Has_Purchased_Brand AS HPB ON HPB.Amperity_ID = MC.Amperity_ID

#. In the screen that comes up click **Generate field descriptions** and then **Save**.

   .. image:: /_images/ex04_generate_field_descriptions2.png
      :width: 500 px
      :alt: Generate field descriptions
      :align: left
      :class: no-scaled-link

#. Click **Activate** in the database editor window.

   .. image:: /_images/ex04_activate_database.png
      :width: 500 px
      :alt: Activate database
      :align: left
      :class: no-scaled-link

#. Click **Review changes** in the sandbox promote notification.

   .. image:: /_images/ex04_review_changes.png
      :width: 400 px
      :alt: Review changes
      :align: left
      :class: no-scaled-link

#. Select **Yes**, continue and update all necessary tables. Amperity requires a **Merge message** for promotion. Provide a descriptive **Merge message** such as: "This merge updates existing tables and adds new tables." Click on **Promote**.

   .. image:: /_images/ex04_update_necessary_tables.png
      :width: 500 px
      :alt: Update necessary tables
      :align: left
      :class: no-scaled-link

#. In the **Promote changes** modal, select the default **Promote and delete sandbox** and click **Promote**.

   .. image:: /_images/ex04_promote_changes.png
      :width: 380 px
      :alt: Promote changes
      :align: left
      :class: no-scaled-link

#. After you are returned to your production tenant, select the **Sources** page and on the **Actions** kebab menu |fa-kebab| to the right of the **Courier group Daily** and select **Run**.

   .. image:: /_images/ex04_open_sources_page.png
      :width: 500 px
      :alt: Open sources page
      :align: left
      :class: no-scaled-link

#. Select **Partial workflow** and click on **Run**.

   .. image:: /_images/ex04_partial_workflow.png
      :width: 400 px
      :alt: Partial workflow
      :align: left
      :class: no-scaled-link

#. Check that the **Daily** workflow under the **Workflows** page has started.
