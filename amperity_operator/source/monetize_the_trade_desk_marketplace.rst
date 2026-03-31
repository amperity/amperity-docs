.. https://docs.amperity.com/operator/


.. |destination-name| replace:: The Trade Desk Data Marketplace
.. |plugin-name| replace:: "The Trade Desk Data Marketplace"
.. |credential-type| replace:: "tradedesk-audience-monetization"
.. |required-credentials| replace:: "advertiser ID", "advertiser secret", "provider ID", and "platform API token"
.. |what-send| replace:: UID2 tokens
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "180"
.. |filter-the-list| replace:: "trade"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours

.. meta::
    :description lang=en:
        Configure Amperity to send audiences to The Trade Desk Data Marketplace.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to The Trade Desk Data Marketplace.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to The Trade Desk Data Marketplace

=================================================================
Send audiences to The Trade Desk Data Marketplace
=================================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-marketplace-start
   :end-before: .. term-thetradedesk-marketplace-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-audience-monetization-start
   :end-before: .. term-audience-monetization-end

.. destination-the-trade-desk-marketplace-about-start

Use this destination to monetize your brand's UID 2.0-based audiences by making them available for purchase by advertisers at various rates in |destination-name|.

.. destination-the-trade-desk-marketplace-about-end

.. include:: ../../amperity_operator/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-whatis-20-start
   :end-before: .. destination-the-trade-desk-whatis-20-end


.. _destination-the-trade-desk-marketplace-howitworks:

How this destination works
==================================================

.. destination-the-trade-desk-marketplace-howitworks-start

Send audiences to |destination-name| using the `The Trade Desk Partner API <https://partner.thetradedesk.com/v3/portal/api/overview>`__ |ext_link| to make ID-based audiences available to advertisers for more granular targeting.

.. destination-the-trade-desk-marketplace-howitworks-end

.. image:: ../../images/howitworks-the-trade-desk-marketplace.png
   :width: 600 px
   :alt: The Trade Desk Data Marketplace connector
   :align: left
   :class: no-scaled-link

.. destination-the-trade-desk-marketplace-howitworks-table-start

|destination-name| destination works like this:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **START WORKFLOW**

       A workflow starts on the configured schedule, such as "every 2 weeks at 4:00 PM UTC starting June 20, 2026".

       Amperity uses specific endpoints in the The Trade Desk Platform API for this workflow:

       #. `POST /v3/thirdpartydata/query <https://partner.thetradedesk.com/v3/portal/api/ref/post-thirdpartydata-query>`__ |ext_link|
       #. `POST /v3/thirdpartydata <https://partner.thetradedesk.com/v3/portal/api/ref/post-thirdpartydata>`__ |ext_link|
       #. `PUT /v3/thirdpartydata <https://partner.thetradedesk.com/v3/portal/api/ref/put-thirdpartydata>`__ |ext_link|
       #. `POST /v3/datarate/batch <https://partner.thetradedesk.com/v3/portal/api/ref/post-datarate-batch>`__ |ext_link|

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **AUDIENCE LIST**

       Amperity uses the `POST /v3/thirdpartydata/query <https://partner.thetradedesk.com/v3/portal/api/ref/post-thirdpartydata-query>`__ |ext_link| endpoint to retrieve a filterable list of audiences for a specific data provider. The status for each existing audience is returned, including `taxonomy compliance status <https://partner.thetradedesk.com/v3/portal/data/doc/ThirdPartyDataManagement#check-status>`__ |ext_link|, if the `audience is buyable <https://partner.thetradedesk.com/v3/portal/data/doc/ThirdPartyDataManagement>`__ |ext_link|, the number of `active and received IDs <https://partner.thetradedesk.com/v3/portal/api/doc/Audience>`__ |ext_link|, and the time at which the audience was last updated.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **TAXONOMY FOR CUSTOM AUDIENCES**

       Amperity uses the `POST /v3/thirdpartydata <https://partner.thetradedesk.com/v3/portal/api/ref/post-thirdpartydata>`__ |ext_link| endpoint to identify the taxonomy location and buyable status for custom audiences. New custom audiences are added to the taxonomy starting at a custom location and must be buyable.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **TAXONOMY FOR SYNDICATED AUDIENCES**

       Amperity uses the `POST /v3/thirdpartydata <https://partner.thetradedesk.com/v3/portal/api/ref/post-thirdpartydata>`__ |ext_link| endpoint to identify the taxonomy location and buyable status for syndicated audiences. New syndicated audiences are added to the taxonomy starting at the root of the taxonomy and must be buyable.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - **UPDATE AND CREATE AUDIENCES**

       Amperity uses the `POST /v3/thirdpartydata <https://partner.thetradedesk.com/v3/portal/api/ref/post-thirdpartydata>`__ |ext_link| endpoint to update and create audiences in |destination-name|.

       If an audience does not exist Amperity will create it. If an error occurs while creating an audience Amperity will retry using a custom taxonomy location at the root of the taxonomy.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - **SEND DATA RATES FOR APPROVAL**

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-data-marketplace-concept-data-rates-start
          :end-before: .. monetize-data-marketplace-concept-data-rates-end

       Amperity uses the `POST /v3/datarate/batch <https://partner.thetradedesk.com/v3/portal/api/ref/post-datarate-batch>`__ |ext_link| endpoint to send data rates for processing and approval.

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-the-trade-desk-marketplace-best-practices-start
             :end-before: .. setting-the-trade-desk-marketplace-best-practices-end

       The following settings define the data rates sent for approval. Depending on the type of audience--custom or syndicated--and the intended consumer--partner or advertiser--some combination of the following settings define the data rate sent for approval.


       **Cost per thousand (CPM)**

          .. include:: ../../amperity_reference/source/monetize.rst
             :start-after: .. monetize-data-marketplace-concept-cpm-start
             :end-before: .. monetize-data-marketplace-concept-cpm-end

          .. include:: ../../amperity_reference/source/monetize.rst
             :start-after: .. monetize-data-marketplace-concept-cpm-the-trade-desk-start
             :end-before: .. monetize-data-marketplace-concept-cpm-the-trade-desk-end


       **Percent of media cost**

          .. include:: ../../amperity_reference/source/monetize.rst
             :start-after: .. monetize-data-marketplace-concept-percentage-start
             :end-before: .. monetize-data-marketplace-concept-percentage-end

          .. include:: ../../amperity_reference/source/monetize.rst
             :start-after: .. monetize-data-marketplace-concept-percentage-the-trade-desk-start
             :end-before: .. monetize-data-marketplace-concept-percentage-the-trade-desk-end


       **Rate level**

          .. include:: ../../amperity_reference/source/monetize.rst
             :start-after: .. monetize-data-marketplace-concept-rate-levels-start
             :end-before: .. monetize-data-marketplace-concept-rate-levels-end

          **System**
             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-level-system-start
                :end-before: .. monetize-data-marketplace-concept-rate-level-system-end

          **Partner**
             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-level-partner-start
                :end-before: .. monetize-data-marketplace-concept-rate-level-partner-end

             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-level-partner-the-trade-desk-start
                :end-before: .. monetize-data-marketplace-concept-rate-level-partner-the-trade-desk-end

          **Advertiser**
             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-level-advertiser-start
                :end-before: .. monetize-data-marketplace-concept-rate-level-advertiser-end

             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-level-advertiser-the-trade-desk-start
                :end-before: .. monetize-data-marketplace-concept-rate-level-advertiser-the-trade-desk-end


       **Rate type**

          .. include:: ../../amperity_reference/source/monetize.rst
             :start-after: .. monetize-data-marketplace-concept-rate-types-start
             :end-before: .. monetize-data-marketplace-concept-rate-types-end

          **CPM**
             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-type-cpm-start
                :end-before: .. monetize-data-marketplace-concept-rate-type-cpm-end

          **Hybrid**
             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-type-hybrid-start
                :end-before: .. monetize-data-marketplace-concept-rate-type-hybrid-end

          **Percent of media cost**
             .. include:: ../../amperity_reference/source/monetize.rst
                :start-after: .. monetize-data-marketplace-concept-rate-type-percent-start
                :end-before: .. monetize-data-marketplace-concept-rate-type-percent-end


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step seven.
          :align: center
          :class: no-scaled-link
     - **UPDATE BUYABLE STATUS**

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-data-marketplace-concept-buyable-start
          :end-before: .. monetize-data-marketplace-concept-buyable-end

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-data-marketplace-concept-buyable-the-trade-desk-start
          :end-before: .. monetize-data-marketplace-concept-buyable-the-trade-desk-end

       Amperity uses the `PUT /v3/thirdpartydata <https://partner.thetradedesk.com/v3/portal/api/ref/put-thirdpartydata>`__ |ext_link| endpoint to update an audience's buyable status.


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step seven.
          :align: center
          :class: no-scaled-link
     - **END WORKFLOW**

       After Amperity has created or updated all audiences for membership, data rates, and buyable status, the workflow ends.


.. destination-the-trade-desk-marketplace-howitworks-table-end


.. _destination-the-trade-desk-marketplace-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-the-trade-desk-marketplace-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **UID2**

       .. include:: ../../amperity_reference/source/uid2.rst
          :start-after: .. uid2-overview-start
          :end-before: .. uid2-overview-end

       .. include:: ../../amperity_reference/source/uid2.rst
          :start-after: .. uid2-prerequisite-get-access-start
          :end-before: .. uid2-prerequisite-get-access-end

       .. include:: ../../amperity_reference/source/uid2.rst
          :start-after: .. uid2-prerequisite-participate-start
          :end-before: .. uid2-prerequisite-participate-end

       .. include:: ../../amperity_reference/source/uid2.rst
          :start-after: .. uid2-prerequisite-get-credentials-start
          :end-before: .. uid2-prerequisite-get-credentials-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Marketplace agreement**

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-requirement-marketplace-agreement-start
          :end-before: .. monetize-requirement-marketplace-agreement-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Brand ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-brand-id-start
             :end-before: .. credential-the-trade-desk-marketplace-brand-id-end

       **Provider ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-id-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-id-end

       **Provider secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-secret-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-secret-end

       **Platform API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-platform-api-token-start
             :end-before: .. credential-the-trade-desk-marketplace-platform-api-token-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Taxonomy**

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-data-marketplace-concept-taxonomy-start
          :end-before: .. monetize-data-marketplace-concept-taxonomy-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 5.
          :align: center
          :class: no-scaled-link
     - **Partner ID**

       The partner ID for an account with |destination-name|.

       .. note:: A **Partner ID** is required when **Partner** is selected as the **Rate level**.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 6.
          :align: center
          :class: no-scaled-link
     - **Advertiser ID**

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-the-trade-desk-advertiser-id-start
          :end-before: .. credential-the-trade-desk-advertiser-id-end

       .. note:: An **Advertiser ID** is required when **Advertiser** is selected as the **Rate level**.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 7.
          :align: center
          :class: no-scaled-link
     - **Standard policies**

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-requirement-standard-policies-start
          :end-before: .. monetize-requirement-standard-policies-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 8.
          :align: center
          :class: no-scaled-link
     - **Amps consumption**

       .. include:: ../../amperity_reference/source/monetize.rst
          :start-after: .. monetize-requirement-amps-start
          :end-before: .. monetize-requirement-amps-end


.. destination-the-trade-desk-marketplace-get-details-end


.. _destination-the-trade-desk-marketplace-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for The Trade Desk Data Marketplace**

.. destination-the-trade-desk-marketplace-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Brand ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-brand-id-start
             :end-before: .. credential-the-trade-desk-marketplace-brand-id-end

       **Provider ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-id-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-id-end

       **Provider secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-provider-secret-start
             :end-before: .. credential-the-trade-desk-marketplace-provider-secret-end

       **Platform API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-the-trade-desk-marketplace-platform-api-token-start
             :end-before: .. credential-the-trade-desk-marketplace-platform-api-token-end

.. destination-the-trade-desk-marketplace-credentials-steps-end


.. _destination-the-trade-desk-marketplace-add:

Add destination
==================================================

|destination-name| has two types of audiences: :ref:`custom <destination-the-trade-desk-marketplace-add-custom>` and :ref:`syndicated <destination-the-trade-desk-marketplace-add-syndicated>`.


.. _destination-the-trade-desk-marketplace-add-custom:

For custom audiences
--------------------------------------------------

.. include:: ../../amperity_reference/source/monetize.rst
   :start-after: .. monetize-howtos-create-custom-audience-start
   :end-before: .. monetize-howtos-create-custom-audience-end

**To create a custom audience**

.. include:: ../../amperity_reference/source/monetize.rst
   :start-after: .. monetize-howtos-create-custom-audience-steps-start
   :end-before: .. monetize-howtos-create-custom-audience-steps-end


.. _destination-the-trade-desk-marketplace-add-syndicated:

For syndicated audiences
--------------------------------------------------

.. include:: ../../amperity_reference/source/monetize.rst
   :start-after: .. monetize-howtos-create-syndicated-audience-start
   :end-before: .. monetize-howtos-create-syndicated-audience-end

**To create a syndicated audience**

.. include:: ../../amperity_reference/source/monetize.rst
   :start-after: .. monetize-howtos-create-syndicated-audience-steps-start
   :end-before: .. monetize-howtos-create-syndicated-audience-steps-end
