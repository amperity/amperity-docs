.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The Amperity Expression Language (AEL) reference for configuring real-time event streams, event types, and real-time segments and attributes.

.. meta::
    :content class=swiftype name=body data-type=text:
        The Amperity Expression Language (AEL) reference for configuring real-time event streams, event types, and real-time segments and attributes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Expressions for real-time

Expressions for real-time
==================================================

.. realtime-expressions-intro-start

Amperity Expression Language (AEL) defines how real-time events and profiles are recognized, filtered, and computed. This page is the reference for the AEL operations used to configure real-time event streams, event types, real-time segments, and real-time attributes.

The catalog is shared by the expression evaluator and the expression editor, so the syntax and metadata shown here stay aligned with the product.

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


.. _ael-reference-syntax:

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

Function calls use the function name followed by comma-separated operands. Operators use the source syntax shown in each reference entry. String literals use single quotes, and the values ``TRUE``, ``FALSE``, and ``NULL`` are available as literals.

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


.. _ael-reference-categories:

.. _realtime-expressions-more:

Complete AEL operation reference
==================================================

.. realtime-expressions-more-start

This page includes the complete AEL operation catalog. Each operation documents its AEL syntax, behavior, return type, accepted arity, and parameters.

.. realtime-expressions-more-end

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Category
     - Operations
   * - :ref:`Conditional <ael-category-conditional>`
     - :ref:`Coalesce <ael-operation-coalesce>`, :ref:`Case <ael-operation-case>`, :ref:`Condition <ael-operation-cond>`, :ref:`If <ael-operation-if>`
   * - :ref:`Comparison <ael-category-comparison>`
     - :ref:`Equal <ael-operation-equal>`, :ref:`Not equal <ael-operation-not-equal>`, :ref:`Less than <ael-operation-less-than>`, :ref:`Less than or equal <ael-operation-less-than-or-equal>`, :ref:`Greater than <ael-operation-greater-than>`, :ref:`Greater than or equal <ael-operation-greater-than-or-equal>`
   * - :ref:`Logical <ael-category-logical>`
     - :ref:`And <ael-operation-and>`, :ref:`Or <ael-operation-or>`, :ref:`Not <ael-operation-not>`
   * - :ref:`Numeric <ael-category-numeric>`
     - :ref:`Add <ael-operation-add>`, :ref:`Subtract <ael-operation-subtract>`, :ref:`Divide <ael-operation-divide>`, :ref:`Multiply <ael-operation-multiply>`, :ref:`Absolute value <ael-operation-abs>`, :ref:`Modulus <ael-operation-modulus>`, :ref:`Minimum <ael-operation-min>`, :ref:`Maximum <ael-operation-max>`
   * - :ref:`String <ael-category-string>`
     - :ref:`Starts with <ael-operation-startswith>`, :ref:`Ends with <ael-operation-endswith>`, :ref:`Contains <ael-operation-contains>`, :ref:`Replace <ael-operation-replace>`, :ref:`Lowercase <ael-operation-lower>`, :ref:`Uppercase <ael-operation-upper>`, :ref:`Concatenate <ael-operation-concat>`, :ref:`Concatenate with separator <ael-operation-concat-ws>`, :ref:`Split <ael-operation-split>`, :ref:`SHA-2 hash <ael-operation-sha2>`
   * - :ref:`Date and time <ael-category-date>`
     - :ref:`Add days <ael-operation-date-add>`, :ref:`Subtract days <ael-operation-date-sub>`, :ref:`Date difference <ael-operation-date-diff>`, :ref:`Date in last <ael-operation-date-in-last>`, :ref:`Date in next <ael-operation-date-in-next>`, :ref:`Timestamp difference <ael-operation-timestamp-diff>`, :ref:`Timestamp in last <ael-operation-timestamp-in-last>`, :ref:`Timestamp in next <ael-operation-timestamp-in-next>`, :ref:`Day of year <ael-operation-day-of-year>`, :ref:`Day of week <ael-operation-day-of-week>`, :ref:`Week of year <ael-operation-week-of-year>`, :ref:`Timestamp from milliseconds <ael-operation-timestamp-from-millis>`
   * - :ref:`Type conversion <ael-category-cast>`
     - :ref:`To boolean <ael-operation-to-boolean>`, :ref:`To integer <ael-operation-to-int>`, :ref:`To float <ael-operation-to-float>`, :ref:`To decimal <ael-operation-to-decimal>`, :ref:`To date <ael-operation-to-date>`, :ref:`To timestamp <ael-operation-to-timestamp>`, :ref:`To string <ael-operation-to-string>`
   * - :ref:`Collection <ael-category-collection>`
     - :ref:`In <ael-operation-in>`, :ref:`Not in <ael-operation-not-in>`, :ref:`Size <ael-operation-size>`, :ref:`Get element <ael-operation-get>`, :ref:`Array <ael-operation-array>`, :ref:`Map <ael-operation-map>`, :ref:`Named struct <ael-operation-named-struct>`, :ref:`Struct or map field <ael-operation-field-access>`, :ref:`Array, struct, or map lookup <ael-operation-indexed-access>`, :ref:`Filter <ael-operation-filter>`, :ref:`Transform <ael-operation-transform>`, :ref:`Sort array <ael-operation-array-sort>`, :ref:`Union <ael-operation-union>`, :ref:`Distinct <ael-operation-distinct>`, :ref:`Difference <ael-operation-difference>`, :ref:`Most common element <ael-operation-array-mode>`, :ref:`Count by value <ael-operation-array-counts>`, :ref:`Sum array <ael-operation-array-sum>`, :ref:`Average array <ael-operation-array-avg>`, :ref:`Minimum of array <ael-operation-array-min>`, :ref:`Maximum of array <ael-operation-array-max>`, :ref:`Take first <ael-operation-take>`, :ref:`Skip first <ael-operation-skip>`, :ref:`Intersect arrays <ael-operation-array-intersect>`, :ref:`Zip arrays <ael-operation-array-zip>`
   * - :ref:`Null handling <ael-category-null>`
     - :ref:`Is null <ael-operation-isnull>`, :ref:`Is not null <ael-operation-isnotnull>`


Operations
==================================================

.. _ael-category-conditional:

Conditional
--------------------------------------------------

.. _ael-operation-coalesce:

Coalesce
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``coalesce(value, value, …)``

**Description:** Evaluates operands in order, returning the first non-nil operand.

**Returns:** ``any``

**Arity:** At least 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to consider.

.. _ael-operation-case:

Case
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``case(value, match, result, …)``

**Description:** Selects a result based on matching a test value against possible cases.

**Returns:** ``any``

**Arity:** At least 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to match against.
   * - ``match``
     - ``any``
     - A candidate value.
   * - ``result``
     - ``any``
     - Result returned when the candidate matches.

.. _ael-operation-cond:

Condition
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``cond(predicate, result, …)``

**Description:** Evaluates predicates in order, returning the result paired with the first true predicate.

**Returns:** ``any``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``predicate``
     - ``boolean``
     - A predicate to evaluate in order.
   * - ``result``
     - ``any``
     - Result returned when the predicate is true.

.. _ael-operation-if:

If
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``if(condition, then, else)``

**Description:** Returns the second operand if the first operand (condition) is true, otherwise returns the third operand. NULL conditions are treated as false.

**Returns:** ``any``

**Arity:** 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``condition``
     - ``boolean``
     - The condition to test.
   * - ``then``
     - ``any``
     - Result when the condition is true.
   * - ``else``
     - ``any``
     - Result when the condition is false.

.. _ael-category-comparison:

Comparison
--------------------------------------------------

.. _ael-operation-equal:

Equal
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value = value``

**Description:** Returns true if all operands are equal to each other.

**Returns:** ``boolean``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to compare.

.. _ael-operation-not-equal:

Not equal
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value != value``

**Description:** Returns true if at least one operand is not equal to the others.

**Returns:** ``boolean``

**Arity:** At least 2 arguments.

**Aliases:** ``not=``

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to compare.

.. _ael-operation-less-than:

Less than
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value < value``

**Description:** Returns true if each operand is less than the operand that follows it.

**Returns:** ``boolean``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to compare.

.. _ael-operation-less-than-or-equal:

Less than or equal
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value <= value``

**Description:** Returns true if each operand is less than or equal to the operand that follows it.

**Returns:** ``boolean``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to compare.

.. _ael-operation-greater-than:

Greater than
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value > value``

**Description:** Returns true if each operand is greater than the operand that follows it.

**Returns:** ``boolean``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to compare.

.. _ael-operation-greater-than-or-equal:

Greater than or equal
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value >= value``

**Description:** Returns true if each operand is greater than or equal to the operand that follows it.

**Returns:** ``boolean``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A value to compare.

.. _ael-category-logical:

Logical
--------------------------------------------------

.. _ael-operation-and:

And
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value AND value``

**Description:** Returns true if all operands are truthy. Short-circuits evaluation on the first falsey value.

**Returns:** ``boolean``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``boolean``
     - A value to test.

.. _ael-operation-or:

Or
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value OR value``

**Description:** Returns true if any operand is truthy. Short-circuits evaluation on the first truthy value.

**Returns:** ``boolean``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``boolean``
     - A value to test.

.. _ael-operation-not:

Not
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``NOT value``

**Description:** Returns true if the operand is falsey.

**Returns:** ``boolean``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``boolean``
     - A value to test.

.. _ael-category-numeric:

Numeric
--------------------------------------------------

.. _ael-operation-add:

Add
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value + value``

**Description:** Adds operands.

**Returns:** ``number``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``number``
     - A value to add.

.. _ael-operation-subtract:

Subtract
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value - value``

**Description:** Subtracts operands.

**Returns:** ``number``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``number``
     - A value to subtract.

.. _ael-operation-divide:

Divide
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value / value``

**Description:** Divides operands. Treats division by zero as a nil result.

**Returns:** ``number``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``number``
     - A value to divide.

.. _ael-operation-multiply:

Multiply
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value * value``

**Description:** Multiplies operands.

**Returns:** ``number``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``number``
     - A value to multiply.

.. _ael-operation-abs:

Absolute value
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``abs(number)``

**Description:** Returns the absolute value of the operand.

**Returns:** ``number``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``number``
     - ``number``
     - The value to take the absolute value of.

.. _ael-operation-modulus:

Modulus
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value % value``

**Description:** Returns the modulus of the first operand divided by the second operand.

**Returns:** ``number``

**Arity:** 2 arguments.

**Aliases:** ``mod``

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``number``
     - ``number``
     - A number.

.. _ael-operation-min:

Minimum
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``min(value, value, …)``

**Description:** Returns the minimum value from operands, ignoring nil values.

**Returns:** ``number``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``number``
     - A value to compare.

.. _ael-operation-max:

Maximum
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``max(value, value, …)``

**Description:** Returns the maximum value from operands, ignoring nil values.

**Returns:** ``number``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``number``
     - A value to compare.

.. _ael-category-string:

String
--------------------------------------------------

.. _ael-operation-startswith:

Starts with
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``startswith(string, prefix)``

**Description:** Returns true if the first operand string starts with the second operand string.

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to test.
   * - ``prefix``
     - ``string``
     - The prefix to look for.

.. _ael-operation-endswith:

Ends with
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``endswith(string, suffix)``

**Description:** Returns true if the first operand string ends with the second operand string.

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to test.
   * - ``suffix``
     - ``string``
     - The suffix to look for.

.. _ael-operation-contains:

Contains
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``contains(string, substring)``

**Description:** Returns true if the first operand string contains the second operand string.

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to search.
   * - ``substring``
     - ``string``
     - The substring to look for.

.. _ael-operation-replace:

Replace
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``replace(string, search, replacement)``

**Description:** Replaces all occurrences of the second operand string in the first operand string with the third operand string.

**Returns:** ``string``

**Arity:** 2 to 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to operate on.
   * - ``search``
     - ``string``
     - The substring to replace.
   * - ``replacement``
     - ``string``
     - The replacement substring.

.. _ael-operation-lower:

Lowercase
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``lower(string)``

**Description:** Converts the operand string to lower case.

**Returns:** ``string``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to convert.

.. _ael-operation-upper:

Uppercase
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``upper(string)``

**Description:** Converts the operand string to upper case.

**Returns:** ``string``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to convert.

.. _ael-operation-concat:

Concatenate
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``concat(value, value, …)``

**Description:** Concatenates operands together with no spaces/separator.

**Returns:** ``string``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``string``
     - A value to join.

.. _ael-operation-concat-ws:

Concatenate with separator
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``concat_ws(separator, value, …)``

**Description:** Concatenates operands together. The first operand should be a (possibly empty) separator string.

**Returns:** ``string``

**Arity:** At least 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``separator``
     - ``string``
     - The separator placed between values.
   * - ``value``
     - ``string``
     - A value to join.

.. _ael-operation-split:

Split
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``split(string, delimiter)``

**Description:** Splits the first operand string on each literal occurrence of the second operand string, returning an array of strings. The delimiter is matched literally, not as a regular expression. Empty trailing elements are preserved, so the result length is stable for fixed-shape values. An empty delimiter splits the string into one element per code point, matching SparkSQL.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to split.
   * - ``delimiter``
     - ``string``
     - The literal delimiter to split on. An empty delimiter splits into single characters.

.. _ael-operation-sha2:

SHA-2 hash
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``sha2(string, bits)``

**Description:** Returns a checksum of SHA-2 family as a hex string of expr. SHA-224, SHA-256, SHA-384, and SHA-512 are supported. Bit length of 0 is equivalent to 256.

**Returns:** ``string``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``string``
     - ``string``
     - The string to hash.
   * - ``bits``
     - ``integer``
     - Bit length: 224, 256, 384 or 512 (0 means 256).

.. _ael-category-date:

Date and time
--------------------------------------------------

.. _ael-operation-date-add:

Add days
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``date_add(date, days)``

**Description:** Adds the specified number of days to a date.

**Returns:** ``date``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``date``
     - ``date``
     - The starting date.
   * - ``days``
     - ``integer``
     - Number of days to add.

.. _ael-operation-date-sub:

Subtract days
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``date_sub(date, days)``

**Description:** Subtracts the specified number of days from a date.

**Returns:** ``date``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``date``
     - ``date``
     - The starting date.
   * - ``days``
     - ``integer``
     - Number of days to subtract.

.. _ael-operation-date-diff:

Date difference
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``date_diff(date, date)``

**Description:** Returns the absolute number of days between two dates.

**Returns:** ``integer``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``date``
     - ``date``
     - The first date.
   * - ``date``
     - ``date``
     - The second date.

.. _ael-operation-date-in-last:

Date in last
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``date_in_last(days, date)``

**Description:** True if the given date is within the past ``n`` days of today. A value of zero will only match today, a value of one will match yesterday, etc.

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``days``
     - ``integer``
     - Number of days in the window.
   * - ``date``
     - ``date``
     - The date to test.

.. _ael-operation-date-in-next:

Date in next
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``date_in_next(days, date)``

**Description:** True if the given date is within the next ``n`` days from today. A value of zero will only match today, a value of one will match tomorrow, etc.

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``days``
     - ``integer``
     - Number of days in the window.
   * - ``date``
     - ``date``
     - The date to test.

.. _ael-operation-timestamp-diff:

Timestamp difference
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``timestamp_diff(unit, timestamp, timestamp)``

**Description:** Returns the time difference between two timestamps in the specified unit (SECONDS, MINUTES, HOURS). Takes three arguments: unit (string), timestamp1, timestamp2.

**Returns:** ``integer``

**Arity:** 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``unit``
     - ``string``
     - SECONDS, MINUTES or HOURS.
   * - ``timestamp``
     - ``datetime``
     - The first timestamp.
   * - ``timestamp``
     - ``datetime``
     - The second timestamp.

.. _ael-operation-timestamp-in-last:

Timestamp in last
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``timestamp_in_last(n, unit, timestamp)``

**Description:** True if the given timestamp is within the past ``n`` units of the current time.

**Returns:** ``boolean``

**Arity:** 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``n``
     - ``integer``
     - Size of the window.
   * - ``unit``
     - ``string``
     - SECONDS, MINUTES or HOURS.
   * - ``timestamp``
     - ``datetime``
     - The timestamp to test.

.. _ael-operation-timestamp-in-next:

Timestamp in next
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``timestamp_in_next(n, unit, timestamp)``

**Description:** True if the given timestamp is within the next ``n`` units from the current time.

**Returns:** ``boolean``

**Arity:** 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``n``
     - ``integer``
     - Size of the window.
   * - ``unit``
     - ``string``
     - SECONDS, MINUTES or HOURS.
   * - ``timestamp``
     - ``datetime``
     - The timestamp to test.

.. _ael-operation-day-of-year:

Day of year
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``day_of_year(date)``

**Description:** Returns the day of year (1-366) for the given date

**Returns:** ``integer``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``date``
     - ``date``
     - The date to evaluate.

.. _ael-operation-day-of-week:

Day of week
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``day_of_week(date)``

**Description:** Returns the ISO day of week (1-7, where Monday is 1 and Sunday is 7) for the given date

**Returns:** ``integer``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``date``
     - ``date``
     - The date to evaluate.

.. _ael-operation-week-of-year:

Week of year
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``week_of_year(date)``

**Description:** Returns the ISO-8601 week of the week-based year (1-53) for the given date, where weeks start Monday and week 1 contains the year's first Thursday

**Returns:** ``integer``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``date``
     - ``date``
     - The date to evaluate.

.. _ael-operation-timestamp-from-millis:

Timestamp from milliseconds
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``timestamp_from_millis(millis)``

**Description:** Coerces milliseconds since the Unix epoch (1970-01-01T00:00:00Z), given as a number, to a timestamp. Returns nil for nil, non-numeric, or out-of-range input.

For numeric epoch fields in event payloads (e.g. GA4 ``event_timestamp``) that ``:to-timestamp`` cannot parse.

**Returns:** ``datetime``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``millis``
     - ``integer``
     - Milliseconds since 1970-01-01T00:00:00Z.

.. _ael-category-cast:

Type conversion
--------------------------------------------------

.. _ael-operation-to-boolean:

To boolean
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_boolean(value)``

**Description:** Coerces a value to boolean. Returns nil if coercion is not possible.

**Returns:** ``boolean``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to coerce.

.. _ael-operation-to-int:

To integer
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_int(value)``

**Description:** Coerces a value to a 64-bit integer. Returns nil if coercion is not possible.

**Returns:** ``integer``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to coerce.

.. _ael-operation-to-float:

To float
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_float(value)``

**Description:** Coerces a value to float. Returns nil if coercion is not possible.

**Returns:** ``float``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to coerce.

.. _ael-operation-to-decimal:

To decimal
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_decimal(value, precision, scale)``

**Description:** Coerces a value to big decimal, with precision 38 and scale 2 by default. The optional precision and scale parameters must be integer literals. Returns nil if the coerced value is wider than the precision.

**Returns:** ``decimal``

**Arity:** 1 to 3 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to coerce.
   * - ``precision``
     - ``integer``
     - Optional decimal precision, 1 to 38. Must be a literal number.
   * - ``scale``
     - ``integer``
     - Optional decimal scale, 0 to the precision. Must be a literal number.

.. _ael-operation-to-date:

To date
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_date(value, format)``

**Description:** Coerces a value to date. Returns nil if coercion is not possible.

**Returns:** ``date``

**Arity:** 1 to 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to coerce.
   * - ``format``
     - ``string``
     - Optional date parse format.

.. _ael-operation-to-timestamp:

To timestamp
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_timestamp(value, format)``

**Description:** Coerces a value to timestamp. Returns nil if coercion is not possible.

**Returns:** ``datetime``

**Arity:** 1 to 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to coerce.
   * - ``format``
     - ``string``
     - Optional timestamp parse format.

.. _ael-operation-to-string:

To string
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``to_string(value)``

**Description:** Converts a value to string. Returns nil if the input is nil.

**Returns:** ``string``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to convert.

.. _ael-category-collection:

Collection
--------------------------------------------------

.. _ael-operation-in:

In
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value IN (array)``

**Description:** Returns true if the first operand is contained in the second operand (a collection).

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to find.
   * - ``array``
     - ``array``
     - The array to search.

.. _ael-operation-not-in:

Not in
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value NOT IN (array)``

**Description:** Returns true if the first operand is not contained in the second operand (a collection).

**Returns:** ``boolean``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to find.
   * - ``array``
     - ``array``
     - The array to search.

.. _ael-operation-size:

Size
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``size(collection)``

**Description:** Returns the integer element count of the operand, or NULL if the operand is NULL.

**Returns:** ``integer``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``collection``
     - ``array``
     - The collection to measure.

.. _ael-operation-get:

Get element
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``get(array, index)``

**Description:** Returns the element of the input array at the given (0-based) index. If the index points outside of the array boundaries, or if the index is negative, then this function returns NULL.

**Returns:** ``any``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to index into.
   * - ``index``
     - ``integer``
     - The 0-based index.

.. _ael-operation-array:

Array
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array(value, value, …)``

**Description:** Returns an array of operands in order. All operands must be of the same type.

**Returns:** ``array``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - An array element.

.. _ael-operation-map:

Map
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``map(key, value, …)``

**Description:** Returns a map of the given key/value pairs. All keys and all values must be of the same type.

**Returns:** ``map``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``key``
     - ``any``
     - A map key.
   * - ``value``
     - ``any``
     - A map value.

.. _ael-operation-named-struct:

Named struct
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``named_struct(key, value, …)``

**Description:** Returns a struct with the given field names and values. Each name must be written as text, must be a valid field name, and may not be repeated.

**Returns:** ``struct``

**Arity:** Any number of arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``key``
     - ``string``
     - A struct field name, written directly as text. Letters, numbers, and underscores, with at least one letter or underscore, and unique within the struct.
   * - ``value``
     - ``any``
     - A struct field value.

.. _ael-operation-field-access:

Struct or map field
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value.key``

**Description:** Gets a field from a struct, or a string key from a map.

**Returns:** ``any``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - A struct or map.
   * - ``key``
     - ``any``
     - A field or map key.

.. _ael-operation-indexed-access:

Array, struct, or map lookup
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value[index]``

**Description:** Gets an integer offset from an array, a field from a struct, or an arbitrary key from a map.

**Returns:** ``any``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - An array, struct, or map.
   * - ``key``
     - ``any``
     - An index, field, or map key.

.. _ael-operation-filter:

Filter
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``filter(array, element -> predicate)``

**Description:** Filters an array using a function that takes one argument (which will be bound to each element in the array, in order) and returns a boolean. Returns an array containing only the elements for which the function returned true.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to filter.
   * - ``function``
     - ``function``
     - A one-argument function whose argument is bound to each element in turn, and which returns a boolean.

.. _ael-operation-transform:

Transform
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``transform(array, element -> expression)``

**Description:** Transforms an array using a function that takes each element of the array, in order, and returns a new value. Returns an array of the values returned by the function. The function may take an optional second argument, which will be bound to the zero-based index of the element.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to transform.
   * - ``function``
     - ``function``
     - A function whose first argument is bound to each element in turn. An optional second argument is bound to that element's 0-based index: (element, index) -> expression.

.. _ael-operation-array-sort:

Sort array
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_sort(array, comparator)``

**Description:** Sorts the input array. If no comparator function is provided, sorts in ascending order. The elements of the input array must be orderable. NaN is greater than any non-NaN elements for double/float type. Null elements will be placed at the end of the returned array.

With a comparator function: sorts and returns the array based on the given comparator function. The comparator takes two arguments representing two elements of the array. It returns a negative integer, 0, or a positive integer as the first element is less than, equal to, or greater than the second element. If the comparator function returns null, the function will throw an exception.

**Returns:** ``array``

**Arity:** 1 to 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to sort.
   * - ``comparator``
     - ``function``
     - Optional two-argument comparator function.

.. _ael-operation-union:

Union
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``union(array, array, …)``

**Description:** Concatenates two or more arrays into a single array, preserving order and keeping duplicate elements. All operands must be arrays of primitive or flat-struct elements with a common element type.

**Returns:** ``array``

**Arity:** At least 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - An array to concatenate.

.. _ael-operation-distinct:

Distinct
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``distinct(array)``

**Description:** Returns the input array with duplicate elements removed, preserving the order of first occurrence.

**Returns:** ``array``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to deduplicate.

.. _ael-operation-difference:

Difference
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``difference(array, array)``

**Description:** Returns the elements of the first array that are not present in the second array, preserving the order and duplicates of the first array.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``source``
     - ``array``
     - The source array.
   * - ``remove``
     - ``array``
     - The array of elements to remove.

.. _ael-operation-array-mode:

Most common element
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_mode(array)``

**Description:** Returns the most frequently occurring element of the input array, or NULL if the input is NULL or contains no non-NULL elements. NULL elements are not counted. Ties are broken by the natural sort order of the tied elements, matching the ``mode`` aggregation.

**Returns:** ``any``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to reduce. Extract a field from a struct array first with transform().

.. _ael-operation-array-counts:

Count by value
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_counts(array)``

**Description:** Returns a frequency table for the input array: an array of structs with a ``value`` field holding each distinct non-NULL element and a ``count`` field holding how many times it occurs. Ordered by count descending, then by the natural sort order of the value, matching the ``mode`` aggregation's tie-break. NULL elements are not counted. Returns NULL if the input is NULL, and an empty array if the input is empty or holds only NULLs.

**Returns:** ``array``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to tally. Extract a field from a struct array first with transform().

.. _ael-operation-array-sum:

Sum array
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_sum(array)``

**Description:** Returns the sum of the input array's non-NULL elements, which must be numeric. Returns 0 for an empty array or one holding only NULLs, matching the ``sum`` aggregation over zero records. Returns NULL if the input is NULL.

**Returns:** ``number``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array of numbers to add.

.. _ael-operation-array-avg:

Average array
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_avg(array)``

**Description:** Returns the mean of the input array's non-NULL elements, which must be numeric. Returns NULL if the input is NULL, empty, or holds only NULLs, matching the ``average`` aggregation over zero records.

**Returns:** ``number``

**Arity:** 1 argument.

**Aliases:** ``array-average``

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array of numbers to average.

.. _ael-operation-array-min:

Minimum of array
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_min(array)``

**Description:** Returns the smallest of the input array's non-NULL elements. Unlike the scalar ``min``, the elements need only be orderable, so arrays of strings, dates, and timestamps are supported. Returns NULL if the input is NULL, empty, or holds only NULLs.

**Returns:** ``any``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to take the minimum of.

.. _ael-operation-array-max:

Maximum of array
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_max(array)``

**Description:** Returns the largest of the input array's non-NULL elements. Unlike the scalar ``max``, the elements need only be orderable, so arrays of strings, dates, and timestamps are supported. Returns NULL if the input is NULL, empty, or holds only NULLs.

**Returns:** ``any``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to take the maximum of.

.. _ael-operation-take:

Take first
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``take(array, limit)``

**Description:** Returns the first ``limit`` elements of the input array. A ``limit`` longer than the array returns the whole array, and a ``limit`` of zero returns an empty array. Returns NULL if either operand is NULL or if ``limit`` is negative.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to take from.
   * - ``limit``
     - ``integer``
     - How many elements to take.

.. _ael-operation-skip:

Skip first
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``skip(array, offset)``

**Description:** Returns the input array without its first ``offset`` elements. An ``offset`` at or past the end of the array returns an empty array. Returns NULL if either operand is NULL or if ``offset`` is negative. Compose with ``take`` for a window out of the middle: ``take(skip(arr, 1), 2)``.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``array``
     - ``array``
     - The array to skip into.
   * - ``offset``
     - ``integer``
     - How many leading elements to skip.

.. _ael-operation-array-intersect:

Intersect arrays
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_intersect(array, array)``

**Description:** Returns the elements present in both arrays, with duplicates removed, in the order they first appear in the first array. Returns NULL if either operand is NULL. Matches SparkSQL's ``array_intersect`` on all three points.

**Returns:** ``array``

**Arity:** 2 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``source``
     - ``array``
     - The source array.
   * - ``keep``
     - ``array``
     - The array of elements to keep.

.. _ael-operation-array-zip:

Zip arrays
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``array_zip(name, array, name, array, …)``

**Description:** Combines two or more arrays element-wise into an array of structs. Shorter arrays are padded with NULL, so the result length is that of the longest input, and the result is NULL if any input array is NULL — both as in SparkSQL's ``arrays_zip``. Operands alternate between a field name and the array supplying that field's values, as in ``named_struct``: SparkSQL derives struct field names from the input column names, and an AEL operand is an expression with no name to derive.

**Returns:** ``array``

**Arity:** At least 4 arguments.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``name``
     - ``string``
     - A struct field name, written directly as text.
   * - ``array``
     - ``array``
     - The array supplying that field's values.

.. _ael-category-null:

Null handling
--------------------------------------------------

.. _ael-operation-isnull:

Is null
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value IS NULL``

**Description:** Returns true if the operand is null.

**Returns:** ``boolean``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to test.

.. _ael-operation-isnotnull:

Is not null
++++++++++++++++++++++++++++++++++++++++++++++++++

**Syntax:** ``value IS NOT NULL``

**Description:** Returns true if the operand is not null.

**Returns:** ``boolean``

**Arity:** 1 argument.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``value``
     - ``any``
     - The value to test.
