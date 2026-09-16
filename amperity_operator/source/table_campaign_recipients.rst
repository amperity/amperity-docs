.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure and manage the Campaign Recipients table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Campaign Recipients table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Campaign Recipients table

==================================================
Campaign Recipients table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-campaign-recipients-table-start
   :end-before: .. term-campaign-recipients-table-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-campaign-recipients-about-start
   :end-before: .. data-tables-campaign-recipients-about-end

.. _table-campaign-recipients-requirements:

Requirements
==================================================

.. table-campaign-recipients-requirements-start

The **Campaign Recipients** table requires at least one campaign to be configured, and then sent from Amperity.

.. table-campaign-recipients-requirements-end


.. _table-campaign-recipients-delivery-dates:

Campaign delivery dates
==================================================

.. table-campaign-recipients-delivery-dates-start

The following query returns campaigns sorted by earliest and latest delivery dates by campaign ID or campaign name.

.. code-block:: sql
   :linenos:

   SELECT
     campaign_id
     ,campaign_name
     ,sub_audience_name
     ,treatment_name 
     ,treatment_id
     ,delivery_datetime
     ,MIN(delivery_datetime) AS earliest_delivery_date
     ,MAX(delivery_datetime) AS latest_delivery_date
   FROM Campaign_Recipients 
   WHERE campaign_id IN ('campaign-id')
   OR campaign_name IN ('campaign-name')
   GROUP BY 1,2,3,4,5,6
   ORDER BY 5,6,7

where the **WHERE** statement is updated for the specific campaign ID or campaign name.

.. table-campaign-recipients-delivery-dates-end


.. _table-campaign-recipients-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-campaign-recipients-table-about-start
   :end-before: .. data-tables-campaign-recipients-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-campaign-recipients-table-start
   :end-before: .. data-tables-campaign-recipients-table-end
