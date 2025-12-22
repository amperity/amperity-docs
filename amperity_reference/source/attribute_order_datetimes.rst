.. https://docs.amperity.com/reference/


.. |what-access| replace:: order datetime attributes
.. |what-choose| replace:: **first order datetime**, **second order datetime**, or **latest order datetime**
.. |what-find| replace:: "order datetime"


.. meta::
    :description lang=en:
        The date and time at which each transaction occurred.

.. meta::
    :content class=swiftype name=body data-type=text:
        The date and time at which each transaction occurred.

.. meta::
    :content class=swiftype name=title data-type=string:
        Order datetime

==================================================
Order datetime
==================================================

.. attribute-datetimes-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-order-date-start
   :end-before: .. term-order-date-end

* .. include:: ../../shared/terms.rst
     :start-after: .. term-first-order-date-start
     :end-before: .. term-first-order-date-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-latest-order-date-start
     :end-before: .. term-latest-order-date-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-second-order-date-start
     :end-before: .. term-second-order-date-end

.. attribute-datetimes-end


.. _attribute-datetimes-examples:

Examples
==================================================

.. attribute-datetimes-examples-start

The following topics contain examples of using datetimes:

* |usecase_customers_lapsing|
* |usecase_customers_high_value_new|
* |usecase_customers_website_new|

.. attribute-datetimes-examples-end


.. _attribute-datetimes-segment:

Use in segments
==================================================

.. attribute-datetimes-access-start

You can access datetime attributes directly from the **Segment Editor**. To add these attributes to your segments, To add these attributes to your segment, click **Add condition** and then **Add attribute**. Select the **Transaction Attributes Extended** source (for **First Order Datetime**, **Latest Order Datetime**, and **Second Order Datetime**) *or* the **Unified Transactions** table (for **Order Datetime**), apply a condition, and then specify a value.

.. attribute-datetimes-access-end


.. _attribute-order-datetimes-conditions-conditions:

Available operators
==================================================

.. attribute-order-datetimes-conditions-start

The following table lists the operators that are available to these attributes.

.. note:: These attributes have a **datetime** data type. All **datetime** data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Avoid using the **is** condition with these attributes unless you intend to use a specific date, such as "2022-08-22" ("yyyy-mm-dd").

   * - **is after**
     - |attribute-recommended| **More useful**

       Return all dates that occur after the selected calendar date, excluding the selected calendar date.

   * - **is before**
     - |attribute-recommended| **More useful**

       Return all dates that occur before the selected calendar date, excluding the selected calendar date.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns dates that exist within a defined start and end date.

       For example, all orders made during a holiday shopping window or all orders made during a calendar year. Combine these attributes and condition with channels, brands, and purchase locations to build more specific audiences.

   * - **is not between**
     - Returns order dates that exist outside of a defined start and end date.

       For example, if you choose August 10, 2022 and August 12, 2022 as your start and end dates, all orders before August 10. 2022 and all orders after August 12, 2022 is returned.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

   * - **is on or after**
     - Returns all dates that occur on or after the selected calendar date. Use a relative date to define a rolling window.

       For example, use "today - 90 days" to return orders that have been made during the previous 90 days.

   * - **is on or before**
     - Return all dates that occur on or before the selected calendar date. Use a relative date to define a rolling window.

       For example, use "today - 1080 days" to return orders that were made 3 or more years ago.

.. attribute-order-datetimes-conditions-end


.. _attribute-order-datetimes-relative-dates:

About relative dates
==================================================

.. include:: ../../amperity_reference/source/segment_editor.rst
   :start-after: .. segments-editor-relative-dates-start
   :end-before: .. segments-editor-relative-dates-end

**Relative date values**

.. include:: ../../amperity_reference/source/segment_editor.rst
   :start-after: .. segments-editor-relative-date-values-start
   :end-before: .. segments-editor-relative-date-values-end
