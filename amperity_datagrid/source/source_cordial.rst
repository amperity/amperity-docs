.. https://docs.amperity.com/datagrid/


.. |source-name| replace:: Cordial
.. |plugin-name| replace:: Cordial
.. |feed-name| replace:: Email
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **cordial**
.. |what-pull| replace:: contact and activity data
.. |credential-fields| replace:: the name of the credential, a description, the |source-name| API key and secret
.. |box-names| replace:: Contacts or Contacts Activities


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Cordial.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Cordial.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Cordial

==================================================
Pull from Cordial
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-cordial-start
   :end-before: .. term-cordial-end

.. source-cordial-about-start

|source-name| can send contact and activity data to Amperity for use with a variety of email engagement workflows.

.. source-cordial-about-end

.. source-cordial-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-cordial-get-details>`
#. :ref:`Add courier <source-cordial-add-courier>`
#. :ref:`Run courier <source-cordial-run-courier>`
#. :ref:`Review feed and domain table <source-cordial-review-data>`
#. :ref:`Add to courier group <source-cordial-add-to-courier-group>`

.. source-cordial-steps-to-pull-end


.. _source-cordial-get-details:

Get details
==================================================

.. source-cordial-get-details-start

The |source-name| data source requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The API key and secret for |source-name|.

       .. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - Optional. The |source-name| audience key.

       Use an audience key to configure Amperity to pull contacts from a specific audience from |source-name|. This value should be the |ext_cordial_audience| in |source-name|.

       .. note:: When this field is empty, Amperity will pull all contacts.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - Optional. A comma-separated list of activity types. For example:

       ::

          crdl_subscribeStatusChange,
          open,
          crdl-pdm-actn-success,
          crdl_sms_delivered

       Activity types (also known as "event types" within |source-name|) contain |ext_cordial_events_overview|. 

       |source-name| provides the following groupings of activity types, each with a unique subset of activity types:

       * All channels
       * Email
       * Push
       * Podium (the orchestration engine for |source-name|)
       * SMS
       * REST API
       * Other events

       Review |ext_cordial_system_events| to determine the right combination of activity types for your brand to pull to Amperity.

       .. note:: When this field is empty, Amperity will pull all activity types.

.. source-cordial-get-details-end


.. _source-cordial-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-cordial-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.
#. Enter the name of the courier. For example: "|source-name|".
#. From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.

#. Under **Settings**, configure one or both of the following:

   Use **Audience key** to configure Amperity to pull contacts from a specific audience from |source-name|. This value should be the |ext_cordial_audience| in |source-name|.

   .. note:: When this field is empty, Amperity will pull all contacts.

   Use **List of activity types** to enter a comma-separated list of activity types. Review |ext_cordial_system_events| to determine the right combination of activity types for your brand to pull to Amperity. For example:

   ::

      crdl_subscribeStatusChange, open, crdl-pdm-actn-success, crdl_sms_delivered

   .. note:: When this field is empty, Amperity will pull all activity types.

#. Under **Select Data**, enable |box-names|.
#. Click **Create**.

.. source-cordial-add-courier-end


.. _source-cordial-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-cordial-review-data:

Review feed and domain table
==================================================

.. source-cordial-review-feed-and-domain-table-start

After running the |source-name| courier a feed is created automatically with a pre-defined list of fields. You may apply semantic tags to these fields and you may make the domain table available to Stitch, depending on your use cases. A domain table named |domain-table-name| will be added.

.. source-cordial-review-feed-and-domain-table-end

.. _source-cordial-review-data-email:

Email contacts
--------------------------------------------------

.. source-cordial-contacts-start

The feed and domain table for email contacts will match the following fields:

The contacts ingress type will only capture all data, regardless of if a date restriction is placed in the UI.

* **_id** (assigned the **ck** semantic tag)
* **emailAddress** (assigned the **email** semantic tag)
* **cID**
* **createDate**
* **ID**
* **subscribedAt**
* **subscribeStatus**

.. source-cordial-contacts-start


.. _source-cordial-contact-activities:

Contact activities
--------------------------------------------------

.. source-cordial-contact-activities-start

Contact activities capture all activities or events - opens, clicks, and custom actions created by the user. Contact activities are linked with a customer via their primary and secondary identifier. The secondary identifier can have multiple values i.e. email address, phone number, customer ID, etc. For this reason, contact activities can encompass email activity, web engagement, etc.

The feed and domain table for contact activities will match the following fields:

* **_id** (assigned the **ck** semantic tag)
* **browser**
* **cID**
* **jobID**
* **device**
* **fromSubscribeStatus**
* **platform**
* **activityDate**
* **toSubscribeStatus**
* **activityType**
* **fromSubscribeStatus**

.. source-cordial-contact-activities-end


.. _source-cordial-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
