.. 
.. https://docs.amperity.com/ampiq/
.. 


.. meta::
    :description lang=en:
        Customers become members of your loyalty program to earn points for discounts and rewards.

.. meta::
    :content class=swiftype name=body data-type=text:
        Customers become members of your loyalty program to earn points for discounts and rewards.

.. meta::
    :content class=swiftype name=title data-type=string:
        Loyalty membership

==================================================
Loyalty membership
==================================================

.. attribute-loyalty-membership-overview-start

Loyalty programs help brands increase customer loyalty and provide incentives for customers to continue to interact with brands. Through offering their customers membership in loyalty programs, companies can further incentivize customers to interact more with their brand by providing more personalized rewards and discounts.

.. attribute-loyalty-membership-overview-end

.. attribute-loyalty-membership-links-start

Amperity provides the following attributes to build audiences that help brands better understand how to bring more value to their customers through their loyalty program:

* :doc:`Loyalty balances <attribute_loyalty_balances>`
* :doc:`Loyalty membership <attribute_loyalty_membership>`
* :doc:`Loyalty profiles <attribute_loyalty_profiles>`
* :doc:`Loyalty spend <attribute_loyalty_spend>`
* :doc:`Loyalty tiers <attribute_loyalty_tiers>`

.. attribute-loyalty-membership-links-end


.. _attribute-loyalty-membership-attributes:

Loyalty membership attributes
==================================================

.. attribute-loyalty-membership-attributes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-loyalty-membership-start
   :end-before: .. term-loyalty-membership-end

Amperity provides the following attributes that your brand can use to build audiences around customer interaction with your loyalty program:

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Attribute
     - Description
   * - **Current Balance Expiration Datetime**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-balance-expiration-datetime-start
          :end-before: .. loyalty-current-balance-expiration-datetime-end

   * - **Current Tier Expiration Datetime**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-tier-expiration-datetime-start
          :end-before: .. loyalty-current-tier-expiration-datetime-end

   * - **Current Tier Start Datetime**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-current-tier-start-datetime-start
          :end-before: .. loyalty-current-tier-start-datetime-end

   * - **Is Opted In**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-is-opted-in-start
          :end-before: .. loyalty-is-opted-in-end

       .. tip:: Set the condition for this attribute to **is true** to return an audience with filtered out opted out customers.

   * - **Latest Opted Out Datetime**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-latest-opt-out-datetime-start
          :end-before: .. loyalty-latest-opt-out-datetime-end

   * - **Latest Opted In Datetime**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-latest-opted-in-datetime-start
          :end-before: .. loyalty-latest-opted-in-datetime-end

   * - **Latest Update Datetime**
     - .. include:: ../../shared/loyalty-events.rst
          :start-after: .. loyalty-latest-update-datetime-start
          :end-before: .. loyalty-latest-update-datetime-end

.. attribute-loyalty-membership-attributes-end


.. _attribute-loyalty-membership-segment:

Use in segments
==================================================

.. attribute-loyalty-membership-access-attributes-start

You can access loyalty membership attributes directly from the **Segment Editor**. To add these attributes to your segments, click **Add criteria**, select the **Unified Loyalty** table, and then add the combination of loyalty membership attributes you want to use in your segment. Apply conditions and specify values for each attribute as necessary.

.. attribute-loyalty-membership-access-attributes-end


.. _attribute-loyalty-membership-conditions:

Available conditions
==================================================

.. attribute-loyalty-membership-conditions-start

The following table lists the conditions that are available to these attributes.

.. note:: These attributes have a Datetime data type. All Datetime data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description
   * - **is**
     - |attribute-stop| **Less useful**

       Avoid using the **is** condition with these loyalty membership attributes unless you intend to use a specific date, such as "2022-08-22" ("yyyy-mm-dd").

   * - **is after**
     - Returns all dates that occur after the selected calendar date, excluding the selected calendar date.

   * - **is before**
     - |attribute-recommended| **More useful**

       Returns all dates that occur before the selected date, excluding the selected date.

       .. tip:: Use the **Current Balance Expiration Datetime**, **Current Tier Expiration Datetime**, **Latest Opted Out Datetime**, **Latest Opted In Datetime**, and **Current Tier Start Datetime** attributes with this condition to return audiences based on the selected date.

          For example, the **Current Tier Expiration Datetime** attribute returns an audience based on the selected date before which a customer’s membership in their current rewards tier will end.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns dates that exist within a defined start and end date.

       .. tip:: Use the **Current Balance Expiration Datetime**, **Current Tier Expiration Datetime**, **Latest Opted Out Datetime**, **Latest Opted In Datetime**, **Latest Update Datetime**, and **Current Tier Start Datetime** attributes with this condition to return dates that exist within a defined start and end date.

   * - **is false**
     - |attribute-recommended| **More useful**

       Returns an audience that contains customers who have not opted in to being contacted by your loyalty program.

       .. tip:: Combine the **Is Opted In** and **Latest Opted Out Datetime** attributes with this condition to return an audience of customers who have opted out of being contacted by your loyalty program to exclude from an advertising campaign.

   * - **is not**
     - **is not** returns an audience with any customer records that are not associated with a selected date.

       .. tip:: Use the **Latest Update Datetime** attribute with this condition to return an audience of customers---who have made no updates to their loyalty profile within the defined selected dates---to send out a reminder message to ensure their loyalty profile information is up to date.

   * - **is not between**
     - |attribute-stop| **Less useful**

       Returns dates that exist outside of a defined start and end date.

   * - **is not NULL**
     - |attribute-recommended| **More useful**

       Returns customer records that are associated with a datetime or are opted in to being contacted by your loyalty program.

       .. tip:: Use the **Latest Opted In Datetime** attribute with this condition to return an audience with customers---that have opted in to being contacted by your loyalty program---to be included in an advertising campaign.

   * - **is NULL**
     - Returns customer records that are not opted in to being contacted by your loyalty membership or associated with a datetime.

   * - **is on or after**
     - Returns all dates that occur on or after the selected date. Use a relative date to define a rolling window.

   * - **is on or before**
     - Returns all dates that occur on or before the selected date.

       .. tip:: Use the **Current Balance Expiration Datetime**, **Current Tier Expiration Datetime**, **Latest Opted Out Datetime**, **Latest Opted In Datetime**, and **Current Tier Start Datetime** attributes with this condition to return audiences based on the selected date.

          For example, use "today - 730 days" to return customer records with a current tier start datetime that occurred two years ago to include in a discount campaign that encourages customers to move up to the next tier.

   * - **is true**
     - |attribute-recommended| **More useful**

       Return customer records with customers who opted in to being contacted by your loyalty program.

       .. tip:: Use the **Is Opted In** attribute with this condition to return an audience that has opted in to being contacted by your loyalty program to include in a sales campaign.

.. attribute-loyalty-membership-conditions-end
