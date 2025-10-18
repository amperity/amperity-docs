.. https://docs.amperity.com/operator/


.. |source-name| replace:: Google BigQuery
.. |destination-name| replace:: Google BigQuery

.. meta::
    :description lang=en:
        Amperity Bridge for Google BigQuery is a first-class integration that uses BigQuery Sharing to enable inbound data access to Amperity from Google BigQuery.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity Bridge for Google BigQuery is a first-class integration that uses BigQuery Sharing to enable inbound data access to Amperity from Google BigQuery.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Amperity Bridge to Google BigQuery

==================================================
Connect Amperity Bridge to Google BigQuery
==================================================

.. bridge-google-bigquery-about-start

Amperity Bridge for Google BigQuery is a first-class integration enables inbound data access to Amperity from Google BigQuery without copying data or scheduling ETL workloads.

.. bridge-google-bigquery-about-end

.. bridge-google-bigquery-what-is-bigquery-sharing-start

.. admonition:: What is BigQuery Sharing?

   `BigQuery Sharing <https://console.cloud.google.com/bigquery/analytics-hub?inv=1&invt=Ab26qA>`__ |ext_link| publishes and shares datasets between organizations. Create an exchange, and then invite organizations to publish or subscribe to data in the exchange.

.. bridge-google-bigquery-what-is-bigquery-sharing-end

.. bridge-google-bigquery-switch-to-bridge-start

.. tip:: Amperity Bridge shares data directly with Google BigQuery. A bridge does not require a courier or a database export to be configured. A bridge can be configured to run automatically as part of any scheduled workflow.

.. bridge-google-bigquery-switch-to-bridge-end


.. _bridge-google-bigquery-data-types:

Data types
==================================================

.. bridge-google-bigquery-data-types-start

Most `Google BigQuery data types <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types>`__ |ext_link| are supported by Amperity Bridge.

.. include:: ../../amperity_reference/source/bridge.rst
   :start-after: .. bridge-howto-sync-datatypes-start
   :end-before: .. bridge-howto-sync-datatypes-end

.. note:: **BYTES** and **RANGE** data types are unsupported.

The following table describes how Google BigQuery data types map to Amperity data types.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Google BigQuery data type
     - Amperity data type

   * - `ARRAY <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type>`__ |ext_link|

       An ordered list of zero or more elements of non-array values.

       Each element must be a Google BigQuery type that maps to a supported Amperity type.

     - **Array**

       An ordered list of zero or more elements of non-array values by field name and value.

       Fields within an **Array** must contain values for data types supported by Amperity.


   * - `BIGINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value and an alias for **INT64**.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values less than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `BIGNUMERIC <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A decimal value with precision of 76.

       .. important:: Amperity supports precision for **BIGNUMERIC** data types when they are less than or equal to 38. Precision that is greater than 38 is not supported.

     - **Decimal**

       A fixed point number, such as for prices or message sizes. The number of characters in the decimal value is configurable. For example:

       * 1.50 (prices)
       * 1874.380 (message sizes)
       * 141.48042 (order subtotals)


   * - `BOOLEAN <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#boolean_type>`__ |ext_link|, **BOOL**

       A value that can be **TRUE**, **FALSE**, or **NULL**.

     - **Boolean**

       A value that can be **TRUE**, **FALSE**, or **NULL**.


   * - `BYTES <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#bytes_type>`__ |ext_link|

       Variable-length binary data.

     - .. warning:: The Google BigQuery **BYTES** data type is unsupported. Exclude fields with **BYTES** data types from tables before sharing them with Amperity.


   * - `BYTEINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value and an alias for **INT64**.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values less than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `DATE <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#date_type>`__ |ext_link|

       A Gregorian calendar date, independent of time zone.

     - **Date**

       An ISO-8601 compliant date value, such as a birthdate. For example:

       * 2021-11-04


   * - `DATETIME <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type>`__ |ext_link|

       A Gregorian date and time, as they might be displayed on a watch, independent of time zone.

     - **Datetime**

       ISO-8601 compliant date and time values, such as a purchase or transaction, the time at which data was last updated, or a campaign launch date. For example:

       * Mon Nov 30 2020 16:00:00 GMT-0800 (Pacific Standard Time)
       * Sat Sep 02 2017 14:36:19 GMT-0700 (Pacific Daylight Time)


   * - `DECIMAL (p,s) <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_linK|

       A decimal value with a precision of 38 digits.

     - **Decimal**

       A fixed point number, such as for prices or message sizes. The number of characters in the decimal value is configurable. For example:

       * 1.50 (prices)
       * 1874.380 (message sizes)
       * 141.48042 (order subtotals)


   * - `FLOAT64 <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       An approximate double precision numeric value.

     - **Float**

       A floating point number. For example:

       * 3.14
       * 3.14159


   * - `GEOGRAPHY <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type>`__ |ext_link|

       A collection of points, linestrings, and polygons that represent a set or subset of the surface of the Earth.

     - **String**

       A string of characters.


   * - `INT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value and an alias for **INT64**.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values less than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `INT64 <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value up to 64 bits.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values less than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `INTEGER <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value and an alias for **INT64**.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values less than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `JSON <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#json_type>`__ |ext_link|

       Represents JSON, a lightweight data-interchange format.

     - **String**

       A string of characters.


   * - `NUMERIC (p,s) <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A decimal value with a precision of up to 38 digits.

     - **Decimal**

       A fixed point number, such as for prices or message sizes. The number of characters in the decimal value is configurable. For example:

       * 1.50 (prices)
       * 1874.380 (message sizes)
       * 141.48042 (order subtotals)


   * - `RANGE <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#range_type>`__ |ext_link|

       A contiguous range between two dates, datetimes, or timestamps.

     - .. warning:: The Google BigQuery **RANGE** data type is unsupported. Exclude fields with **RANGE** data types from tables before sharing them with Amperity.


   * - `SMALLINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value and an alias for **INT64**.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values less than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345


   * - `STRING <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type>`__ |ext_link|

       Variable-length character data.

     - **String**

       A sequence of characters, such as first and last names, email addresses, physical addresses, UUIDs and other IDs, phone numbers, zip codes, product names, and descriptions. May be empty. For example:

       * John
       * Smith
       * John Smith
       * johnsmith @ domain.com
       * 123 Main Street
       * 206-555-1111
       * 00002ac0-0915-3cb4-b7c7-5ee192b3bd49
       * ACME
       * pants
       * 
       * "A data source that pulls from an Amazon S3 bucket."


   * - `STRUCT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type>`__ |ext_link|

       A container of ordered fields. Fields within a **STRUCT** must contain values for data types supported by Amperity.

     - **Struct**

       A container of ordered fields by name and type.


   * - `TIME <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#time_type>`__ |ext_link|

       A time of day, as might be displayed on a clock, independent of a specific date and time zone.

     - **String**

       A sequence of characters that represents the time of day.


   * - `TIMESTAMP <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type>`__ |ext_link|

       An absolute point in time, independent of any time zone or convention, such as daylight saving time (DST).

     - **Datetime**

       ISO-8601 compliant date and time values, such as a purchase or transaction, the time at which data was last updated, or a campaign launch date. For example:

       * Mon Nov 30 2020 16:00:00 GMT-0800 (Pacific Standard Time)
       * Sat Sep 02 2017 14:36:19 GMT-0700 (Pacific Daylight Time)


   * - `TINYINT <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types>`__ |ext_link|

       A numeric value and an alias for **INT64**.

       .. note:: **BIGINT**, **BYTEINT**, **INT**, **INTEGER**, **SMALLINT**, and **TINYINT** data types are aliases for **INT64** and represent values with fewer than 64 bits.

     - **Integer**

       A numeric value, such as the quantity of items purchased. For example:

       * 1
       * 12345

.. bridge-google-bigquery-data-types-end


.. _bridge-google-bigquery-sync-with-amperity:

From Google BigQuery
==================================================

.. bridge-google-bigquery-sync-amperity-start

A connection from |source-name| to Amperity requires configuration steps to be made in both Amperity and |source-name|.

.. bridge-google-bigquery-sync-amperity-end

.. bridge-google-bigquery-sync-amperity-links-start

#. :ref:`Get details <bridge-google-bigquery-sync-amperity-get-details>`
#. :ref:`Configure Google BigQuery <bridge-google-bigquery-sync-amperity-configure-bigquery>`
#. :ref:`Add inbound bridge <bridge-google-bigquery-sync-amperity-add-bridge>`

.. bridge-google-bigquery-sync-amperity-links-end


.. _bridge-google-bigquery-sync-amperity-get-details:

Get details
--------------------------------------------------

.. bridge-google-bigquery-sync-amperity-get-details-start

Before you can create inbound sharing between |source-name| and Amperity you need to collect the following information.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 1.
          :align: center
          :class: no-scaled-link
     - The individual who configures Amperity to share data with |destination-name| must be assigned the **Datagrid Administrator** policy in Amperity or have the ability to configure a bridge for |source-name| in a sandbox.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 2.
          :align: center
          :class: no-scaled-link
     - A Google Cloud account with the `BigQuery API enabled <https://cloud.google.com/bigquery/docs/bigquery-web-ui>`__ |ext_link|.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 3.
          :align: center
          :class: no-scaled-link
     - The user who creates the data exchange and listing in |source-name| must have permission to access to the Google Analytics Hub API. The following `permissions <https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#required_permissions>`__ |ext_link| are required:

       * **serviceUsage.services.get**
       * **serviceUsage.services.list**
       * **serviceUsage.services.enable**

       .. note:: **roles/serviceusage.serviceUsageAdmin** is a predefined IAM role that includes the permissions required to access the Analytics Hub API.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 4.
          :align: center
          :class: no-scaled-link
     - The user who creates the data exchange and listing in |destination-name| must have permission to create listings. The following `permissions <https://cloud.google.com/bigquery/docs/access-control#bigquery>`__ |ext_link| are required:

       * **bigquery.datasets.get**
       * **bigquery.datasets.update**

       .. note:: **roles/bigquery.dataOwner** and **roles/bigquery.admin** are predefined IAM roles that include the permissions required to create listings in |destination-name|.


   * - .. image:: ../../images/steps-arrow-off-black.png
          :width: 60 px
          :alt: Requirement 5.
          :align: center
          :class: no-scaled-link

     - The following values are required to connect Amperity to a |source-name| data listing:

       #. **Share link** (for the data exchange)

          This value is available after creating the :ref:`data exchange <bridge-google-bigquery-sync-amperity-configure-bigquery-exchange>` and :ref:`data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing>` in |source-name|. Copy this value. It is required when :ref:`adding the inbound share <bridge-google-bigquery-sync-amperity-add-bridge>`.

          ::

             https://console.cloud.google.com/bigquery/ \
             analytics-hub/exchanges/projects/123456789012/ \
             locations/<location>/dataExchanges/<exchange>/ \
             listings/<listing>

       #. **Subscriber**

          Amperity generates an account identifer to use for activating sharing in |source-name|. Copy this value and use it to configure permissions to the data exchange. Add a principal using this value and assign it to the `Analytics Hub Subscriber <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#ah-subscriber-role>`__ |ext_link| role.

          The account identifier generated by Amperity is similar to:

          ::

             amperity-bridge-<bridge-id>@ \
             amperity.iam.gserviceaccount.com


.. bridge-google-bigquery-sync-amperity-get-details-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery:

Configure Google BigQuery
--------------------------------------------------

.. bridge-google-bigquery-sync-amperity-configure-bigquery-start

To configure |source-name| to sync data with Amperity do the following:

#. :ref:`Create data exchange <bridge-google-bigquery-sync-amperity-configure-bigquery-exchange>`
#. :ref:`Create data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing>`
#. :ref:`Configure subscriber and share link <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>`

.. bridge-google-bigquery-sync-amperity-configure-bigquery-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery-exchange:

Create data exchange
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-start

A `data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#console>`__ |ext_link| in |destination-name| is private by default. Only users and groups that have access to the data exchange can view or subscribe to data listings within the data exchange.

`Create a data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#create-exchange>`__ |ext_link| in |destination-name| and then allow Amperity access to that data exchange.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-end

**To create a Google BigQuery data exchange**

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **BigQuery Console** to the **Sharing** page.

       On the **Sharing** page click **Create exchange**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - In the **Exchange configuration** pane, do the following:

       #. Select the project and region for the data exchange.
       #. Enter a display name.
       #. Add your Amperity account locator.

       .. note:: If you are configuring a new bridge, leave the Amperity account locator field blank. This will be added after the :ref:`account identifier is created <bridge-google-bigquery-sync-amperity-add-bridge>`.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Click **Create exchange**.

       .. important:: Do not configure permissions for the data exchange. The value for the **Add principal** field must be the value that is :ref:`generated by Amperity <bridge-google-bigquery-sync-amperity-add-bridge>`.

       Click **Skip**.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-exchange-steps-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing:

Create data listing
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-start

A `data listing <https://cloud.google.com/bigquery/docs/analytics-hub-manage-listings>`__ |ext_link| in |destination-name| is a reference to a shared dataset that exists in a data exchange. A data listing is private by default.

A `data listing within a private data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-manage-listings#create_a_listing>`__ |ext_link| may be shared with Amperity.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-end

**To create a Google BigQuery data listing**

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Sharing** page click the name of the exchange.

       On the **Listings** tab for the exchange click **Create listing**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - From the **Resource type** dropdown select "BigQuery Dataset", and then select a dataset.

       .. note:: Configuring data egress controls is optional.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Configure a series of details for the data listing.

       Click **Next**.

       * Required. Add a display name.
       * Optional. Configure listing details, discoverability, and email logging.

       Click **Next**

       * Optional. Configure the contact information for primary, provider, and publisher contacts.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Click **Publish**.

       On the **Listings** tab, in the row for the listing that will be shared with Amperity, from the ellipses menu select **Copy share link**.

       Amperity generates a URL similar to:

       ::

          https://console.cloud.google.com/bigquery/analytics-hub/exchanges/projects/123456789012/locations/<location>/dataExchanges/<exchange>/listings/<listing>

       Configure this identifier in |source-name| as the :ref:`subscriber for the data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>`.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-data-listing-steps-end


.. _bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share:

Configure subscriber and share link
++++++++++++++++++++++++++++++++++++++++++++++++++

.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-start

A `subscriber is allowed to view and access a data listing <https://cloud.google.com/bigquery/docs/analytics-hub-manage-subscriptions>`__ |ext_link|. Configure Amperity as the subscriber to the |source-name| data listing.

A share link allows a subscriber to connect to a data listing. Copy the share link for the data listing in |source-name| and configure that link in Amperity.

.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-end

**To configure a Google BigQuery subscriber and share link**

.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - On the **Sharing** page in the row for the exchange that will share data with Amperity select **Set permissions** from the ellipses menu.

       Click **Add principal**

       Paste the Amperity account identifier into the **New principal** field and set the role to be `Analytics Hub Subscriber <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#ah-subscriber-role>`__ |ext_link|.

       Click **Save**

       This returns you to the **Sharing** page.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - On the **Sharing** page in the row for the exchange that will share data with Amperity select **Copy share link** from the ellipses menu.

       .. important:: This value required when :ref:`adding the inbound share <bridge-google-bigquery-sync-amperity-add-bridge>`.


.. bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share-steps-end


.. _bridge-google-bigquery-sync-amperity-add-bridge:

Add inbound bridge
--------------------------------------------------

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-start

Configure an inbound bridge to connect Google BigQuery to Amperity.

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-end

**To add an inbound bridge for Google BigQuery**

.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Sources** page. Under **Inbound shares** click **Add bridge**. 

       Choose **Google BigQuery**.

       .. image:: ../../images/bridge-inbound-choose-bigquery.png
          :width: 320 px
          :alt: Add a bridge for a connection.
          :align: left
          :class: no-scaled-link

       This opens the **Add bridge** dialog box. 

       .. image:: ../../images/bridge-inbound-name-description.png
          :width: 500 px
          :alt: Add a bridge for a connection.
          :align: left
          :class: no-scaled-link

       Add a name and description for the bridge *or* select an existing bridge, and then click **Confirm**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Add the :ref:`share link <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>` that was copied from the |source-name| data exchange.

       Amperity generates the subscriber link *after* the share link has been configured. The share link is a URL similar to:

       ::

          https://console.cloud.google.com/bigquery/analytics-hub/exchanges/projects/123456789012/locations/<location>/dataExchanges/<exchange>/listings/<listing>

       Configure this identifier in |source-name| as the :ref:`subscriber for the data listing <bridge-google-bigquery-sync-amperity-configure-bigquery-subscriber-and-share>`.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Use the **Select tables** dialog box to select any combination of schemas and tables to be connected to Amperity.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       If you select a schema, all tables in that schema will be connected. Any new tables added later need to be manually added to the connection. 

       When finished, click **Next**. This opens the **Domain table mapping** dialog box.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Map the tables that are connected from |source-name| to domain tables in Amperity.

       .. image:: ../../images/bridge-map-inbound-to-domain.png
          :width: 500 px
          :alt: Map connected tables to domain tables.
          :align: left
          :class: no-scaled-link

       Tables that are connected with Amperity are added as domain tables.

       * The names of connected tables must be unique among all domain tables.
       * Primary keys are not assigned.
       * Semantic tags are not applied.

       .. tip:: Use a custom domain table to assign primary keys, apply semantic tags, and shape data within connected tables to support any of your Amperity workflows.

       When finished, click **Save and sync**. This will start a workflow that connects data from |source-name| to Amperity and creates the mapped domain table names.

       You can manually sync tables that are connected with Amperity using the **Sync** option from the **Actions** menu for the inbound bridge.


.. bridge-google-bigquery-sync-amperity-add-inbound-bridge-steps-end


.. _bridge-google-bigquery-sync-with-google-bigquery:

To Google BigQuery
==================================================

.. bridge-google-bigquery-sync-with-google-bigquery-start

A connection between Amperity and Google BigQuery requires configuration steps to be made in both Amperity and Google BigQuery.

.. bridge-google-bigquery-sync-with-google-bigquery-end

.. bridge-google-bigquery-sync-sandbox-start

.. note:: Configuration state for an outbound bridge **is not copied** from production to a sandbox. An outbound bridge must be configured within a sandbox.

.. bridge-google-bigquery-sync-sandbox-end

.. bridge-google-bigquery-sync-with-google-bigquery-links-start

#. :ref:`Verify subscriber details <bridge-google-bigquery-sync-with-google-bigquery-verify-subscribers>`
#. :ref:`Add bridge <bridge-google-bigquery-sync-with-google-bigquery-add-bridge>`
#. :ref:`Select tables to share <bridge-google-bigquery-sync-with-google-bigquery-select-tables>`
#. :ref:`Configure recipients <bridge-google-bigquery-sync-with-google-bigquery-recipients>`
#. :ref:`Subscribe to datasets <bridge-google-bigquery-sync-with-google-bigquery-subscribe>`
#. :ref:`Verify table sharing <bridge-google-bigquery-sync-with-google-bigquery-verify-table-sharing>`

.. bridge-google-bigquery-sync-with-databricks-links-end


.. _bridge-google-bigquery-sync-with-google-bigquery-verify-subscribers:

Verify subscriber details
--------------------------------------------------

.. bridge-google-bigquery-sync-with-google-bigquery-verify-subscribers-start

Verify that `IAM principals <https://cloud.google.com/iam/docs/principals-overview>`__ |ext_link| are configured in Google BigQuery.

IAM principals must be authorized to the following roles:

* `Google BigQuery User <https://cloud.google.com/bigquery/docs/access-control#bigquery.user>`__ |ext_link|
* `Analytics Hub Subscription Owner <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#ah-subscription-owner-role>`__ |ext_link|

IAM principals must have the following permissions:

* View and subscribe to the `data exchange <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#grant-role-data-exchange>`__ |ext_link|
* View and subscribe to the `listing <https://cloud.google.com/bigquery/docs/analytics-hub-grant-roles#ah-subscription-owner-role>`__ |ext_link|

.. bridge-google-bigquery-sync-with-google-bigquery-verify-subscribers-end


.. _bridge-google-bigquery-sync-with-google-bigquery-add-bridge:

Add outbound bridge
--------------------------------------------------

.. bridge-google-bigquery-sync-with-google-bigquery-add-bridge-start

Configure an outbound bridge to connect Amperity with Google BigQuery.

.. bridge-google-bigquery-sync-with-google-bigquery-add-bridge-end

**To add an outbound bridge**

.. bridge-google-bigquery-sync-with-databricks-add-bridge-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Destinations** page. Select the **Outbound shares** tab, and then click **Add bridge**. Choose Google BigQuery. This opens the **Create bridge** dialog box.

       .. image:: ../../images/bridge-inbound-choose-bigquery.png
          :width: 320 px
          :alt: Add a bridge for a connection.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Add a name and description for the bridge *or* select an existing bridge.

       Click **Next**, after which you will :ref:`select the tables to be shared with Google BigQuery <bridge-google-bigquery-sync-with-google-bigquery-select-tables>`.

.. bridge-google-bigquery-sync-with-databricks-add-bridge-steps-end


.. _bridge-google-bigquery-sync-with-google-bigquery-select-tables:

Select tables to share
--------------------------------------------------

.. bridge-google-bigquery-sync-with-google-bigquery-select-tables-start

You can configure Amperity to share any combination of schemas and tables that are available from the **Customer 360** page.

.. bridge-google-bigquery-sync-with-google-bigquery-select-tables-end

**To select schemas and tables to share**

.. bridge-google-bigquery-sync-with-google-bigquery-select-tables-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - After you have :ref:`configured the settings for the bridge <bridge-google-bigquery-sync-with-google-bigquery-add-bridge>`, click **Next** to open the **Select tables** dialog box.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - You may select any combination of schemas and tables.

       If you select a schema, all tables in that schema will be shared, including all changes made to all tables in that schema.

       When finished, click **Save**.

.. bridge-google-bigquery-sync-with-google-bigquery-select-tables-steps-end


.. _bridge-google-bigquery-sync-with-google-bigquery-recipients:

Configure recipients
--------------------------------------------------

.. bridge-google-bigquery-sync-with-google-bigquery-recipients-start

Authorize `specific IAM principals <https://cloud.google.com/iam/docs/principals-overview>`__ |ext_link| configured in your brand's Google Cloud environment.

Principals are authorized to subscribe to the shared schema Amperity connects to Google BigQuery. There are four types of recipients that can be configured: **Service acounts**, **Users**, **Groups**, and **Domains**.

.. note:: You may click **Next** and skip this step without authorizing principals. As long as this bridge exists in Amperity the list of configured recipients may be edited to authorize new principals or to revoke authorization for existing principals.

 :ref:`The next steps are done in Google BigQuery <bridge-google-bigquery-sync-with-google-bigquery-subscribe>`.

.. bridge-google-bigquery-sync-with-google-bigquery-recipients-end


.. _bridge-google-bigquery-sync-with-google-bigquery-subscribe:

Subscribe to datasets
--------------------------------------------------

.. bridge-google-bigquery-sync-with-google-bigquery-subscribe-start

After tables are shared and recipients are configured you must finish setup in Google BigQuery. Click the **Share link** button, which redirects you to the listing in the Google Cloud console. `All authorized principals who will access data in the share must subscribe to the dataset <https://cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings>`__ |ext_link|.

.. bridge-google-bigquery-sync-with-google-bigquery-subscribe-end

.. _bridge-google-bigquery-sync-with-google-bigquery-verify-table-sharing:

Verify table sharing
--------------------------------------------------

.. bridge-google-bigquery-sync-with-google-bigquery-verify-table-sharing-start

Verify that the tables shared from Amperity are available from a database in Google BigQuery.

.. bridge-google-bigquery-sync-with-google-bigquery-verify-table-sharing-end

**To verify that tables were shared from Amperity to Google BigQuery**

.. bridge-google-bigquery-sync-with-google-bigquery-verify-table-sharing-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - From the **Google Cloud** console, open **Solutions**, **All products**, and then under **Analytics** click **BigQuery** or navigate directly to `https://console.cloud.google.com/bigquery <https://console.cloud.google.com/bigquery>`__ |ext_link|.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Use the **Explorer** to browse the data collection. Find the tables shared from Amperity and verify the data within them.

.. bridge-google-bigquery-sync-with-google-bigquery-verify-table-sharing-steps-end
