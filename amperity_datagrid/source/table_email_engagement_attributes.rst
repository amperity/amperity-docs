.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Email Engagement Attributes table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Email Engagement Attributes table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Email Engagement Attributes table

==================================================
Email Engagement Attributes table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-engagement-attributes-table-start
   :end-before: .. term-email-engagement-attributes-table-end

.. table-email-engagement-attributes-important-start

.. important:: The **Email Engagement Attributes**, :doc:`Email Engagement Summary <table_email_engagement_summary>`, and :doc:`Unified Email Events <table_unified_email_events>` tables are used to enable email engagement workflows within Amperity.

   The **Email Engagement Summary** and **Unified Email Events** tables are generated as Stitch output after applying |semantics_email_events| semantic tags to data sources that contain email engagement data, such as opens, clicks, opt-in and opt-out preferences, or conversions, along with |semantics_email_events_summary| if that data is available.

   The **Email Engagement Attributes** table is built in your customer 360 database using a built-in SQL template. Some customization of this SQL template is necessary to align the behavior of this table to the data that exists in your tenant.

.. table-email-engagement-attributes-important-end

.. table-email-engagement-attributes-note-start

.. note:: The **Email Engagement Attributes** table relies on the **Merged Customers** table and must be added to your customer 360 database using a SQL template.

.. table-email-engagement-attributes-note-end


.. _table-email-engagement-attributes-add:

Add table
==================================================

.. table-email-engagement-attributes-add-start

The **Email Engagement Attributes** table is a table that contains one email address for each Amperity ID. This table may be used to apply email engagement data to campaigns. The **Email Engagement Attributes** table is built from a SQL template, is customized for your tenant, and then applies a series of **email-attribute** semantic tags to the fields in the table.

.. table-email-engagement-attributes-add-end

**To add the Customer360 table**

.. table-email-engagement-attributes-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "Email Engagement Attributes".
#. Set the build mode to **SQL**.
#. Click **Apply template**, and then select **Email Engagement Attributes**.
#. Step through the table, and then apply any necessary customizations.
#. Click **Next**. This opens the **Database Table Definition** page.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. Verify that the **db/required** and **db/unique** database field semantics were applied to the **amperity_id** column.
#. Verify that **email-attribute** :ref:`semantic tags <table-email-engagement-attributes-semantic-tags>` are applied to all fields.
#. Review picklists to ensure they have the desired sorting parameters.
#. Add friendly names for any field.
#. From the **Table Semantics** drop-down, select **Email Engagement Attributes**.
#. Click **Save**.

.. table-email-engagement-attributes-add-steps-end


.. _table-email-engagement-attributes-semantic-tags:

Apply semantic tags
==================================================

.. table-email-engagement-attributes-semantic-tags-start

Apply the following email attributes table semantics to the table that is created by the **Email Attributes** SQL template. Use the built-in list of semantics when building a table in your customer 360 database. Email attributes semantics are prefixed with **email-attributes/** and are applied to database tables using the database editor.

.. table-email-engagement-attributes-semantic-tags-end

.. table-email-engagement-attributes-semantic-tags-warning-start

.. warning:: Email attributes semantic tags must be applied to a SQL table in your customer 360 database. Email attributes semantic tags cannot be applied to raw email events data on the Sources page.

.. table-email-engagement-attributes-semantic-tags-warning-end

.. table-email-engagement-semantics-attributes-about-start

The following table lists the tags available to this semantic group (with required semantic tags noted by "|checkmark-required| **Required**." and recommended semantic tags noted by "|checkmark-recommended| **Recommended**"):

.. table-email-engagement-semantics-attributes-table-about-end

.. table-email-engagement-semantics-attributes-table-start

.. list-table::
   :widths: 150 50 400
   :header-rows: 1

   * - Semantic Name
     - Datatype
     - Description
   * - **brand**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-brand-start
          :end-before: .. email-events-brand-end

   * - **email**
     - String
     - |checkmark-required| **Required**.

       .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-email-start
          :end-before: .. email-events-email-end
   * - **email-clicks-last-x-days**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-clicks-x-days-start
          :end-before: .. email-events-clicks-x-days-end
   * - **email-clicks-last-x-months**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-clicks-x-months-start
          :end-before: .. email-events-clicks-x-months-end
   * - **email-opens-last-x-days**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-opens-x-days-start
          :end-before: .. email-events-opens-x-days-end
   * - **email-opens-last-x-months**
     - Integer
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-opens-x-months-start
          :end-before: .. email-events-opens-x-months-end
   * - **engagement-frequency-last-15-months**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-engagement-frequency-15-months-start
          :end-before: .. email-events-engagement-frequency-15-months-end
   * - **engagement-status-last-15-months**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-engagement-status-15-months-start
          :end-before: .. email-events-engagement-status-15-months-end
   * - **first-email-click-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-first-click-start
          :end-before: .. email-events-first-click-end
   * - **first-email-open-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-first-open-start
          :end-before: .. email-events-first-open-end
   * - **first-email-send-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-first-send-start
          :end-before: .. email-events-first-send-end
   * - **most-recent-bounce-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-bounce-start
          :end-before: .. email-events-most-recent-bounce-end
   * - **most-recent-email-click-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-click-start
          :end-before: .. email-events-most-recent-click-end
   * - **most-recent-email-open-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-open-start
          :end-before: .. email-events-most-recent-open-end
   * - **most-recent-email-optin-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-optin-start
          :end-before: .. email-events-most-recent-optin-end
   * - **most-recent-email-optout-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-optout-start
          :end-before: .. email-events-most-recent-optout-end
   * - **most-recent-email-send-datetime**
     - Datetime
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-most-recent-send-start
          :end-before: .. email-events-most-recent-send-end
   * - **purchase_before_signup**
     - Boolean
     - Indicates when an Amperity ID is associated with a transaction that occurred before signing up with this email address.

       .. important:: This semantic tag requires the **Transaction Attributes** and **Unified Transactions** tables to be joined to the **Email Engagement Attributes** table.

   * - **region**
     - String
     - .. include:: ../../shared/email-events.rst
          :start-after: .. email-events-region-start
          :end-before: .. email-events-region-end
   * - **signup_to_purchase_days**
     - Integer
     - The amount of time (in days) between using this email to sign up and the next transaction associated with this Amperity ID. This field is NULL if there has not been a transaction.

       .. important:: This semantic tag requires the **Transaction Attributes** and **Unified Transactions** tables to be joined to the **Email Engagement Attributes** table.

.. table-email-engagement-semantics-attributes-table-end
