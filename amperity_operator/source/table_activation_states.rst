.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        What are the Activation States tables?

.. meta::
    :content class=swiftype name=body data-type=text:
        What are the Activation States tables?

.. meta::
    :content class=swiftype name=title data-type=string:
        Activation States tables

==================================================
Activation States tables
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-activation-states-tables-start
   :end-before: .. term-activation-states-tables-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-campaign-recipients-summary-about-start
   :end-before: .. data-tables-campaign-recipients-summary-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-campaign-recipients-summary-sandboxes-start
   :end-before: .. data-tables-campaign-recipients-summary-sandboxes-end


.. _table-activation-states-campaigns:

For campaigns
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-activation-states-campaigns-start
   :end-before: .. data-tables-activation-states-campaigns-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-activation-states-campaigns-usewith-start
   :end-before: .. data-tables-activation-states-campaigns-usewith-end

.. table-activation-states-campaigns-tip-start

.. tip:: Each filter for campaign activation states applies an **AND** operator to the criteria. The potential audience gets smaller as additional filters are applied.

   For example, if the entry count is 3 and the campaign sends a sub-audience to Braze, then only customers activated 3 or more times *and* belong to the sub-audience activated in Braze will be returned by the segment.

.. table-activation-states-campaigns-tip-end

**To use campaigns activation activity in a segment**

.. table-activation-states-campaigns-usewith-steps-start

#. Open the **Segments Editor**.
#. Click **Add condition**, choose **Activation activity**, and then select **In a campaigns**.

#. From the **Segments Editor** click the **Filters** link for the selected activiation activity. This opens the **Filter criteria** dialog box.

#. From the **Filter criteria** dialog box select a campaigns from the **Campaigns** dropdown.

   Optional. Apply additional filters:

   Select a destination from the **Destination** dropdown.

   Select a sub-audience from the **Sub audience** dropdown.

   Select a treatment from the **Treatment** dropdown.

   Use **Entry count** to define the number of customers who belong to the campaign.

   Use the **First entry time** and **Last entry time** fields to define the first and last times on which a customer was part of the campaign.

#. Click **Save**.

.. table-activation-states-campaigns-usewith-steps-end

**Field reference**

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-activation-states-campaigns-fields-start
   :end-before: .. data-tables-activation-states-campaigns-fields-end


.. _table-activation-states-journeys:

For journeys
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-activation-states-journeys-start
   :end-before: .. data-tables-activation-states-journeys-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-activation-states-journeys-usewith-start
   :end-before: .. data-tables-activation-states-journeys-usewith-end

.. table-activation-states-journeys-tip-start

.. tip:: Each filter for journey activation states applies an **AND** operator to the criteria. The potential audience gets smaller as additional filters are applied.

   For example, if the entry count is 5 and the node is an activation that sends an audience to Braze, then only customers activated 5 or more times *and* activated in Braze will be returned by the segment.

.. table-activation-states-journeys-tip-end

**To use journey activation activity in a segment**

#. Open the **Segments Editor**.
#. Click **Add condition**, choose **Activation activity**, and then select **In a journey**.

#. From the **Segments Editor** click the **Filters** link for the selected activiation activity. This opens the **Filter criteria** dialog box.

#. From the **Filter criteria** dialog box select a journey from the **Journey** dropdown.

   Optional. Apply additional filters:

   Select a node within that journey from the **Node** dropdown.

   Use **Entry count** to define the number of customers who have entered the node.

   Use the **First entry time** and **Last entry time** fields to define the first and last times on which a customer entered the selected node.

#. Click **Save**.

.. table-activation-states-journeys-usewith-end

**Field reference**

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-activation-states-journeys-fields-start
   :end-before: .. data-tables-activation-states-journeys-fields-end
