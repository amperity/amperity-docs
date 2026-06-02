.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Amperity expression language is a SQL-inspired expression language used to compute values, filter events, and extract fields from incoming data.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity expression language is a SQL-inspired expression language used to compute values, filter events, and extract fields from incoming data.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity expression language


==================================================
Amperity expression language
==================================================

.. ael-intro-start

Amperity expression language is a SQL-inspired expression language used throughout Amperity to compute values from records. An expression is evaluated over a record--a set of named fields--and returns a computed value: a boolean, a number, a string, a date, or a collection.

In the context of event streaming, expressions extract and transform fields from incoming event JSON. When you define an event type, each field you configure uses an expression that tells Amperity how to pull a value out of the raw event body.

.. ael-intro-end


.. _ael-quickstart:

Quick start
==================================================

.. ael-quickstart-start

The most common things you will write when defining event type fields:

.. code-block:: sql

   email

Returns the value of the **email** field directly from the event body.

.. code-block:: sql

   user.email

Returns ``user.email`` from a nested object: ``{"user": {"email": "..."}}``

.. code-block:: sql

   coalesce(loyalty_id, phone, email)

Returns the first non-null value--useful when a profile might be identified by different keys in different events.

.. code-block:: sql

   to_decimal(amount, 10, 2)

Coerces the **amount** field to a decimal with precision 10, scale 2.

.. code-block:: sql

   if(currency IS NULL, 'USD', currency)

Returns ``'USD'`` when the **currency** field is missing, otherwise returns its value.

.. ael-quickstart-end


.. _ael-sample-record:

Sample record
==================================================

.. ael-sample-record-start

All examples in this reference evaluate against the following record. In event streaming, this record represents an incoming event JSON body.

.. code-block:: json

   {
     "first_name": "Ada",
     "last_name": "Lovelace",
     "email": "ada@example.com",
     "age": 39,
     "loyalty_tier": "gold",
     "lifetime_spend": 4250.75,
     "visit_count": 12,
     "signup_date": "2018-06-12",
     "last_booking_date": "2026-04-10",
     "last_login_at": "2026-04-30T09:15:00Z",
     "preferences": {"newsletter": true, "sms": false},
     "tags": ["frequent", "vip", "weekend"],
     "scores": [82, 91, 73, 88],
     "favorite_room_size": null
   }

Examples that use date or timestamp operators treat the current time as ``2026-04-30T12:00:00Z``.

.. ael-sample-record-end


.. _ael-syntax:

Syntax
==================================================

.. _ael-syntax-literals:

Literals
--------------------------------------------------

.. ael-syntax-literals-start

.. list-table::
   :widths: 20 35 45
   :header-rows: 1

   * - Type
     - Examples
     - Notes

   * - Integer
     - ``42``, ``-3``
     -

   * - Decimal
     - ``3.14``, ``-0.5``
     - Parsed as a double.

   * - String
     - ``'gold'``, ``'it\'s ok'``
     - Single quotes only. Escape sequences: ``\t \n \r \'``.

   * - Boolean
     - **TRUE**, **FALSE**
     - Case-insensitive.

   * - Null
     - **NULL**
     - Case-insensitive.

.. ael-syntax-literals-end


.. _ael-syntax-fields:

Field references
--------------------------------------------------

.. ael-syntax-fields-start

A bare identifier references a field on the record. Field lookup is case-insensitive.

.. code-block:: sql

   first_name

Returns ``"Ada"``.

Use dot syntax to access nested map fields:

.. code-block:: sql

   preferences.newsletter

Returns **true** from ``{"preferences": {"newsletter": true}}``.

Use bracket syntax for array indexing (zero-based):

.. code-block:: sql

   tags[0]

Returns ``"frequent"``.

.. code-block:: sql

   tags[size(tags) - 1]

Returns the last element: ``"weekend"``.

Use backticks to quote field names that contain spaces or hyphens:

.. code-block:: sql

   `first name`

.. ael-syntax-fields-end


.. _ael-syntax-precedence:

Operator precedence
--------------------------------------------------

.. ael-syntax-precedence-start

From tightest binding to loosest:

.. list-table::
   :widths: 15 50 35
   :header-rows: 1

   * - Tier
     - Operators
     - Associativity

   * - 0 (tightest)
     - Field access ``.`` and indexing ``[]``
     - left

   * - 1
     - ``*`` ``/`` ``%``
     - left

   * - 2
     - ``+`` ``-``
     - left

   * - 3
     - ``=`` ``!=`` ``<`` ``<=`` ``>`` ``>=``; **IN**, ``NOT IN``
     - non-associative

   * - 4
     - ``IS NULL``, ``IS NOT NULL``
     - postfix

   * - 5
     - **NOT**
     - prefix

   * - 6
     - **AND**
     - left

   * - 7
     - **OR**
     - left

   * - 8 (loosest)
     - ``->`` (lambda)
     - right

Parenthesize when in doubt:

.. code-block:: sql

   age < 0 OR age > 0 AND age != 39

**AND** binds tighter than **OR**, so this reads as ``age < 0 OR (age > 0 AND age != 39)``, which evaluates to **false**.

.. ael-syntax-precedence-end


.. _ael-syntax-functions:

Function calls and lambdas
--------------------------------------------------

.. ael-syntax-functions-start

Function calls use ``name(arg, arg, ...)`` syntax:

.. code-block:: sql

   coalesce(favorite_room_size, 'queen')

Returns ``"queen"`` because **favorite_room_size** is null.

Some operators, such as **filter** and **array_sort**, take a lambda, which is an inline anonymous function using ``->`` arrow syntax:

.. code-block:: sql

   filter(scores, s -> s >= 85)

Returns ``[91, 88]``.

Multiple parameters use parentheses: ``(a, b) -> a + b``. The arrow binds looser than everything else.

.. ael-syntax-functions-end


.. _ael-syntax-case:

Case sensitivity and whitespace
--------------------------------------------------

.. ael-syntax-case-start

* **Keywords**, such as **AND**, **OR**, **NOT**, **IN**, **IS NULL**, **TRUE**, and **NULL**, are case-insensitive.
* **Field names** are case-insensitive. The runtime lowercases both sides before comparing.
* **String literals** are case-sensitive: ``'Gold'`` is not ``'gold'``.
* **Whitespace** between tokens is ignored. Newlines are allowed.
* **Comments** are not supported.

.. ael-syntax-case-end


.. _ael-operators:

Operator catalog
==================================================

.. _ael-operators-arithmetic:

Arithmetic
--------------------------------------------------

.. ael-operators-arithmetic-start

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Operator
     - Description

   * - **+** **-** **\*** **/**
     - Variadic. Division by zero returns **NULL**.

   * - **%** / **mod(a, b)**
     - Modulus.

   * - **abs(x)**
     - Absolute value.

   * - **min(a, b, ...)** / **max(a, b, ...)**
     - Minimum or maximum, ignoring nulls.

.. code-block:: sql

   lifetime_spend / visit_count

Returns ``354.23`` (4250.75 ÷ 12).

.. code-block:: sql

   10 % 3

Returns ``1``.

.. ael-operators-arithmetic-end


.. _ael-operators-comparison:

Comparison
--------------------------------------------------

.. ael-operators-comparison-start

Comparison operators do **not** coerce types. Comparing a number to its string representation always returns **false**.

.. code-block:: sql

   age = 39

Returns **true**.

.. code-block:: sql

   age >= 18 AND age < 65

Returns **true**.

.. ael-operators-comparison-end


.. _ael-operators-logical:

Logical and null
--------------------------------------------------

.. ael-operators-logical-start

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Operator
     - Description

   * - **AND**
     - Short-circuits on the first falsey value.

   * - **OR**
     - Short-circuits on the first truthy value.

   * - **NOT x**
     - True when **x** is falsey (**false** or **NULL**).

   * - **x IS NULL** / **x IS NOT NULL**
     - Explicit null checks.

.. code-block:: sql

   favorite_room_size IS NULL

Returns **true**.

.. code-block:: sql

   loyalty_tier = 'gold' OR loyalty_tier = 'platinum'

Returns **true**.

.. ael-operators-logical-end


.. _ael-operators-membership:

Membership
--------------------------------------------------

.. ael-operators-membership-start

**IN** takes a literal parenthesized list, not a field that holds a collection. To check whether an array field contains a value, use **filter** and **size**.

.. code-block:: sql

   loyalty_tier IN ('gold', 'platinum', 'diamond')

Returns **true**.

.. code-block:: sql

   loyalty_tier NOT IN ('bronze', 'silver')

Returns **true**.

.. ael-operators-membership-end


.. _ael-operators-string:

String
--------------------------------------------------

.. ael-operators-string-start

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Operator
     - Description

   * - **startswith(s, prefix)**
     - True if **s** begins with **prefix**.

   * - **endswith(s, suffix)**
     - True if **s** ends with **suffix**.

   * - **contains(s, substr)**
     - True if **s** contains **substr**.

   * - **concat(a, b, ...)**
     - Joins operands with no separator.

   * - **concat_ws(sep, a, b, ...)**
     - Joins operands with **sep** between each.

   * - **replace(s, target, replacement)**
     - Replaces all occurrences of **target** in **s**.

.. code-block:: sql

   startswith(email, 'ada')

Returns **true**.

.. code-block:: sql

   concat_ws(' ', first_name, last_name)

Returns ``"Ada Lovelace"``.

.. ael-operators-string-end


.. _ael-operators-collection:

Collection and lambdas
--------------------------------------------------

.. ael-operators-collection-start

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Operator
     - Description

   * - **size(x)**
     - Element count of an array, map, or string.

   * - **get(arr, i)**
     - 0-based array lookup. Out-of-bounds returns **NULL**.

   * - **filter(arr, fn)**
     - Keeps elements for which the lambda returns truthy.

   * - **array(a, b, ...)**
     - Constructs an array. All elements must share a type.

   * - **array_sort(arr [, cmp])**
     - Sorts ascending. Pass a comparator lambda to sort by a derived value.

.. code-block:: sql

   size(tags)

Returns ``3``.

.. code-block:: sql

   filter(scores, s -> s >= 85)

Returns ``[91, 88]``.

To check whether an array contains a specific value, combine **filter** and **size**:

.. code-block:: sql

   size(filter(tags, t -> t = 'vip')) > 0

Returns **true**.

.. ael-operators-collection-end


.. _ael-operators-date:

Date and timestamp
--------------------------------------------------

.. ael-operators-date-start

The runtime distinguishes *dates* (calendar day, no time) from *timestamps* (instants, UTC). Both are accepted as ISO 8601 strings from incoming event JSON.

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Operator
     - Description

   * - **date_add(d, n)**
     - Returns **d** plus **n** days.

   * - **date_sub(d, n)**
     - Returns **d** minus **n** days.

   * - **date_diff(a, b)**
     - Absolute number of days between two dates.

   * - **date_in_last(n, d)**
     - True if **d** is within the past **n** days of today.

   * - **date_in_next(n, d)**
     - True if **d** is within the next **n** days from today.

   * - **day_of_year(d)**
     - Returns a value between 1 and 366.

   * - **timestamp_diff(unit, t1, t2)**
     - Difference in the given unit: ``'SECONDS'``, ``'MINUTES'``, or ``'HOURS'``.

   * - **timestamp_in_last(n, unit, t)**
     - True if **t** is within the past **n** units of now.

   * - **timestamp_in_next(n, unit, t)**
     - True if **t** is within the next **n** units of now.

.. note:: **date_in_last** and **timestamp_in_last** take the count as the **first** argument, not the date. ``date_in_last(30, last_booking_date)`` is correct; ``date_in_last(last_booking_date, 30)`` silently returns **NULL**.

.. code-block:: sql

   date_in_last(30, last_booking_date)

Returns **true** (``2026-04-10`` is within 30 days of ``2026-04-30``).

.. code-block:: sql

   timestamp_in_last(24, 'HOURS', last_login_at)

Returns **true** (``2026-04-30T09:15:00Z`` is within 24 hours of ``2026-04-30T12:00:00Z``).

.. code-block:: sql

   date_diff(last_booking_date, signup_date)

Returns ``2859`` (days between ``2026-04-10`` and ``2018-06-12``).

.. ael-operators-date-end


.. _ael-operators-conditional:

Conditional
--------------------------------------------------

.. ael-operators-conditional-start

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Operator
     - Description

   * - **if(cond, then, else)**
     - Two-branch conditional. **NULL** condition is treated as false.

   * - **case(value, m1, r1, m2, r2, ..., default)**
     - Matches **value** against each **m_i**, returning **r_i** for the first match. The final lone argument is the default.

   * - **cond(p1, r1, p2, r2, ..., default)**
     - Returns **r_i** for the first truthy predicate **p_i**. Use a trailing **TRUE** branch as the default.

   * - **coalesce(a, b, ...)**
     - Returns the first non-null operand.

.. code-block:: sql

   if(lifetime_spend > 1000, 'high_value', 'standard')

Returns ``"high_value"``.

.. code-block:: sql

   case(loyalty_tier, 'gold', 'VIP', 'platinum', 'VIP', 'standard')

Returns ``"VIP"`` (**loyalty_tier** is ``'gold'``).

.. code-block:: sql

   cond(lifetime_spend > 5000, 'whale', lifetime_spend > 1000, 'high', TRUE, 'standard')

Returns ``"high"`` (spend is 4250.75, which clears 1000 but not 5000).

.. code-block:: sql

   coalesce(favorite_room_size, 'queen')

Returns ``"queen"`` (**favorite_room_size** is null).

.. ael-operators-conditional-end


.. _ael-operators-coercion:

Coercion
--------------------------------------------------

.. ael-operators-coercion-start

Use these to convert between types when the incoming value is not already in the form you need. Failed coercions return **NULL** rather than an error.

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Operator
     - Description

   * - **to_string(x)**
     - Converts to string. **NULL** stays **NULL**.

   * - **to_int(x)**
     - Parses an integer. Returns **NULL** on failure.

   * - **to_float(x)**
     - Parses a floating-point number.

   * - **to_decimal(x [, precision, scale])**
     - Big-decimal coercion with optional precision and scale.

   * - **to_boolean(x)**
     - Parses a boolean.

   * - **to_date(x [, format])**
     - Parses a date string. Accepts ISO 8601 without a format argument.

   * - **to_timestamp(x [, format])**
     - Parses a timestamp string. Accepts ISO 8601 without a format argument.

.. code-block:: sql

   to_string(age)

Returns ``"39"``.

.. code-block:: sql

   to_decimal(amount, 10, 2)

Coerces **amount** to a decimal with precision 10 and scale 2.

.. code-block:: sql

   to_int('not-a-number')

Returns **NULL**--no error.

.. ael-operators-coercion-end


.. _ael-patterns:

Patterns and recipes
==================================================

.. ael-patterns-start

**Extract a nested field with a fallback**

Useful when an event may or may not include a nested identifier:

.. code-block:: sql

   coalesce(user.loyalty_id, user.email)

Returns the first non-null value from the nested **user** object.

**Route events by type**

A routing expression that maps each incoming event to an event type by name:

.. code-block:: sql

   cond(
     event_name = 'purchase', 'purchase',
     event_name = 'cart_view', 'cart_view',
     event_name = 'page_view', 'page_view',
     TRUE, 'unknown'
   )

The trailing **TRUE** branch catches anything that does not match.

**Coerce a price that arrives as a string**

.. code-block:: sql

   to_decimal(item_price, 10, 2)

**Check membership in a repeated field**

**IN** requires a literal list. To test whether an array field contains a value:

.. code-block:: sql

   size(filter(tags, t -> t = 'vip')) > 0

Returns **true** if **tags** contains ``'vip'``.

**Compute a tier label from a spend value**

.. code-block:: sql

   cond(lifetime_spend > 5000, 'whale', lifetime_spend > 1000, 'high', TRUE, 'standard')

**Default a missing timestamp to the received-at time**

When a field is configured as the event timestamp and this expression is empty, Amperity falls back to the time the event was received. To express a conditional extraction:

.. code-block:: sql

   coalesce(event_timestamp, NULL)

Leave the timestamp expression blank to use the received time automatically.

.. ael-patterns-end


.. _ael-gotchas:

Gotchas
==================================================

.. ael-gotchas-start

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **NULL equals NULL**
     - Unlike standard SQL three-valued logic, the ``=`` operator treats ``NULL = NULL`` as **true**. Use this deliberately. Do not import SQL intuitions blindly.

   * - **No type coercion in comparisons**
     - Comparing a number to its string representation is **false**, not **true**. Coerce explicitly with **to_int**, **to_string**, etc.

.. code-block:: sql

   age = '39'

Returns **false** even though **age** is ``39``.

**Division by zero returns NULL, not an error**

Wrap with **coalesce** if you need a defined fallback:

.. code-block:: sql

   coalesce(lifetime_spend / visit_count, 0)

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **IN does not accept an array field**
     - ``'vip' IN tags`` will not parse. Use **filter** and **size** instead (see :ref:`ael-operators-collection`).

   * - **Argument order on date_in_last and timestamp_in_last**
     - The count comes first: ``date_in_last(30, last_booking_date)``. Putting the date first silently returns **NULL**.

   * - **Reserved words**
     - **AND**, **OR**, **NOT**, **IN**, **IS**, **NULL**, **TRUE**, **FALSE** are reserved. If a field in your event JSON uses one of these names, quote it with backticks:

.. code-block:: sql

   `null`

.. ael-gotchas-end
