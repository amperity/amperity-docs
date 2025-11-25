.. https://docs.amperity.com/user/


.. |destination-name| replace:: Dynamic Yield
.. |plugin-name| replace:: Amazon S3
.. |what-send| replace:: CSV files


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Dynamic Yield.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Dynamic Yield.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Dynamic Yield

==================================================
Send query results to Dynamic Yield
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dynamic-yield-start
   :end-before: .. term-dynamic-yield-end

.. sendto-dynamic-yield-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-dynamic-yield-build-query>`
#. :ref:`Add orchestration <sendto-dynamic-yield-add-orchestration>`
#. :ref:`Run orchestration <sendto-dynamic-yield-run-orchestration>`

.. sendto-dynamic-yield-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-dynamic-yield-build-query:

Build query
==================================================

.. sendto-dynamic-yield-build-query-start

Build a query that shapes the data so that fields in the output are mapped to the fields required by |destination-name|. Data shaping is typically required only one time. For example:

.. code-block:: sql
   :linenos:

   SELECT
     product_id AS sku
     ,other_product_id AS group_id
     ,product_name AS name
     ,product_url AS url
     ,product_price AS price
     ,product_available AS in_stock
     ,product_image AS image_url
     ,product_category AS categories
     ,product_more_info AS keywords
   FROM Your_Product_Catalog_Table

.. important:: The results of this query must match the product feed structure, which requires case-sensitive columns:

   #. **sku**. Required. A product's unique ID. Values cannot contain spaces or "//" (double backslashes). For example: "1234".
   #. **group_id**. Required. An identifier for a group of products with different product attributes. For example: "4321".
   #. **name**. Required. The name of the product. For example: "t-shirt".
   #. **url**. Required. A valid URL of a product. For example: ``https://store.com/product_page.html``.
   #. **price**. Required. The price of a product. For example: "9.99".
   #. **in_stock**. Required. Indicates if the product is in stock. For example: "true".
   #. **image_url**. Required. A valid URL of a product's image. For example: ``https://store.com/images/image.png``.
   #. **categories**. Required. The categories associated with a product.
   #. **keywords**. Optional. Additional information that describes a product.

   Refer to |destination-name| documentation for more information about these fields and their requirements.

.. sendto-dynamic-yield-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-dynamic-yield-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-dynamic-yield-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
