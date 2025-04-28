.. https://docs.amperity.com/operator/


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

The default activation ID within Amperity is the **Amperity ID**. Your brand can configure additional identifiers as activation IDs, such as email addresses, loyalty account IDs, mobile advertising IDs, customer account IDs, or any other unique identifier, to support using segments to build audiences for those activation IDs, and then make those audiences availble for use in campaigns.

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

   Choose a table, and then choose a field in that table that will be used as an activation ID.

#. Required. Assign the activation ID a friendly name, along with a singular and a plural version of the friendly name.

   These terms will be used within the Amperity user interface.

   For example: "Email ID" is the friendly name, "email address" is the singular version, and "email addresses" is the plural version.

   .. important:: Type the friendly name and the singular and plural versions of the friendly name exactly as you want them to appear in the Amperity user interface. These are case-sensitive and are required. For example: "customer_id", "Customer_ID", "Customer ID", or "CustomerID" for the friendly name, "customer ID" for the singular, and "customer IDs" for the plural.

#. Optional. Add a description of the activation ID.
#. Click **Save**, and then **Activate**.

   Activation IDs are available immediately after the database is activated and do not require the database to be run.

.. activation-ids-configure-steps-end


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
