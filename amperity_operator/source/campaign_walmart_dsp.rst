.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Walmart DSP
.. |destination-api| replace:: The Trade Desk API
.. |plugin-name| replace:: "The Trade Desk"
.. |credential-type| replace:: "tradedesk"
.. |required-credentials| replace:: "advertiser ID" and "advertiser secret"
.. |what-send| replace:: email addresses or UID2 tokens
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "180"
.. |filter-the-list| replace:: "trade"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Walmart DSP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Walmart DSP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Walmart DSP

==================================================
Configure campaigns for Walmart DSP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-walmart-connect-start
   :end-before: .. term-walmart-connect-end

.. campaign-walmart-dsp-about-start

.. admonition:: United States audiences only

   Your brand should only send custom audiences that contain customers who reside within the United States to |destination-name|.

.. campaign-walmart-dsp-about-end

.. campaign-walmart-dsp-api-note-start

.. note:: This destination uses the `The Trade Desk API <https://api.thetradedesk.com/v3/portal/data/doc/UnifiedIDs>`__ |ext_link| to manage audiences.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. campaign-walmart-dsp-api-note-end


.. _campaign-walmart-dsp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-walmart-dsp-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
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
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Advertiser ID**
          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-id-start
          :end-before: .. credential-the-trade-desk-advertiser-id-end

       **Advertiser secret**
          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-secret-start
          :end-before: .. credential-the-trade-desk-advertiser-secret-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-find-id-and-secret-start
          :end-before: .. credential-the-trade-desk-find-id-and-secret-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Segment name** (Required at orchestration)

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-the-trade-desk-segment-name-start
          :end-before: .. setting-the-trade-desk-segment-name-end

.. campaign-walmart-dsp-get-details-end


.. _campaign-walmart-dsp-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Walmart DSP**

.. campaign-walmart-dsp-credentials-steps-start

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

       **Advertiser ID**
          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-id-start
          :end-before: .. credential-the-trade-desk-advertiser-id-end

       **Advertiser secret**
          |checkmark-required| **Required**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-secret-start
          :end-before: .. credential-the-trade-desk-advertiser-secret-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-find-id-and-secret-start
          :end-before: .. credential-the-trade-desk-find-id-and-secret-end

.. campaign-walmart-dsp-credentials-steps-end


.. _campaign-walmart-dsp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Walmart DSP**

.. campaign-walmart-dsp-add-steps-start

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

       To configure a destination for |destination-name|, do one of the following:

       #. Click the row in which The Trade Desk is located. Destinations are listed alphabetically and you can scroll up and down the list.
       #. Search for The Trade Desk. Start typing |filter-the-list|. The list will filter to show only matching destinations.


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

       **Segment name** (Required at orchestration)

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-the-trade-desk-segment-name-start
          :end-before: .. setting-the-trade-desk-segment-name-end

       **Membership duration**

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-common-membership-duration-start
          :end-before: .. setting-common-membership-duration-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-the-trade-desk-membership-duration-minmax-start
          :end-before: .. setting-the-trade-desk-membership-duration-minmax-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-the-trade-desk-membership-duration-example-start
          :end-before: .. setting-the-trade-desk-membership-duration-example-end


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

.. campaign-walmart-dsp-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
