.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A real-time journey is an always-on program that customers enter by real-time segment membership and move through as their behavior changes.

.. meta::
    :content class=swiftype name=body data-type=text:
        A real-time journey is an always-on program that customers enter by real-time segment membership and move through as their behavior changes.

.. meta::
    :content class=swiftype name=title data-type=string:
        About real-time journeys

==================================================
About real-time journeys
==================================================

.. real-time-journeys-overview-start

A **real-time journey** is an always-on program that customers move through as their behavior changes. Travelers enter a real-time journey through their membership in a :doc:`real-time segment <real_time_segments>`, move through the journey's stages--activations, waits, and splits--and exit when they meet the journey's exit criteria. Every traveler's path is recorded in a **travel log**.

.. real-time-journeys-overview-end


.. _real-time-journeys-vs-batch:

Real-time journeys and batch journeys
==================================================

.. real-time-journeys-vs-batch-start

Real-time journeys and :doc:`batch journeys <journeys>` share the journey canvas and the same building blocks--activation, wait, conditional-split, percent-split, and merge nodes--but differ in when and how they run:

* A **real-time journey** runs continuously. Travelers enter and advance in real time as inbound events change their profiles.
* A **batch journey** runs on a schedule or recurrence.

Real-time journeys add a **quiet-hours** node, which holds travelers until a quiet window--such as overnight in the customer's local time zone--ends, so that messages are not sent at inconvenient times. A profile collection supports up to 50 real-time journeys.

Real-time journeys deliberately do not include the batch journey's measurement features. **Goals, milestones, and conversion-rate metrics are batch-only**; a real-time journey does not track them. To analyze a real-time journey, use its travel log.

.. real-time-journeys-vs-batch-end


.. _real-time-journeys-entry:

How travelers enter
==================================================

.. real-time-journeys-entry-start

Travelers enter a real-time journey through **real-time segment membership**: a customer enters the moment they become a member of the segment that gates the journey, and the journey reacts to that entry as it happens.

To start a journey in response to a specific event--an abandoned cart, a status change--model that event as a real-time segment. Define an attribute that captures the event and a segment whose predicate tests it; the customer enters the journey the moment that event moves them into the segment. Because a real-time segment re-evaluates whenever a profile changes--on each event, and on the scheduled recalculation of time-dependent attributes--segment membership is how a real-time journey responds to "when X happens."

.. real-time-journeys-entry-end

.. TODO: event-triggered entry ("Trigger event" journey type) is in progress: the web UI and web-api support it only behind the new-journey-wizard flag, there is no filter on the trigger event, and the MCP refuses inclusion_event (Linear P-TECH-55, target 2026-10-30). Per Q2, the docs frame segment entry as the supported path with no availability label. Revisit when event-triggered journeys reach GA.


.. _real-time-journeys-reentry:

Re-entry and testing
==================================================

.. real-time-journeys-reentry-start

A real-time journey controls whether, and how soon, a traveler can enter again:

* **Re-entry** allows a customer who has left the journey to enter it again the next time they join its segment.
* A **cooldown**--from minutes to months--sets how long after leaving a traveler must wait before re-entering.
* **Linked journeys** extend the re-entry check to other journeys you name, so that a customer's recent path through a related journey is considered when deciding whether they can enter this one.

Use **test mode** to validate a real-time journey before it sends. In test mode, travelers move through the journey as they would in production, but activations are not sent to the destination and the journey does not write to its travel log.

.. real-time-journeys-reentry-end


.. _real-time-journeys-travel-log:

The travel log
==================================================

.. real-time-journeys-travel-log-start

As travelers move through a real-time journey, Amperity records their paths in a **travel log**. The travel log holds one row for each **stage** a traveler enters--the start of the journey, each node, and how they left, by meeting an exit or by completing the journey. Each row records when the traveler entered the stage and the stage they came from, so the rows for a traveler reconstruct their path in order. When a traveler exits, the row captures **why**: the segment, journey, or event that caused the exit.

The travel log is data, not a screen in Amperity. To analyze it--who entered, how they moved, and where they left--:ref:`export it <real-time-journeys-export>` to a downstream system.

.. real-time-journeys-travel-log-end


.. _real-time-journeys-holdout:

Holdout and A/B testing
==================================================

.. real-time-journeys-holdout-start

When a real-time journey splits travelers with a percent-split node, the travel log rows for each path record the path's **test group** name and whether it is the **control** group. Designate one path as the control group and the others as test groups, then use the test-group and control information in the travel log to measure the journey's effect against the holdout.

.. real-time-journeys-holdout-end


.. _real-time-journeys-export:

Exporting the travel log
==================================================

.. real-time-journeys-export-start

A real-time journey's scheduled work is exporting its travel log. On its schedule, the journey sends new travel-log records to a configured :doc:`destination <page_destinations>`, so that the data can land in a downstream system for analysis. Each run picks up the records added since the previous export.

.. real-time-journeys-export-end


.. _real-time-journeys-in-segments:

Real-time journeys in segments
==================================================

.. real-time-journeys-in-segments-start

You can reference a real-time journey from a segment. A segment can test whether a customer is **currently in** a real-time journey and use that membership as part of its definition.

Segment clauses that test whether a customer **reached a goal** or **reached an exit** do not apply to real-time journeys: real-time journeys do not track goals and exits the way batch journeys do, so those clauses return no results for a real-time journey.

.. real-time-journeys-in-segments-end

.. TODO: verify with <eng> -- that "reached a goal" / "reached an exit" segment clauses return no results for real-time journeys. Not confirmed in the feature context; the journey entity does carry goal segments.

.. TODO: open-as-segment (turning a real-time journey's travelers into a segment) is not documented here pending NC8 -- no backend path was found in discovery; confirm whether it is a web-UI action and how it behaves before documenting it.
