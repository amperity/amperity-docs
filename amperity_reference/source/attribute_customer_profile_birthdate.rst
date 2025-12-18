.. https://docs.amperity.com/reference/


.. |what-access| replace:: the **birthdate** attribute
.. |what-choose| replace:: **birthdate**
.. |what-find| replace:: "birthdate"


.. meta::
    :description lang=en:
        Birthdates

.. meta::
    :content class=swiftype name=body data-type=text:
        Birthdates

.. meta::
    :content class=swiftype name=title data-type=string:
        Birthdates

==================================================
Birthdates
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-birthdate-start
   :end-before: .. term-birthdate-end


.. _attribute-customer-profile-birthdate-segment:

Use in segments
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-customer-profile-birthdates-conditions:

Available operators
==================================================

.. attribute-customer-profile-birthdate-conditions-start

The following table lists the operators that are available to this attribute.

.. note:: This attribute has a Date data type. All Date data types share the same set of operators. Recommended operators for this attribute are identified with "|attribute-recommended| **More useful**" and operators with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Operator
     - Description
   * - **is**
     - Avoid using **is** condition with this attribute unless you intend to use a specific date, such as "2022-08-22" ("yyyy-mm-dd").

   * - **is after**
     - |attribute-recommended| **More useful**

       Returns all dates that occur after the selected calendar date, excluding the selected calendar date.

   * - **is before**
     - |attribute-recommended| **More useful**

       Returns all dates that occur before the selected calendar date, excluding the selected calendar date.

   * - **is between**
     - |attribute-recommended| **More useful**

       Returns dates that exist within a defined start and end date.

   * - **is not between**
     - Returns order dates that exist outside of a defined start and end date.

   * - **is not NULL**
     - Returns customer records that have a value.

   * - **is NULL**
     - Returns customer records that do not have a value.

   * - **is on or after**
     - Return all dates that occur on or after the selected calendar date. Use a relative date to define a rolling window. 

   * - **is on or before**
     - Return all dates that occur on or before the selected calendar date. Use a relative date to define a rolling window. 

.. attribute-customer-profile-birthdate-conditions-end


.. _attribute-customer-profile-birthdate-relative-dates:

About relative dates
==================================================

.. include:: ../../amperity_reference/source/segment_editor.rst
   :start-after: .. segments-editor-relative-dates-start
   :end-before: .. segments-editor-relative-dates-end

**Relative date values**

.. include:: ../../amperity_reference/source/segment_editor.rst
   :start-after: .. segments-editor-relative-date-values-start
   :end-before: .. segments-editor-relative-date-values-end
