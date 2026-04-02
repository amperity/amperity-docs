.. https://docs.amperity.com/reference/


==================================================
Lab 02: Enhancing C360 views
==================================================

The quality of your customer 360 data is dependent on the quantity and quality of the customer data in the tenant. A common routine task would be to enhance your tenant's customer 360 view with a new dataset.

.. admonition:: Reference materials

   * `Customer 360 table <../reference/data_tables.html#customer-360>`__ |ext_link|
   * `Semantic Tags <../reference/semantics.html>`__ |ext_link|


Objective
==================================================

In this exercise, you will learn how to work with personally identifiable information (PII) in Amperity to improve a customer 360 view by bringing in additional point-of-sale PII data using **Amperity Bridge**.


Enhance customer 360 view
==================================================

#. Navigate to the **Quick start** page and click on **View Details** to the right of **Identity resolution**.

   .. image:: /_images/ex02_start_page.png
      :width: 500 px
      :alt: Start page
      :align: left
      :class: no-scaled-link

#. Under **Datasources**, click **Training Data Bridge**.

   .. image:: /_images/ex02_training_data_bridge.png
      :width: 500 px
      :alt: Training Data Bridge
      :align: left
      :class: no-scaled-link

#. Click **Edit Selections**.

   .. image:: /_images/ex02_edit_selections_button.png
      :width: 400 px
      :alt: Edit Selections button
      :align: left
      :class: no-scaled-link

#. Select the checkbox next to **POS Customers Out** and click **Next**.

   .. image:: /_images/ex02_pos_customers_out_selection.png
      :width: 400 px
      :alt: POS Customers Out selection
      :align: left
      :class: no-scaled-link

#. Click **Save and Sync**.

   .. image:: /_images/ex02_save_and_sync_button.png
      :width: 400 px
      :alt: Data exclusion
      :align: left
      :class: no-scaled-link

#. Click the **Workflows** page and explore the "Bridge - Training Data Bridge" workflow.

   This workflow should take 3 to 5 minutes to complete. This is a good time to stretch your legs, grab a beverage, anything that you may need to do.

#. When the workflow is complete, click on the **Quick start** page and select **View Details**.

#. Click **AmpAI Select** to have **AmpAI** select identity tables and appropriately configure everything. This should only take ~20 seconds to complete.

   .. note:: If **AmpAI Select** does not appear to make any changes please refresh the page. This is a known bug.

      .. image:: /_images/ex02_ampai_select.png
         :width: 400 px
         :alt: AmpAI Select
         :align: left
         :class: no-scaled-link

#. Click **Edit on Identity tables**. You will see that both the **online_customers_out** and the **pos_customers_out** because they have identity data in them. Click **Cancel** to return back.

   .. image:: /_images/ex02_identity_tables.png
      :width: 400 px
      :alt: Identity tables
      :align: left
      :class: no-scaled-link

#. Click **Edit on Primary Key**.

   .. image:: /_images/ex02_primary_key_edit.png
      :width: 500 px
      :alt: Data exclusion
      :align: left
      :class: no-scaled-link

#. With the **online_customers_out** table selected in the top left-hand corner, select **dtUpdateDate** to add it to the **PK Selection**. Validate will run to make sure the key is 100% unique. Repeat these steps for the **pos_customers_out** table and then click **Save**.

   .. image:: /_images/ex02_primary_key_selection.png
      :width: 600 px
      :alt: Primary Key selection
      :align: left
      :class: no-scaled-link

#. Click **Edit** on **Identify your fields**.

   .. image:: /_images/ex02_identity_your_fields.png
      :width: 520 px
      :alt: Identify your fields
      :align: left
      :class: no-scaled-link

#. With the **online_customers_out** table selected in the top left-hand corner, check that the semantic tag for the **dtUpdateDate** field is set to **update-dt**. If it is not, use the dropdown to select it. Repeat these steps for the **pos_customers_out** table and then click **Save & Close**.

   These steps will prevent errors that have to be resolved when promoting the sandbox later.

   .. image:: /_images/ex02_semantic_tags_configurations.png
      :width: 500 px
      :alt: Semantic tags configuration
      :align: left
      :class: no-scaled-link

#. Click **Edit** on **Data exclusion** and review the data exclusions that are applied by default. These values are often edited to deal with unique data situations. Click on **Cancel** to return to **Quick start**.

   .. image:: /_images/ex02_data_exclusions.png
      :width: 520 px
      :alt: Data exclusion
      :align: left
      :class: no-scaled-link

#. Click on **Run Stitch** on **Generate Amperity IDs with Stitch**.

   .. image:: /_images/ex02_run_stitch.png
      :width: 500 px
      :alt: Run Stitch
      :align: left
      :class: no-scaled-link

#. Click the **Workflows** page and explore the **Manually triggered stitch job** workflow. This workflow should fail after about 9 to 12 minutes. We will troubleshoot this issue after the next lesson.
