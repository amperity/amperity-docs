.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A real-time segment is an always-on audience whose membership Amperity maintains continuously as customer profiles change.

.. meta::
    :content class=swiftype name=body data-type=text:
        A real-time segment is an always-on audience whose membership Amperity maintains continuously as customer profiles change.

.. meta::
    :content class=swiftype name=title data-type=string:
        About real-time segments

==================================================
About real-time segments
==================================================

.. real-time-segments-overview-start

A **real-time segment** is an always-on audience defined over a :doc:`profile collection <real_time_profiles>`. Rather than a query you run to produce a list, a real-time segment is a predicate that Amperity evaluates continuously: as inbound events change a profile, Amperity re-evaluates the segment for that profile and adds or removes it. A real-time segment is a dynamically maintained audience, not a point-in-time query result. It is also called an :ref:`always-on segment <a-always-on-segment>`.

.. real-time-segments-overview-end


.. _real-time-segments-vs-database:

Real-time segments and database segments
==================================================

.. real-time-segments-vs-database-start

Real-time segments and :doc:`database segments <segments>` are different objects, and Amperity manages them separately:

* A **real-time segment** is a predicate bound to a **profile collection**. Its membership is maintained continuously, in real time, as the collection's profiles change.
* A **database segment** is a query bound to a **database**. Its membership is produced by running that query as a batch job.

Use a real-time segment when membership has to reflect a customer's most recent activity the moment it happens--for example, to drive a :ref:`real-time journey <r-real-time-journey>`. Use a database segment for audiences built from your customer 360 database on a scheduled or on-demand basis.

.. real-time-segments-vs-database-end


.. _real-time-segments-membership:

How membership is maintained
==================================================

.. real-time-segments-membership-start

A real-time segment's predicate is written in :doc:`Amperity's expression language <expressions>` and evaluated against each profile in the bound collection. As events update a profile, Amperity re-evaluates the predicate for that profile: a profile that newly satisfies it **enters** the segment, and a profile that no longer satisfies it **exits**. These entries and exits are the signal that drives :ref:`real-time journeys <r-real-time-journey>`--a customer entering a segment is what starts them on a journey.

You can read a segment's current membership--the profiles that belong to it right now--through the Real-time API. See the `Real-time API endpoint reference <../api/endpoints_realtime.html>`__.

.. real-time-segments-membership-end


.. _real-time-segments-backfill:

Backfill and membership state
==================================================

.. real-time-segments-backfill-start

When you create a real-time segment, or change its definition, Amperity **backfills** its membership by evaluating the collection's existing profiles against the predicate. Backfill has a status of its own: pending, in progress, complete, or paused.

A segment's **member count** and its **backfill status** are distinct. In particular, a membership count shown as a dash is not the same as a count of zero:

* A **dash** means membership has not been computed yet--for example, a backfill that has not started.
* A **0** means membership has been computed and the segment currently has no members.

Reading a segment's state returns the backfill status separately from the member count, so you can tell "not computed yet" apart from "computed and empty."

.. real-time-segments-backfill-end
