.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        An activation ID is a unique identifier that is used for precise segmentation and campaign targeting.

.. meta::
    :content class=swiftype name=body data-type=text:
        An activation ID is a unique identifier that is used for precise segmentation and campaign targeting.

.. meta::
    :content class=swiftype name=title data-type=string:
        Activation IDs

==================================================
About activation IDs
==================================================

.. activation-ids-intro-start

An activation ID is any unique identifier that your brand wants to use for precise segmentation and campaign targeting. Use activation IDs to associate a unique ID that is applied to certain types of marketing activity with the audiences you send downstream from Amperity.

The default activation ID within Amperity is the **Amperity ID**. Your brand can configure additional identifiers as activation IDs, such as email addresses, loyalty account IDs, mobile advertising IDs, customer account IDs, or any other unique identifier, to support using segments to build audiences for those activation IDs, and then make those audiences available for use in campaigns.

.. activation-ids-intro-end


.. _activation-ids-configure:

Configure activation IDs
==================================================

.. activation-ids-configure-start

Additional activation IDs may be configured.

.. activation-ids-configure-end

**To configure activation IDs**

.. activation-ids-configure-steps-start

#. From the **Customer 360** page, open the **Databases** tab.
#. Open a database in **Edit** mode.
#. In the right-side navigation pane, under **Activation IDs**, click **Add activation ID**. This opens the **Activation ID** dialog.
#. Open the **Base table** dropdown.

   Choose a table, and then choose a field in that table that is used as an activation ID.

#. Required. Assign the activation ID a friendly name, along with a singular and a plural version of the friendly name.

   These terms is used within the Amperity user interface.

   For example: "Email ID" is the friendly name, "email address" is the singular version, and "email addresses" is the plural version.

   .. important:: Type the friendly name and the singular and plural versions of the friendly name exactly as you want them to appear in the Amperity user interface. These are case-sensitive and are required. For example: "customer_id", "Customer_ID", "Customer ID", or "CustomerID" for the friendly name, "customer ID" for the singular, and "customer IDs" for the plural.

#. Optional. Add a description of the activation ID.
#. Click **Save**, and then **Activate**.

   Activation IDs are available immediately after the database is activated and do not require the database to be run.

.. activation-ids-configure-steps-end


.. _activation-ids-configure-default-attributes:

About default attributes and activation IDs
==================================================

.. activation-ids-configure-default-attributes-start

Default attributes are applied automatically when a destination is selected within a campaign.

Each default attribute is associated with a database *and* an activation ID. The list of tables from which attributes may be selected is filtered to match only those tables with a matching activation ID.

Configure default attributes for each combination of destination + activation ID that is used with campaigns. For example, configure default attributes for each of the following combinations:

* Send to Braze from the **C360** database for **Loyalty ID**.
* Send to Braze from the **C360** database for **Customer ID**.
* Send to Meta Ads Manager from the **C360** database for **Customer ID**. Map the **Customer ID** field to **EXTERN_ID**.
* Send to The Trade Desk from the C360 database for **email**, which is sent as a UID2 token from Amperity.

.. activation-ids-configure-default-attributes-end

**To configure default attributes**

.. activation-ids-configure-default-attributes-steps-start

#. Open the **Activations** page and select the **Campaigns** tab.
#. Click **Settings**.

#. On the **Default attributes** tab, click **Add default attributes**. This opens the **Configure attributes** dialog.

#. Under **Configure attributes** do the following:

   Select a destination from the **Destination** dropdown.

   Select a database from the **Databases** dropdown.

   Select a configured activation ID from the **Activation ID** dropdown.

#. Under **Default attributes** click **Add attribute**. Select a table, and then choose an attribute.

#. After all default attributes are configured click **Save**.

.. activation-ids-configure-default-attributes-steps-end


.. _activation-ids-use-in-segments:

Use in segments
==================================================

.. include:: ../../amperity_reference/source/segments_howtos.rst
   :start-after: .. segments-choose-activation-id-start
   :end-before: .. segments-choose-activation-id-end

**To use an activation ID in a segment**

.. include:: ../../amperity_reference/source/segments_howtos.rst
   :start-after: .. segments-choose-activation-id-steps-start
   :end-before: .. segments-choose-activation-id-steps-end


.. _activation-ids-use-in-campaigns:

Use in campaigns
==================================================

.. include:: ../../amperity_reference/source/campaigns.rst
   :start-after: .. campaigns-choose-activation-id-start
   :end-before: .. campaigns-choose-activation-id-end
