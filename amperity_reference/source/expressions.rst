.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The subset of Amperity Expression Language (AEL) used to configure real-time event streams, event types, and real-time segments and attributes.

.. meta::
    :content class=swiftype name=body data-type=text:
        The subset of Amperity Expression Language (AEL) used to configure real-time event streams, event types, and real-time segments and attributes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Expressions for real-time

==================================================
Expressions for real-time
==================================================

.. realtime-expressions-intro-start

Amperity Expression Language (AEL) defines how real-time events and profiles are recognized, filtered, and computed. This page describes the subset of AEL used to configure real-time features; it is not a complete AEL reference.

.. realtime-expressions-intro-end


.. _realtime-expressions-where:

Where expressions are used
==================================================

.. realtime-expressions-where-start

You write expressions in these real-time settings:

* **Event streams** -- a routing expression recognizes each incoming event and determines its event type. A stream may also define expressions for the event timestamp and event ID.
* **Event types** -- each field in an event type uses an expression to extract and coerce a value from the raw event payload.
* **Real-time segments** -- a segment is defined by a boolean expression that is evaluated against a profile's attributes.
* **Real-time attributes** -- aggregation and computed attributes use expressions over a profile's events and attributes.

.. realtime-expressions-where-end


.. _realtime-expressions-fields:

Referencing fields
==================================================

.. realtime-expressions-fields-start

Reference a field by name. Enclose a name that contains spaces or other non-identifier characters in backticks, reach a nested field with dot notation, and reach an array item with bracket notation and a zero-based index:

::

   email
   `loyalty tier`
   address.city
   items[0]

.. important:: Use bracket notation for array indexes (``items[0]``). Dot notation followed by a number (``items.0``) is not valid.

.. realtime-expressions-fields-end


.. _realtime-expressions-operators:

Comparing and combining values
==================================================

.. realtime-expressions-operators-start

Real-time segment expressions and aggregation conditions are boolean expressions. The following operators are available:

* Comparison: ``=``, ``!=``, ``<``, ``<=``, ``>``, ``>=``
* Membership: ``in``, ``not in``
* Null checks: ``is null``, ``is not null``
* Logical: ``and``, ``or``, ``not``

.. realtime-expressions-operators-end


.. _realtime-expressions-parsing:

Parsing event values
==================================================

.. realtime-expressions-parsing-start

Event type field expressions often coerce raw payload values into the field's type. Commonly used functions include:

* ``to_timestamp`` and ``timestamp_from_millis`` -- produce a timestamp from a string or an epoch-milliseconds value.
* ``to_int`` and ``to_string`` -- cast a value to an integer or a string.
* ``coalesce`` -- return the first non-null value from a list.

.. realtime-expressions-parsing-end


.. _realtime-expressions-time:

Working with time windows
==================================================

.. realtime-expressions-time-start

Time-windowed expressions--such as those used in real-time segments and aggregation attributes--take a ``unit`` argument. The valid values are ``SECONDS``, ``MINUTES``, and ``HOURS``.

.. realtime-expressions-time-end


.. _realtime-expressions-more:

Beyond this subset
==================================================

.. realtime-expressions-more-start

AEL includes many additional operators and functions--arithmetic, decimal precision, array operations, and more--that are beyond the subset needed for real-time configuration.

.. realtime-expressions-more-end


.. ael-generated-start

.. Generated from the AEL operation catalog by amperity.attribute.docs.
   Do not edit by hand; run bin/generate-ael-reference in amperity/app.

.. _expressions-operations:

AEL operations
==================================================

.. expressions-operations-start

Each operation below shows how it is written, the type of value it produces, the parameters it accepts, and an example.

Behavior and errors
--------------------------------------------------

.. This generated section is the part to review with Sam for writer's voice.

Parameters are required unless marked with an Optional or Repeatable badge.

There is no global NULL rule; each operation documents its own NULL behavior.

Date and time operations are evaluated in UTC.

Value comparisons are case-sensitive, while field-name resolution is case-insensitive.

Logical operators use two-valued logic: NOT NULL is true.

When an expression fails at run time in the expression preview, it shows ``Evaluation error: ...``.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Category
     - Operations

   * - :ref:`Comparison <expressions-category-comparison>`
     - :ref:`Equal <expressions-operation-equal>`, :ref:`Greater than <expressions-operation-greater-than>`, :ref:`Greater than or equal <expressions-operation-greater-than-or-equal>`, :ref:`Less than <expressions-operation-less-than>`, :ref:`Less than or equal <expressions-operation-less-than-or-equal>`, :ref:`Not equal <expressions-operation-not-equal>`

   * - :ref:`Logical <expressions-category-logical>`
     - :ref:`And <expressions-operation-and>`, :ref:`Not <expressions-operation-not>`, :ref:`Or <expressions-operation-or>`

   * - :ref:`Null <expressions-category-null>`
     - :ref:`Is not null <expressions-operation-is-not-null>`, :ref:`Is null <expressions-operation-is-null>`

   * - :ref:`Conditional <expressions-category-conditional>`
     - :ref:`Case <expressions-operation-case>`, :ref:`Coalesce <expressions-operation-coalesce>`, :ref:`Condition <expressions-operation-condition>`, :ref:`If <expressions-operation-if>`

   * - :ref:`Type conversion <expressions-category-cast>`
     - :ref:`To boolean <expressions-operation-to-boolean>`, :ref:`To date <expressions-operation-to-date>`, :ref:`To decimal <expressions-operation-to-decimal>`, :ref:`To float <expressions-operation-to-float>`, :ref:`To integer <expressions-operation-to-integer>`, :ref:`To string <expressions-operation-to-string>`, :ref:`To timestamp <expressions-operation-to-timestamp>`

   * - :ref:`Collection <expressions-category-collection>`
     - :ref:`Array <expressions-operation-array>`, :ref:`Array, struct, or map lookup <expressions-operation-array-struct-or-map-lookup>`, :ref:`Average array <expressions-operation-average-array>`, :ref:`Count by value <expressions-operation-count-by-value>`, :ref:`Difference <expressions-operation-difference>`, :ref:`Distinct <expressions-operation-distinct>`, :ref:`Filter <expressions-operation-filter>`, :ref:`Get element <expressions-operation-get-element>`, :ref:`In <expressions-operation-in>`, :ref:`Intersect arrays <expressions-operation-intersect-arrays>`, :ref:`Map <expressions-operation-map>`, :ref:`Maximum of array <expressions-operation-maximum-of-array>`, :ref:`Minimum of array <expressions-operation-minimum-of-array>`, :ref:`Most common element <expressions-operation-most-common-element>`, :ref:`Named struct <expressions-operation-named-struct>`, :ref:`Not in <expressions-operation-not-in>`, :ref:`Size <expressions-operation-size>`, :ref:`Skip first <expressions-operation-skip-first>`, :ref:`Sort array <expressions-operation-sort-array>`, :ref:`Struct or map field <expressions-operation-struct-or-map-field>`, :ref:`Sum array <expressions-operation-sum-array>`, :ref:`Take first <expressions-operation-take-first>`, :ref:`Transform <expressions-operation-transform>`, :ref:`Union <expressions-operation-union>`, :ref:`Zip arrays <expressions-operation-zip-arrays>`

   * - :ref:`Text <expressions-category-string>`
     - :ref:`Concatenate <expressions-operation-concatenate>`, :ref:`Concatenate with separator <expressions-operation-concatenate-with-separator>`, :ref:`Contains <expressions-operation-contains>`, :ref:`Ends with <expressions-operation-ends-with>`, :ref:`Lowercase <expressions-operation-lowercase>`, :ref:`Replace <expressions-operation-replace>`, :ref:`SHA-2 hash <expressions-operation-sha-2-hash>`, :ref:`Split <expressions-operation-split>`, :ref:`Starts with <expressions-operation-starts-with>`, :ref:`Uppercase <expressions-operation-uppercase>`

   * - :ref:`Numeric <expressions-category-numeric>`
     - :ref:`Absolute value <expressions-operation-absolute-value>`, :ref:`Add <expressions-operation-add>`, :ref:`Divide <expressions-operation-divide>`, :ref:`Maximum <expressions-operation-maximum>`, :ref:`Minimum <expressions-operation-minimum>`, :ref:`Modulus <expressions-operation-modulus>`, :ref:`Multiply <expressions-operation-multiply>`, :ref:`Subtract <expressions-operation-subtract>`

   * - :ref:`Date & time <expressions-category-date>`
     - :ref:`Add days <expressions-operation-add-days>`, :ref:`Date difference <expressions-operation-date-difference>`, :ref:`Date in last <expressions-operation-date-in-last>`, :ref:`Date in next <expressions-operation-date-in-next>`, :ref:`Day of week <expressions-operation-day-of-week>`, :ref:`Day of year <expressions-operation-day-of-year>`, :ref:`Subtract days <expressions-operation-subtract-days>`, :ref:`Timestamp difference <expressions-operation-timestamp-difference>`, :ref:`Timestamp from milliseconds <expressions-operation-timestamp-from-milliseconds>`, :ref:`Timestamp in last <expressions-operation-timestamp-in-last>`, :ref:`Timestamp in next <expressions-operation-timestamp-in-next>`, :ref:`Week of year <expressions-operation-week-of-year>`

.. expressions-operations-end


.. _expressions-category-comparison:

Comparison
--------------------------------------------------

.. expressions-category-comparison-start

Operations: :ref:`Equal <expressions-operation-equal>`, :ref:`Greater than <expressions-operation-greater-than>`, :ref:`Greater than or equal <expressions-operation-greater-than-or-equal>`, :ref:`Less than <expressions-operation-less-than>`, :ref:`Less than or equal <expressions-operation-less-than-or-equal>`, :ref:`Not equal <expressions-operation-not-equal>`

.. expressions-category-comparison-end


.. _expressions-operation-equal:

Equal
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-equal-start

Written as **value = value**, returning **boolean**. Returns true if all operands are equal to each other.

.. code-block:: none
   :caption: Example

   1 = 1
   # => true

.. expressions-operation-equal-end


.. _expressions-operation-greater-than:

Greater than
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-greater-than-start

Written as **value > value**, returning **boolean**. Returns true if each operand is greater than the operand that follows it.

.. warning::
   The operands are not comparable. This operation throws at run time.

.. code-block:: none
   :caption: Example

   3 > 2
   # => true

.. expressions-operation-greater-than-end


.. _expressions-operation-greater-than-or-equal:

Greater than or equal
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-greater-than-or-equal-start

Written as **value >= value**, returning **boolean**. Returns true if each operand is greater than or equal to the operand that follows it.

.. warning::
   The operands are not comparable. This operation throws at run time.

.. code-block:: none
   :caption: Example

   2 >= 2
   # => true

.. expressions-operation-greater-than-or-equal-end


.. _expressions-operation-less-than:

Less than
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-less-than-start

Written as **value < value**, returning **boolean**. Returns true if each operand is less than the operand that follows it.

.. warning::
   The operands are not comparable. This operation throws at run time.

.. code-block:: none
   :caption: Example

   1 < 2
   # => true

.. expressions-operation-less-than-end


.. _expressions-operation-less-than-or-equal:

Less than or equal
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-less-than-or-equal-start

Written as **value <= value**, returning **boolean**. Returns true if each operand is less than or equal to the operand that follows it.

.. warning::
   The operands are not comparable. This operation throws at run time.

.. code-block:: none
   :caption: Example

   2 <= 2
   # => true

.. expressions-operation-less-than-or-equal-end


.. _expressions-operation-not-equal:

Not equal
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-not-equal-start

Written as **value != value**, returning **boolean**. Returns true if at least one operand is not equal to the others.

.. code-block:: none
   :caption: Example

   1 != 2
   # => true

.. expressions-operation-not-equal-end


.. _expressions-category-logical:

Logical
--------------------------------------------------

.. expressions-category-logical-start

Operations: :ref:`And <expressions-operation-and>`, :ref:`Not <expressions-operation-not>`, :ref:`Or <expressions-operation-or>`

.. expressions-category-logical-end


.. _expressions-operation-and:

And
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-and-start

Written as **value AND value AND ...**, returning **boolean**. Returns true if all operands are truthy. Short-circuits evaluation on the first falsey value.

.. note:: Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   is_active AND has_subscription

.. expressions-operation-and-end


.. _expressions-operation-not:

Not
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-not-start

Written as **NOT value**, returning **boolean**. Returns true if the operand is falsey.

.. code-block:: none
   :caption: Example

   NOT is_active

.. expressions-operation-not-end


.. _expressions-operation-or:

Or
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-or-start

Written as **value OR value OR ...**, returning **boolean**. Returns true if any operand is truthy. Short-circuits evaluation on the first truthy value.

.. note:: Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   has_browsed_product_l24h OR NOT (has_purchased_product_l24h OR has_activity_l2h)

.. expressions-operation-or-end


.. _expressions-category-null:

Null
--------------------------------------------------

.. expressions-category-null-start

Operations: :ref:`Is not null <expressions-operation-is-not-null>`, :ref:`Is null <expressions-operation-is-null>`

.. expressions-category-null-end


.. _expressions-operation-is-not-null:

Is not null
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-is-not-null-start

Written as **value IS NOT NULL**, returning **boolean**. Returns true if the operand is not null.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   'email' IS NOT NULL
   # => true

.. expressions-operation-is-not-null-end


.. _expressions-operation-is-null:

Is null
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-is-null-start

Written as **value IS NULL**, returning **boolean**. Returns true if the operand is null.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   NULL IS NULL
   # => true

.. expressions-operation-is-null-end


.. _expressions-category-conditional:

Conditional
--------------------------------------------------

.. expressions-category-conditional-start

Operations: :ref:`Case <expressions-operation-case>`, :ref:`Coalesce <expressions-operation-coalesce>`, :ref:`Condition <expressions-operation-condition>`, :ref:`If <expressions-operation-if>`

.. expressions-category-conditional-end


.. _expressions-operation-case:

Case
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-case-start

Written as **case(value, match, result, ...)**, returning **any**. Selects a result based on matching a test value against possible cases.

**value**
   Any. The value to match against.

**match**
   Any, :bdg-muted:`Repeatable`. A candidate value.

**result**
   Any, :bdg-muted:`Repeatable`. Result returned when the candidate matches.

.. note:: Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   case('GOLD', 'GOLD', 0.2, 'SILVER', 0.1, 0.05)
   # => 0.2

.. expressions-operation-case-end


.. _expressions-operation-coalesce:

Coalesce
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-coalesce-start

Written as **coalesce(value, value, ...)**, returning **any**. Evaluates operands in order, returning the first non-NULL operand.

**value**
   Any, :bdg-muted:`Repeatable`. A value to consider.

.. note:: Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   coalesce(NULL, NULL, 'there')
   # => 'there'

.. expressions-operation-coalesce-end


.. _expressions-operation-condition:

Condition
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-condition-start

Written as **cond(predicate, result, ...)**, returning **any**. Evaluates predicates in order, returning the result paired with the first true predicate.

**predicate**
   Boolean, :bdg-muted:`Repeatable`. A predicate to evaluate in order.

**result**
   Any, :bdg-muted:`Repeatable`. Result returned when the predicate is true.

.. note:: Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   cond('GOLD' = 'GOLD', 0.2, 'SILVER' = 'GOLD', 0.1, 0.05)
   # => 0.2

.. expressions-operation-condition-end


.. _expressions-operation-if:

If
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-if-start

Written as **if(condition, then, else)**, returning **any**. Returns the second operand if the first operand (condition) is true, otherwise returns the third operand. NULL conditions are treated as false.

**condition**
   Boolean. The condition to test.

**then**
   Any. Result when the condition is true.

**else**
   Any. Result when the condition is false.

.. note:: Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   if(100 > 50, 'free', 'standard')
   # => 'free'

.. expressions-operation-if-end


.. _expressions-category-cast:

Type conversion
--------------------------------------------------

.. expressions-category-cast-start

Operations: :ref:`To boolean <expressions-operation-to-boolean>`, :ref:`To date <expressions-operation-to-date>`, :ref:`To decimal <expressions-operation-to-decimal>`, :ref:`To float <expressions-operation-to-float>`, :ref:`To integer <expressions-operation-to-integer>`, :ref:`To string <expressions-operation-to-string>`, :ref:`To timestamp <expressions-operation-to-timestamp>`

.. expressions-category-cast-end


.. _expressions-operation-to-boolean:

To boolean
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-boolean-start

Written as **to_boolean(value)**, returning **boolean**. Coerces a value to boolean. Returns NULL if coercion is not possible.

**value**
   Any. The value to coerce.

.. warning::
   The value has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   to_boolean('true')
   # => true

.. expressions-operation-to-boolean-end


.. _expressions-operation-to-date:

To date
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-date-start

Written as **to_date(value, format)**, returning **date**. Coerces a value to date. Returns NULL if coercion is not possible.

**value**
   Any. The value to coerce.

**format**
   String, :bdg-muted:`Optional`. Optional date parse format.

.. note::
   The format pattern is invalid. This operation returns NULL.

.. code-block:: none
   :caption: Example

   to_date('2024-01-15', 'yyyy-MM-dd')
   # => to_date('2024-01-15')

.. expressions-operation-to-date-end


.. _expressions-operation-to-decimal:

To decimal
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-decimal-start

Written as **to_decimal(value, precision, scale)**, returning **decimal**. Coerces a value to big decimal, with precision 38 and scale 2 by default. The optional precision and scale parameters must be integer literals. Returns NULL if the coerced value is wider than the precision.

**value**
   Any. The value to coerce.

**precision**
   Integer, :bdg-muted:`Optional`. Optional decimal precision, 1 to 38. Must be a literal number.

**scale**
   Integer, :bdg-muted:`Optional`. Optional decimal scale, 0 to the precision. Must be a literal number.

.. code-block:: none
   :caption: Example

   to_decimal('12.345', 10, 2)
   # => to_decimal('12.35')

.. expressions-operation-to-decimal-end


.. _expressions-operation-to-float:

To float
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-float-start

Written as **to_float(value)**, returning **float**. Coerces a value to float. Returns NULL if coercion is not possible.

**value**
   Any. The value to coerce.

.. warning::
   The value has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   to_float('12.5')
   # => 12.5

.. expressions-operation-to-float-end


.. _expressions-operation-to-integer:

To integer
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-integer-start

Written as **to_int(value)**, returning **integer**. Coerces a value to a 64-bit integer. Returns NULL if coercion is not possible.

**value**
   Any. The value to coerce.

.. warning::
   The value has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   to_int('12.9')
   # => 12

.. expressions-operation-to-integer-end


.. _expressions-operation-to-string:

To string
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-string-start

Written as **to_string(value)**, returning **string**. Converts a value to string. Returns NULL if the input is NULL.

**value**
   Any. The value to convert.

.. warning::
   The value has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   to_string(123)
   # => '123'

.. expressions-operation-to-string-end


.. _expressions-operation-to-timestamp:

To timestamp
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-timestamp-start

Written as **to_timestamp(value, format)**, returning **datetime**. Coerces a value to timestamp. Returns NULL if coercion is not possible.

**value**
   Any. The value to coerce.

**format**
   String, :bdg-muted:`Optional`. Optional timestamp parse format.

.. note::
   The format pattern is invalid. This operation returns NULL.

.. code-block:: none
   :caption: Example

   to_timestamp('2024-01-15T12:34:56Z')
   # => to_timestamp('2024-01-15T12:34:56Z')

.. expressions-operation-to-timestamp-end


.. _expressions-category-collection:

Collection
--------------------------------------------------

.. expressions-category-collection-start

Operations: :ref:`Array <expressions-operation-array>`, :ref:`Array, struct, or map lookup <expressions-operation-array-struct-or-map-lookup>`, :ref:`Average array <expressions-operation-average-array>`, :ref:`Count by value <expressions-operation-count-by-value>`, :ref:`Difference <expressions-operation-difference>`, :ref:`Distinct <expressions-operation-distinct>`, :ref:`Filter <expressions-operation-filter>`, :ref:`Get element <expressions-operation-get-element>`, :ref:`In <expressions-operation-in>`, :ref:`Intersect arrays <expressions-operation-intersect-arrays>`, :ref:`Map <expressions-operation-map>`, :ref:`Maximum of array <expressions-operation-maximum-of-array>`, :ref:`Minimum of array <expressions-operation-minimum-of-array>`, :ref:`Most common element <expressions-operation-most-common-element>`, :ref:`Named struct <expressions-operation-named-struct>`, :ref:`Not in <expressions-operation-not-in>`, :ref:`Size <expressions-operation-size>`, :ref:`Skip first <expressions-operation-skip-first>`, :ref:`Sort array <expressions-operation-sort-array>`, :ref:`Struct or map field <expressions-operation-struct-or-map-field>`, :ref:`Sum array <expressions-operation-sum-array>`, :ref:`Take first <expressions-operation-take-first>`, :ref:`Transform <expressions-operation-transform>`, :ref:`Union <expressions-operation-union>`, :ref:`Zip arrays <expressions-operation-zip-arrays>`

.. expressions-category-collection-end


.. _expressions-operation-array:

Array
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-array-start

Written as **array(value, value, ...)**, returning **array**. Returns an array of operands in order. All operands must be of the same type.

**value**
   Any, :bdg-muted:`Repeatable`. An array element.

.. code-block:: none
   :caption: Example

   array(1, 2, 3)
   # => array(1, 2, 3)

.. expressions-operation-array-end


.. _expressions-operation-array-struct-or-map-lookup:

Array, struct, or map lookup
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-array-struct-or-map-lookup-start

Written as **value[key]**, returning **any**. Gets an integer offset from an array, a field from a struct, or an arbitrary key from a map.

.. note::
   The index is negative or outside the array bounds. This operation returns NULL.

.. code-block:: none
   :caption: Example

   array('sku')[0]
   # => 'sku'

.. expressions-operation-array-struct-or-map-lookup-end


.. _expressions-operation-average-array:

Average array
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-average-array-start

Written as **array_avg(array)**, returning **number**. Returns the mean of the input array's non-NULL elements, which must be numeric. Returns NULL if the input is NULL, empty, or holds only NULLs, matching the ``average`` aggregation over zero records.

Also accepts the name **array_average**.

**array**
   Array. The array of numbers to average. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_avg(array(1, 2, 4))
   # => 2.3333333333333335

.. expressions-operation-average-array-end


.. _expressions-operation-count-by-value:

Count by value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-count-by-value-start

Written as **array_counts(array)**, returning **array**. Returns a frequency table for the input array: an array of structs with a ``value`` field holding each distinct non-NULL element and a ``count`` field holding how many times it occurs. Ordered by count descending, then by the natural sort order of the value, matching the ``mode`` aggregation's tie-break. NULL elements are not counted. Returns NULL if the input is NULL, and an empty array if the input is empty or holds only NULLs.

**array**
   Array. The array to tally. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   take(array_counts(array('wool', 'silk', 'wool')), 2)
   # => array(map('value', 'wool', 'count', 2), map('value', 'silk', 'count', 1))

.. expressions-operation-count-by-value-end


.. _expressions-operation-difference:

Difference
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-difference-start

Written as **difference(source, remove)**, returning **array**. Returns the elements of the first array that are not present in the second array, preserving the order and duplicates of the first array. A NULL second operand removes nothing, so ``difference(a, NULL)`` is ``a``. SparkSQL spells this ``array_except`` and removes duplicates; that spelling is not accepted here.

**source**
   Array. The source array.

**remove**
   Array. The array of elements to remove.

.. code-block:: none
   :caption: Example

   difference(array('spring', 'summer'), array('summer'))
   # => array('spring')

.. expressions-operation-difference-end


.. _expressions-operation-distinct:

Distinct
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-distinct-start

Written as **distinct(array)**, returning **array**. Returns the input array with duplicate elements removed, preserving the order of first occurrence.

**array**
   Array. The array to deduplicate.

.. code-block:: none
   :caption: Example

   distinct(array('spring', 'spring', 'summer'))
   # => array('spring', 'summer')

.. expressions-operation-distinct-end


.. _expressions-operation-filter:

Filter
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-filter-start

Written as **filter(array, element -> predicate)**, returning **array**. Filters an array using a function that takes one argument (which will be bound to each element in the array, in order) and returns a boolean. Returns an array containing only the elements for which the function returned true.

**array**
   Array. The array to filter.

**function**
   Function. A one-argument function whose argument is bound to each element in turn, and which returns a boolean.

.. code-block:: none
   :caption: Example

   filter(array('ON', 'OFF'), x -> x = 'ON')
   # => array('ON')

.. expressions-operation-filter-end


.. _expressions-operation-get-element:

Get element
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-get-element-start

Written as **get(array, index)**, returning **any**. Returns the element of the input array at the given (0-based) index. If the index points outside of the array boundaries, or if the index is negative, then this function returns NULL.

**array**
   Array. The array to index into.

**index**
   Integer. The 0-based index.

.. code-block:: none
   :caption: Example

   get(array('Merino', 'wool'), 0)
   # => 'Merino'

.. expressions-operation-get-element-end


.. _expressions-operation-in:

In
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-in-start

Written as **value IN (array)**, returning **boolean**. Returns true if the value is one of the listed values. The right operand is a parenthesized list written into the expression, not a field holding an array; to test membership of an array-valued field, use ``size(filter(field, x -> x = value)) > 0``, or ``size(array_intersect(a, b)) > 0`` when both sides are arrays in the record.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   'GOLD' IN ('GOLD', 'PLATINUM')
   # => true

.. expressions-operation-in-end


.. _expressions-operation-intersect-arrays:

Intersect arrays
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-intersect-arrays-start

Written as **array_intersect(source, keep)**, returning **array**. Returns the elements present in both arrays, with duplicates removed, in the order they first appear in the first array. Returns NULL if either operand is NULL. Matches SparkSQL's ``array_intersect`` on all three points.

**source**
   Array. The source array.

**keep**
   Array. The array of elements to keep.

.. code-block:: none
   :caption: Example

   array_intersect(array('a', 'b'), array('b', 'c'))
   # => array('b')

.. expressions-operation-intersect-arrays-end


.. _expressions-operation-map:

Map
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-map-start

Written as **map(key, value, ...)**, returning **map**. Returns a map of the given key/value pairs. All keys and all values must be of the same type.

**key**
   Any, :bdg-muted:`Repeatable`. A map key.

**value**
   Any, :bdg-muted:`Repeatable`. A map value.

.. code-block:: none
   :caption: Example

   map('sku', 'ABC', 'brand', 'Wool')
   # => map('sku', 'ABC', 'brand', 'Wool')

.. expressions-operation-map-end


.. _expressions-operation-maximum-of-array:

Maximum of array
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-maximum-of-array-start

Written as **array_max(array)**, returning **any**. Returns the largest of the input array's non-NULL elements. Unlike the scalar ``max``, the elements need only be orderable, so arrays of strings, dates, and timestamps are supported. Returns NULL if the input is NULL, empty, or holds only NULLs.

**array**
   Array. The array to take the maximum of. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_max(array(1, 2, 3))
   # => 3

.. expressions-operation-maximum-of-array-end


.. _expressions-operation-minimum-of-array:

Minimum of array
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-minimum-of-array-start

Written as **array_min(array)**, returning **any**. Returns the smallest of the input array's non-NULL elements. Unlike the scalar ``min``, the elements need only be orderable, so arrays of strings, dates, and timestamps are supported. Returns NULL if the input is NULL, empty, or holds only NULLs.

**array**
   Array. The array to take the minimum of. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_min(array(1, 2, 3))
   # => 1

.. expressions-operation-minimum-of-array-end


.. _expressions-operation-most-common-element:

Most common element
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-most-common-element-start

Written as **array_mode(array)**, returning **any**. Returns the most frequently occurring element of the input array, or NULL if the input is NULL or contains no non-NULL elements. NULL elements are not counted. Ties are broken by the natural sort order of the tied elements, matching the ``mode`` aggregation.

**array**
   Array. The array to reduce. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_mode(array('wool', 'silk', 'wool'))
   # => 'wool'

.. expressions-operation-most-common-element-end


.. _expressions-operation-named-struct:

Named struct
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-named-struct-start

Written as **named_struct(key, value, ...)**, returning **struct**. Returns a struct with the given field names and values. Each name must be written as text, must be a valid field name, and may not be repeated.

**key**
   String, :bdg-muted:`Repeatable`. A struct field name, written directly as text. Letters, numbers, and underscores, with at least one letter or underscore, and unique within the struct.

**value**
   Any, :bdg-muted:`Repeatable`. A struct field value.

.. code-block:: none
   :caption: Example

   named_struct('sku', 'ABC', 'count', 2)
   # => map('sku', 'ABC', 'count', 2)

.. expressions-operation-named-struct-end


.. _expressions-operation-not-in:

Not in
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-not-in-start

Written as **value NOT IN (array)**, returning **boolean**. Returns true if the value is none of the listed values. The right operand is a parenthesized list written into the expression, not a field holding an array; to test membership of an array-valued field, use ``size(filter(field, x -> x = value)) = 0``.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   'SILVER' NOT IN ('GOLD', 'PLATINUM')
   # => true

.. expressions-operation-not-in-end


.. _expressions-operation-size:

Size
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-size-start

Written as **size(collection)**, returning **integer**. Returns the integer element count of the operand, or NULL if the operand is NULL.

**collection**
   Array. The collection to measure.

.. warning::
   The operand is not a collection. This operation throws at run time.

.. code-block:: none
   :caption: Example

   size(array('Merino', 'wool'))
   # => 2

.. expressions-operation-size-end


.. _expressions-operation-skip-first:

Skip first
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-skip-first-start

Written as **skip(array, offset)**, returning **array**. Returns the input array without its first ``offset`` elements. An ``offset`` at or past the end of the array returns an empty array. Returns NULL if either operand is NULL or if ``offset`` is negative. Compose with ``take`` for a window out of the middle: ``take(skip(arr, 1), 2)``.

**array**
   Array. The array to skip into.

**offset**
   Integer. How many leading elements to skip.

.. code-block:: none
   :caption: Example

   skip(array(1, 2, 3), 1)
   # => array(2, 3)

.. expressions-operation-skip-first-end


.. _expressions-operation-sort-array:

Sort array
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-sort-array-start

Written as **array_sort(array, comparator)**, returning **array**. Sorts the input array, ascending by default, placing NULL elements at the end and ordering NaN above every other float. A comparator sorts by any other order: it takes two elements and returns a negative number, zero, or a positive number as the first sorts before, with, or after the second, and returning NULL from it fails the expression. An array of structs has no default order, so it requires a comparator.

**array**
   Array. The array to sort.

**comparator**
   Function, :bdg-muted:`Optional`. Optional two-argument comparator function.

.. warning::
   A comparator returns NULL. This operation throws at run time.

.. code-block:: none
   :caption: Example

   array_sort(array(3, 1, 2))
   # => array(1, 2, 3)

.. expressions-operation-sort-array-end


.. _expressions-operation-struct-or-map-field:

Struct or map field
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-struct-or-map-field-start

Written as **value.key**, returning **any**. Gets a field from a struct, or a string key from a map.

.. code-block:: none
   :caption: Example

   map('city', 'Seattle').city
   # => 'Seattle'

.. expressions-operation-struct-or-map-field-end


.. _expressions-operation-sum-array:

Sum array
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-sum-array-start

Written as **array_sum(array)**, returning **number**. Returns the sum of the input array's non-NULL elements, which must be numeric. Returns 0 for an empty array or one holding only NULLs, matching the ``sum`` aggregation over zero records. Returns NULL if the input is NULL.

**array**
   Array. The array of numbers to add. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_sum(array(1, 2, 3))
   # => 6

.. expressions-operation-sum-array-end


.. _expressions-operation-take-first:

Take first
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-take-first-start

Written as **take(array, limit)**, returning **array**. Returns the first ``limit`` elements of the input array. A ``limit`` longer than the array returns the whole array, and a ``limit`` of zero returns an empty array. Returns NULL if either operand is NULL or if ``limit`` is negative.

**array**
   Array. The array to take from.

**limit**
   Integer. How many elements to take.

.. code-block:: none
   :caption: Example

   take(array(1, 2, 3), 2)
   # => array(1, 2)

.. expressions-operation-take-first-end


.. _expressions-operation-transform:

Transform
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-transform-start

Written as **transform(array, element -> expression)**, returning **array**. Transforms an array using a function that takes each element of the array, in order, and returns a new value. Returns an array of the values returned by the function. The function may take an optional second argument, which will be bound to the zero-based index of the element.

**array**
   Array. The array to transform.

**function**
   Function. A function whose first argument is bound to each element in turn. An optional second argument is bound to that element's 0-based index: (element, index) -> expression.

.. code-block:: none
   :caption: Example

   transform(array('wool', 'silk'), x -> upper(x))
   # => array('WOOL', 'SILK')

.. expressions-operation-transform-end


.. _expressions-operation-union:

Union
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-union-start

Written as **union(array, array, ...)**, returning **array**. Concatenates two or more arrays into a single array, preserving order and keeping duplicate elements. All operands must be arrays of primitive or flat-struct elements with a common element type. NULL operands are skipped rather than propagated, so ``union(a, NULL)`` is ``a``. SparkSQL spells this ``array_union`` and removes duplicates; that spelling is not accepted here.

**array**
   Array, :bdg-muted:`Repeatable`. An array to concatenate.

.. code-block:: none
   :caption: Example

   union(array('spring'), array('summer'))
   # => array('spring', 'summer')

.. expressions-operation-union-end


.. _expressions-operation-zip-arrays:

Zip arrays
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-zip-arrays-start

Written as **array_zip(name, array, name, array, ...)**, returning **array**. Combines two or more arrays element-wise into an array of structs. Shorter arrays are padded with NULL, so the result length is that of the longest input, and the result is NULL if any input array is NULL -- both as in SparkSQL's ``arrays_zip``. Operands alternate between a field name and the array supplying that field's values, as in ``named_struct``: SparkSQL derives struct field names from the input column names, and an AEL operand is an expression with no name to derive.

**name**
   String, :bdg-muted:`Repeatable`. A struct field name, written directly as text.

**array**
   Array, :bdg-muted:`Repeatable`. The array supplying that field's values.

.. code-block:: none
   :caption: Example

   array_zip('sku', array('A', 'B'), 'brand', array('Wool', 'Silk'))
   # => array(map('sku', 'A', 'brand', 'Wool'), map('sku', 'B', 'brand', 'Silk'))

.. expressions-operation-zip-arrays-end


.. _expressions-category-string:

Text
--------------------------------------------------

.. expressions-category-string-start

Operations: :ref:`Concatenate <expressions-operation-concatenate>`, :ref:`Concatenate with separator <expressions-operation-concatenate-with-separator>`, :ref:`Contains <expressions-operation-contains>`, :ref:`Ends with <expressions-operation-ends-with>`, :ref:`Lowercase <expressions-operation-lowercase>`, :ref:`Replace <expressions-operation-replace>`, :ref:`SHA-2 hash <expressions-operation-sha-2-hash>`, :ref:`Split <expressions-operation-split>`, :ref:`Starts with <expressions-operation-starts-with>`, :ref:`Uppercase <expressions-operation-uppercase>`

.. expressions-category-string-end


.. _expressions-operation-concatenate:

Concatenate
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-concatenate-start

Written as **concat(value, value, ...)**, returning **string**. Concatenates operands together with no spaces/separator.

**value**
   String, :bdg-muted:`Repeatable`. A value to join.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   concat('Merino', ' ', 'wool')
   # => 'Merino wool'

.. expressions-operation-concatenate-end


.. _expressions-operation-concatenate-with-separator:

Concatenate with separator
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-concatenate-with-separator-start

Written as **concat_ws(separator, value, ...)**, returning **string**. Concatenates operands together. The first operand should be a (possibly empty) separator string.

**separator**
   String. The separator placed between values.

**value**
   String, :bdg-muted:`Repeatable`. A value to join.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   concat_ws('-', 'Merino', 'wool')
   # => 'Merino-wool'

.. expressions-operation-concatenate-with-separator-end


.. _expressions-operation-contains:

Contains
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-contains-start

Written as **contains(string, substring)**, returning **boolean**. Returns true if the first operand string contains the second operand string.

**string**
   String. The string to search.

**substring**
   String. The substring to look for.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   contains('Merino wool blend', 'Merino')
   # => true

.. expressions-operation-contains-end


.. _expressions-operation-ends-with:

Ends with
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-ends-with-start

Written as **endswith(string, suffix)**, returning **boolean**. Returns true if the first operand string ends with the second operand string.

**string**
   String. The string to test.

**suffix**
   String. The suffix to look for.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   endswith('receipt@example.com', '@example.com')
   # => true

.. expressions-operation-ends-with-end


.. _expressions-operation-lowercase:

Lowercase
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-lowercase-start

Written as **lower(string)**, returning **string**. Converts the operand string to lower case.

**string**
   String. The string to convert.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   lower('Merino')
   # => 'merino'

.. expressions-operation-lowercase-end


.. _expressions-operation-replace:

Replace
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-replace-start

Written as **replace(string, search, replacement)**, returning **string**. Replaces all occurrences of the second operand string in the first operand string with the third operand string.

**string**
   String. The string to operate on.

**search**
   String. The substring to replace.

**replacement**
   String, :bdg-muted:`Optional`. The replacement substring.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   replace('555-1234', '-', '')
   # => '5551234'

.. expressions-operation-replace-end


.. _expressions-operation-sha-2-hash:

SHA-2 hash
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-sha-2-hash-start

Written as **sha2(string, bits)**, returning **string**. Returns a checksum of SHA-2 family as a hex string of expr. SHA-224, SHA-256, SHA-384, and SHA-512 are supported. Bit length of 0 is equivalent to 256.

**string**
   String. The string to hash.

**bits**
   Integer. Bit length: 224, 256, 384 or 512 (0 means 256).

.. note::
   The bit length is not 0, 224, 256, 384, or 512. This operation returns NULL.

.. code-block:: none
   :caption: Example

   sha2('abc', 256)
   # => 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'

.. expressions-operation-sha-2-hash-end


.. _expressions-operation-split:

Split
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-split-start

Written as **split(string, delimiter)**, returning **array**. Splits the first operand string on each literal occurrence of the second operand string, returning an array of strings. The delimiter is matched literally, not as a regular expression. Empty trailing elements are preserved, so the result length is stable for fixed-shape values. An empty delimiter splits the string into one element per code point, matching SparkSQL.

**string**
   String. The string to split.

**delimiter**
   String. The literal delimiter to split on. An empty delimiter splits into single characters.

.. code-block:: none
   :caption: Example

   split('Merino wool', ' ')[0]
   # => 'Merino'

.. expressions-operation-split-end


.. _expressions-operation-starts-with:

Starts with
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-starts-with-start

Written as **startswith(string, prefix)**, returning **boolean**. Returns true if the first operand string starts with the second operand string.

**string**
   String. The string to test.

**prefix**
   String. The prefix to look for.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   startswith('Merino wool blend', 'Merino')
   # => true

.. expressions-operation-starts-with-end


.. _expressions-operation-uppercase:

Uppercase
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-uppercase-start

Written as **upper(string)**, returning **string**. Converts the operand string to upper case.

**string**
   String. The string to convert.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   upper('wool')
   # => 'WOOL'

.. expressions-operation-uppercase-end


.. _expressions-category-numeric:

Numeric
--------------------------------------------------

.. expressions-category-numeric-start

Operations: :ref:`Absolute value <expressions-operation-absolute-value>`, :ref:`Add <expressions-operation-add>`, :ref:`Divide <expressions-operation-divide>`, :ref:`Maximum <expressions-operation-maximum>`, :ref:`Minimum <expressions-operation-minimum>`, :ref:`Modulus <expressions-operation-modulus>`, :ref:`Multiply <expressions-operation-multiply>`, :ref:`Subtract <expressions-operation-subtract>`

.. expressions-category-numeric-end


.. _expressions-operation-absolute-value:

Absolute value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-absolute-value-start

Written as **abs(number)**, returning **number**. Returns the absolute value of the operand.

**number**
   Number. The number whose absolute value to return.

.. warning::
   The operand is NULL. This operation throws at run time.

.. code-block:: none
   :caption: Example

   abs(-5)
   # => 5

.. expressions-operation-absolute-value-end


.. _expressions-operation-add:

Add
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-add-start

Written as **value + value + ...**, returning **number**. Adds operands.

.. warning::
   The operands exceed the numeric range supported by the operation. This operation throws at run time.

.. code-block:: none
   :caption: Example

   1 + 2
   # => 3

.. expressions-operation-add-end


.. _expressions-operation-divide:

Divide
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-divide-start

Written as **value / value / ...**, returning **number**. Divides operands. Treats division by zero as a NULL result.

.. note::
   A divisor is zero. This operation returns NULL.

.. code-block:: none
   :caption: Example

   6 / 2
   # => 3.0

.. expressions-operation-divide-end


.. _expressions-operation-maximum:

Maximum
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-maximum-start

Written as **max(value, value, ...)**, returning **number**. Returns the maximum value from operands, ignoring NULL values.

**value**
   Number, :bdg-muted:`Repeatable`. A value to compare.

.. code-block:: none
   :caption: Example

   max(3, 1)
   # => 3

.. expressions-operation-maximum-end


.. _expressions-operation-minimum:

Minimum
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-minimum-start

Written as **min(value, value, ...)**, returning **number**. Returns the minimum value from operands, ignoring NULL values.

**value**
   Number, :bdg-muted:`Repeatable`. A value to compare.

.. code-block:: none
   :caption: Example

   min(3, 1)
   # => 1

.. expressions-operation-minimum-end


.. _expressions-operation-modulus:

Modulus
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-modulus-start

Written as **dividend % divisor**, returning **number**. Returns the modulus of the first operand divided by the second operand.

Also accepts the name **mod**.

.. warning::
   Either operand is NULL. This operation throws at run time.
   The divisor is zero. This operation throws at run time.

.. code-block:: none
   :caption: Example

   10 % 3
   # => 1

.. expressions-operation-modulus-end


.. _expressions-operation-multiply:

Multiply
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-multiply-start

Written as **value * value * ...**, returning **number**. Multiplies operands.

.. warning::
   The operands exceed the numeric range supported by the operation. This operation throws at run time.

.. code-block:: none
   :caption: Example

   3 * 4
   # => 12

.. expressions-operation-multiply-end


.. _expressions-operation-subtract:

Subtract
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-subtract-start

Written as **value - value - ...**, returning **number**. Subtracts operands.

.. warning::
   The operands exceed the numeric range supported by the operation. This operation throws at run time.

.. code-block:: none
   :caption: Example

   5 - 2
   # => 3

.. expressions-operation-subtract-end


.. _expressions-category-date:

Date & time
--------------------------------------------------

.. expressions-category-date-start

Operations: :ref:`Add days <expressions-operation-add-days>`, :ref:`Date difference <expressions-operation-date-difference>`, :ref:`Date in last <expressions-operation-date-in-last>`, :ref:`Date in next <expressions-operation-date-in-next>`, :ref:`Day of week <expressions-operation-day-of-week>`, :ref:`Day of year <expressions-operation-day-of-year>`, :ref:`Subtract days <expressions-operation-subtract-days>`, :ref:`Timestamp difference <expressions-operation-timestamp-difference>`, :ref:`Timestamp from milliseconds <expressions-operation-timestamp-from-milliseconds>`, :ref:`Timestamp in last <expressions-operation-timestamp-in-last>`, :ref:`Timestamp in next <expressions-operation-timestamp-in-next>`, :ref:`Week of year <expressions-operation-week-of-year>`

.. expressions-category-date-end


.. _expressions-operation-add-days:

Add days
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-add-days-start

Written as **date_add(date, days)**, returning **date**. Adds the specified number of days to a date.

**date**
   Date. The starting date.

**days**
   Integer. Number of days to add.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   date_add(to_date('2024-01-15'), 30)
   # => to_date('2024-02-14')

.. expressions-operation-add-days-end


.. _expressions-operation-date-difference:

Date difference
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-date-difference-start

Written as **date_diff(start, end)**, returning **integer**. Returns the absolute number of days between two dates.

**start**
   Date. The first date.

**end**
   Date. The second date.

.. warning::
   Either date is NULL. This operation throws at run time.
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   date_diff(to_date('2024-01-15'), to_date('2024-01-18'))
   # => 3

.. expressions-operation-date-difference-end


.. _expressions-operation-date-in-last:

Date in last
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-date-in-last-start

Written as **date_in_last(days, date)**, returning **boolean**. Returns true if the date falls within the past ``n`` days of today. A value of zero matches only today, a value of one also matches yesterday, and so on.

**days**
   Integer. Number of days in the window.

**date**
   Date. The date to test.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. note:: Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   date_in_last(30, to_date('2024-01-15'))

.. expressions-operation-date-in-last-end


.. _expressions-operation-date-in-next:

Date in next
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-date-in-next-start

Written as **date_in_next(days, date)**, returning **boolean**. Returns true if the date falls within the next ``n`` days from today. A value of zero matches only today, a value of one also matches tomorrow, and so on.

**days**
   Integer. Number of days in the window.

**date**
   Date. The date to test.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. note:: Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   date_in_next(7, to_date('2024-01-15'))

.. expressions-operation-date-in-next-end


.. _expressions-operation-day-of-week:

Day of week
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-day-of-week-start

Written as **day_of_week(date)**, returning **integer**. Returns the ISO day of week for the date, from 1 for Monday through 7 for Sunday.

**date**
   Date. The date to evaluate.

.. warning::
   The date has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   day_of_week(to_date('2024-03-04')) >= 1
   # => true

.. expressions-operation-day-of-week-end


.. _expressions-operation-day-of-year:

Day of year
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-day-of-year-start

Written as **day_of_year(date)**, returning **integer**. Returns the day of the year for the date, from 1 to 366.

**date**
   Date. The date to evaluate.

.. warning::
   The date has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   day_of_year(to_date('2024-03-01'))
   # => 61

.. expressions-operation-day-of-year-end


.. _expressions-operation-subtract-days:

Subtract days
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-subtract-days-start

Written as **date_sub(date, days)**, returning **date**. Subtracts the specified number of days from a date.

**date**
   Date. The starting date.

**days**
   Integer. Number of days to subtract.

.. warning::
   An operand has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   date_sub(to_date('2024-01-15'), 7)
   # => to_date('2024-01-08')

.. expressions-operation-subtract-days-end


.. _expressions-operation-timestamp-difference:

Timestamp difference
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-difference-start

Written as **timestamp_diff(unit, timestamp, timestamp)**, returning **integer**. Returns the whole number of units between two timestamps.

**unit**
   String. A quoted, case-insensitive string literal: 'seconds', 'minutes' or 'hours'.

**timestamp**
   Datetime. The first timestamp.

**timestamp**
   Datetime. The second timestamp.

.. warning::
   Either timestamp is NULL. This operation throws at run time.
   The unit is not 'seconds', 'minutes', or 'hours'. This operation throws at run time.
   A timestamp has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   timestamp_diff('hours', to_timestamp('2024-01-15T00:00:00Z'), to_timestamp('2024-01-15T03:00:00Z'))
   # => 3

.. expressions-operation-timestamp-difference-end


.. _expressions-operation-timestamp-from-milliseconds:

Timestamp from milliseconds
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-from-milliseconds-start

Written as **timestamp_from_millis(millis)**, returning **datetime**. Coerces milliseconds since the Unix epoch (1970-01-01T00:00:00Z), given as a number, to a timestamp. Returns NULL for NULL, non-numeric, or out-of-range input.

For numeric epoch fields in event payloads (e.g. GA4 ``event_timestamp``) that ``:to-timestamp`` cannot parse.

**millis**
   Integer. Milliseconds since 1970-01-01T00:00:00Z.

.. warning::
   The value has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   timestamp_from_millis(0)
   # => to_timestamp('1970-01-01T00:00:00Z')

.. expressions-operation-timestamp-from-milliseconds-end


.. _expressions-operation-timestamp-in-last:

Timestamp in last
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-in-last-start

Written as **timestamp_in_last(n, unit, timestamp)**, returning **boolean**. Returns true if the timestamp falls within the past ``n`` units of the current time.

**n**
   Integer. Size of the window.

**unit**
   String. A quoted, case-insensitive string literal: 'seconds', 'minutes' or 'hours'.

**timestamp**
   Datetime. The timestamp to test.

.. warning::
   The window size is zero. This operation returns NULL.
   An operand has an unsupported type. This operation throws at run time.

.. note:: Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   timestamp_in_last(2, 'hours', to_timestamp('2024-01-15T00:00:00Z'))

.. expressions-operation-timestamp-in-last-end


.. _expressions-operation-timestamp-in-next:

Timestamp in next
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-in-next-start

Written as **timestamp_in_next(n, unit, timestamp)**, returning **boolean**. Returns true if the timestamp falls within the next ``n`` units from the current time.

**n**
   Integer. Size of the window.

**unit**
   String. A quoted, case-insensitive string literal: 'seconds', 'minutes' or 'hours'.

**timestamp**
   Datetime. The timestamp to test.

.. warning::
   The window size is zero. This operation returns NULL.
   An operand has an unsupported type. This operation throws at run time.

.. note:: Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   timestamp_in_next(2, 'hours', to_timestamp('2024-01-15T00:00:00Z'))

.. expressions-operation-timestamp-in-next-end


.. _expressions-operation-week-of-year:

Week of year
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-week-of-year-start

Written as **week_of_year(date)**, returning **integer**. Returns the ISO-8601 week of the week-based year for the date, from 1 to 53. Weeks start on Monday, and week 1 is the one containing the year's first Thursday.

**date**
   Date. The date to evaluate.

.. warning::
   The date has an unsupported type. This operation throws at run time.

.. code-block:: none
   :caption: Example

   week_of_year(to_date('2024-01-04'))
   # => 1

.. expressions-operation-week-of-year-end

.. ael-generated-end
