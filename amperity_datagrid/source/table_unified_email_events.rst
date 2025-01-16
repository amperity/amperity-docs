.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Configure and manage the Unified Email Events table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Unified Email Events table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Unified Email Events table

==================================================
Unified Email Events table
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-email-events-table-start
   :end-before: .. term-unified-email-events-table-end

.. table-unified-email-events-important-start

.. important:: The :doc:`Email Engagement Attributes <table_email_engagement_attributes>`, :doc:`Email Engagement Summary <table_email_engagement_summary>`, and **Unified Email Events** tables are used to enable email engagement workflows within Amperity.

   The **Email Engagement Summary** and **Unified Email Events** tables are generated as Stitch output after applying |semantics_email_events| semantic tags to data sources that contain email engagement data, such as opens, clicks, opt-in and opt-out preferences, or conversions, along with |semantics_email_events_summary| if that data is available.

   The **Email Engagement Attributes** table is built in your customer 360 database using a built-in SQL template. Some customization of this SQL template is necessary to align the behavior of this table to the data that exists in your tenant.

.. table-unified-email-events-important-end


.. _table-unified-email-events-requirements:

Requirements
==================================================

.. table-unified-email-events-requirements-start

The **Unified Email Events** table has a dependency on the **Email Engagement Summary** table. The **Email Engagement Summary** table requires email summary semantic tags to be applied feeds and/or custom domain tables that contain email engagement data.

.. table-unified-email-events-requirements-end


.. _table-unified-email-events-reference:

Column reference
==================================================

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-email-events-table-about-start
   :end-before: .. data-tables-unified-email-events-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-email-events-table-start
   :end-before: .. data-tables-unified-email-events-table-end
