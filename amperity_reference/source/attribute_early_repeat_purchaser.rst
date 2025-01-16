.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        What percentage of first-time buyers returned to make a second purchase within 90 days?

.. meta::
    :content class=swiftype name=body data-type=text:
        What percentage of first-time buyers returned to make a second purchase within 90 days?

.. meta::
    :content class=swiftype name=title data-type=string:
        Early repeat purchaser

==================================================
Early repeat purchaser
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-early-repeat-purchasers-start
   :end-before: .. term-early-repeat-purchasers-end

.. attribute-early-repeat-purchaser-start

Use the **Early Repeat Purchaser** attribute to build segments that support campaigns that turn one-time buyers into repeat customers. Compare your one-time buyers with early repeat purchasers. Move customers who have made a repeat purchase within 90 days out of your one-time buyer campaign and into other campaigns.

.. attribute-early-repeat-purchaser-end

.. attribute-early-repeat-purchaser-tip-start

.. tip:: A one-time buyer could, in theory, make their elusive second purchase 60 days or 600 days after their first purchase. For early repeat purchaser to be a useful metric you cannot wait 600 days. Amperity defaults to 90 days; many customers choose to use a shorter time window.

   To use a shorter time window, update the **Transaction Attributes Extended** table for your preferred value. For example, to use 60 days as the definition for an early repeat purchaser, change the current value to **60**:

   .. code-block:: sql

      CASE
        WHEN DATE_DIFF(attrs.second_order_datetime, attrs.first_order_datetime) <= 60 THEN true
        WHEN DATE_DIFF(attrs.second_order_datetime, attrs.first_order_datetime) > 60 THEN false
        WHEN DATE_DIFF(CURRENT_DATE(), attrs.first_order_datetime) > 60 THEN false
      END AS `early_repeat_purchaser`

.. attribute-early-repeat-purchaser-tip-end


.. _attribute-early-repeat-purchaser-segment:

Use in segments
==================================================

.. attribute-early-repeat-purchaser-segment-start

To find early repeat purchasers, start with the **Early Repeat Purchaser** attribute, and then set its condition to **is true**.

.. attribute-early-repeat-purchaser-segment-end


.. _attribute-early-repeat-purchaser-conditions:

Available operators
==================================================

.. attribute-early-repeat-purchaser-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a Boolean data type. All Boolean data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is false**
     - |attribute-recommended| **More useful**

       Filters your segment to contain customers who have not made a second purchase within the timeframe that defines an early repeat purchaser. By default this timeframe is "within 90 days".

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

   * - **is true**
     - |attribute-recommended| **More useful**

       Filters your segment to contain customers who have made a second purchase within the timeframe that defines an early repeat purchaser. By default this timeframe is "within 90 days".

.. attribute-early-repeat-purchaser-conditions-end
