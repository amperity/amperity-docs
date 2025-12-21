.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Loyalty tiers incentivize customers to increase their interactions with your brand.

.. meta::
    :content class=swiftype name=body data-type=text:
        Loyalty tiers incentivize customers to increase their interactions with your brand.

.. meta::
    :content class=swiftype name=title data-type=string:
        Loyalty tiers

==================================================
Loyalty tiers
==================================================

.. attribute-loyalty-tiers-overview-start

Loyalty tiers exist within loyalty programs to incentivize customers to interact more with a brand. For example, a loyalty program may provide customers incentives to buy more products to move up to the next loyalty tier.

.. attribute-loyalty-tiers-overview-end


.. _attribute-loyalty-tiers-attributes:

Loyalty tier attributes
==================================================

.. attribute-loyalty-tiers-attributes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-loyalty-tiers-start
   :end-before: .. term-loyalty-tiers-end

Amperity provides the following attributes that your brand can use to build audiences around loyalty tiers within your loyalty programs:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Attribute
     - Description
   * - **Current Tier**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-tier-start
          :end-before: .. loyalty-current-tier-end

       .. tip:: Combine this attribute with the **Spend to Keep Tier** to build audiences for campaigns that encourage your customers to take steps to remain in their current tier.

   * - **Next Tier**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-next-tier-start
          :end-before: .. loyalty-next-tier-end

       .. tip:: Combine this attribute with the **Spend to Next Tier** to build audiences to include in a campaign that encourages your customers to take steps to move to the next tier.

   * - **Sign-up Channel**, **Sign-up Method**
     - Use the **Sign-up Channel** and **Sign-up Method** attributes to filter customers who belong to your brand's loyalty program.

       For example, to build audiences for customers who signed up for your loyalty program in-store or online or joined your loyalty program using their email address or phone number.

.. attribute-loyalty-tiers-attributes-end


.. _attribute-loyalty-tiers-segment:

Use in segments
==================================================

.. attribute-loyalty-tiers-attributes-start

You can access loyalty tier attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Loyalty** table, and then add the combination of loyalty tier attributes you want to use in your segment. Apply operators and specify values for each attribute as necessary.

.. attribute-loyalty-tiers-attributes-end


.. _attribute-loyalty-tiers-conditions:

Available operators
==================================================

.. attribute-loyalty-tiers-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a **string** data type. All **string** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description

   * - **contains**
     - |attribute-recommended| **More useful**

       Returns customer records with values that match a string of characters.

   * - **does not contain**
     - |attribute-recommended| **More useful**

       Returns customer records with values that do not match a string of characters.

   * - **ends with**
     - Returns customer records with values that end with the specified characters.

   * - **is empty**
     - Returns customer records that do not have a value in this field.

   * - **is exactly**
     - |attribute-recommended| **More useful**

       Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-loyalty-tiers-conditions-end
