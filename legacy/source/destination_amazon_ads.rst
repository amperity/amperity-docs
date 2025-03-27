.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Amazon Ads
.. |destination-api| replace:: Amazon Ads API
.. |plugin-name| replace:: Amazon Ads
.. |what-send| replace:: audience lists
.. |filter-the-list| replace:: "ama"
.. |email-plus-send| replace:: additional attributes
.. |credential-type| replace:: amazon-ads
.. |credential-details| replace:: the Amazon Ads API refresh token
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: advertiser ID and marketplace settings
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: send audience lists
.. |channel-linkx| replace:: send campaigns


==================================================
Send data to Amazon Ads
==================================================

.. note:: This topic contains information for configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination for sending query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/datagrid/destination_amazon_ads.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-ads-start
   :end-before: .. term-amazon-ads-end

.. warning:: Please ask your Amperity representative for assistance with setting up |destination-name| as a destination within your tenant.

.. destination-amazon-ads-start

Amperity can manage audiences within |destination-name| for use with a variety of advertising and paid media channels, such as: 

* Sponsored ads for products and brands that appear within search results on the Amazon website and within the mobile app.
* Sponsored display ads that reach audiences as they browse, research, or buy products on Amazon, on Twitch, or by using Amazon DSP, a demand-side platform that allows you to programmatically buy ads to reach new and existing audiences on and off Amazon.
* Video ads for streaming TV and online video. Streaming TV ads can appear on Twitch, live sports events, top TV and network broadcaster apps, and curated news on Fire TV. Online video ads reach audiences on Amazon-owned sites, including IMDb.com and Twitch and may appear on third-party sites through Amazon Publisher Direct.
* Audio ads that are heard during breaks in premium audio content, including first-party Amazon Music ad-supported tiers, connected TV environments, Twitch News, Alexa-enabled devices, and third-party sites through Amazon Publisher Direct.
* Access to a secure, privacy-safe, and cloud-based clean room solution when the instance name for your brand's |ext_amazon_marketing_cloud| account is configured.

.. destination-amazon-ads-end

.. destination-amazon-ads-api-note-start

.. note:: This destination uses the |ext_amazon_ads_api| to manage audiences. If the audience does not exist, Amperity will create it. If the audience exists, Amperity will update the list of members to match the list that is sent.

.. destination-amazon-ads-api-note-end

.. destination-amazon-ads-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-amazon-ads-get-details>`
#. :ref:`Add destination <destination-amazon-ads-add-destination>`
#. :ref:`Add data template <destination-amazon-ads-add-data-template>`

.. destination-amazon-ads-steps-to-send-end


.. _destination-amazon-ads-get-details:

Get details
==================================================

.. destination-amazon-ads-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Configuration details for |destination-name|.

       #. An |destination-name| demand-side platform (DSP) advertiser.
       #. Optional. Your brand's |ext_amazon_marketing_cloud_instance|.

          .. important:: If an instance for Amazon Marketing Cloud **is not** configured, the connector will skip adding audience members to Amazon Marketing Cloud.

             If an Amazon Marketing Cloud instance is configured, the connector will attempt to use an existing connection for Amazon Marketing Cloud *or* will create a connection between the chosen demand-side platform advertiser and the instance for Amazon Marketing Cloud.

       .. note:: The |ext_amazon_ads_refresh_token| is provided :ref:`after the OAuth process is completed <destination-amazon-ads-configure-oauth>`.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - Details for the audiences in |destination-name| that will be managed by Amperity.

       #. An audience name and description. If there is not an audience that exactly matches the one sent from Amperity to |destination-name|, Amperity will create a new audience.

       #. The amount of time (in seconds) an audience member will belong to this audience, after which they are removed. Maximum value: "34,300,800" (which is the equivalent of 9528 hours or 397 days).

          .. tip:: Set this value to "0" to remove all audience members.

       #. Leave the the external ID setting empty.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - Use a query to return an audience that contains any of the following attributes:

       .. code-block:: sql

          SELECT
            ,amperity_id
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

       .. important:: The following columns are required:

          * **amperity_id**
          * If first and last names are returned, the column names must be **firstname** and **lastname**
          * **country** is required by the :ref:`Digital Markets Act <destination-amazon-ads-workflow-actions-missing-required-field>`.

       A phone number must be in |ext_e164_format| format. Amperity applies hashing to the PII by default.

       All personally identifiable information (PII)---email, phone, address, and so on---is sent to |destination-name| as SHA-256 hashed data.

.. destination-amazon-ads-get-details-end


.. _destination-amazon-ads-about-amc:

About Amazon Marketing Cloud (AMC)
==================================================

.. destination-amazon-ads-about-amc-start

Amazon Marketing Cloud (AMC) uses pseudonymized inputs from Amazon Ads campaign events, such as ad impressions, ad clicks, and ad-attributed conversions that span across media including streaming TV, audio, video, display, and sponsored ads. These inputs are uploaded into a dedicated instance of AMC---a "clean room"---after which that data stays within that instance and cannot be accessed or exported by Amazon.

Audience analysis takes place within Amazon Marketing Cloud, including across dimensions like audiences, device, time, or campaigns. Results are aggregated and may be exported as anonymous reports.

Amperity can send data to your brand's |ext_amazon_marketing_cloud_instance| when the instance name is :ref:`configured alongside the demand-side platform (DSP) advertiser <destination-amazon-ads-get-details>` to which this destination will send data.

.. destination-amazon-ads-about-amc-end

.. _destination-european-union-user-consent:

European Union user consent
==================================================
.. destination-european-union-user-consent-start

.. important:: `Amazon Ads requires <https://advertising.amazon.com/resources/ad-policy/consent-signal-requirements>`__ |ext_link| that if personal information is transmitted to them to use any Amazon advertising services you must use the IAB European Transparency & Consent Framework or the Amazon consent signal. Not including these signals may result in lower match rates. 

.. destination-european-union-user-consent-end


.. _destination-amazon-ads-configure-oauth:

Configure OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-intro-start
   :end-before: .. destinations-oauth-intro-end

**To configure OAuth**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-1-start
          :end-before: .. destinations-oauth-configure-step-1-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-2-start
          :end-before: .. destinations-oauth-configure-step-2-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-3-start
          :end-before: .. destinations-oauth-configure-step-3-end


.. _destination-amazon-ads-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-amazon-ads-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-amazon-ads-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select-amazon-ads.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-amazon-ads.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       To create a new credential for |destination-name|, generate an authorization link, and then use that link to log into your |destination-name| account. After you have completed that process, you will be provided a refresh token. Add the value for the refresh token to the **Refresh Token** setting in Amperity.

       .. image:: ../../images/mockup-destinations-tab-credentials-02-select-amazon-ads.png
          :width: 500 px
          :alt: Set the following credentials for Amazon Ads.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       Use the **DSP advertiser** dropdown to select a demand-side platform that is associated with your |destination-name| account.

       Optional. Use the **AMC instance** dropdown to select an Amazon Marketing Cloud instance.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-amazon-ads-add-destination-steps-end


.. _destination-amazon-ads-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add a data template**

.. destination-amazon-ads-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details-amazon-ads.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-amazon-ads.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. important:: The audience name must exactly match an audience in |destination-name| to update membership. If there is not an audience that exactly matches the one sent from Amperity to |destination-name|, Amperity will a new audience.

          Leave the **External ID** setting empty.

          Set the membership duration in seconds. For example, an audience that lasts 180 days should have a value of "15,552,000" for the **Membership duration** setting.

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

       After you have saved the data template, and depending on how you configured it, business users can |sendto-link| to |destination-name|.

.. destination-amazon-ads-add-data-template-steps-end


.. _destination-amazon-ads-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-amazon-ads-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
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
          :align: left
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
          :align: left
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
          :align: left
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

.. destination-amazon-ads-workflow-actions-end


.. _destination-amazon-ads-workflow-actions-invalid-advertiser-id:

Invalid advertiser account ID
--------------------------------------------------

.. destination-amazon-ads-workflow-actions-invalid-advertiser-id-start

|destination-name| requires a valid advertiser account ID to be associated with an advertiser. When an advertiser is not associated with an advertiser account ID --- such as when an advertiser account ID has been deleted --- Amperity will be unable to manage audiences within |destination-name| and a workflow action will be shown.

.. destination-amazon-ads-workflow-actions-invalid-advertiser-id-end

.. destination-amazon-ads-workflow-actions-invalid-advertiser-id-steps-start

To resolve this error, verify that the advertiser account ID exists in |destination-name|, and then update Amperity for the correct advertiser ID (if necessary).

#. Open the |destination-name| management console and verify your advertiser account ID.
#. Open the **Destinations** page in Amperity, and then open the destination for |destination-name| that is associated with this workflow.
#. Update the destination for the correct advertiser account ID.
#. Return to the workflow action, and then click **Resolve** to retry.

.. destination-amazon-ads-workflow-actions-invalid-advertiser-id-steps-start


.. _destination-amazon-ads-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-generic-invalid-credentials-start
   :end-before: .. workflow-actions-generic-invalid-credentials-end


.. _destination-amazon-ads-workflow-actions-missing-required-field:

Missing required field
--------------------------------------------------

.. destination-amazon-ads-workflow-actions-missing-required-field-start

|destination-name| requires the **country** field to be included in query results. This helps |destination-name| identify if user data was collected within a country that is regulated by the |ext_digital_markets_act|, a European Union regulation that seeks to make the digital economy fairer and more equitable for all participants.

.. destination-amazon-ads-workflow-actions-missing-required-field-end

.. destination-amazon-ads-workflow-actions-missing-required-field-steps-start

To resolve this error, verify that **country** is included in the query results.

#. Open the **Queries** page, and then open the query used with this workflow.
#. Verify that "country" is included in the query results. Update the query if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-amazon-ads-workflow-actions-missing-required-field-steps-start
