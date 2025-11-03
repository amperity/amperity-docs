.. 
.. xxxxx
..


.. |sftp-type| replace:: ``xxxxx``
.. |sftp-hostname| replace:: ``xxxxx``


This is a shared topic for Paid Media campaigns to share content across collections.

.. vale off

**About paid media campaigns** (config)

.. TODO: This is the intro for segments and campaigns topics section titled "Match rates" and then for each paid media destination a callout in the "Data templates" section. Purpose is to explain, but also provide cross-site linking.

.. vale on

.. paid-media-admonition-about-start

Amperity provides the right set of data to support your brand's paid media advertising with |destination-name|.

#. **Merged Customers** vs. **Unified Paid Media**

   The |table_merged_customers| table contains each of your customers' best profiles.

   The |table_unified_paid_media| table contains all your customer's known profile data.

   Your brand requires additional data templates to use the **Unified Paid Media** table alongside the **Merged Customers** table to support paid media campaigns.

#. Enable dedicated data templates for each table.

   Use a consistent naming pattern to label data templates that use data from the **Merged Customers** table. For example: "Best profile".

   Use a consistent naming pattern to label data templates that use data from the **Unified Paid Media** table. For example: "Full profile".

#. After data templates are configured for both tables, use the |campaign_default_attributes| component on the **Campaigns** page to configure which attributes is associated with the destination, including the table from which those attributes is pulled.

   The selected table will affect your brand's downstream match rates *and* overall customer matches within your |paid_media|. The decision behind which table to use depends on your brand's downstream use case and the type and amount of customer profile data your brand wants to use to match customers.

   You brand should expect to see higher |paid_media_match_rates| when sending audiences from the **Merged Customers** table, but a higher number of matched customer profiles when sending audiences from the **Unified Paid Media** table. Use A/B testing to compare the results from each table, after which your brand can use the audience that works best for your campaigns.

.. paid-media-admonition-about-end



.. vale off

**What type of profile to send?** (segments / campaigns)

.. vale on

.. paid-media-ampiq-about-start

Amperity provides the right set of data to support your brand's paid media advertising from two tables, both of which contain customer profile data.

* The **Merged Customers** table contains your customers' best profiles, such as their best email address, best phone number, and best physical address.
* The **Unified Paid Media** table contains your customers complete profile, including all known email addresses, all known phone numbers, and all known physical addresses.

Your brand can send data from one or both of these tables to any paid media advertising application. You can configure the |campaign_default_attributes| for each data set from the **Campaigns** page.

The table your brand uses to send data will affect your brand's downstream match rates *and* overall customer matches within your |paid_media|. The decision behind which table to use depends on your brand's downstream use case and the type and amount of customer profile data your brand wants to use to match customers.

You brand should expect to see higher |paid_media_match_rates| when sending audiences from the **Merged Customers** table, but a higher number of matched customer profiles when sending audiences from the **Unified Paid Media** table. Use A/B testing to compare the results from each table, after which your brand can use the audience that works best for your campaigns.

.. paid-media-ampiq-about-end


