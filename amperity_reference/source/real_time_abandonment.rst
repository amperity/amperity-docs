.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Recognize customers who abandon a cart and re-engage them in near real time with an always-on segment and a real-time journey.

.. meta::
    :content class=swiftype name=body data-type=text:
        Recognize customers who abandon a cart and re-engage them in near real time with an always-on segment and a real-time journey.

.. meta::
    :content class=swiftype name=title data-type=string:
        Recognize and re-engage abandoning customers

==================================================
Recognize and re-engage abandoning customers
==================================================

.. real-time-abandonment-overview-start

Recognize customers who add to their cart but do not check out, and re-engage them within minutes--while the intent is still fresh. This article shows how to assemble Amperity's real-time objects into an abandoned-cart program that reacts to a customer's behavior as it happens.

.. real-time-abandonment-overview-end


.. _real-time-abandonment-problem:

The problem
==================================================

.. real-time-abandonment-problem-start

A customer adds items to their cart and leaves without purchasing. The window to win that purchase back is short: a reminder sent the next day, after a batch job runs, often arrives too late. To be effective, your brand needs to recognize the abandonment within minutes and act on it while the customer is still in a buying mindset.

The challenge is that abandonment is not a single event--it is a *state* that depends on two things happening, or not happening, in sequence: the customer added to their cart, and they did not purchase within some window.

.. real-time-abandonment-problem-end


.. _real-time-abandonment-approach:

Model abandonment as a segment
==================================================

.. real-time-abandonment-approach-start

It is tempting to think of this as "start a journey each time a cart is abandoned." Amperity models it differently, and more robustly: you capture abandonment as a **state on the customer's profile**, express that state as an always-on :doc:`real-time segment <real_time_segments>`, and let the customer **enter a journey when they enter the segment**.

Because a real-time segment re-evaluates on every event that touches a profile, a customer enters the segment--and the journey--the moment their profile qualifies as abandoned. This is the supported pattern for reacting to "when X happens" in real time: model X as a segment.

.. real-time-abandonment-approach-end

.. TODO: verify with Shawn -- this recipe deliberately uses segment entry, because event-triggered journey entry is built in the backend but not user-authorable (AMP-1633; MCP refuses inclusion_event; §3.6). Per Q2 the framing is positive (model the trigger as a segment) with no availability label. Confirm.


.. _real-time-abandonment-pipeline:

How the pipeline fits together
==================================================

.. real-time-abandonment-pipeline-start

The program is built from the real-time objects in sequence:

#. **Cart events on an event stream.** Send add-to-cart and purchase events to an :doc:`event stream <event_streams>`. Model the cart as an **array** field on the event type, so that a single event carries all of its line items.
#. **A profile collection with the right attributes.** Route the events to a :doc:`profile collection <real_time_profiles>` and define two attributes on it:

   * An **aggregate attribute** that captures the most recent cart--its contents and value--scoped to the cart event type.
   * A **computed attribute**, a boolean, that is true when the customer has a recent cart *and* has not purchased within your chosen window.

#. **An always-on segment.** Define a :doc:`real-time segment <real_time_segments>` whose predicate is that boolean. A customer joins the segment the moment they qualify as abandoned, and leaves it when they purchase or the window passes.
#. **A real-time journey.** Build a :doc:`real-time journey <real_time_journeys>` that travelers enter by membership in that segment. The journey sends the re-engagement message and can exit a traveler as soon as they purchase.
#. **Activation and measurement.** The journey activates to your real-time connector. Use a percent-split to hold out a control group, then read the resulting **test group** and **control** information from the journey's travel log to measure the program's lift.

.. real-time-abandonment-pipeline-end


.. _real-time-abandonment-build:

Build it
==================================================

.. real-time-abandonment-build-start

To build each piece, see the concept page for the objects it uses:

* :doc:`About event streams and event types <event_streams>` -- send cart events and model the cart as an array field.
* :doc:`About profile collections and real-time profiles <real_time_profiles>` -- define the collection and its attributes.
* :doc:`Expressions for real-time <expressions>` -- write the aggregation scope, the array handling, and the computed boolean.
* :doc:`About real-time segments <real_time_segments>` -- define the always-on segment on the boolean.
* :doc:`About real-time journeys <real_time_journeys>` -- build the journey, hold out a control group, and export the travel log.

For an orientation to how these objects fit together, see :doc:`About real-time <real_time>`.

.. real-time-abandonment-build-end
