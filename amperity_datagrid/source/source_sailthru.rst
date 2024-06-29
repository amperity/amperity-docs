.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |source-name| replace:: Sailthru
.. |plugin-name| replace:: Sailthru
.. |feed-name| replace:: Users
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **sailthru**
.. |what-pull| replace:: user profiles
.. |credential-fields| replace:: the name of the credential, a description, the |source-name| API key and secret
.. |settings-details| replace:: the list name that is configured in |source-name|
.. |box-names| replace:: Users



.. meta::
    :description lang=en:
        Configure Amperity to pull data from Sailthru.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Sailthru.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Sailthru

==================================================
Pull from Sailthru
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sailthru-start
   :end-before: .. term-sailthru-end

.. source-sailthru-about-start

Sailthru can send |ext_sailthru_email_event_stream| to Amperity using the |ext_sailthru_api_get_user_profile|. The user profile endpoint provides |what-pull| to Amperity. User profile events include data for clicks, email addresses, opens, optouts, signups, lifetime purchases and purchase price, devices, and views.

.. source-sailthru-about-end

.. source-sailthru-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-sailthru-get-details>`
#. :ref:`Add courier <source-sailthru-add-courier>`
#. :ref:`Run courier <source-sailthru-run-courier>`
#. :ref:`Review feed and domain table <source-sailthru-review-data>`
#. :ref:`Add to courier group <source-sailthru-add-to-courier-group>`

.. source-sailthru-steps-to-pull-end


.. _source-sailthru-get-details:

Get details
==================================================

.. source-sailthru-get-details-start

|source-name| requires the following configuration details:

#. The |ext_sailthru_api_key_and_secret| for |source-name|.
#. The list name.

.. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-sailthru-get-details-end


.. _source-sailthru-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-sailthru-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.
   
#. Under **Settings** enter the |settings-details|.
#. Under **Select Data**, enable |box-names|.
#. Click **Create**.

.. source-sailthru-add-courier-end


.. _source-sailthru-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-sailthru-review-data:

Review feed and domain table
==================================================

.. sources-add-courier-review-feed-and-domain-table-start

After running the |source-name| courier a feed is created automatically with a pre-defined list of fields. You may apply semantic tags to these fields and you may make the domain table available to Stitch, depending on your use cases. A domain table named |domain-table-name| will be added.

.. sources-add-courier-review-feed-and-domain-table-end

.. source-sailthru-review-data-start

The feed and domain table will match the fields defined in the |ext_sailthru_api_get_user_profile|:

* **click_time**
* **create_time**
* **device**
* **email** (assigned the **email** semantic tag; this field is also the unique identifier)
* **engagement**
* **lifetime_click**
* **lifetime_message**
* **lifetime_purchased**
* **lifetime_purchased_price**
* **lifetime_pv**
* **login_time**
* **open_time**
* **optout_email**
* **signup_time**
* **view_time**

.. source-sailthru-review-data-end


.. _source-sailthru-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
