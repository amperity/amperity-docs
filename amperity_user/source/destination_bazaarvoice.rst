.. https://docs.amperity.com/user/


.. |destination-name| replace:: Bazaarvoice
.. |what-send| replace:: CSV, TSV, or PSV files
.. |sftp-type| replace:: **sftp**
.. |sftp-hostname| replace:: **sftp.bazaarvoice.com**
.. |file-format| replace:: CSV, TSV, or PSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Bazaarvoice.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Bazaarvoice.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Bazaarvoice

==================================================
Send query results to Bazaarvoice
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bazaarvoice-start
   :end-before: .. term-bazaarvoice-end

.. sendto-bazaarvoice-start

You can send data about brands, product categories, and products to support features that are powered by the product catalog in |destination-name|, such as:

* Updating the product catalog
* Supporting downstream syndication of user-generated content based on product matches
* Identifying content for post-interaction email (PIE) messages
* Integrating with other downstream workflows

.. sendto-bazaarvoice-end

.. sendto-bazaarvoice-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-bazaarvoice-build-query>`
#. :ref:`Add orchestration <sendto-bazaarvoice-add-orchestration>`
#. :ref:`Run orchestration <sendto-bazaarvoice-run-orchestration>`

.. sendto-bazaarvoice-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-bazaarvoice-build-query:

Build query
==================================================

.. sendto-bazaarvoice-build-query-start

You must build a query that shapes the data so that fields in the output are mapped to the fields required by |destination-name|. Data shaping is typically required only one time.

You can do this in the following ways:

#. Use |sql_spark| to add a SQL table to the customer 360 database that selects PII fields from the **Customer 360** table, and then outputs them to a table with columns that map to the required naming patterns.

   .. note:: PII fields may require |sql_spark_one_way_hash| or conversion to a UUID using the |sql_spark_cast| function.

#. Use |sql_presto| to add a SQL query that filters within the query, and then outputs results that map to the required patterns.

   .. note:: PII fields may require |sql_presto_one_way_hash| or conversion to a UUID using the |sql_presto_cast| function.

The correct approach here depends on the data and the desired use cases for downstream workflows.

.. sendto-bazaarvoice-build-query-end


.. _sendto-bazaarvoice-build-query-pii:

Bazaarvoice and PII data
--------------------------------------------------

.. sendto-bazaarvoice-build-query-pii-start

|destination-name| recommends to not include PII data.

.. sendto-bazaarvoice-build-query-pii-end


.. _sendto-bazaarvoice-build-query-map-to-product-catalog:

Map to product catalog
--------------------------------------------------

.. sendto-bazaarvoice-build-query-map-to-product-catalog-start

A SQL query can return results for use with the product catalog in Bazaarvoice. Add a SQL table with a **SELECT** statement similar to:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS ExternalId
     ,product_name AS Name
     ,product_description AS Description
     ,product_brand AS Brand
     ,product_id AS BrandExternalId
     ,product_category_name AS Category
     ,product_base_id AS CategoryExternalId
     ,product_url AS ProductUrl
     ,image_url AS ImageUrl
   FROM customer360
   LIMIT 2000

and then assign this query to a destination that sends results to |destination-name|.

.. sendto-bazaarvoice-build-query-map-to-product-catalog-end

.. sendto-bazaarvoice-build-query-map-to-product-catalog-note-start

.. note:: When building this query:

   * Do not include instances of a delimiter, such as commas, pipes, or tabs, within the field values, such as **Name** or **Description**.
   * Do not use double-quotes around field values.
   * Avoid including leading and trailing spaces in field values because they will be included with the value when stored in the |destination-name| database.

   Refer to `product catalog <https://docs.bazaarvoice.com/articles/vibe/upload-a-product-catalog-file>`__ |ext_link| for additional details.

.. sendto-bazaarvoice-build-query-map-to-product-catalog-note-end

.. sendto-bazaarvoice-build-query-map-to-product-catalog-important-start

.. important:: |destination-name| requires the **ExternalId**, **ProductUrl**, and **ImageURL** fields to be in the results. The **Brand**, **BrandExternalId**, **Category**, and **CategoryExternalId** fields are recommended. Refer to the `column definitions <https://docs.bazaarvoice.com/articles/ratings-reviews/text_feed>`__ |ext_link| for complete details.

.. sendto-bazaarvoice-build-query-map-to-product-catalog-important-end


.. _sendto-bazaarvoice-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. sendto-bazaarvoice-add-orchestration-important-start

.. important:: Sending data to |destination-name| should follow recommendations for the `product catalog <https://docs.bazaarvoice.com/articles/vibe/upload-a-product-catalog-file>`__ |ext_link|. |destination-name| supports the following `file formats <https://docs.bazaarvoice.com/articles/ratings-reviews-legacy-prr/product_feeds>`__ |ext_link|:

   * CSV
   * PSV
   * TSV

   Use a single file for each product catalog to which Amperity will send data.

   Enable the **Include header row in output files** option for the Amperity destination.

.. sendto-bazaarvoice-add-orchestration-important-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-bazaarvoice-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
