.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Enhanced Conversions
.. |plugin-name| replace:: "Google Enhanced Conversions"
.. |credential-type| replace:: "google-ads"
.. |required-credentials| replace:: "Customer ID"
.. |what-send| replace:: events
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "google"


.. meta::
    :description lang=en:
        Configure Amperity to send events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send events to Google Enhanced Conversions.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configire events for Google Enhanced Conversions

=======================================================
Configure events for Google Enhanced Conversions
=======================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-enhanced-conversions-start
   :end-before: .. term-google-enhanced-conversions-end

.. events-google-enhanced-conversions-about-start

When a customer purchases something from your brand's website, you likely collect some first-party data from that customer to complete the transaction. For example, a physical address, an email address, a phone number, and a full name.

First-party customer data that is associated with online transactions can be sent to |destination-name|, after which it can be used to enhance conversion measurement in Google Ads. For example:

* Track sales and events that happen on a website.
* Track sales that happen from a website.
* Match customers to their Google accounts, which were signed-in to when they engaged with one of your ads.
* Attribute customer engagment with a Google Ads campaign by matching data collected on your website with the signed-in Google accounts that engaged with your ads.

.. events-google-enhanced-conversions-about-end

.. events-google-enhanced-conversions-offline-start

.. admonition:: How to send events to Google Enhanced Conversions?

   First-party customer data that is associated with `offline transactions <https://support.google.com/google-ads/answer/10018336?hl=en&ref_topic=15532419&sjid=11531980841842439788-NC>`__ |ext_link| can be uploaded to |destination-name|, after which it can be used to enhance conversion measurement in Google Ads.

   Configure Amperity to send a CSV file to |destination-name| using :doc:`SFTP <destination_sftp>`.

.. events-google-enhanced-conversions-offline-end


.. _events-google-enhanced-conversions-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-google-enhanced-conversions-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Configure Google Ads**

       Enable enhanced conversions for leads in Google Ads:

       #. `Enable conversion tracking in Google Ads <https://developers.google.com/google-ads/api/docs/conversions/enhanced-conversions/leads-setup>`__ |ext_link|.
       #. Accept customer data terms and opt-in to enhanced conversions for leads.
       #. Set up tagging through Google Tag Manager.
       #. Create at least one ConversionAction.

          The conversion_action_type must be set to **UPLOAD_CLICKS**.

       #. `Configure Google tag settings <https://support.google.com/google-ads/answer/11021502#configure>`__ |ext_link| to enable enhanced conversions for leads.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Events data**

       Load to Amperity data that tracks events data for carts, items in carts, and customer consent. This dataset should include the Google Ads click ID. Some of this data :ref:`may be sent to Google Enhanced Conversions for customer attribution <events-google-enhanced-conversions-fields>`.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for "Google Enhanced Conversions" *must* be completed within Google prior to configuring Amperity to send ads to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-customer-id-end

.. events-google-enhanced-conversions-get-details-table-end


.. _events-google-enhanced-conversions-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure OAuth**

.. events-google-enhanced-conversions-credentials-steps-start

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

       **Refresh token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. events-google-enhanced-conversions-credentials-steps-end


.. _events-google-enhanced-conversions-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Enhanced Conversions**

.. events-google-enhanced-conversions-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Conversion action name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-action-name-start
             :end-before: .. setting-google-enhanced-conversions-action-name-end

       **Customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-enhanced-conversions-customer-id-start
             :end-before: .. setting-google-enhanced-conversions-customer-id-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end


.. events-google-enhanced-conversions-add-steps-end


.. _events-google-enhanced-conversions-fields:

Fields for enhanced conversions
==================================================

.. events-google-enhanced-conversions-fields-start

Fields for enhanced conversions must include hashed customer profile data--email addresses and phone numbers--and should include a transaction identifier and the Google Ads click ID.

The following table describes the fields that may be sent to |destination-name| for customer attribution. You should send as many of these fields as you can for each potential attribution to customer activity.

.. events-google-enhanced-conversions-fields-end

.. events-google-enhanced-conversions-fields-table-start

.. list-table::
   :widths: 130 130 340
   :header-rows: 1

   * - Amperity
     - Google
     - Description
   * - Varies.
     - **ad_personalization**
     - The customer consent status for personalization for Google Ads.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads, but may be located in a table for consent tracking.


   * - Varies.
     - **ad_user_data**
     - The customer consent status for Google Ads.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads, but may be located in a table for consent tracking.


   * - Varies.
     - **conversion_environment**
     - The environment in which the conversion occurred. For example: ``APP`` or ``WEB``.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads.


   * - Varies.
     - **currency_code**
     - The `currency code <https://developers.google.com/google-ads/api/data/codes-formats#currency_codes>`__ |ext_link| for the conversion_value.


   * - **Email**
     - **email**
     - The email address for the customer.

       The value for the email address **must** be SHA-256 hashed.

       .. tip:: Use the **email** field in the **Merged Customers** table.


   * - Varies.
     - **feed_language_code**
     - The language code used in Google services to set the language of an advertising feed.


   * - Varies.
     - **feed_country_code**
     - The country code used in Google services to set the language of an advertising feed.


   * - Varies.
     - **gbraid**
     - A gbraid is a URL parameter present when a user clicks on an ad on the web, and then is directed to your brand's iOS app.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads.


   * - Varies.
     - **gclid**
     - A `gclid <https://support.google.com/google-ads/answer/9744275>`__ |ext_link| is an identifier captured from URL parameters when a customer clicks on an ad, and then navigates to your brand's website.

       This is the best identifier for online events and Google Ads.

       .. important:: Send all relevant data for a conversion even if the **gclid** is unavailable. Converstions data that only includes user-provided data is still useful.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads.


   * - **Item Cost**
     - **local_transaction_cost**
     - The individual cost for each item in the order.

       .. tip:: Use the **Item Cost** field in the **Unified Itemized Transactions** table.


   * - **Store ID**
     - **merchant_id**
     - A store ID is a unique identifier for the location of a store.

       .. tip:: Use the **Store ID** field in the **Unified Itemized Transactions** table.


   * - **Order ID**
     - **order_id**
     - An order ID is the unique identifier for the order. It links together all items in the same transaction. For returns and cancellations, the order ID is the unique identifier for the original order, including returned or canceled items.

       |destination-name| refers to this as the transaction ID for the conversion. This field is optional, but strongly recommended.

       .. tip:: Use the **Order ID** field in the **Unified Itemized Transactions** table.


   * - **Phone**
     - **phone**
     - The phone number for the customer.

       The value for the phone number **must** be SHA-256 hashed.

       .. tip:: Use the **phone** field in the **Merged Customers** table.


   * - **Product ID**
     - **product_id**
     - The unique identifier for a product.

       .. tip:: Use the **Product ID** field in the **Unified Itemized Transactions** table.


   * - **Item Quantity**
     - **quantity**
     - Item quantity is the total number of items in an order. For returned and canceled items, item quantity is the total number of returned or canceled items.

       .. tip:: Use the **Item Quantity** field in the **Unified Itemized Transactions** table.


   * - Varies.
     - **timestamp**
     - The date and time of the conversion. The value must have a timezone and the format must be ``yyyy-mm-dd HH:mm:ss+|-HH:mm``. Daylight Savings Time (DST) may be ignored.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads *or* it may be the **Order Datetime** field in the **Unified Itemized Transactions** table.


   * - **Unit List Price**
     - **unit_price**
     - Unit list price is the manufacturer's suggested retail price (MSRP) for a single unit of an item.

       .. tip:: Use the **Unit List Price** field in the **Unified Itemized Transactions** table.


   * - Varies.
     - **wbraid**
     - A **wbraid** is a URL parameter that is present when a user clicks on an ad in an iOS app and is directed to a webpage.

       .. note:: This field should be in the table that contains online events data for websites and mobile apps collected by Google Ads.

.. events-google-enhanced-conversions-fields-table-end
