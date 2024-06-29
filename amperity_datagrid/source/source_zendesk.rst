.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |source-name| replace:: Zendesk
.. |plugin-name| replace:: Zendesk
.. |feed-name| replace:: Users
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **zendesk-api-token**
.. |what-pull| replace:: customer support histories
.. |credential-fields| replace:: the name of the credential, a description, the email address used to access |source-name|, and the API token for |source-name|
.. |settings-details| replace:: the subdomain for the |source-name| account. For example: "acme" is the subdomain in "acme.zendesk.com"
.. |box-names| replace:: Users


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Zendesk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Zendesk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Zendesk

==================================================
Pull from Zendesk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-zendesk-start
   :end-before: .. term-zendesk-end

.. source-zendesk-about-start

Use the |ext_zendesk_rest_api_tickets_users| to pull |what-pull| to Amperity, and then associate them to your customer profiles and transaction histories.

.. source-zendesk-about-end

.. source-zendesk-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-zendesk-get-details>`
#. :ref:`Add courier with empty load operation <source-zendesk-add-courier>`
#. :ref:`Run courier manually <source-zendesk-run-courier>`
#. :ref:`Review feed and domain table <source-zendesk-review-data>`
#. :ref:`Add to courier group <source-zendesk-add-to-courier-group>`

.. source-zendesk-steps-to-pull-end


.. _source-zendesk-get-details:

Get details
==================================================

.. source-zendesk-get-details-start

|source-name| requires the following configuration details:

#. The email address the customer uses to access |source-name|.
#. The customer's |source-name| API token.
#. The subdomain for the customer's |source-name| account, e.g. "acme" (in ``acme.zendesk.com``).

.. source-zendesk-get-details-end


.. _source-zendesk-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. sources-add-courier-api-automatic-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.
   
#. Under **Settings** enter the |settings-details|.
#. Under **Select Data**, enable |box-names|.
#. Click **Create**.

.. sources-add-courier-api-automatic-end


.. _source-zendesk-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-zendesk-review-data:

Review feed and domain table
==================================================

.. sources-add-courier-review-feed-and-domain-table-start

After running the |source-name| courier a feed is created automatically with a pre-defined list of fields. You may apply semantic tags to these fields and you may make the domain table available to Stitch, depending on your use cases. A domain table named |domain-table-name| will be added.

.. sources-add-courier-review-feed-and-domain-table-end

.. source-zendesk-review-data-start

The feed and domain table will match the fields defined in the |ext_zendesk_rest_api_tickets_users|:

* **active**
* **alias**
* **chat_only**
* **created_at**
* **custom_role_id**
* **default_group_id**
* **details**
* **email** (assigned the **email** semantic tag)
* **external_id**
* **iana_time_zone**
* **id** (assigned the **pk** semantic tag)
* **last_login_at**
* **locale**
* **locale_id**
* **moderator**
* **name** (assigned the **full-name** semantic tag)
* **notes**
* **only_private_comments**
* **organization_id**
* **phone** (assigned the **phone** semantic tag)
* **photo**
* **remote_photo_url**
* **report_csv**
* **restricted_agent**
* **role**
* **role_type**
* **shared**
* **shared_agent**
* **shared_phone_number**
* **signature**
* **suspended**
* **tags**
* **ticket_restriction**
* **time_zone**
* **two_factor_auth_enabled**
* **updated_at**
* **url**
* **user_fields**
* **verified**

.. source-zendesk-review-data-end


.. _source-zendesk-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
