.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        How large of an audience is required to grow revenue over the next 30 days? 

.. meta::
    :content class=swiftype name=body data-type=text:
        How large of an audience is required to grow revenue over the next 30 days?

.. meta::
    :content class=swiftype name=title data-type=string:
        Audience sizes

==================================================
Audience sizes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-recommended-audience-size-start
   :end-before: .. term-recommended-audience-size-end

.. attribute-audience-sizes-start

Audience size attributes include:

* :ref:`Large audience sizes <attribute-audience-sizes-large>`
* :ref:`Medium audience sizes <attribute-audience-sizes-medium>`
* :ref:`Small audience sizes <attribute-audience-sizes-small>`

.. attribute-audience-sizes-end

.. include:: ../../amperity_reference/source/model_product_affinity.rst
   :start-after: .. model-product-affinity-recommended-audiences-usecase-start
   :end-before: .. model-product-affinity-recommended-audiences-usecase-end

.. include:: ../../amperity_reference/source/model_product_affinity.rst
   :start-after: .. model-product-affinity-use-cases-recommended-audiences-about-start
   :end-before: .. model-product-affinity-use-cases-recommended-audiences-about-end

.. important::

   .. include:: ../../amperity_user/source/recommended_audiences.rst
      :start-after: .. recommended-audience-sizes-low-purchase-frequencies-start
      :end-before: .. recommended-audience-sizes-low-purchase-frequencies-end


.. _attribute-audience-sizes-purchase-curve:

About the purchase curve
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-purchase-curve-start
   :end-before: .. term-purchase-curve-end

.. include:: ../../amperity_user/source/recommended_audiences.rst
   :start-after: .. recommended-audiences-purchase-curve-about-start
   :end-before: .. recommended-audiences-purchase-curve-about-end

.. image:: ../../images/use-cases-recommended-audience-size-all.png
   :width: 600 px
   :alt: All audience sizes and the purchase curve.
   :align: left
   :class: no-scaled-link

.. include:: ../../amperity_user/source/recommended_audiences.rst
   :start-after: .. recommended-audiences-purchase-curve-context-start
   :end-before: .. recommended-audiences-purchase-curve-context-end


.. _attribute-audience-sizes-large:

Large audience sizes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-audience-size-large-start
   :end-before: .. term-audience-size-large-end

.. image:: ../../images/use-cases-recommended-audience-size-large.png
   :width: 600 px
   :alt: A large audience size.
   :align: left
   :class: no-scaled-link

.. attribute-audience-sizes-large-start

To find large audience sizes, start with the **Audience Size Large** attribute in the **Predicted Affinity** table, and then set its condition to **is true**.

.. attribute-audience-sizes-large-end

.. attribute-audience-sizes-large-combine-with-product-start

.. important:: Combine **Audience Size Large** attribute with the **Product Attribute** attribute to build an audience size for the selected product attribute. 

.. attribute-audience-sizes-large-combine-with-product-end


.. _attribute-audience-sizes-medium:

Medium audience sizes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-audience-size-medium-start
   :end-before: .. term-audience-size-medium-end

.. image:: ../../images/use-cases-recommended-audience-size-medium.png
   :width: 600 px
   :alt: A medium audience size.
   :align: left
   :class: no-scaled-link

.. attribute-audience-sizes-medium-start

To find medium audience sizes, start with the **Audience Size Medium** attribute in the **Predicted Affinity** table, and then set its condition to **is true**.

.. attribute-audience-sizes-medium-end

.. attribute-audience-sizes-medium-combine-with-product-start

.. important:: Combine **Audience Size Medium** attribute with the **Product Attribute** attribute to build an audience size for the selected product attribute. 

.. attribute-audience-sizes-medium-combine-with-product-end


.. _attribute-audience-sizes-small:

Small audience sizes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-audience-size-small-start
   :end-before: .. term-audience-size-small-end

.. image:: ../../images/use-cases-recommended-audience-size-small.png
   :width: 600 px
   :alt: A small audience size.
   :align: left
   :class: no-scaled-link

.. attribute-audience-sizes-small-start

To find small audience sizes, start with the **Audience Size Small** attribute in the **Predicted Affinity** table, and then set its condition to **is true**.

.. attribute-audience-sizes-small-end

.. attribute-audience-sizes-small-combine-with-product-start

.. important:: Combine **Audience Size Small** attribute with the **Product Attribute** attribute to build an audience size for the selected product attribute. 

.. attribute-audience-sizes-small-combine-with-product-end


.. _attribute-audience-sizes-conditions:

Available operators
==================================================

.. attribute-audience-sizes-conditions-start

The following table lists the operators that are available to audience size attributes.

.. note:: These attributes have a Boolean data type. All Boolean data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Returns a list of customers who do not belong to the specified audience size.

   * - **is not NULL**
     - Returns a list of customers who belong to all audience sizes.

   * - **is NULL**
     - Returns a list of customers who do not belong to any audience size.

   * - **is true**
     - |attribute-recommended| **More useful**

       Returns a list of customers who belong to the specified audience size.

.. attribute-audience-sizes-conditions-end
