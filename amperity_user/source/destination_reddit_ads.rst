.. https://docs.amperity.com/user/


.. |destination-name| replace:: Reddit Ads
.. |plugin-name| replace:: SFTP


.. meta::
    :description lang=en:
        Use queries and orchestrations to send audiences from Amperity to Reddit Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use queries and orchestrations to send audiences from Amperity to Reddit Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Reddit Ads

==================================================
Send audiences to Reddit Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-reddit-ads-start
   :end-before: .. term-reddit-ads-end

.. destination-reddit-ads-about-start

You can send audience lists to |destination-name| using a CSV file that contains hashed email addresses and is sent to cloud storage or SFTP, after which you can upload the CSV file to |destination-name| through the |destination-name| Manager.

An audience list should contain hashed email addresses. Upload the audience list to |destination-name|, and then used it for :ref:`audience targeting in Reddit Ads <destination-reddit-ads-audience-targeting>`. There are two options:

:ref:`Use a query to return a list of hashed email addresses <destination-reddit-ads-audience-targeting-query>`, download the results of that query, and then upload it to |destination-name|.

:ref:`Add a hashed email column to your customer 360 database <destination-reddit-ads-audience-targeting-database>`, and then send a file that contains those hashed email address to a location from which they can be uploaded to |destination-name|.

.. destination-reddit-ads-about-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end


.. _destination-reddit-ads-audience-targeting:

Custom audiences
==================================================

.. destination-reddit-ads-audience-targeting-start

Upload a `customer audiences <https://redditinc.force.com/helpcenter/s/article/Overview-Custom-Audience-Customer-List-Targeting#csvUpload>`__ |ext_link|, and then use that audience to engage with your customers within communities in Reddit.

The following examples show how to build the same audience using :ref:`a query that returns hashed email addresses <destination-reddit-ads-audience-targeting-query>` and a campaign that uses :ref:`an attribute for hashed email addresses <destination-reddit-ads-audience-targeting-database>` that is available from your customer 360 database.

.. destination-reddit-ads-audience-targeting-end


.. _destination-reddit-ads-audience-targeting-query:

Query results
--------------------------------------------------

.. destination-reddit-ads-audience-targeting-query-start

The following example describes the steps required to send an audience from Amperity to |destination-name| using a query that returns a list of hashed email addresses.

.. note:: This example uses attributes from Amperity standard output to build a list of customers who are active and who have recently purchased products from your brand.


.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Query Editor.
          :align: center
          :class: no-scaled-link

     - Open the **Query Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 350 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Build a query that returns a list of email addresses.
          :align: center
          :class: no-scaled-link

     - Build a query that returns a list of hashed email addresses that are contactable by your brand. Use additional filters to scope your audience for your use cases and goals for marketing to your customers within |destination-name|.

       For example, the following query returns a list of hashed email addresses for customers who are engaged with your brand, have opted in to receiving email communication, have made at least 4 purchases within the previous year, and have spent at least $400.

       .. code-block:: sql
          :linenos:

          SELECT
            TO_HEX(
              SHA256(
                TO_UTF8(
                  UPPER(
                    TRIM(email)
                  )
                )
              )
            ) AS email
          FROM Merged_Customers mc
          INNER JOIN Customer_Attributes ca
            ON mc.amperity_id = ca.amperity_id
          INNER JOIN Transaction_Attributes_Extended tae
            ON mc.amperity_id = tae.amperity_id
          WHERE (
            LOWER(mc.email) IS NOT NULL
            AND ca.contactable_email = TRUE
            AND tae.L12M_order_frequency >= 4
            AND tae.L12M_order_revenue >= 400
          )

       .. admonition:: How does this example work?

          This example does the following: returns a list of hashed email addresses from the **Merged Customers** table, which is the source of truth for personally identifiable information (PII) within your customer profiles, and then filters that list to:

          #. Ensure these email addresses are contactable (using the **contactable_email** attribute from the **Customer Attributes** table).
          #. Find customers who have purchased at least four times *and* spent at least $400 in the previous year (using the **L12M_order_frequency** and **L12M_order_revenue** attributes from the **Transaction Attributes Extended** table).


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Download query results.
          :align: center
          :class: no-scaled-link

     - In the **Queries** page, click the **Download** button to download the list of email addresses as a CSV file.

       .. tip:: Open the file in a local text editor and remove the header row. If you used the SQL in the example in step 2 the header row is ``email``.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done in Amperity! Give your query a name that clearly describes the purpose. For example: "Reddit Active Customers High Spend".

       Click the **Activate** button in the top right corner of the **Query Editor**. 

       .. tip:: Use good naming patterns to ensure that you can always find your queries when you need them. Be sure to include the brand name and/or the region name if you have multiple brands or have multiple regions and want to build queries that are brand- and/or region-specific.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Upload the CSV file to Reddit Ads.
          :align: center
          :class: no-scaled-link

     - The last step is to upload the list to Reddit Ads. Open Reddit Ads and log in to your business account. Click **Ads**, then **Audiences**, and then click **Create audience**.

       Create your audience as a list of customers that you upload, configure the name and description for the audience, and then upload to |destination-name| the CSV file you downloaded from Amperity.

       .. note:: Your uploaded audience must have at least 100 matches before it will be available for use in Reddit Ads Manager.

          Depending on the size of your audience, this may take up to 48 hours to appear in the **Audiences** page within Reddit Ads Manager.

.. destination-reddit-ads-audience-targeting-query-end


.. _destination-reddit-ads-audience-targeting-database:

Database column
--------------------------------------------------

.. destination-reddit-ads-audience-targeting-database-start

The following example describes the steps required to add a column to your customer 360 database for hashed email addresses, and then to use that column in a campaign.

.. note:: This example uses attributes from Amperity standard output to build a list of customers who are active and who have recently purchased products from your brand.


.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Query Editor.
          :align: center
          :class: no-scaled-link

     - .. important:: This step must be done by a user who is assigned the **DataGrid Operator** policy and is required to enable the use of an attribute that contains a hashed email address within a campaign.

       On the **Customer 360** page, open your customer 360 database in edit mode. Add the following line of SQL to your **Customer 360** table:

       .. code-block:: sql

          ,SHA2(LOWER(TRIM(email)),256) AS hashed_email

       Use the **email** column from the **Merged Customers** table. This example adds a column named "hashed_email" to the **Customer 360** table and will make "hashed_email" available as a selectable attribute from the **Edit Attributes** page in a campaign.

       Run the database to refresh the table and make the hashed email attribute available to segments and campaigns.

       .. tip:: Configure a data template for |destination-name| that removes header rows.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Build a campaign that sends hashed email addresses to cloud storage or SFTP.
          :align: center
          :class: no-scaled-link

     - Build a segment that returns a list of hashed email addresses that are contactable by your brand. Use additional filters to scope your audience for your use cases and goals for marketing to your customers within |destination-name|.

       For example, the following segment returns a list of email addresses for customers who are engaged with your brand, have opted in to receiving email communication, have made at least 4 purchases within the previous year, and have spent at least $400.

       .. image:: ../../images/destination-pinterest-and-reddit-segment-example.png
          :width: 540 px
          :alt: Opted in, more than 4 purchases, more than $400.
          :align: left
          :class: no-scaled-link

       When finished, save your segment:

       .. image:: ../../images/destination-reddit-ads-segment-example-save.png
          :width: 540 px
          :alt: Opted in, more than 4 purchases, more than $400.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Use a campaign to send hashed email addresses to Reddit.
          :align: center
          :class: no-scaled-link

     - Configure a one-time campaign to use the hashed email address segment as its starting audience, and then set the control group to 0%. Select your destination -- SFTP or cloud storage -- and then open the **Edit Attributes** page.

       Choose the **Hashed Email** attribute from the **Customer 360** table.

       .. image:: ../../images/destination-reddit-ads-campaign-add-hashed.png
          :width: 540 px
          :alt: Add hashed email addresses to your campaign.
          :align: left
          :class: no-scaled-link

       Configure the rest of your campaign, and then schedule it.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Upload the CSV file to Reddit Ads.
          :align: center
          :class: no-scaled-link

     - The last step is to upload the list to Reddit Ads. Open Reddit Ads and log in to your business account. Click **Ads**, then **Audiences**, and then click **Create audience**.

       Create your audience as a list of customers that you upload, configure the name and description for the audience, and then upload to |destination-name| the CSV file from the location to which the file was sent from Amperity.

       .. note:: Your uploaded audience must have at least 100 matches before it will be available for use in Reddit Ads Manager.

          Depending on the size of your audience, this may take up to 48 hours to appear in the **Audiences** page within Reddit Ads Manager.

.. destination-reddit-ads-audience-targeting-database-end
