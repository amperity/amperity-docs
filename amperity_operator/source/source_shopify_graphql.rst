.. https://docs.amperity.com/operator/


.. |source-name| replace:: Shopify (GraphQL)
.. |plugin-name| replace:: Shopify (GraphQL)
.. |credential-type| replace:: **shopify**
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: customer, order, product, and location data
.. |credential-fields| replace:: the name of the credential, a description, and the |source-name| **Shop name** and **Access token**


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Shopify (GraphQL).

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Shopify (GraphQL).

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Shopify (GraphQL)

==================================================
Pull from Shopify (GraphQL)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-shopify-start
   :end-before: .. term-shopify-end

.. source-shopify-graphql-context-start

|source-name| pulls |what-pull| into Amperity using the `Shopify GraphQL Admin API <https://shopify.dev/docs/api/admin-graphql>`__ |ext_link|. It reads the same Shopify store as the REST-based Shopify source and can run alongside it.

Select the data types to pull. Amperity creates a feed and a domain table for each selected data type. Each courier run reads records that were updated within the run's time range; because Shopify sets the updated timestamp when a record is created, records that are new to the store are included as well. Location records are the exception -- Shopify does not filter locations by an updated timestamp, so every location is read on each run.

.. source-shopify-graphql-context-end

.. source-shopify-graphql-beta-start

.. admonition:: Beta

   The |source-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. source-shopify-graphql-beta-end

.. source-shopify-graphql-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-shopify-graphql-get-details>`
#. :ref:`Add courier <source-shopify-graphql-add-courier>`
#. :ref:`Run courier <source-shopify-graphql-run-courier>`
#. :ref:`Review feed and domain table <source-shopify-graphql-review-data>`
#. :ref:`Add to courier group <source-shopify-graphql-add-to-courier-group>`

.. source-shopify-graphql-steps-to-pull-end


.. _source-shopify-graphql-get-details:

Get details
==================================================

.. source-shopify-graphql-get-details-start

|source-name| requires the following configuration details:

#. The **Shop name** and **Access token** for |source-name|.

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-shopify-find-credentials-start
      :end-before: .. credential-shopify-find-credentials-end

#. The data types to pull. You can select any combination of the following:

   * **customer**, **customer-address**, **customer-metafield**, and **customer-tags**
   * **order**, **order-line**, **order-line-refund**, **order-tags**, **discount-allocation**, and **discount-codes**
   * **product**, **product-tags**, and **product-variant**
   * **locations**

#. The **Ingest strategy** (optional) that controls how Amperity reads from Shopify:

   * **auto** (the default) runs a bulk export for a full historical load and paginated queries for a run that is bounded to a time range.
   * **bulk** forces a bulk export, which is worth doing for a bounded but very large backfill.
   * **paginated** forces paginated queries.

   The **order-line-refund** data type cannot be exported in bulk. Under **auto** it is read with paginated queries automatically; when the **Ingest strategy** is set to **bulk** and **order-line-refund** is selected, the run stops with an error.

.. note:: On the paginated strategy, a parent record that has more than 250 related child records -- for example, an order with more than 250 line items, or a customer with more than 250 addresses or metafields -- has the additional child records truncated. A bulk export has no such limit. Under **auto**, a run that is bounded to a time range uses the paginated strategy, so use **bulk** to read a parent that has a very large number of child records.

.. tip:: Use |ext_snappass| to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-shopify-graphql-get-details-end


.. _source-shopify-graphql-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-shopify-graphql-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".

   From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.

   When finished click **Continue**.

#. Under **Data types**, select the data types to pull to Amperity.
#. Optionally, set the **Ingest strategy**.
#. Click **Create**.

   Amperity creates a feed and a domain table for each selected data type.

.. source-shopify-graphql-add-courier-end


.. _source-shopify-graphql-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-shopify-graphql-review-data:

Review feed and domain table
==================================================

.. source-shopify-graphql-review-data-start

After running the |source-name| courier, a feed and domain table are created automatically for each data type that you selected. You may apply semantic tags to the fields in these tables and you may make a domain table available to Stitch, depending on your use case.

The data types cover the following areas of your Shopify store:

* **Customers** -- customer records and their addresses, metafields, and tags.
* **Orders** -- orders and their line items, refunded line items, tags, discount codes, and discount allocations.
* **Products** -- products and their variants and tags.
* **Locations** -- store locations.

The columns in each domain table mirror the corresponding table from the REST-based Shopify source, with some differences in coverage between the two connectors. Contact your Amperity representative for details about specific columns.

.. source-shopify-graphql-review-data-end


.. _source-shopify-graphql-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
