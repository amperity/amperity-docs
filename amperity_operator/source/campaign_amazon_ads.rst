.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Amazon Ads
.. |plugin-name| replace:: "Amazon Ads"
.. |credential-type| replace:: "amazon-ads"
.. |required-credentials| replace:: "the Amazon Ads API refresh token"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in seconds)
.. |duration-value| replace:: "0" - "34,300,800"
.. |filter-the-list| replace:: "amaz"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Amazon Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Amazon Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Amazon Ads

==================================================
Configure campaigns for Amazon Ads
==================================================

.. campaign-amazon-ads-start

Amazon Ads is an online advertising platform that supports a variety of advertising options, including sponsored, search, display, video, and audio.

Amperity can manage audiences within |destination-name| for use with a variety of advertising and paid media channels, such as: 

* Sponsored ads for products and brands that appear within search results on the Amazon website and within the mobile app.
* Sponsored display ads that reach audiences as they browse, research, or buy products on Amazon, on Twitch, or by using Amazon DSP, a demand-side platform that allows you to programmatically buy ads to reach new and existing audiences on and off Amazon.
* Video ads for streaming TV and online video. Streaming TV ads can appear on Twitch, live sports events, top TV and network broadcaster apps, and curated news on Fire TV. Online video ads reach audiences on Amazon-owned sites, including IMDb.com and Twitch and may appear on third-party sites through Amazon Publisher Direct.
* Audio ads that are heard during breaks in premium audio content, including first-party Amazon Music ad-supported tiers, connected TV environments, Twitch News, Alexa-enabled devices, and third-party sites through Amazon Publisher Direct.
* Access to a secure, privacy-safe, and cloud-based clean room solution when the instance name for your brand's `Amazon Marketing Cloud (AMC) <https://advertising.amazon.com/solutions/products/amazon-marketing-cloud>`__ |ext_link| account is configured.

.. campaign-amazon-ads-end

.. campaign-amazon-ads-ask-start

.. warning:: Please ask your Amperity representative for assistance with setting up |destination-name| as a destination within your tenant.

.. campaign-amazon-ads-ask-end

.. campaign-amazon-ads-api-note-start

.. note:: This destination uses the `Amazon Ads API <https://advertising.amazon.com/API/docs/en-us/info/api-overview>`__ |ext_link| to manage audiences. If the audience does not exist, Amperity creates it. If the audience exists, Amperity updates the list of members to match the list that is sent.

.. campaign-amazon-ads-api-note-end


.. _campaign-amazon-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-amazon-ads-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. note:: The `refresh token <https://advertising.amazon.com/API/docs/en-us/getting-started/retrieve-access-token>`__ |ext_link| is provided :ref:`after the OAuth process is completed <destination-amazon-ads-credentials>`.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-audience-description-start
             :end-before: .. setting-amazon-ads-audience-description-end

       **Audience description** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-audience-description-start
             :end-before: .. setting-amazon-ads-audience-description-end

       **DSP advertiser**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-dsp-advertiser-start
             :end-before: .. setting-amazon-ads-dsp-advertiser-end

          Use the **DSP advertiser** dropdown to select a demand-side platform that is associated with your |destination-name| account.

       **AMC instance**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-amc-instance-start
             :end-before: .. setting-amazon-ads-amc-instance-end

          Optional. Use the **AMC instance** dropdown to select an Amazon Marketing Cloud instance.

          .. important:: If an instance for Amazon Marketing Cloud **is not** configured, Amperity will skip adding audience members to Amazon Marketing Cloud.

             If an Amazon Marketing Cloud instance is configured, Amperity will attempt to use an existing connection for Amazon Marketing Cloud *or* creates a connection between the chosen demand-side platform advertiser and the instance for Amazon Marketing Cloud.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: center
          :class: no-scaled-link
     - When you have an **extern_id** that is available and appropriately configured for your downstream destination, use a query to return an audience that contains any of the following attributes:

       .. code-block:: sql
          :linenos:

           SELECT
               ,extern_id
               ,email
               ,phone
               ,address
               ,city
               ,state
               ,postal
               ,country
               ,given_name AS 'firstname'
               ,surname AS 'lastname'
           FROM Customer_360

       You may also use an **amperity_id** but it should be labeled as an **extern_id**.

       .. code-block:: sql
          :linenos:

           SELECT
               ,amperity_id AS extern_id
               ,email
               ,phone
               ,address
               ,city
               ,state
               ,postal
               ,country
               ,given_name AS 'firstname'
               ,surname AS 'lastname'
           FROM Customer_360

       .. important::

           The following columns are required:
    
           * **extern_id** (recommended) or **amperity_id** (supported for existing integrations)
           * If first and last names are returned, the column names must be **firstname** and **lastname**
           * **country** is required by the Digital Markets Act

       .. note::

           If both **extern_id** and **amperity_id** are provided, only **extern_id** is used.

       A phone number must be in `E.164 format <https://en.wikipedia.org/wiki/E.164>`__ |ext_link|.

       All personally identifiable information (PII)—email, phone, address, and so on—is sent to |destination-name| as SHA-256 hashed data.

.. campaign-amazon-ads-get-details-table-end


.. _campaign-amazon-ads-about-amc:

About Amazon Marketing Cloud (AMC)
==================================================

.. campaign-amazon-ads-about-amc-start

Amazon Marketing Cloud (AMC) uses pseudonymized inputs from Amazon Ads campaign events, such as ad impressions, ad clicks, and ad-attributed conversions that span across media including streaming TV, audio, video, display, and sponsored ads. These inputs are uploaded into a dedicated instance of AMC--a "clean room"--after which that data stays within that instance and cannot be accessed or exported by Amazon.

Audience analysis takes place within Amazon Marketing Cloud, including across dimensions like audiences, device, time, or campaigns. Results are aggregated and may be exported as anonymous reports.

Amperity can send data to your brand's `instance of Amazon Marketing Cloud (AMC) <https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works>`__ |ext_link| when the instance name is :ref:`configured alongside the demand-side platform (DSP) advertiser <destination-amazon-ads-get-details>` to which this destination sends data.

.. campaign-amazon-ads-about-amc-end


.. _campaign-amazon-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Amazon Ads**

.. campaign-amazon-ads-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. campaign-amazon-ads-credentials-steps-end

.. _campaign-amazon-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-oauth-reauthorize-start
   :end-before: .. credential-oauth-reauthorize-end


.. _campaign-amazon-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Amazon Ads**

.. campaign-amazon-ads-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-audience-description-start
             :end-before: .. setting-amazon-ads-audience-description-end

       **Audience description** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-audience-description-start
             :end-before: .. setting-amazon-ads-audience-description-end

       **DSP advertiser**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-dsp-advertiser-start
             :end-before: .. setting-amazon-ads-dsp-advertiser-end

       **AMC instance**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amazon-ads-amc-instance-start
             :end-before: .. setting-amazon-ads-amc-instance-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end

          (A membership duration of "34,300,800 is equivalent to "9528" hours or "397" days.)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-frequency-start
             :end-before: .. setting-common-membership-duration-frequency-end

       **Campaign file settings**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-amazon-ads-add-steps-end


.. _campaign-amazon-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. campaign-amazon-ads-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
          :width: 500 px
          :alt: Review a notifications error.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-b-start
          :end-before: .. workflow-actions-common-table-section-one-b-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The Workflow page, showing a workflow with errors.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. image:: ../../images/workflow-actions-amazon-ads-group-name.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-amazon-ads-workflow-actions-invalid-advertiser-id`
       * :ref:`destination-amazon-ads-workflow-actions-invalid-credentials`
       * :ref:`destination-amazon-ads-workflow-actions-missing-required-field`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. image:: ../../images/workflow-actions-amazon-ads-group-name-steps.png
          :width: 300 px
          :alt: Choose a workflow action from the list of actions.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. campaign-amazon-ads-workflow-actions-end


.. _campaign-amazon-ads-workflow-actions-invalid-advertiser-id:

Invalid advertiser account ID
--------------------------------------------------

.. campaign-amazon-ads-workflow-actions-invalid-advertiser-id-start

|destination-name| requires a valid advertiser account ID to be associated with an advertiser. When an advertiser is not associated with an advertiser account ID --- such as when an advertiser account ID has been deleted --- Amperity will be unable to manage audiences within |destination-name| and a workflow action is shown.

.. campaign-amazon-ads-workflow-actions-invalid-advertiser-id-end

.. campaign-amazon-ads-workflow-actions-invalid-advertiser-id-steps-start

To resolve this error, verify that the advertiser account ID exists in |destination-name|, and then update Amperity for the correct advertiser ID if necessary.

#. Open the |destination-name| management console and verify your advertiser account ID.
#. Open the **Destinations** page in Amperity, and then open the destination for |destination-name| that is associated with this workflow.
#. Update the destination for the correct advertiser account ID.
#. Return to the workflow action, and then click **Resolve** to retry.

.. campaign-amazon-ads-workflow-actions-invalid-advertiser-id-steps-start


.. _campaign-amazon-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _campaign-amazon-ads-workflow-actions-missing-required-field:

Missing required field
--------------------------------------------------

.. campaign-amazon-ads-workflow-actions-missing-required-field-start

|destination-name| requires the **country** field to be included in query results. This helps |destination-name| identify if user data was collected within a country that is regulated by the `Digital Markets Act <https://en.wikipedia.org/wiki/Digital_Markets_Act>`__ |ext_link|, a European Union regulation that seeks to make the digital economy fairer and more equitable for all participants.

.. campaign-amazon-ads-workflow-actions-missing-required-field-end

.. campaign-amazon-ads-workflow-actions-missing-required-field-steps-start

To resolve this error, verify that **country** is included in the query results.

#. Open the **Queries** page, and then open the query used with this workflow.
#. Verify that "country" is included in the query results. Update the query if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. campaign-amazon-ads-workflow-actions-missing-required-field-steps-start
