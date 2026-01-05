.. https://docs.amperity.com/reference/


.. |what-access| replace:: product catalog attributes
.. |what-choose| replace:: a product catalog
.. |what-find| replace:: "product"


.. meta::
    :description lang=en:
        The brands, categories, and sub-categories that define a product catalog.

.. meta::
    :content class=swiftype name=body data-type=text:
        The brands, categories, and sub-categories that define a product catalog.

.. meta::
    :content class=swiftype name=title data-type=string:
        Product catalogs

==================================================
Product catalogs
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-product-catalog-start
   :end-before: .. term-product-catalog-end

.. attribute-product-important-start

.. important:: A product catalog is most often available from the **Unified Itemized Transactions** table, but may also be available from other tables in your database.

   Items in your product catalog are semantically tagged in the data sources that were made available to Amperity, after which it is available from the **Unified Itemized Transactions** table.

.. attribute-product-important-end


.. _attribute-product-category-segment:

Use in segments
==================================================

.. attribute-product-category-segment-start

You can access product catalog attributes directly from the **Segment Editor**. To add these attributes to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Itemized Transactions** table, select one of your product catalog attributes, apply a condition, and then specify a value.

.. attribute-product-category-segment-end


.. _attribute-product-category-conditions:

Available operators
==================================================

.. attribute-product-category-conditions-start

The following table lists the operators that are available to product catalog attributes.

.. note:: Product catalog attributes have a **string** data type. All **string** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description

   * - **contains**
     - |attribute-recommended| **More useful**

       Returns customer records with values that match a string of characters.

       For example: a list that specifies "shorts" and "shoes" will return customers who have purchased "shorts" and "shoes", but not "pants" or "socks".

   * - **does not contain**
     - Returns customer records with values that do not match a string of characters.

       For example:

       * A list that specifies "shorts" and "shoes" will return customers who have purchased "pants" or "socks", but not "shorts" and "shoes".
       * "sh" will return "pants" and "socks", but not "shirts" or "shorts".

   * - **ends with**
     - Returns customer records with values that end with the specified characters.

   * - **is empty**
     - |attribute-stop| **Less useful**

       Returns customer records that do not have a value in this field.

   * - **is exactly**
     - |attribute-recommended| **More useful**

       Returns all customer records with values that match the specified characters.

       For example, "shorts" will return "shorts" and not "pants", "shirts", or "socks".

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

       For example: "shorts" will return "pants", "shirts", and "socks".

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-product-category-conditions-end
