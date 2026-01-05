.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Incentivize customers to use their loyalty points for discounts and rewards.

.. meta::
    :content class=swiftype name=body data-type=text:
        Incentivize customers to use their loyalty points for discounts and rewards.

.. meta::
    :content class=swiftype name=title data-type=string:
        Loyalty spend

==================================================
Loyalty spend
==================================================

.. attribute-loyalty-spend-overview-start

Brands can incentivize customers to spend more with their brands through personalized discounts, loyalty tiers, and rewards.

.. attribute-loyalty-spend-overview-end


.. _attribute-loyalty-spend-attributes:

Loyalty spend attributes
==================================================

.. attribute-loyalty-spend-attributes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-loyalty-spend-start
   :end-before: .. term-loyalty-spend-end

Amperity provides the following attributes that your brand can use to build audiences around the amount customers spend to remain in or move to the next loyalty tier.

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Attribute
     - Description
   * - **Spend To Keep Tier**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-balance-start
          :end-before: .. loyalty-current-balance-end

   * - **Spend To Next Tier**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-spend-to-next-tier-start
          :end-before: .. loyalty-spend-to-next-tier-end

.. attribute-loyalty-spend-attributes-end


.. _attribute-loyalty-spend-segment:

Use in segments
==================================================

.. attribute-loyalty-spend-access-attribute-start

You can access loyalty spend attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Loyalty** table, and then add the combination of loyalty spend attributes you want to use in your segment. Apply operators and specify values for each attribute as necessary.

.. attribute-loyalty-spend-access-attribute-end


.. _attribute-loyalty-spend-conditions:

Available operators
==================================================

.. attribute-loyalty-spend-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have an **decimal** data type. All **decimal** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Returns the specified amount.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns customer records with loyalty spend made within a defined start and end date.

   * - **is greater than**
     - Returns customer records with values that are greater than the amount of loyalty spend.

   * - **is greater than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with a purchase amount that is greater than or equal to the amount needed to stay in a loyalty tier.

   * - **is less than**
     - |attribute-recommended| **More useful**

       Returns customer records with a purchase amount that is just below the next loyalty tier.

   * - **is less than or equal to**
     - |attribute-recommended| **More useful**

       Returns customer records with purchase amounts that are less than or equal to the amount just below the next loyalty tier.

   * - **is not**
     - |attribute-recommended| **More useful**

       Returns an audience that is associated with a specified purchase amount.

   * - **is not between**
     - Returns customers purchases made outside of a defined start and end date.

   * - **is not NULL**
     - Returns customer records that are associated with the purchase amount necessary to stay in a loyalty tier or move up to the next tier.

   * - **is NULL**
     - |attribute-stop| **Less useful**
       
       Returns customer records that are not associated with the purchase amount necessary to stay in a loyalty tier or move up to the next tier.

.. attribute-loyalty-spend-conditions-end
