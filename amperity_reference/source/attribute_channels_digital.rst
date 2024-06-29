.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        Through which channel was a digital purchase made?

.. meta::
    :content class=swiftype name=body data-type=text:
        Through which channel was a digital purchase made?

.. meta::
    :content class=swiftype name=title data-type=string:
        Digital channels

==================================================
Digital channels
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-digital-channel-start
   :end-before: .. term-digital-channel-end


.. _attribute-channels-digital-segment:

Use in segments
==================================================

.. attribute-channels-digital-start

You can access digital channels directly from the **Segment Editor**. To add this attribute to your segment, click **Add criteria**, select the **Unified Transactions** table, select the **Digital Channel** attribute, apply a condition, and then specify a value.

For example, if your tenant had digital channels defined for "Email", "Paid media", "Paid search", "SMS", and "Streaming" the list of options would be:

.. attribute-channels-digital-end


.. _attribute-channels-digital-conditions:

Available conditions
==================================================

.. attribute-channels-digital-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description

   * - **contains**
     - |attribute-recommended| **More useful**

       Returns customer records with values that match a string of characters.

   * - **does not contain**
     - Returns customer records with values that do not match a string of characters.

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

.. attribute-channels-digital-conditions-end
