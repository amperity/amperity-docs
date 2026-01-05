.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Customer 360 table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Customer 360 table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Customer 360 table

==================================================
Customer 360 table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-customer360-table-start
   :end-before: .. term-customer360-table-end


.. _table-customer360-add:

Add table
==================================================

.. table-customer360-add-start

The **Customer 360** table is the most important table in the customer 360 database. The **Customer 360** table is built as a passthrough from the **Merged Customers** table, which makes available to the **Customer 360** table a unified view of the customer across all points of engagement, along with any attributes that cross systems.

Attributes vary tenant-to-tenant, but typically include:

* Profile information, such as names, addresses, email, and phone
* Interactions by channel, such as ecommerce, point of sale, and loyalty
* Insights, such as total lifetime value, transaction frequency, and recency
* Predictions, such as next best purchase, next best action, and churn prediction

.. table-customer360-add-end

.. table-customer360-add-important-start

.. important:: This table is added automatically when the "Customer 360" template is used to add the customer 360 database. Using a template is the recommended way to add the recommended way to add the **Customer 360** table.

.. table-customer360-add-important-end

**To add the Customer360 table**

.. table-customer360-add-steps-start

#. From the **Customer 360** page, select the **Databases** tab, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Customer_360".
#. Set the build mode to **SQL**.
#. Click **Apply template**, and then select **Customer 360**.
#. Click **Validate** to verify the SQL runs without error.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that the **db/required** and **db/unique** database field semantics were applied to the **amperity_id** column.
#. Verify that semantic tags--**given_name**, **surname**, **email**, **phone**, **address**, **city**, **state**, **postal**, **birthdate**, **gender**, etc.--were applied to all PII fields correctly.

   .. tip:: You can clear incorrectly tagged semantics individually or for the entire table. To clear semantic tags for the entire table, under **Semantic Suggestions** click **Clear semantics**.
#. Review picklists to ensure they have the desired sorting parameters.
#. Add friendly names for any field. For example, add **First Name** as a friendly name for **given_name**.

   .. tip:: The profile attribute names under **Customer Profile** on the **Customer 360** page are the same names that are entered in the **Friendly Names** column. If a friendly name is not added, Amperity uses the **Field Name** as the profile attribute name, including capitalization and underscores.
#. Define the general sort order for fields in the customer profile.
#. Review icons assigned to fields. Assigned icons are visible under **Customer Profile** on the **Customer 360** page.

   .. note::

      .. include:: ../../shared/databases.rst
         :start-after: .. databases-font-awesome-picker-useany-start
         :end-before: .. databases-font-awesome-picker-useany-end

#. From the **Table Semantics** dropdown, select **Customer 360**.
#. Leave everything else unchanged.
#. Click **Save**.

.. table-customer360-add-steps-end


.. _table-customer360-add-hashed-columns:

Add SHA-256 hashed columns
==================================================

.. table-customer360-add-hashed-columns-start

You can add SHA-256 hashed PII columns to your **Customer 360** table to enable their use from within campaigns.

For example, Pinterest Ads and Reddit Ads allow audiences to be upload directly to their ads managers as a CSV file when the CSV file contains SHA-256 hashed email addresses. Build an audience Amperity, and then from the **Campaigns** page choose the column that contains the SHA-256 hashed email address from the **Edit attributes** page, send the results as a CSV file to cloud storage or SFTP, and then upload that CSV file to Pinterest Ads or Reddit Ads.

Add hashed PII columns to the **Customer 360** table using the |sql_spark_function_sha2| function:

.. code-block:: sql

   ,SHA2(LOWER(TRIM(email)),256) AS hashed_email
   ,SHA2(phone,256) AS hashed_phone

.. table-customer360-add-hashed-columns-end


.. _table-customer360-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-customer-360-table-about-start
   :end-before: .. data-tables-customer-360-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-customer-360-table-start
   :end-before: .. data-tables-customer-360-table-end
