.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Walmart DSP
.. |destination-api| replace:: The Trade Desk API
.. |plugin-name| replace:: The Trade Desk
.. |what-send| replace:: audience lists
.. |filter-the-list| replace:: "trad"
.. |email-plus-send| replace:: additional attributes
.. |credential-type| replace:: **tradedesk**
.. |credential-details| replace:: the The Trade Desk API key and API secret
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: segment name and membership duration settings
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: send queries
.. |channel-link| replace:: send campaigns
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Walmart DSP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Walmart DSP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Walmart DSP

==================================================
Send audiences to Walmart DSP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-walmart-connect-start
   :end-before: .. term-walmart-connect-end

.. destination-walmart-dsp-about-start

.. admonition:: United States audiences only

   Your brand should only send custom audiences that contain customers who reside within the United States to |destination-name|.

.. destination-walmart-dsp-about-end

.. destination-walmart-dsp-api-note-start

.. note:: This destination uses the `The Trade Desk API <https://api.thetradedesk.com/v3/portal/data/doc/UnifiedIDs>`__ |ext_link| to manage audiences.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-walmart-dsp-api-note-end

.. destination-walmart-dsp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-walmart-dsp-get-details>`
#. :ref:`Add destination <destination-walmart-dsp-add-destination>`
#. :ref:`Add data template <destination-walmart-dsp-add-data-template>`

.. destination-walmart-dsp-steps-to-send-end


.. _destination-walmart-dsp-get-details:

Get details
==================================================

.. destination-walmart-dsp-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - **UID 2.0 agreement**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-unified-id-20-start
          :end-before: .. term-unified-id-20-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-the-trade-desk-uid2-agreement-start
          :end-before: .. setting-the-trade-desk-uid2-agreement-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Configuration details for |destination-name|.

       * The advertiser ID
       * The advertiser secret

       .. tip:: You can find the advertiser ID and secret key from the management console within |destination-name|. Open **Preferences**, and then **First Party Data Credentials**. The advertiser ID and secret key are shown there.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - The name of a segment in |destination-name|.

       Membership duration defines the length of time (in days) at which individual audience members will belong to the segment in |destination-name|. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the default duration. The maximum value is "180".

       .. tip:: Set this value to "0" to remove all audience members.

       .. caution:: The membership duration is measured in days. Adjust the membership duration value to be greater than (or equal to) than the frequency at which your brand will send campaigns or orchestrations from Amperity.

          For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

          If a campaign is sent every 30 days, but the membership duration is 14, then the audience size for the last 16 days of the duration window will be 0.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - You may use a query to build the list of email addresses or you may select the **email** attribute from the attribute editor in your campaigns.

       .. important:: The **email** column is required and may not be aliased.

       **Example query**

       .. include:: ../../shared/sendtos.rst
          :start-after: .. sendtos-build-query-email-only-start
          :end-before: .. sendtos-build-query-email-only-end

       .. include:: ../../amperity_amp360/source/destination_the_trade_desk.rst
          :start-after: .. sendto-the-trade-desk-build-query-start
          :end-before: .. sendto-the-trade-desk-build-query-end


.. destination-walmart-dsp-get-details-end


.. _destination-walmart-dsp-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-walmart-dsp-add-destination-steps-start

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

       .. image:: ../../images/mockup-destinations-tab-add-01-select-the-trade-desk.png
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

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-the-trade-desk.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-02-select-the-trade-desk.png
          :width: 500 px
          :alt: Set the following credentials for The Trade Desk.
          :align: left
          :class: no-scaled-link

       Add the advertiser ID and secret key for your account with |destination-name|.

       .. tip:: You can find the advertiser ID and secret key from the management console within |destination-name|. Open **Preferences**, and then **First Party Data Credentials**. The advertiser ID and secret key are shown there.

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

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-the-trade-desk.png
          :width: 500 px
          :alt: Settings for The Trade Desk.
          :align: left
          :class: no-scaled-link

       Optional. You may define a segment name and membership duration (in days) for individual audience members. These may be left blank, and then specified with a data template.

       .. tip:: The membership duration is measured in days. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the recommended duration, but this value should be greater than (or equal to) the frequency at which your brand sends campaigns or orchestrations to |destination-name|.

          For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

          Set this value to "0" to clear out the audience in the segment.

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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-allow-start
          :end-before: .. destinations-business-users-allow-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-walmart-dsp-add-destination-steps-end


.. _destination-walmart-dsp-add-data-template:

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

.. destination-walmart-dsp-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-01-details-the-trade-desk.png
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

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access-no-campaigns.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings-the-trade-desk.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. tip:: The membership duration is measured in days. The minimum value should be "7" because |destination-name| uses the previous seven days when building audiences. "14" is the recommended duration, but this value should be greater than (or equal to) the frequency at which your brand sends campaigns or orchestrations to |destination-name|.

          For example, if your brand sends a campaign to |destination-name| every 30 days, then the membership duration should be set to "30". If your brand sends a campaign every 14 days, then the membership duration should be set to "14".

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

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-start
          :end-before: .. destinations-data-template-save-after-end

.. destination-walmart-dsp-add-data-template-steps-end
