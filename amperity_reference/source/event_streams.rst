.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Event streams ingest customer events in real time. Event types are the schemas that shape, type, and validate those events.

.. meta::
    :content class=swiftype name=body data-type=text:
        Event streams ingest customer events in real time. Event types are the schemas that shape, type, and validate those events.

.. meta::
    :content class=swiftype name=title data-type=string:
        About event streams and event types

==================================================
About event streams and event types
==================================================

.. event-streams-overview-start

An **event stream** is the inbound side of Amperity's real-time pipeline: a configured flow of customer events--website activity, loyalty actions, email or SMS engagement--that Amperity ingests and processes as each event arrives. An **event type** is the schema Amperity applies to the events on a stream. It names the fields an event carries, the data type of each field, and the expression that produces each field's value.

Together, event streams and event types turn raw inbound events into typed, recognized records that update :ref:`profile collections <p-profile-collection>` and, through them, the :ref:`real-time segments <r-real-time-segment>` and :ref:`real-time journeys <r-real-time-journey>` that act on customer behavior.

.. event-streams-overview-end


.. _event-streams-streams:

Event streams
==================================================

.. event-streams-streams-start

An event stream defines how Amperity receives and interprets a flow of inbound events. Each stream is configured with:

* A **recognition method** that resolves every inbound event to one of the event types defined for the stream. An event whose type cannot be resolved is left unrecognized rather than processed.
* A **routing expression**, a **timestamp expression**, and an **event-id expression**. These extract, respectively, the value used to route the event, the time of the event itself, and a unique identifier for the event.
* A **mode** that determines whether the stream accepts, silently drops, or rejects the events sent to it.

Events reach a stream through the Real-time API endpoint ``POST /prof/events/{stream-id}``. The stream's mode governs the response the sender receives. For the exact status codes and the request constraints, see :ref:`How events are processed <api-realtime-async>` and the `Real-time API endpoint reference <../api/endpoints_realtime.html>`__.

A :ref:`profile collection <p-profile-collection>` subscribes to one or more event streams; the events on a subscribed stream are what keep the collection's profiles current. A single stream can feed more than one collection.

.. event-streams-streams-end


.. _event-streams-types:

Event types
==================================================

.. event-streams-types-start

An event type is the schema Amperity applies to the events on a stream. An event type is a set of fields, and each field declares:

* A **name**.
* An **expression** that produces the field's value from the inbound event, written in :doc:`Amperity's expression language <expressions>`.
* A **data type** that the produced value is coerced to.
* Whether a value is **required**. When a required field produces no value, the event is marked invalid.

A field can also be designated a **linking key**--an identifier, such as an email address, that Amperity uses to link the event to a customer. Recognizing *which* customer an event belongs to is a distinct step from recognizing the event's type, and is covered separately in real-time identity recognition. A field can additionally carry a **format** that constrains how its value is interpreted.

.. event-streams-types-end


.. _event-streams-complex-fields:

Complex and nested field types
==================================================

.. event-streams-complex-fields-start

Event-type fields are not limited to scalar values. A field's data type can be complex, and complex types can nest:

* An **array** holds an ordered list of values of a single element type--for example, the line items in a cart.
* A **struct** holds a fixed set of named sub-fields, each with its own data type, as a nested record within the event.
* A **map** holds a set of key-value pairs with declared key and value types.

Because the element type of an array, the value type of a map, or a sub-field of a struct can itself be complex, event types can model deeply nested payloads: an array of structs, a struct that contains an array, and so on. A **decimal** field additionally declares a precision and a scale, so that monetary and other fixed-point values keep an exact representation.

.. event-streams-complex-fields-end

.. TODO: verify with <eng> -- coerce-body recursively coerces primitives, arrays (:transform), and structs (:named-struct) but has no :map branch (lib/attribute/src/amperity/attribute/expression.cljc:149-192); map-typed fields are declarable but may not be recursively coerced on ingest. Do not state that map fields are fully coerced until confirmed (NC7).


.. _event-streams-processing:

How Amperity processes an inbound event
==================================================

.. event-streams-processing-start

Amperity does two things with an event when it arrives on a stream: it recognizes the event's type, and it coerces the event's fields to their declared types.

**Recognition** applies the stream's recognition method to resolve the event to one of the stream's event types. Recognition produces one of three outcomes:

* **unknown**--the recognition method did not resolve the event to a type.
* **classified**--the event resolved to an event type that is configured for processing.
* **ignored**--the event resolved to a type that the stream is not configured to process.

**Coercion** then evaluates each field of a classified event. When an event type is saved, Amperity wraps each field's expression with a coercion to that field's declared data type. As each event arrives, Amperity evaluates the wrapped expression to produce the typed value. The event is marked **invalid** when a required field produces no value or a field's expression fails to evaluate; otherwise it is **valid**, and it updates the profiles its linking keys resolve to.

.. event-streams-processing-end


.. _event-streams-sample:

Configure an event type from a sample
==================================================

.. event-streams-sample-start

Amperity retains a reservoir of the most recent events received for each stream and event type. When you define an event type's fields, you can work from a recognized sample event instead of declaring every field by hand: selecting a property from the sample adds a field that reads that property. Because the sample reflects the events the stream has actually received, the fields you define match the shape of your real payloads.

.. event-streams-sample-end
