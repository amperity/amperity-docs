.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the SMS Opt Status table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the SMS Opt Status table.

.. meta::
    :content class=swiftype name=title data-type=string:
        SMS Opt Status table

==================================================
SMS Opt Status table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sms-opt-status-table-start
   :end-before: .. term-sms-opt-status-table-end

.. table-sms-opt-status-important-start

.. important:: Amperity is not the source of truth for SMS consent status. SMS consent status can change, including between the time of this table's most recent update and the time at which your brand wants to send your customers an SMS message as part of a campaign.

   The source of truth for consent status exists downstream from Amperity, often directly within the marketing tool or application that you are using to configure the SMS campaign, such as Cordial, Braze, Klaviyo, or Attentive.

   Use this table to filter audiences in Amperity to include customers who have consented to receiving SMS messages, and then build a step within the downstream marketing tool that verifies consent status immediately prior to sending an SMS message.

.. table-sms-opt-status-important-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-optin-status-sms-note-start
   :end-before: .. data-tables-optin-status-sms-note-end


.. _table-sms-opt-status-add:

Add table
==================================================

.. table-sms-opt-status-add-start

The **SMS Opt Status** table is a recommended table for the customer 360 database and is always built as a passthrough table.

.. important:: This table is only available *after* semantic tags for |semantics_sms_optin| have been applied in your tenant.

.. table-sms-opt-status-add-end

**To add the SMS Opt Status table**

.. table-sms-opt-status-add-steps-start

#. From the **Customer 360** page, under **All Databases**, select the menu for the customer 360 database, and then click **Edit**.
#. From the **Database Editor**, click **Add Table**.
#. Name the table "SMS Opt Status".
#. Set the build mode to **Passthrough**.
#. From the **Source Table** dropdown, select the **SMS Opt Status** table.
#. Click **Next**.
#. Add a table description. This enables a tooltip that is visible from other areas in Amperity.
#. From the **Table Semantics** dropdown, select **SMS Opt Status**.

   .. important:: Remove any automatically applied customer profile semantic tags, such as **phone**, before saving the table.

#. Under **Version History**, select **Enable table version history**.
#. Click **Save**.

.. table-sms-opt-status-add-steps-end


.. _table-sms-opt-status-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-optin-status-sms-table-about-start
   :end-before: .. data-tables-optin-status-sms-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-optin-status-sms-table-start
   :end-before: .. data-tables-optin-status-sms-table-end
