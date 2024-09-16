.. 
.. https://docs.amperity.com/ampiq/
.. 


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

.. attribute-multibrand-access-start

You can access multi-brand purchases directly from the **Segment Editor**. To add this attribute to your segment, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source, select the **Multi Purchase Brand** attribute, and then apply a condition.

.. attribute-multibrand-access-end


.. _attribute-multibrand-conditions:

Available conditions
==================================================

.. attribute-multibrand-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
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
