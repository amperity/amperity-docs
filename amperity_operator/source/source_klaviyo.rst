.. https://docs.amperity.com/operator/


.. |source-name| replace:: Klaviyo
.. |plugin-name| replace:: Klaviyo
.. |feed-name| replace:: Email metrics
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **klaviyo**
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: email engagement metrics
.. |credential-fields| replace:: the name of the credential, a description, the |source-name| API key
.. |box-names| replace:: Email Metrics and List Membership


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Klaviyo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Klaviyo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Klaviyo

==================================================
Pull from Klaviyo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-klaviyo-start
   :end-before: .. term-klaviyo-end

.. source-klaviyo-context-start

Klaviyo can send |what-pull| to Amperity using the `events API <https://developers.klaviyo.com/en/reference/get_events>`__ |ext_link|, which provides email events data for `opens, clicks (for email and SMS), bounces, opt-ins, unsubscribes, custom metrics, and more <https://developers.klaviyo.com/en/reference/events_api_overview#use-cases>`__ |ext_link|.

.. source-klaviyo-context-end

.. source-klaviyo-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-klaviyo-get-details>`
#. :ref:`Add courier <source-klaviyo-add-courier>`
#. :ref:`Run courier <source-klaviyo-run-courier>`
#. :ref:`Review feed and domain table <source-klaviyo-review-data>`
#. :ref:`Add to courier group <source-klaviyo-add-to-courier-group>`

.. source-klaviyo-steps-to-pull-end


.. _source-klaviyo-get-details:

Get details
==================================================

.. source-klaviyo-get-details-start

|source-name| requires the following configuration details:

#. The `API key <https://developers.klaviyo.com/en/docs/retrieve-api-credentials>`__ |ext_link| for |source-name|.

.. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-klaviyo-get-details-end


.. _source-klaviyo-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-klaviyo-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".

   From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.

   When finished click **Continue**.

#. Add the **List name** that will be pulled to Amperity.
#. Under **Select Data**, enable |box-names|.
#. Click **Create**.

   Amperity will create a feed and domain table for each selected data source: :ref:`Klaviyo_Email_Metrics <source-klaviyo-review-data-email>` and :ref:`Klaviyo_List_Membership <source-klaviyo-review-data-list>`.

.. source-klaviyo-add-courier-end


.. _source-klaviyo-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-klaviyo-review-data:

Review feeds and domain tables
==================================================

.. sources-add-courier-review-feed-and-domain-table-start

After running the |source-name| courier feeds are created automatically with a pre-defined list of fields. You may apply semantic tags to these fields and you may make the domain table available to Stitch, depending on your use case.

.. sources-add-courier-review-feed-and-domain-table-end


.. _source-klaviyo-review-data-email:

Klaviyo_Email_Metrics table
--------------------------------------------------

.. source-klaviyo-review-data-email-start

A feed and domain table are created for the **Klaviyo_Email_Metrics** data source with the following fields and semantic tags:

* **emailAddress** (assigned the **email-event/email** semantic tag)
* **eventDateTime** (assigned the **email-event/event-datetime** semantic tag)
* **eventType** (assigned the **email-event/event-type** semantic tag)
* **eventUuid** (assigned the **pk** semantic tag)
* **metricId**
* **sendId** (assigned the **email-event/send-id** semantic tag)

.. source-klaviyo-review-data-email-end


.. _source-klaviyo-review-data-list:

Klaviyo_List_Membership table
----------------------------------------------------

.. source-klaviyo-review-data-list-start

A feed and domain table are created for the **Klaviyo_List_Membership** data source with the following fields and semantic tags:

* **email**
* **id** (assigned the **pk** semantic tag)
* **list_id**
* **phone**

.. source-klaviyo-review-data-list-end


.. _source-klaviyo-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
