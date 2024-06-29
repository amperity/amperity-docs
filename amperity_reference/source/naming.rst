.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Use naming conventions to help your brand stay organized within Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use naming conventions to help your brand stay organized within Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Naming conventions


==================================================
Naming conventions
==================================================

.. naming-start

Use the following naming conventions to ensure that your tenant is configured with consistent and predictable names, including feed names, domain table names, database and database table names, query and orchestration names, and segment and campaign names.

.. naming-end

.. naming-note-start

.. note:: A tenant that is configured to support multiple brands or regions should use a consistent prefix for each brand and/or region.

.. naming-note-end

.. naming-important-start

.. important:: Avoid using dates within names as much as possible. Most data sources that are provided to Amperity are live datasets that contain records that are added or upserted on a regular bases. If you must use a date within a name, use the YYYYMMDD format.

   The following situations often require using a date within a name.

   #. Snapshots that compare data at different points in time.
   #. Feeds and couriers that capture files that change over time.

.. naming-important-end


.. _naming-campaigns:

Campaigns
==================================================

.. naming-campaigns-start

Use a name that describes the purpose of the campaign.

For example:

* Mothers Day Cross Channel
* Google Ads Midwest High AOV


.. tip:: Consider using a consistent prefix for any of the following patterns:

   * Brand names
   * Channel names
   * Region names

.. naming-campaigns-end


.. _naming-couriers:

Courier names
==================================================

.. naming-couriers-start

Use a combination of source and feed for the name of the courier as much as possible. Separate the source and feed name using an underscore (``_``). Add details like "historical", "daily", or "test" as appropriate. Add details if the data is regional or by brand. Consider if the courier is pulling a dedicated data source or if it is pulling multiple sources.

For example:

* Adobe_Clickstream
* Adobe_Clickstream_Daily
* Amazon_S3:Static (which contains individual files for postal codes, geolocation data, etc.)
* Braze_Audience_EMEA
* Braze_Audience_PNW
* Sailthru_Responses

.. naming-couriers-end


.. _naming-custom-databases:

Custom database names
==================================================

.. naming-custom-databases-start

Use title case to describe the data that is contained within this database, including category and purpose.

For example:

* Amperity Analytics
* Brand Production
* Production

.. naming-custom-databases-end


.. _naming-database-tables:

Database table names
==================================================

.. naming-database-tables-start

Use a combination of source and feed for the name of the database table as much as possible. Separate the source and feed name using an underscore (``_``). Each word in the database table name should begin with a capital letter.

For example:

* Adobe_Clickstream
* Amazon_S3_StateCodes
* Braze_Audience
* Sailthru_Responses
* Shopify_Orders

.. naming-database-tables-end


.. _naming-destinations:

Destination names
==================================================

.. naming-destinations-start

Use the name of the system to which Amperity will send data.

For example:

* Adobe
* Amazon_S3
* Oracle_Responsys
* Pebble_Post

.. naming-destinations-end


.. _naming-domain-tables:

Domain table names
==================================================

.. naming-domain-tables-start

The name of a domain table is determined by the name of the data source, and then the name of the feed, separated by a colon (``:``).

For example:

* Adobe:Clickstream
* Amazon_S3:StateCodes
* Braze:Audience
* Sailthru:Responses
* Shopify:Orders

.. important:: Custom domain tables should follow the source/feed naming convention as often as possible. Apply a consistent prefix to the source name to identify the table as a custom domain table, and then append the purpose of the table. For example, a custom domain table that filters Shopify data, and then applies semantic tags for unified transactions: CDT_Shopify_Orders_UT.

.. naming-domain-tables-end


.. _naming-feeds:

Feed names
==================================================

.. naming-feeds-start

Use the name of the dataset provided by the system that provided this data to Amperity.

For example:

* Audience
* Clickstream
* Orders
* Responses
* StateCodes

.. important:: All internal feed names, such as the feed for the bad-values blocklist, should be prefixed with "Amperity". For example: "Amperity:Blocklist".

.. naming-feeds-end


.. _naming-folders:

Folder names
==================================================

.. naming-folders-start

Group queries and segments using folders. Assign each folder a functional name that accurately describes all of the items within that folder.

For example:

* Braze
* Direct_Mail

.. tip:: Use short folder names as often as possible.

.. naming-folders-end


.. _naming-queries:

Query names
==================================================

.. naming-queries-start

Use a name that describes the purpose and result type for the query. Add details like "historical", "daily", or "test" as appropriate. Add details if the data is regional or by brand.

For example:

* Braze_Audience_Test
* Customers_Hawaii, Customers_California

.. tip:: Prefix a query in a folder with that folder name as often as possible. For example: Direct_Mail_Customers_Hawaii.

.. naming-queries-end


.. _naming-segments:

Segment names
==================================================

.. naming-segments-start

Use a name that describes the purpose and audience type for the segment. Add details like "historical", "daily", or "test" as appropriate. Add details if the data is regional or by brand.

For example:

* Birthdays_Under_40
* High_AOV_Active_Loyal
* High_CLV_Historical

.. tip:: Prefix a segment in a folder with that folder name as often as possible. Braze_Birthdays_Under_40.

.. naming-segments-end


.. _naming-sources:

Source names
==================================================

.. naming-sources-start

Use the name of the system that provided this data to Amperity.

For example:

* Adobe
* Amazon S3
* Braze
* Sailthru
* Shopify

.. naming-sources-end
