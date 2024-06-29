.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Configure and manage the Email Engagement Summary table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Email Engagement Summary table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Email Engagement Summary table

==================================================
Email Engagement Summary table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-engagement-summary-table-start
   :end-before: .. term-email-engagement-summary-table-end

.. table-email-engagement-attributes-important-start

.. important:: The :doc:`Email Engagement Attributes <table_email_engagement_attributes>`, **Email Engagement Summary**, and :doc:`Unified Email Events <table_unified_email_events>` tables are used to enable email engagement workflows within Amperity.

   The **Email Engagement Summary** and **Unified Email Events** tables are generated as Stitch output after applying |semantics_email_events| semantic tags to data sources that contain email engagement data, such as opens, clicks, opt-in and opt-out preferences, or conversions, along with |semantics_email_events_summary| if that data is available.

   The **Email Engagement Attributes** table is built using a built-in SQL template in your customer 360 database. Some customization of this SQL template is necessary to align the behavior of this table to the data that exists in your tenant.

.. table-email-engagement-attributes-important-end


.. _table-email-engagement-attributes-requirements:

Requirements
==================================================

.. table-email-engagement-attributes-requirements-start

The **Email Engagement Summary** table requires a specific set of fields to be present before rolled-up calculations are enabled:

* Email clicks for 1, 3, 5, 7, 14 day intervals
* Email clicks for 3, 6, 9, 12 month intervals
* Email opens for 1, 3, 5, 7, 14 day intervals
* Email opens for 3, 6, 9, 12 month intervals

along with fields that track the date and time for the most recent click. Use the |semantics_email_events_summary| semantic tags to identify these fields.

Ask your Amperity representative about how to configure email engagement data when these requirements are not present.

.. table-email-engagement-attributes-requirements-end


.. _table-email-engagement-summary-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-email-engagement-summary-table-about-start
   :end-before: .. data-tables-email-engagement-summary-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-email-engagement-summary-table-start
   :end-before: .. data-tables-email-engagement-summary-table-end
