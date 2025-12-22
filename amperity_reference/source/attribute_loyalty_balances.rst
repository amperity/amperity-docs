.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Point-based loyalty programs provide reward points to their members, which can be accrued based on money spent in a loyalty balance.

.. meta::
    :content class=swiftype name=body data-type=text:
        Point-based loyalty programs provide reward points to their members, which can be accrued based on money spent in a loyalty balance.

.. meta::
    :content class=swiftype name=title data-type=string:
        Loyalty balances

==================================================
Loyalty balances
==================================================

.. attribute-loyalty-balances-overview-start

Point-based loyalty programs provide reward points to their members, which can be accrued based on money spent in a loyalty balance.

.. attribute-loyalty-balances-overview-end


.. _attribute-loyalty-balances-attributes:

Loyalty balance attributes
==================================================

.. attribute-loyalty-balances-attributes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-loyalty-balances-start
   :end-before: .. term-loyalty-balances-end

Amperity provides the following attributes that your brand can use to build audiences around customer loyalty reward points balance thresholds:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Attribute
     - Description
   * - **Current Balance**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-balance-start
          :end-before: .. loyalty-current-balance-end

   * - **Lifetime Balance**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-lifetime-balance-start
          :end-before: .. loyalty-lifetime-balance-end

       For example, to return an audience customer records with a low lifetime reward points balance that brands can include in a discounts campaign to intice at-risk customers to make more purchases with their brand.

.. attribute-loyalty-balances-attributes-end


.. _attribute-loyalty-balances-segment:

Use in segments
==================================================

.. attribute-loyalty-balances-access-attributes-start

You can access loyalty balance attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Loyalty** table, and then add the combination of loyalty balance attributes you want to use in your segment. Apply operators and specify values for each attribute as necessary.

.. attribute-loyalty-balances-overview-end


.. _attribute-loyalty-balances-conditions:

Available operators
==================================================

.. attribute-loyalty-balances-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have an **integer** data type. All **integer** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description

   * - **contains**
     - Returns customer records with values that match a string of characters.

   * - **does not contain**
     - Returns customer records with values that do not match a string of characters.

   * - **ends with**
     - Returns customer records with values that end with the specified characters.

   * - **is empty**
     - Returns customer records that do not have a value in this field.

   * - **is exactly**
     - Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-loyalty-balances-conditions-end
