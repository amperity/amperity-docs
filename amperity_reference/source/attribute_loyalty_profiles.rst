.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A loyalty profile is a collection of personally identifiable information (PII) that uniquely identifies each member of your loyalty program.

.. meta::
    :content class=swiftype name=body data-type=text:
        A loyalty profile is a collection of personally identifiable information (PII) that uniquely identifies each member of your loyalty program.

.. meta::
    :content class=swiftype name=title data-type=string:
        Loyalty profiles

==================================================
Loyalty profiles
==================================================

.. attribute-loyalty-profiles-overview-start

Loyalty programs help brands increase customer loyalty and provide incentives for customers to continue to interact with brands. Loyalty programs may require their members to provide their PII, which is used by companies to offer more personalized incentives to their customers.

.. attribute-loyalty-profiles-overview-end

.. attribute-loyalty-profiles-links-start

Amperity provides the following attributes to build audiences that help brands better understand how to bring more value to their customers through their loyalty program:

* :doc:`Loyalty balances <attribute_loyalty_balances>`
* :doc:`Loyalty membership <attribute_loyalty_membership>`
* :doc:`Loyalty profiles <attribute_loyalty_profiles>`
* :doc:`Loyalty spend <attribute_loyalty_spend>`
* :doc:`Loyalty tiers <attribute_loyalty_tiers>`

.. attribute-loyalty-profiles-links-end


.. _attribute-loyalty-profiles-segment:

Loyalty profile attributes
==================================================

.. attribute-loyalty-profiles-attributes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-loyalty-profiles-start
   :end-before: .. term-loyalty-profiles-end

Amperity provides the following attributes that your brand can use to build audiences around customer PII:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Attribute
     - Description
   * - **Loyalty ID**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-id-start
          :end-before: .. loyalty-id-end

   * - **Email**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-email-start
          :end-before: .. loyalty-email-end

   * - **Birthdate**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-birthdate-start
          :end-before: .. loyalty-birthdate-end

       For example, to build an audience with upcoming birthdays to include in a birthday campaign.

.. attribute-loyalty-profiles-attributes-end


.. _attribute-loyalty-profiles-access-attributes:

Use in segments
==================================================

.. attribute-loyalty-profiles-access-attributes-start

You can access loyalty profile attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Unified Loyalty** table, and then add the combination of loyalty profile attributes you want to use in your segment. Apply operators and specify values for each attribute as necessary.

.. attribute-loyalty-profiles-access-attributes-end


.. _attribut-loyalty-profiles-conditions:

Available operators
==================================================

.. attribute-loyalty-profiles-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a String data type. All String data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

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

.. attribute-loyalty-profiles-conditions-end
