.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Add email engagement records to your tenant.

.. meta::
    :content class=swiftype name=body data-type=text:
        Add email engagement records to your tenant.

.. meta::
    :content class=swiftype name=title data-type=string:
        Enable email engagement

==================================================
Enable email engagement
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-engagement-start
   :end-before: .. term-email-engagement-end

.. email-engagement-start

Amperity provides a standardized way to capture email event details, from which a set of email engagement attributes are calculated.

Use email engagement data by applying :ref:`email events <add-email-engagement-semantics-email-events>` **OR** :ref:`email summary <add-email-engagement-semantics-email-summary>` semantic tags to feeds that contain email engagement data.

.. email-engagement-start


.. _add-email-engagement-data-sources:

About data sources
==================================================

.. add-email-engagement-data-sources-start

Two types of data sources exist for providing email engagement data to Amperity: "raw email events" and "summarized events".

Your tenant's approach to adding email engagement will determine which types of data sources to use, along with which sets of semantic tags will be applied to incoming data.

.. add-email-engagement-data-sources-end


.. _add-email-engagement-data-source-raw:

Raw email events
--------------------------------------------------

.. add-email-engagement-data-source-raw-start

Raw email events data is captured by email service providers when users interact with emails, such as opens, clicks, opt-ins, opt-outs, sends, unsubscribes, and conversions.

A custom domain table is often necessary to :ref:`filter and reshape raw email events data <add-email-engagement-example-custom-domain-table>` prior to applying :ref:`email events <add-email-engagement-semantics-email-events>` semantic tags.

Raw email events data is available from most email service providers, though the specific data points that are available may vary from provider to provider.

Salesforce Marketing Cloud, Oracle Repsonsys, Mailchimp, Campaign Monitor, Bluecore, Klaviyo, Adobe Marketo, Adobe Campaign, Sailthru, Listrak, SendGrid, and HubSpot are all data sources that can provide usable raw email events data to Amperity.

.. add-email-engagement-data-source-raw-end

.. add-email-engagement-data-source-raw-important-start

.. important:: Raw email events data is designed to capture every single interaction and can have very large storage requirements and may contain fields that are not useful. Consider the volume of raw email events data you may require, and then talk with your Amperity representative before adding raw email events data to Amperity.

.. add-email-engagement-data-source-raw-important-end


.. _add-email-engagement-data-source-rollup:

Summarized email events
--------------------------------------------------

.. add-email-engagement-data-source-rollup-start

Summarized email events data is subset of raw email events data that is scoped to support a specific set of email engagement data.

Email events data should be summarized prior to sending that data to Amperity. In some use cases, you may use a custom domain table to do the summarization prior to applying semantic tags, and then apply the :ref:`email summary <add-email-engagement-semantics-email-summary>` semantic tags.

Examples of summarized email events data include:

* Email opens in the previous N days
* Email clicks in the previous N days
* Most recent click, including date and time
* Filters by opt-in and opt-out customers

.. add-email-engagement-data-source-rollup-end

.. add-email-engagement-data-source-rollup-tip-start

.. tip:: Summarized email events data is recommended for email engagement that does not define a complete customer journey.

.. add-email-engagement-data-source-rollup-tip-end


.. _add-email-engagement-semantic-tags:

About semantic tags
==================================================

.. semantics-email-start

Email engagement semantic tags capture email events data, such as clicks, opens, bounces, opt-ins, opt-outs, and conversions from any email service provider (ESP) data source. Use only one of the following sets of semantic tags:

#. Use :ref:`email events <add-email-engagement-semantics-email-events>` semantic tags when raw email events data is sent directly to Amperity.

#. Use :ref:`email summary <add-email-engagement-semantics-email-summary>` semantic tags when email events data is summarized prior to sending it to Amperity.

.. semantics-email-end

.. semantics-email-caution-start

.. caution:: Apply email events semantic tags **OR** email summary semantic tags to your tenant, **AND NOT** both. The set of semantic tags that you should use depends on how email events are made available to your tenant:

   #. :ref:`add-email-engagement-data-source-raw`
   #. :ref:`add-email-engagement-data-source-rollup`

.. semantics-email-caution-end

.. semantics-email-tip-start

.. tip:: If the email service provider does not provide email addresses alongside sends and clicks data, look for a table from that email service provider that provides a list of contacts that may include email addresses along with a unique ID that can be used to link events data.

.. semantics-email-tip-end


.. _add-email-engagement-semantics-email-events:

Email events
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-events-start
   :end-before: .. term-email-events-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-events-start
   :end-before: .. semantics-email-events-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-events-important-start
   :end-before: .. semantics-email-events-important-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-event-table-about-start
   :end-before: .. semantics-email-event-table-about-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-event-table-start
   :end-before: .. semantics-email-event-table-end


.. _add-email-engagement-semantics-email-summary:

Email summary
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-summary-start
   :end-before: .. term-email-summary-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-summary-start
   :end-before: .. semantics-email-summary-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-summary-warning-start
   :end-before: .. semantics-email-summary-warning-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-summary-table-about-start
   :end-before: .. semantics-email-summary-table-about-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-email-summary-table-start
   :end-before: .. semantics-email-summary-table-end


.. _email-engagement-steps:

Steps to enable
==================================================

.. email-engagement-steps-start

Do one of the following:

#. :ref:`Unified engagement from raw email events data <email-engagement-steps-workflow-unified>`
#. :ref:`Summarized engagement from summarized email events data <email-engagement-steps-workflow-summarized>`

Choose the option that matches the type of email engagment data that your organization will make available to Amperity.

.. important:: :ref:`Email engagement attributes <email-engagement-steps-engagement-attributes>` are available to both options. These attributes use the **Merged Customers** table to associate email events data with the Amperity ID. Add the **Email Engagement Attributes** table to your customer 360 database after the **Unified Email Events** and **Email Engagement Summary** tables are available.

.. email-engagement-steps-end


.. _email-engagement-steps-workflow-unified:

Unified
--------------------------------------------------

.. email-engagement-steps-workflow-unified-start

Unified is based on raw email events that contain data for opens and clicks (required), along with sends, unsubscribes, opt-ins, opt-outs, bounces, and conversions (recommended).

This option starts with semantically tagging raw email events data, and then adding the **Unified Email Events** and **Email Engagement Summary** tables to your customer 360 database.

.. email-engagement-steps-workflow-unified-end

**To add the Unified Email Events table**

.. email-engagement-steps-workflow-unified-table-steps-start

#. From the **Sources** page add a custom domain table. Use a prefix like **Email_Events_** to ensure this table can be easily identified as part of email engagement.
#. Use Spark SQL to build a custom domain table that maps the incoming fields to the following field names: **Sent**, **Open**, **Click**, **Unsubscribe**, **Optin**, **Bounce**, and **Converted**. For example:

   .. code-block:: sql
      :linenos:

      ,CASE 
        WHEN EventType = 'Sent' THEN 'Sent'
        WHEN EventType = 'Opened' THEN 'Open'
        WHEN EventType = 'Clicked' THEN 'Click'
        WHEN EventType = 'Unsubscribed' THEN 'Unsubscribe'
        WHEN EventType = 'Convert' THEN 'Converted'
        WHEN EventType = 'Optin' THEN 'Optin'
        WHEN EventType = 'Bounce' THEN 'Bounce'
      END AS EventType

#. A field for **Brand** must be added if it is not already present in the source data. Most email service providers do not provide brand unless there is multi-brand data. Brands may be identifiable by an account ID or some other indicator.
#. A field for **SendID** must be added if it is not already present in the source data. The send ID is a unique identifier for a given email send action. An open and click data point may share the same send ID.

   Some email service providers do not provide a send ID directly. When a **SendID** is not directly available, build one using a concatenation similar to:

   ::

       ,CONCAT(email, '-', EventType, '-',EventDatetime) AS SendID

#. Validate your SQL, and then click **Next**.
#. Apply the email events semantic tags to the corresponding columns. If an email field is tagged with the customer profile **email** semantic tag it must also be tagged with the **email-event/email** semantic tag.
#. Save the custom domain table.
#. Run Stitch.
#. Run the customer 360 database.
#. Add the **Unified Email Events** table to the customer 360 database as a passthrough table.
#. Activate the customer 360 database, and then run it again.

.. email-engagement-steps-workflow-unified-table-steps-end

**To add the Email Engagement Summary table**

.. email-engagement-steps-workflow-summary-table-steps-start

#. Add the **Email Engagement Summary** table to the customer 360 database as a passthrough table.
#. Activate the customer 360 database, and then run it again.

.. email-engagement-steps-workflow-summary-table-steps-end


.. _email-engagement-steps-workflow-summarized:

Summarized
--------------------------------------------------

.. email-engagement-steps-workflow-summarized-start

Summarized is based on summarized email events that contain specific sets of data for opens, clicks, and other data points required to support email engagement.

This option starts with semantically tagging summarized email events data, and then adding the **Email Engagement Summary** table to your customer 360 database.

.. email-engagement-steps-workflow-summarized-end

**To add the Email Engagement Summary table**

.. email-engagement-steps-workflow-summarized-table-steps-start

#. From the **Sources** page apply **email/summary** semantic tags to data source that contain summarized email events.
#. Run Stitch.
#. Run the customer 360 database.
#. Add the **Email Engagement Summary** table to the customer 360 database as a passthrough table.
#. Activate the customer 360 database, and then run it again.

.. email-engagement-steps-workflow-summarized-table-steps-end


.. _email-engagement-steps-engagement-attributes:

Engagement attributes
--------------------------------------------------

.. email-engagement-steps-engagement-attributes-start

The **Email Engagement Attributes** table is available to both options and may be added as a SQL table after the **Unified Email Events** and **Email Events Summary** tables have been added as passthrough tables.

.. important:: To improve the quality of email engagement data be sure that each email address is associated to only one Amperity ID. 

.. email-engagement-steps-engagement-attributes-end


.. _add-email-engagement-example-custom-domain-table:

Example: Raw email events
==================================================

.. add-email-engagement-example-custom-domain-table-start

The following are examples of using custom domain tables to define how raw email events data should be handled from :ref:`Salesforce Marketing Cloud <add-email-engagement-example-custom-domain-table-salesforce>` and :ref:`Oracle Responsys <add-email-engagement-example-custom-domain-table-responsys>`.

.. add-email-engagement-example-custom-domain-table-end

.. add-email-engagement-example-custom-domain-table-important-start

.. important:: The following examples are not templates. The Spark SQL that is required to enable email engagement will vary across tenants. The examples for **<Brand_Name>** is a placeholder. **SendID** represents the ID for a given email send.

.. add-email-engagement-example-custom-domain-table-important-end


.. _add-email-engagement-example-custom-domain-table-salesforce:

Salesforce Marketing Cloud
--------------------------------------------------

.. add-email-engagement-example-custom-domain-table-salesforce-start

.. code-block:: sql
   :linenos:

   WITH union_data AS (
   SELECT
     _uuid_pk
     ,SendID
     ,EventType
     ,EventDate AS EventDatetime
     ,EmailAddress AS EMAIL
   FROM SFMC_Sent

   UNION

   SELECT
     _uuid_pk
     ,SendID
     ,EventType
     ,EventDate AS EventDatetime
     ,EmailAddress AS EMAIL
   FROM SFMC_Opens

   UNION

   SELECT
     _uuid_pk
     ,SendID
     ,EventType
     ,EventDate AS EventDatetime
     ,EmailAddress AS EMAIL
   FROM SFMC_Clicks

   UNION

   SELECT
     _uuid_pk
     ,SendID
     ,EventType
     ,EventDate AS EventDatetime
     ,EmailAddress AS EMAIL
   FROM SFMC_Unsubs

   UNION

   SELECT
     _uuid_pk
     ,SendID
     ,EventType
     ,EventDate AS EventDatetime
     ,EmailAddress AS EMAIL
   FROM SFMC_Bounces

   UNION

   SELECT
     _uuid_pk
     ,NULL AS SendID
     ,'Optin' AS EventType
     ,DateCreated AS EventDatetime
     ,EmailAddress AS EMAIL
   FROM SFMC_Subscribers

   WHERE Status = 'Active'
   )

   ,email_event_types AS (
     SELECT DISTINCT
     _uuid_pk
     ,EventDatetime
     ,EMAIL
     ,SendID
     ,CASE
       WHEN EventType = 'Sent' THEN 'Sent'
       WHEN EventType = 'Open' THEN 'Open'
       WHEN EventType = 'Click' THEN 'Click'
       WHEN EventType = 'Unsubscribe' THEN 'Unsubscribe'
       WHEN EventType = 'Convert' THEN 'Converted'
       WHEN EventType = 'Optin' THEN 'Optin'
       WHEN EventType = 'Bounce' THEN 'Bounce'
     END AS EventType
     FROM union_data
   )
    
   ,email_events AS (
     SELECT
       _uuid_pk
       ,<Brand Name> AS brand
       ,email
       ,EventType
       ,EventDatetime
       ,SendID
     FROM email_event_types
   )

   SELECT * FROM email_events

.. add-email-engagement-example-custom-domain-table-salesforce-end


.. _add-email-engagement-example-custom-domain-table-responsys:

Oracle Responsys
--------------------------------------------------

.. add-email-engagement-example-custom-domain-table-responsys-start

.. code-block:: sql
   :linenos:

   WITH union_data AS (
     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL
     FROM Responsys_Sent

     UNION

     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL_ADDRESS_ AS EMAIL
     FROM Responsys_Open

     UNION

     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL_ADDRESS_ AS EMAIL
     FROM Responsys_Click

     UNION

     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL
     FROM Responsys_OptOut

     UNION

     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL
     FROM Responsys_Bounce

     UNION

     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL
     FROM Responsys_OptIn

     UNION

     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,RIID
       ,Event_Type_ID
       ,EVENT_CAPTURED_DT AS EventDatetime
       ,EMAIL_ADDRESS_ AS EMAIL
     FROM Responsys_Convert
   )

   ,email_event_types AS (
     SELECT DISTINCT
       ACCOUNT_ID
       ,_uuid_pk
       ,EventDatetime
       ,EMAIL
       ,CASE
         WHEN Event_Type_ID = '1' THEN 'Sent'
         WHEN Event_Type_ID = '4' THEN 'Open'
         WHEN Event_Type_ID = '5' THEN 'Click'
         WHEN Event_Type_ID = '7' THEN 'Unsubscribe'
         WHEN Event_Type_ID = '19' THEN 'Converted'
         WHEN Event_Type_ID = '21' THEN 'Optin'
         WHEN Event_Type_ID = '2' THEN 'Bounce'
       END AS EventType
     FROM union_data
   )

   ,email_events AS (
     SELECT
       ACCOUNT_ID
       ,_uuid_pk
       ,CASE
         WHEN ACCOUNT_ID = <> THEN <>
         WHEN ACCOUNT_ID = <> THEN <>
       END AS brand
       ,email
       ,EventType
       ,EventDatetime
     FROM email_event_types
   )

   SELECT 
     _uuid_pk
     ,brand
     ,email
     ,EventType
     ,EventDatetime
   FROM email_events

.. add-email-engagement-example-custom-domain-table-responsys-end
