.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        A recommendation is Pér proposing work worth doing, with its evidence, its constraints and how confident it is attached.

.. meta::
    :content class=swiftype name=body data-type=text:
        A recommendation is Pér proposing work worth doing, with its evidence, its constraints and how confident it is attached.

.. meta::
    :content class=swiftype name=title data-type=string:
        Recommendations


.. _per-recommendations:

==================================================
Recommendations
==================================================

A recommendation is Pér proposing something worth doing, with the argument attached: the claims it
rests on, the numbers behind those claims, where in your data they came from, the constraints it
worked under, and how confident it is and why. Recommendations gather in the Portfolio, which is
where Pér puts the work it thinks deserves your attention.

A recommendation is the part of Pér you are meant to be able to disagree with. An answer you have
to take on trust is worth less than a proposal you can check, and acting on one is the shortest
route from "that looks right" to configured, approved work. This is the
:ref:`Recommend <per-customer-decision-loop-recommend>` stage of the customer decision loop.


.. _per-recommendations-what-it-carries:

What a recommendation carries
==================================================

Each recommendation carries the case for itself, not just the conclusion.

Every part of it is there so you can test the proposal rather than weigh it. If you cannot find
fault with the evidence, that is a reason to act; if you can, you have found it before anything
ran.

A recommendation carries:

* **What it proposes**, as the action to take.
* **Evidence.** A list of claims, each with the measure and value behind it and where in your data
  it came from. A claim drawn from a query records the tables that query read, so you can see what
  it was based on.
* **Constraints.** The limits Pér worked within when it put the proposal together.
* **Confidence.** A grade — **High confidence**, **Medium confidence** or **Low confidence** —
  and the reasoning behind that grade, including what Pér could not establish. A recommendation
  Pér could not assess reads **Needs review** instead.

Opening a recommendation's evidence starts a conversation about it. You get the reasoning behind
the grade and the evidence it was given, and because it is a conversation rather than a panel, you
can push further and have Pér query your data to answer.

.. note::

   The query behind a claim is not shown. What you get is the claim, the number, and the tables it
   was read from.


.. _per-recommendations-refresh:

Where recommendations come from
==================================================

Recommendations are produced by a refresh, which someone asks for.

This answers two questions that come up in the first week: why the board looks the same as it did
yesterday, and why something that was on it has gone. Both have the same answer — the board
changes when a refresh runs, and not before.

.. note::

   Pér produces recommendations when someone asks for a fresh set, not continuously. You can see
   when the current set was produced.

What a refresh draws on:

* Your tenant's own customer data.
* Your company context and your memories.
* What Pér has already carried out for you, and what is already proposed — so the board does not
  keep re-proposing work you have started.
* Recent public news, where it bears on the question.

How a refresh behaves:

* **One at a time.** A tenant runs one refresh at a time; asking for another while one is running
  is declined rather than queued.
* **You can stop one.** A run you stop ends without changing the board.
* **It can honestly find nothing.** A refresh that completes with no new recommendations says so,
  rather than implying something arrived.

Recommendations belong to the tenant, not to you. Everyone working in your tenant sees the same
board, and a recommendation one person dismisses leaves it for everyone.

.. FORWARD-LINK: interface_tour.rst, company_context.rst, memory.rst: link the Portfolio, company
   context and memories once those articles exist.


.. _per-recommendations-acting:

Acting on a recommendation
==================================================

Acting on a recommendation turns it into a :ref:`plan <per-plans>`.

This is the hinge of the whole loop — the point where an argument becomes work. It is also the
point at which the approval boundary takes over, because a plan is a list of changes waiting for
you to approve them.

What happens when you act on one:

* **Pér writes the plan.** It reads the recommendation in full, does the minimum reads needed to
  turn the intent into concrete Amperity changes, and writes the steps. This takes a few seconds.
* **Nothing runs.** Writing a plan executes none of it. Every step still waits for approval.
* **One plan per recommendation.** If a plan has already been written for a recommendation and has
  not been started, acting on it again opens that plan rather than writing a second one.
* **It can come back with no plan.** A recommendation that does not yet map to a change in
  Amperity produces no plan, and Pér says so rather than inventing steps.


.. _per-recommendations-lifecycle:

When a recommendation stops being offered
==================================================

A recommendation leaves the board in one of three ways.

A board that keeps proposing work you have already started is worse than no board, so a
recommendation is retired as soon as there is a reason to retire it.

* **Addressed.** Once the plan written from a recommendation finishes, that recommendation is
  marked as addressed and stops being offered.
* **Dismissed.** You can dismiss a recommendation you do not intend to act on. It leaves the board
  for everyone in the tenant, and the dismissal is recorded in the Activity log.
* **Superseded.** At the end of a successful refresh, earlier recommendations the run did not
  propose again are retired — unless a plan for one is still live, in which case it stays.

.. FORWARD-LINK: activity_log.rst: link "the Activity log" once that article exists.


.. _per-recommendations-using:

Working with recommendations
==================================================

**To read a recommendation's evidence**

#. On a recommendation, click **Evidence →**.

A conversation opens with the recommendation's evidence and the reasoning behind its confidence
grade. Ask follow-up questions there.

**To see why Pér graded its confidence**

#. Click the confidence grade on the recommendation.

The reasoning opens under a heading naming the grade, such as **Why high confidence?**

**To ask for a fresh set of recommendations**

#. In the Portfolio, click **Refresh recommendations**.
#. Wait for the run to finish, or click **Stop** to end it.

**To act on a recommendation**

#. Click **Propose plan**.
#. Wait while Pér writes the plan, then review the steps.

A recommendation that already has a plan waiting reads **View plan** instead.

**To dismiss a recommendation**

#. Open the recommendation's menu and choose to remove it.
#. Confirm.

.. FORWARD-LINK: chatting_with_per.rst: link "a conversation opens" once that article exists.
