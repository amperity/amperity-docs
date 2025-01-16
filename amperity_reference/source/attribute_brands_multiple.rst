.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **multi-brand purchases** attribute
.. |what-choose| replace:: **multi-brand purchases**
.. |what-find| replace:: "multi-brand"


.. meta::
    :description lang=en:
        Which customers purchased from more than one brand?

.. meta::
    :content class=swiftype name=body data-type=text:
        Which customers purchased from more than one brand?

.. meta::
    :content class=swiftype name=title data-type=string:
        Multi-brand purchases?

==================================================
Multi-brand purchases?
==================================================

.. attribute-multibrand-start

Use the **multi-brand purchases** attribute to build segments that support campaigns that focus on customers who have purchased from more than one of your brands.

.. attribute-multibrand-end


.. _attribute-multibrand-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-multibrand-conditions:

Available operators
==================================================

.. attribute-multibrand-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Filters your segment to include only customers who have not purchased from more than one of your brands.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

   * - **is true**
     - |attribute-recommended| **More useful**

       Filters your segment to include only customers who have purchased from more than one of your brands.

.. attribute-multibrand-conditions-end
