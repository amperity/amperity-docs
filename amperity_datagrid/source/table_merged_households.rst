.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Configure and manage the Merged Households table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Merged Households table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Merged Households table

==================================================
Merged Households table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-merged-households-table-start
   :end-before: .. term-merged-households-table-end

.. table-merged-households-start

The **Merged Households** table generates a household ID (as a UUID) for records with an exact match on **full_address** and **surname**. The **Merged Households** table requires the **Merged Customers** table to ensure that household IDs are applied *after* the best address has been identified.

.. table-merged-households-end

**To add the Merged Households table**

.. table-merged-households-steps-start

#. From the **Customer 360** page, under **All Databases**, open the menu for a database, and then click **Edit**.
#. Click **Add Table**.
#. Set **Build Mode** to "SQL", open the **Apply template** drop-down menu, and then select **Merged Households**.
#. Update the name of the table template to append the brand name to the table name.
#. Update the SQL in the table template for the correct name of the address standardization lookup table.
#. Verify semantic tags and ensure that fields that contain PII are marked correctly.
#. Make the table available to the **Segment** editor by selecting the **Make available in Visual Segment Editor** option.

   .. note:: Only tables that contain an Amperity ID may be made available to the **Segment** editor and used with campaigns.
#. Click **Activate** to update the database with your changes.

.. table-merged-households-steps-end
