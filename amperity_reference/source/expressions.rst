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

*boolean* value **=** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-equal-start

Returns true if all operands are equal to each other.

.. code-block:: none
   :caption: Example

   1 = 1
   # => true

.. expressions-operation-equal-end


.. _expressions-operation-greater-than:

*boolean* value **>** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-greater-than-start

Returns true if each operand is greater than the operand that follows it.

.. warning::

   Throws an error if the operands are not comparable.

.. code-block:: none
   :caption: Example

   3 > 2
   # => true

.. expressions-operation-greater-than-end


.. _expressions-operation-greater-than-or-equal:

*boolean* value **>=** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-greater-than-or-equal-start

Returns true if each operand is greater than or equal to the operand that follows it.

.. warning::

   Throws an error if the operands are not comparable.

.. code-block:: none
   :caption: Example

   2 >= 2
   # => true

.. expressions-operation-greater-than-or-equal-end


.. _expressions-operation-less-than:

*boolean* value **<** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-less-than-start

Returns true if each operand is less than the operand that follows it.

.. warning::

   Throws an error if the operands are not comparable.

.. code-block:: none
   :caption: Example

   1 < 2
   # => true

.. expressions-operation-less-than-end


.. _expressions-operation-less-than-or-equal:

*boolean* value **<=** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-less-than-or-equal-start

Returns true if each operand is less than or equal to the operand that follows it.

.. warning::

   Throws an error if the operands are not comparable.

.. code-block:: none
   :caption: Example

   2 <= 2
   # => true

.. expressions-operation-less-than-or-equal-end


.. _expressions-operation-not-equal:

*boolean* value **!=** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-not-equal-start

Returns true if at least one operand is not equal to the others.

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

*boolean* value **AND** value **AND** ...
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-and-start

Returns true if all operands are truthy. Short-circuits evaluation on the first falsey value.

.. note::

   Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   is_active AND has_subscription

.. expressions-operation-and-end


.. _expressions-operation-not:

*boolean* **NOT** value
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-not-start

Returns true if the operand is falsey.

.. code-block:: none
   :caption: Example

   NOT is_active

.. expressions-operation-not-end


.. _expressions-operation-or:

*boolean* value **OR** value **OR** ...
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-or-start

Returns true if any operand is truthy. Short-circuits evaluation on the first truthy value.

.. note::

   Operands after the selected branch are not evaluated.

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

*boolean* value **IS NOT NULL**
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-is-not-null-start

Returns true if the operand is not null.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   'email' IS NOT NULL
   # => true

.. expressions-operation-is-not-null-end


.. _expressions-operation-is-null:

*boolean* value **IS NULL**
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-is-null-start

Returns true if the operand is null.

.. warning::

   Throws an error if an operand has an unsupported type.

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

*any* **case**\ (value, match, result, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-case-start

Selects a result based on matching a test value against possible cases.

**value**
   *Any*. The value to match against.

**match**
   *Any*, :bdg-muted:`Repeatable`. A candidate value.

**result**
   *Any*, :bdg-muted:`Repeatable`. Result returned when the candidate matches.

.. note::

   Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   case('GOLD', 'GOLD', 0.2, 'SILVER', 0.1, 0.05)
   # => 0.2

.. expressions-operation-case-end


.. _expressions-operation-coalesce:

*any* **coalesce**\ (value, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-coalesce-start

Evaluates operands in order, returning the first non-NULL operand.

**value**
   *Any*, :bdg-muted:`Repeatable`. A value to consider.

.. note::

   Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   coalesce(NULL, NULL, 'there')
   # => 'there'

.. expressions-operation-coalesce-end


.. _expressions-operation-condition:

*any* **cond**\ (predicate, result, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-condition-start

Evaluates predicates in order, returning the result paired with the first true predicate.

**predicate**
   *Boolean*, :bdg-muted:`Repeatable`. A predicate to evaluate in order.

**result**
   *Any*, :bdg-muted:`Repeatable`. Result returned when the predicate is true.

.. note::

   Operands after the selected branch are not evaluated.

.. code-block:: none
   :caption: Example

   cond('GOLD' = 'GOLD', 0.2, 'SILVER' = 'GOLD', 0.1, 0.05)
   # => 0.2

.. expressions-operation-condition-end


.. _expressions-operation-if:

*any* **if**\ (condition, then, else)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-if-start

Returns the second operand if the first operand (condition) is true, otherwise returns the third operand. NULL conditions are treated as false.

**condition**
   *Boolean*. The condition to test.

**then**
   *Any*. Result when the condition is true.

**else**
   *Any*. Result when the condition is false.

.. note::

   Operands after the selected branch are not evaluated.

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

*boolean* **to_boolean**\ (value)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-boolean-start

Coerces a value to boolean. Returns NULL if coercion is not possible.

**value**
   *Any*. The value to coerce.

.. warning::

   Throws an error if the value has an unsupported type.

.. code-block:: none
   :caption: Example

   to_boolean('true')
   # => true

.. expressions-operation-to-boolean-end


.. _expressions-operation-to-date:

*date* **to_date**\ (value, format)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-date-start

Coerces a value to date. Returns NULL if coercion is not possible.

**value**
   *Any*. The value to coerce.

**format**
   *String*, :bdg-muted:`Optional`. Optional date parse format.

.. note::

   Returns NULL if the format pattern is invalid.

.. code-block:: none
   :caption: Example

   to_date('2024-01-15', 'yyyy-MM-dd')
   # => to_date('2024-01-15')

.. expressions-operation-to-date-end


.. _expressions-operation-to-decimal:

*decimal* **to_decimal**\ (value, precision, scale)
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-decimal-start

Coerces a value to big decimal, with precision 38 and scale 2 by default. The optional precision and scale parameters must be integer literals. Returns NULL if the coerced value is wider than the precision.

**value**
   *Any*. The value to coerce.

**precision**
   *Integer*, :bdg-muted:`Optional`. Optional decimal precision, 1 to 38. Must be a literal number.

**scale**
   *Integer*, :bdg-muted:`Optional`. Optional decimal scale, 0 to the precision. Must be a literal number.

.. code-block:: none
   :caption: Example

   to_decimal('12.345', 10, 2)
   # => to_decimal('12.35')

.. expressions-operation-to-decimal-end


.. _expressions-operation-to-float:

*float* **to_float**\ (value)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-float-start

Coerces a value to float. Returns NULL if coercion is not possible.

**value**
   *Any*. The value to coerce.

.. warning::

   Throws an error if the value has an unsupported type.

.. code-block:: none
   :caption: Example

   to_float('12.5')
   # => 12.5

.. expressions-operation-to-float-end


.. _expressions-operation-to-integer:

*integer* **to_int**\ (value)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-integer-start

Coerces a value to a 64-bit integer. Returns NULL if coercion is not possible.

**value**
   *Any*. The value to coerce.

.. warning::

   Throws an error if the value has an unsupported type.

.. code-block:: none
   :caption: Example

   to_int('12.9')
   # => 12

.. expressions-operation-to-integer-end


.. _expressions-operation-to-string:

*string* **to_string**\ (value)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-string-start

Converts a value to string. Returns NULL if the input is NULL.

**value**
   *Any*. The value to convert.

.. warning::

   Throws an error if the value has an unsupported type.

.. code-block:: none
   :caption: Example

   to_string(123)
   # => '123'

.. expressions-operation-to-string-end


.. _expressions-operation-to-timestamp:

*datetime* **to_timestamp**\ (value, format)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-to-timestamp-start

Coerces a value to timestamp. Returns NULL if coercion is not possible.

**value**
   *Any*. The value to coerce.

**format**
   *String*, :bdg-muted:`Optional`. Optional timestamp parse format.

.. note::

   Returns NULL if the format pattern is invalid.

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

*array* **array**\ (value, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-array-start

Returns an array of operands in order. All operands must be of the same type.

**value**
   *Any*, :bdg-muted:`Repeatable`. An array element.

.. code-block:: none
   :caption: Example

   array(1, 2, 3)
   # => array(1, 2, 3)

.. expressions-operation-array-end


.. _expressions-operation-array-struct-or-map-lookup:

*any* value[key]
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-array-struct-or-map-lookup-start

Gets an integer offset from an array, a field from a struct, or an arbitrary key from a map.

.. note::

   Returns NULL if the index is negative or outside the array bounds.

.. code-block:: none
   :caption: Example

   array('sku')[0]
   # => 'sku'

.. expressions-operation-array-struct-or-map-lookup-end


.. _expressions-operation-average-array:

*number* **array_avg**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-average-array-start

Returns the mean of the input array's non-NULL elements, which must be numeric. Returns NULL if the input is NULL, empty, or holds only NULLs, matching the ``average`` aggregation over zero records.

Also accepts the name **array_average**.

**array**
   *Array*. The array of numbers to average. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_avg(array(1, 2, 4))
   # => 2.3333333333333335

.. expressions-operation-average-array-end


.. _expressions-operation-count-by-value:

*array* **array_counts**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-count-by-value-start

Returns a frequency table for the input array: an array of structs with a ``value`` field holding each distinct non-NULL element and a ``count`` field holding how many times it occurs. Ordered by count descending, then by the natural sort order of the value, matching the ``mode`` aggregation's tie-break. NULL elements are not counted. Returns NULL if the input is NULL, and an empty array if the input is empty or holds only NULLs.

**array**
   *Array*. The array to tally. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   take(array_counts(array('wool', 'silk', 'wool')), 2)
   # => array(map('value', 'wool', 'count', 2), map('value', 'silk', 'count', 1))

.. expressions-operation-count-by-value-end


.. _expressions-operation-difference:

*array* **difference**\ (source, remove)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-difference-start

Returns the elements of the first array that are not present in the second array, preserving the order and duplicates of the first array. A NULL second operand removes nothing, so ``difference(a, NULL)`` is ``a``. SparkSQL spells this ``array_except`` and removes duplicates; that spelling is not accepted here.

**source**
   *Array*. The source array.

**remove**
   *Array*. The array of elements to remove.

.. code-block:: none
   :caption: Example

   difference(array('spring', 'summer'), array('summer'))
   # => array('spring')

.. expressions-operation-difference-end


.. _expressions-operation-distinct:

*array* **distinct**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-distinct-start

Returns the input array with duplicate elements removed, preserving the order of first occurrence.

**array**
   *Array*. The array to deduplicate.

.. code-block:: none
   :caption: Example

   distinct(array('spring', 'spring', 'summer'))
   # => array('spring', 'summer')

.. expressions-operation-distinct-end


.. _expressions-operation-filter:

*array* **filter**\ (array, element -> predicate)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-filter-start

Filters an array using a function that takes one argument (which will be bound to each element in the array, in order) and returns a boolean. Returns an array containing only the elements for which the function returned true.

**array**
   *Array*. The array to filter.

**function**
   *Function*. A one-argument function whose argument is bound to each element in turn, and which returns a boolean.

.. code-block:: none
   :caption: Example

   filter(array('ON', 'OFF'), x -> x = 'ON')
   # => array('ON')

.. expressions-operation-filter-end


.. _expressions-operation-get-element:

*any* **get**\ (array, index)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-get-element-start

Returns the element of the input array at the given (0-based) index. If the index points outside of the array boundaries, or if the index is negative, then this function returns NULL.

**array**
   *Array*. The array to index into.

**index**
   *Integer*. The 0-based index.

.. code-block:: none
   :caption: Example

   get(array('Merino', 'wool'), 0)
   # => 'Merino'

.. expressions-operation-get-element-end


.. _expressions-operation-in:

*boolean* value **IN** (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-in-start

Returns true if the value is one of the listed values. The right operand is a parenthesized list written into the expression, not a field holding an array; to test membership of an array-valued field, use ``size(filter(field, x -> x = value)) > 0``, or ``size(array_intersect(a, b)) > 0`` when both sides are arrays in the record.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   'GOLD' IN ('GOLD', 'PLATINUM')
   # => true

.. expressions-operation-in-end


.. _expressions-operation-intersect-arrays:

*array* **array_intersect**\ (source, keep)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-intersect-arrays-start

Returns the elements present in both arrays, with duplicates removed, in the order they first appear in the first array. Returns NULL if either operand is NULL. Matches SparkSQL's ``array_intersect`` on all three points.

**source**
   *Array*. The source array.

**keep**
   *Array*. The array of elements to keep.

.. code-block:: none
   :caption: Example

   array_intersect(array('a', 'b'), array('b', 'c'))
   # => array('b')

.. expressions-operation-intersect-arrays-end


.. _expressions-operation-map:

*map* **map**\ (key, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-map-start

Returns a map of the given key/value pairs. All keys and all values must be of the same type.

**key**
   *Any*, :bdg-muted:`Repeatable`. A map key.

**value**
   *Any*, :bdg-muted:`Repeatable`. A map value.

.. code-block:: none
   :caption: Example

   map('sku', 'ABC', 'brand', 'Wool')
   # => map('sku', 'ABC', 'brand', 'Wool')

.. expressions-operation-map-end


.. _expressions-operation-maximum-of-array:

*any* **array_max**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-maximum-of-array-start

Returns the largest of the input array's non-NULL elements. Unlike the scalar ``max``, the elements need only be orderable, so arrays of strings, dates, and timestamps are supported. Returns NULL if the input is NULL, empty, or holds only NULLs.

**array**
   *Array*. The array to take the maximum of. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_max(array(1, 2, 3))
   # => 3

.. expressions-operation-maximum-of-array-end


.. _expressions-operation-minimum-of-array:

*any* **array_min**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-minimum-of-array-start

Returns the smallest of the input array's non-NULL elements. Unlike the scalar ``min``, the elements need only be orderable, so arrays of strings, dates, and timestamps are supported. Returns NULL if the input is NULL, empty, or holds only NULLs.

**array**
   *Array*. The array to take the minimum of. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_min(array(1, 2, 3))
   # => 1

.. expressions-operation-minimum-of-array-end


.. _expressions-operation-most-common-element:

*any* **array_mode**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-most-common-element-start

Returns the most frequently occurring element of the input array, or NULL if the input is NULL or contains no non-NULL elements. NULL elements are not counted. Ties are broken by the natural sort order of the tied elements, matching the ``mode`` aggregation.

**array**
   *Array*. The array to reduce. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_mode(array('wool', 'silk', 'wool'))
   # => 'wool'

.. expressions-operation-most-common-element-end


.. _expressions-operation-named-struct:

*struct* **named_struct**\ (key, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-named-struct-start

Returns a struct with the given field names and values. Each name must be written as text, must be a valid field name, and may not be repeated.

**key**
   *String*, :bdg-muted:`Repeatable`. A struct field name, written directly as text. Letters, numbers, and underscores, with at least one letter or underscore, and unique within the struct.

**value**
   *Any*, :bdg-muted:`Repeatable`. A struct field value.

.. code-block:: none
   :caption: Example

   named_struct('sku', 'ABC', 'count', 2)
   # => map('sku', 'ABC', 'count', 2)

.. expressions-operation-named-struct-end


.. _expressions-operation-not-in:

*boolean* value **NOT IN** (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-not-in-start

Returns true if the value is none of the listed values. The right operand is a parenthesized list written into the expression, not a field holding an array; to test membership of an array-valued field, use ``size(filter(field, x -> x = value)) = 0``.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   'SILVER' NOT IN ('GOLD', 'PLATINUM')
   # => true

.. expressions-operation-not-in-end


.. _expressions-operation-size:

*integer* **size**\ (collection)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-size-start

Returns the integer element count of the operand, or NULL if the operand is NULL.

**collection**
   *Array*. The collection to measure.

.. warning::

   Throws an error if the operand is not a collection.

.. code-block:: none
   :caption: Example

   size(array('Merino', 'wool'))
   # => 2

.. expressions-operation-size-end


.. _expressions-operation-skip-first:

*array* **skip**\ (array, offset)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-skip-first-start

Returns the input array without its first ``offset`` elements. An ``offset`` at or past the end of the array returns an empty array. Returns NULL if either operand is NULL or if ``offset`` is negative. Compose with ``take`` for a window out of the middle: ``take(skip(arr, 1), 2)``.

**array**
   *Array*. The array to skip into.

**offset**
   *Integer*. How many leading elements to skip.

.. code-block:: none
   :caption: Example

   skip(array(1, 2, 3), 1)
   # => array(2, 3)

.. expressions-operation-skip-first-end


.. _expressions-operation-sort-array:

*array* **array_sort**\ (array, comparator)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-sort-array-start

Sorts the input array, ascending by default, placing NULL elements at the end and ordering NaN above every other float. A comparator sorts by any other order: it takes two elements and returns a negative number, zero, or a positive number as the first sorts before, with, or after the second, and returning NULL from it fails the expression. An array of structs has no default order, so it requires a comparator.

**array**
   *Array*. The array to sort.

**comparator**
   *Function*, :bdg-muted:`Optional`. Optional two-argument comparator function.

.. warning::

   Throws an error if a comparator returns NULL.

.. code-block:: none
   :caption: Example

   array_sort(array(3, 1, 2))
   # => array(1, 2, 3)

.. expressions-operation-sort-array-end


.. _expressions-operation-struct-or-map-field:

*any* value.key
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-struct-or-map-field-start

Gets a field from a struct, or a string key from a map.

.. code-block:: none
   :caption: Example

   map('city', 'Seattle').city
   # => 'Seattle'

.. expressions-operation-struct-or-map-field-end


.. _expressions-operation-sum-array:

*number* **array_sum**\ (array)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-sum-array-start

Returns the sum of the input array's non-NULL elements, which must be numeric. Returns 0 for an empty array or one holding only NULLs, matching the ``sum`` aggregation over zero records. Returns NULL if the input is NULL.

**array**
   *Array*. The array of numbers to add. For an array of structs, extract a field first with transform().

.. code-block:: none
   :caption: Example

   array_sum(array(1, 2, 3))
   # => 6

.. expressions-operation-sum-array-end


.. _expressions-operation-take-first:

*array* **take**\ (array, limit)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-take-first-start

Returns the first ``limit`` elements of the input array. A ``limit`` longer than the array returns the whole array, and a ``limit`` of zero returns an empty array. Returns NULL if either operand is NULL or if ``limit`` is negative.

**array**
   *Array*. The array to take from.

**limit**
   *Integer*. How many elements to take.

.. code-block:: none
   :caption: Example

   take(array(1, 2, 3), 2)
   # => array(1, 2)

.. expressions-operation-take-first-end


.. _expressions-operation-transform:

*array* **transform**\ (array, element -> expression)
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-transform-start

Transforms an array using a function that takes each element of the array, in order, and returns a new value. Returns an array of the values returned by the function. The function may take an optional second argument, which will be bound to the zero-based index of the element.

**array**
   *Array*. The array to transform.

**function**
   *Function*. A function whose first argument is bound to each element in turn. An optional second argument is bound to that element's 0-based index: (element, index) -> expression.

.. code-block:: none
   :caption: Example

   transform(array('wool', 'silk'), x -> upper(x))
   # => array('WOOL', 'SILK')

.. expressions-operation-transform-end


.. _expressions-operation-union:

*array* **union**\ (array, array, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-union-start

Concatenates two or more arrays into a single array, preserving order and keeping duplicate elements. All operands must be arrays of primitive or flat-struct elements with a common element type. NULL operands are skipped rather than propagated, so ``union(a, NULL)`` is ``a``. SparkSQL spells this ``array_union`` and removes duplicates; that spelling is not accepted here.

**array**
   *Array*, :bdg-muted:`Repeatable`. An array to concatenate.

.. code-block:: none
   :caption: Example

   union(array('spring'), array('summer'))
   # => array('spring', 'summer')

.. expressions-operation-union-end


.. _expressions-operation-zip-arrays:

*array* **array_zip**\ (name, array, name, array, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-zip-arrays-start

Combines two or more arrays element-wise into an array of structs. Shorter arrays are padded with NULL, so the result length is that of the longest input, and the result is NULL if any input array is NULL -- both as in SparkSQL's ``arrays_zip``. Operands alternate between a field name and the array supplying that field's values, as in ``named_struct``: SparkSQL derives struct field names from the input column names, and an AEL operand is an expression with no name to derive.

**name**
   *String*, :bdg-muted:`Repeatable`. A struct field name, written directly as text.

**array**
   *Array*, :bdg-muted:`Repeatable`. The array supplying that field's values.

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

*string* **concat**\ (value, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-concatenate-start

Concatenates operands together with no spaces/separator.

**value**
   *String*, :bdg-muted:`Repeatable`. A value to join.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   concat('Merino', ' ', 'wool')
   # => 'Merino wool'

.. expressions-operation-concatenate-end


.. _expressions-operation-concatenate-with-separator:

*string* **concat_ws**\ (separator, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-concatenate-with-separator-start

Concatenates operands together. The first operand should be a (possibly empty) separator string.

**separator**
   *String*. The separator placed between values.

**value**
   *String*, :bdg-muted:`Repeatable`. A value to join.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   concat_ws('-', 'Merino', 'wool')
   # => 'Merino-wool'

.. expressions-operation-concatenate-with-separator-end


.. _expressions-operation-contains:

*boolean* **contains**\ (string, substring)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-contains-start

Returns true if the first operand string contains the second operand string.

**string**
   *String*. The string to search.

**substring**
   *String*. The substring to look for.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   contains('Merino wool blend', 'Merino')
   # => true

.. expressions-operation-contains-end


.. _expressions-operation-ends-with:

*boolean* **endswith**\ (string, suffix)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-ends-with-start

Returns true if the first operand string ends with the second operand string.

**string**
   *String*. The string to test.

**suffix**
   *String*. The suffix to look for.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   endswith('receipt@example.com', '@example.com')
   # => true

.. expressions-operation-ends-with-end


.. _expressions-operation-lowercase:

*string* **lower**\ (string)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-lowercase-start

Converts the operand string to lower case.

**string**
   *String*. The string to convert.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   lower('Merino')
   # => 'merino'

.. expressions-operation-lowercase-end


.. _expressions-operation-replace:

*string* **replace**\ (string, search, replacement)
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-replace-start

Replaces all occurrences of the second operand string in the first operand string with the third operand string.

**string**
   *String*. The string to operate on.

**search**
   *String*. The substring to replace.

**replacement**
   *String*, :bdg-muted:`Optional`. The replacement substring.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   replace('555-1234', '-', '')
   # => '5551234'

.. expressions-operation-replace-end


.. _expressions-operation-sha-2-hash:

*string* **sha2**\ (string, bits)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-sha-2-hash-start

Returns a checksum of SHA-2 family as a hex string of expr. SHA-224, SHA-256, SHA-384, and SHA-512 are supported. Bit length of 0 is equivalent to 256.

**string**
   *String*. The string to hash.

**bits**
   *Integer*. Bit length: 224, 256, 384 or 512 (0 means 256).

.. note::

   Returns NULL if the bit length is not 0, 224, 256, 384, or 512.

.. code-block:: none
   :caption: Example

   sha2('abc', 256)
   # => 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'

.. expressions-operation-sha-2-hash-end


.. _expressions-operation-split:

*array* **split**\ (string, delimiter)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-split-start

Splits the first operand string on each literal occurrence of the second operand string, returning an array of strings. The delimiter is matched literally, not as a regular expression. Empty trailing elements are preserved, so the result length is stable for fixed-shape values. An empty delimiter splits the string into one element per code point, matching SparkSQL.

**string**
   *String*. The string to split.

**delimiter**
   *String*. The literal delimiter to split on. An empty delimiter splits into single characters.

.. code-block:: none
   :caption: Example

   split('Merino wool', ' ')[0]
   # => 'Merino'

.. expressions-operation-split-end


.. _expressions-operation-starts-with:

*boolean* **startswith**\ (string, prefix)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-starts-with-start

Returns true if the first operand string starts with the second operand string.

**string**
   *String*. The string to test.

**prefix**
   *String*. The prefix to look for.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   startswith('Merino wool blend', 'Merino')
   # => true

.. expressions-operation-starts-with-end


.. _expressions-operation-uppercase:

*string* **upper**\ (string)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-uppercase-start

Converts the operand string to upper case.

**string**
   *String*. The string to convert.

.. warning::

   Throws an error if an operand has an unsupported type.

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

*number* **abs**\ (number)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-absolute-value-start

Returns the absolute value of the operand.

**number**
   *Number*. The number whose absolute value to return.

.. warning::

   Throws an error if the operand is NULL.

.. code-block:: none
   :caption: Example

   abs(-5)
   # => 5

.. expressions-operation-absolute-value-end


.. _expressions-operation-add:

*number* value **+** value **+** ...
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-add-start

Adds operands.

.. warning::

   Throws an error if the operands exceed the numeric range the operation supports.

.. code-block:: none
   :caption: Example

   1 + 2
   # => 3

.. expressions-operation-add-end


.. _expressions-operation-divide:

*number* value **/** value **/** ...
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-divide-start

Divides operands. Treats division by zero as a NULL result.

.. note::

   Returns NULL if a divisor is zero.

.. code-block:: none
   :caption: Example

   6 / 2
   # => 3.0

.. expressions-operation-divide-end


.. _expressions-operation-maximum:

*number* **max**\ (value, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-maximum-start

Returns the maximum value from operands, ignoring NULL values.

**value**
   *Number*, :bdg-muted:`Repeatable`. A value to compare.

.. code-block:: none
   :caption: Example

   max(3, 1)
   # => 3

.. expressions-operation-maximum-end


.. _expressions-operation-minimum:

*number* **min**\ (value, value, ...)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-minimum-start

Returns the minimum value from operands, ignoring NULL values.

**value**
   *Number*, :bdg-muted:`Repeatable`. A value to compare.

.. code-block:: none
   :caption: Example

   min(3, 1)
   # => 1

.. expressions-operation-minimum-end


.. _expressions-operation-modulus:

*number* dividend **%** divisor
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-modulus-start

Returns the modulus of the first operand divided by the second operand.

Also accepts the name **mod**.

.. warning::

   Throws an error if either operand is NULL or the divisor is zero.

.. code-block:: none
   :caption: Example

   10 % 3
   # => 1

.. expressions-operation-modulus-end


.. _expressions-operation-multiply:

*number* value **\*** value **\*** ...
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-multiply-start

Multiplies operands.

.. warning::

   Throws an error if the operands exceed the numeric range the operation supports.

.. code-block:: none
   :caption: Example

   3 * 4
   # => 12

.. expressions-operation-multiply-end


.. _expressions-operation-subtract:

*number* value **-** value **-** ...
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-subtract-start

Subtracts operands.

.. warning::

   Throws an error if the operands exceed the numeric range the operation supports.

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

*date* **date_add**\ (date, days)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-add-days-start

Adds the specified number of days to a date.

**date**
   *Date*. The starting date.

**days**
   *Integer*. Number of days to add.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   date_add(to_date('2024-01-15'), 30)
   # => to_date('2024-02-14')

.. expressions-operation-add-days-end


.. _expressions-operation-date-difference:

*integer* **date_diff**\ (start, end)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-date-difference-start

Returns the absolute number of days between two dates.

**start**
   *Date*. The first date.

**end**
   *Date*. The second date.

.. warning::

   Throws an error if either date is NULL or an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   date_diff(to_date('2024-01-15'), to_date('2024-01-18'))
   # => 3

.. expressions-operation-date-difference-end


.. _expressions-operation-date-in-last:

*boolean* **date_in_last**\ (days, date)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-date-in-last-start

Returns true if the date falls within the past ``n`` days of today. A value of zero matches only today, a value of one also matches yesterday, and so on.

**days**
   *Integer*. Number of days in the window.

**date**
   *Date*. The date to test.

.. warning::

   Throws an error if an operand has an unsupported type.

.. note::

   Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   date_in_last(30, to_date('2024-01-15'))

.. expressions-operation-date-in-last-end


.. _expressions-operation-date-in-next:

*boolean* **date_in_next**\ (days, date)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-date-in-next-start

Returns true if the date falls within the next ``n`` days from today. A value of zero matches only today, a value of one also matches tomorrow, and so on.

**days**
   *Integer*. Number of days in the window.

**date**
   *Date*. The date to test.

.. warning::

   Throws an error if an operand has an unsupported type.

.. note::

   Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   date_in_next(7, to_date('2024-01-15'))

.. expressions-operation-date-in-next-end


.. _expressions-operation-day-of-week:

*integer* **day_of_week**\ (date)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-day-of-week-start

Returns the ISO day of week for the date, from 1 for Monday through 7 for Sunday.

**date**
   *Date*. The date to evaluate.

.. warning::

   Throws an error if the date has an unsupported type.

.. code-block:: none
   :caption: Example

   day_of_week(to_date('2024-03-04')) >= 1
   # => true

.. expressions-operation-day-of-week-end


.. _expressions-operation-day-of-year:

*integer* **day_of_year**\ (date)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-day-of-year-start

Returns the day of the year for the date, from 1 to 366.

**date**
   *Date*. The date to evaluate.

.. warning::

   Throws an error if the date has an unsupported type.

.. code-block:: none
   :caption: Example

   day_of_year(to_date('2024-03-01'))
   # => 61

.. expressions-operation-day-of-year-end


.. _expressions-operation-subtract-days:

*date* **date_sub**\ (date, days)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-subtract-days-start

Subtracts the specified number of days from a date.

**date**
   *Date*. The starting date.

**days**
   *Integer*. Number of days to subtract.

.. warning::

   Throws an error if an operand has an unsupported type.

.. code-block:: none
   :caption: Example

   date_sub(to_date('2024-01-15'), 7)
   # => to_date('2024-01-08')

.. expressions-operation-subtract-days-end


.. _expressions-operation-timestamp-difference:

*integer* **timestamp_diff**\ (unit, timestamp, timestamp)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-difference-start

Returns the whole number of units between two timestamps.

**unit**
   *String*. A quoted, case-insensitive string literal: 'seconds', 'minutes' or 'hours'.

**timestamp**
   *Datetime*. The first timestamp.

**timestamp**
   *Datetime*. The second timestamp.

.. warning::

   Throws an error if:

   - either timestamp is NULL
   - the unit is not one of ``seconds``, ``minutes``, or ``hours``
   - a timestamp has an unsupported type

.. code-block:: none
   :caption: Example

   timestamp_diff('hours', to_timestamp('2024-01-15T00:00:00Z'), to_timestamp('2024-01-15T03:00:00Z'))
   # => 3

.. expressions-operation-timestamp-difference-end


.. _expressions-operation-timestamp-from-milliseconds:

*datetime* **timestamp_from_millis**\ (millis)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-from-milliseconds-start

Coerces milliseconds since the Unix epoch (1970-01-01T00:00:00Z), given as a number, to a timestamp. Returns NULL for NULL, non-numeric, or out-of-range input.

For numeric epoch fields in event payloads (e.g. GA4 ``event_timestamp``) that ``:to-timestamp`` cannot parse.

**millis**
   *Integer*. Milliseconds since 1970-01-01T00:00:00Z.

.. warning::

   Throws an error if the value has an unsupported type.

.. code-block:: none
   :caption: Example

   timestamp_from_millis(0)
   # => to_timestamp('1970-01-01T00:00:00Z')

.. expressions-operation-timestamp-from-milliseconds-end


.. _expressions-operation-timestamp-in-last:

*boolean* **timestamp_in_last**\ (n, unit, timestamp)
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-in-last-start

Returns true if the timestamp falls within the past ``n`` units of the current time.

**n**
   *Integer*. Size of the window.

**unit**
   *String*. A quoted, case-insensitive string literal: 'seconds', 'minutes' or 'hours'.

**timestamp**
   *Datetime*. The timestamp to test.

.. warning::

   Throws an error if an operand has an unsupported type.

   Returns NULL if the window size is zero.

.. note::

   Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   timestamp_in_last(2, 'hours', to_timestamp('2024-01-15T00:00:00Z'))

.. expressions-operation-timestamp-in-last-end


.. _expressions-operation-timestamp-in-next:

*boolean* **timestamp_in_next**\ (n, unit, timestamp)
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-timestamp-in-next-start

Returns true if the timestamp falls within the next ``n`` units from the current time.

**n**
   *Integer*. Size of the window.

**unit**
   *String*. A quoted, case-insensitive string literal: 'seconds', 'minutes' or 'hours'.

**timestamp**
   *Datetime*. The timestamp to test.

.. warning::

   Throws an error if an operand has an unsupported type.

   Returns NULL if the window size is zero.

.. note::

   Evaluated against the current time, so the result changes as time passes.

.. code-block:: none
   :caption: Example

   timestamp_in_next(2, 'hours', to_timestamp('2024-01-15T00:00:00Z'))

.. expressions-operation-timestamp-in-next-end


.. _expressions-operation-week-of-year:

*integer* **week_of_year**\ (date)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. expressions-operation-week-of-year-start

Returns the ISO-8601 week of the week-based year for the date, from 1 to 53. Weeks start on Monday, and week 1 is the one containing the year's first Thursday.

**date**
   *Date*. The date to evaluate.

.. warning::

   Throws an error if the date has an unsupported type.

.. code-block:: none
   :caption: Example

   week_of_year(to_date('2024-01-04'))
   # => 1

.. expressions-operation-week-of-year-end

.. ael-generated-end
