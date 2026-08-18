.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Dynamic Yield
.. |plugin-name| replace:: "Dynamic Yield Customer Profiles"
.. |credential-type| replace:: "dynamic-yield-customer-profiles"
.. |required-credentials| replace:: "API Key"
.. |what-send| replace:: customer profile attributes
.. |where-send| replace:: a |destination-name| User Data feed
.. |filter-the-list| replace:: "dyn"


.. meta::
    :description lang=en:
        Configure Amperity to send customer profile attributes to a Dynamic Yield User Data feed.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profile attributes to a Dynamic Yield User Data feed.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Dynamic Yield Customer Profiles

==========================================================
Configure destinations for Dynamic Yield Customer Profiles
==========================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dynamic-yield-start
   :end-before: .. term-dynamic-yield-end

.. destination-dynamic-yield-customer-profiles-start

The Dynamic Yield Customer Profiles connector sends |what-send| from Amperity into |where-send|, which keeps |destination-name|'s on-site personalization and recommendation engine current with unified customer profile data.

Each row in the query results is one customer profile. The column named by the **CUID field** setting is sent as the customer identifier; every other column is sent as a profile data field, using the column name and value as-is. |destination-name| requires every attribute to be sent on every update for a customer, so Amperity sends the complete query results on every run. There is no incremental sync.

By default the connector upserts profiles, adding new customers and updating existing ones. A destination can instead be configured to delete profiles, removing each customer in the query results from the feed. Each destination performs a single operation for the entire run, set by the **Operation** setting.

.. .. destination-dynamic-yield-customer-profiles-end

.. destination-dynamic-yield-customer-profiles-api-note-start

.. note:: This destination uses the `Dynamic Yield User Data API <https://dy.dev/reference/user-data-api>`__ |ext_link|.

.. destination-dynamic-yield-customer-profiles-api-note-end

.. destination-dynamic-yield-customer-profiles-beta-start

.. admonition:: Beta

   The Dynamic Yield Customer Profiles connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-dynamic-yield-customer-profiles-beta-end

.. destination-dynamic-yield-customer-profiles-prereq-start

.. note:: The feed and its schema must already exist in |destination-name|. An account admin creates and activates the feed's schema in the |destination-name| console (**Assets > Data Feeds**) before Amperity can send data to it. Amperity sends data to a feed, but cannot create a feed or its schema.

.. destination-dynamic-yield-customer-profiles-prereq-end


.. _destination-dynamic-yield-customer-profiles-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-dynamic-yield-customer-profiles-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dynamic-yield-customer-profiles-api-key-start
             :end-before: .. credential-dynamic-yield-customer-profiles-api-key-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Feed key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-feed-key-start
             :end-before: .. setting-dynamic-yield-customer-profiles-feed-key-end

       **CUID field**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-cuid-field-start
             :end-before: .. setting-dynamic-yield-customer-profiles-cuid-field-end

       **CUID type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-cuid-type-start
             :end-before: .. setting-dynamic-yield-customer-profiles-cuid-type-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional configuration settings**

       **Data center**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-data-center-start
             :end-before: .. setting-dynamic-yield-customer-profiles-data-center-end

       **Operation**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-operation-start
             :end-before: .. setting-dynamic-yield-customer-profiles-operation-end


.. destination-dynamic-yield-customer-profiles-get-details-end


.. _destination-dynamic-yield-customer-profiles-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Dynamic Yield Customer Profiles**

.. destination-dynamic-yield-customer-profiles-credentials-steps-start

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

       **API Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dynamic-yield-customer-profiles-api-key-start
             :end-before: .. credential-dynamic-yield-customer-profiles-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-dynamic-yield-customer-profiles-api-find-key-start
             :end-before: .. credential-dynamic-yield-customer-profiles-api-find-key-end

.. destination-dynamic-yield-customer-profiles-credentials-steps-end


.. _destination-dynamic-yield-customer-profiles-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Dynamic Yield Customer Profiles**

.. destination-dynamic-yield-customer-profiles-add-steps-start

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

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add
          :align: left
          :class: no-scaled-link

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

       **Feed key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-feed-key-start
             :end-before: .. setting-dynamic-yield-customer-profiles-feed-key-end

       **Data center**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-data-center-start
             :end-before: .. setting-dynamic-yield-customer-profiles-data-center-end

       **CUID field**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-cuid-field-start
             :end-before: .. setting-dynamic-yield-customer-profiles-cuid-field-end

       **CUID type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-cuid-type-start
             :end-before: .. setting-dynamic-yield-customer-profiles-cuid-type-end

       **Operation**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-dynamic-yield-customer-profiles-operation-start
             :end-before: .. setting-dynamic-yield-customer-profiles-operation-end

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

.. destination-dynamic-yield-customer-profiles-add-steps-end


.. _destination-dynamic-yield-customer-profiles-validation:

Data validation
==================================================

.. destination-dynamic-yield-customer-profiles-validation-start

Amperity sends every row in the query results, except for rows it cannot build a valid request for. A row is skipped and reported as failed when any of the following is true:

* The **CUID field** is empty for that row.
* The **CUID type** is **he** (hashed email) but the value in the CUID field is not an email address (does not contain an "@"). The value is not hashed and the row is not sent.
* The **Operation** is **upsert** and the row has no columns other than the CUID field, so there are no profile attributes to send.

Skipped rows are reported in the destination's run details and do not stop the run. All other rows are sent.

.. destination-dynamic-yield-customer-profiles-validation-end
