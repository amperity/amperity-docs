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
worked under, and how confident it is and why. Recommendations gather in the
:ref:`Portfolio <per-interface-tour-pages>`, which is where Pér puts the work it thinks deserves
your attention.

A recommendation is the part of Pér you are meant to be able to disagree with. This is the
:ref:`Recommend <per-customer-decision-loop-recommend>` stage of the customer decision loop.


.. _per-recommendations-what-it-carries:

What a recommendation carries
==================================================

Each recommendation presents its evidence, not just the conclusion.

If you cannot find fault with the evidence, that is a reason to act; if you can, you have found it
at an ideal time to correct course, before anything ran.

A recommendation carries:

* **What it proposes**, as the action to take.
* **Evidence.** A list of claims, each with the measure and value behind it and where in your data
  it came from. A claim drawn from a query records the tables that query read, so you can see what
  it was based on.
* **Constraints.** The limits Pér worked within when it put the proposal together.
* **Confidence.** A grade — **High confidence** or **Medium confidence** — and the reasoning
  behind it, including what Pér could not establish. One Pér could not assess at all reads
  **Needs review**. Not every recommendation carries a grade: one Pér was less sure of, or has not
  finished assessing, shows none and sorts below the ones that do.

Opening a recommendation's evidence starts a conversation about it. You get the reasoning behind
the grade and the evidence it was given, and because it is a conversation rather than a panel, you
can push further and have Pér query your data to answer.

.. note::

   The query behind a claim is not shown. What you get is the claim, the number, and the tables it
   was read from.


.. _per-recommendations-refresh:

Where recommendations come from
==================================================

Recommendations are produced by a refresh. Apart from the very first one, a refresh happens
because someone asked for it.

This answers two common questions: why the Portfolio looks the same as it did yesterday, and why
something that was on it has gone. Both have the same answer: the Portfolio changes when a refresh
runs, and not before.

.. note::

   Pér produces recommendations a set at a time, not continuously. You can see when the current
   set was produced.

What a refresh draws on:

* Your tenant's own customer data.
* Your :ref:`company context <per-company-context>` and your :ref:`memories <per-memory>`.
* What Pér has already carried out for you, and what is already proposed — so the Portfolio does
  not keep re-proposing work you have started.
* Recent public news, where it bears on the question.

How a refresh behaves:

* **One at a time.** A tenant runs one refresh at a time; asking for another while one is running
  is declined rather than queued.
* **You can stop one.** A run you stop ends without changing the Portfolio.
* **It can honestly find nothing.** A refresh that completes with no new recommendations says so,
  rather than implying something arrived.
* **The first one starts itself.** On a tenant where no refresh has ever run, Pér starts one when
  the Portfolio is first opened, so it is not empty on arrival. Every refresh after that waits to
  be asked for.

Recommendations belong to the tenant, not to you. Everyone working in your tenant sees the same
Portfolio, and a recommendation one person dismisses leaves it for everyone.


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
* **Nothing runs.** Writing a plan runs none of it. Every step still waits for approval.
* **One plan per recommendation.** If a plan has already been written for a recommendation and has
  not been started, acting on it again opens that plan rather than writing a second one.
* **It can come back with no plan.** A recommendation that does not yet map to a change in
  Amperity produces no plan, and Pér says so rather than inventing steps.


.. _per-recommendations-lifecycle:

When a recommendation stops being offered
==================================================

A recommendation leaves the Portfolio in one of three ways, and is retired as soon as there is a
reason to retire it.

* **Addressed.** Once the plan written from a recommendation finishes, that recommendation is
  marked as addressed and stops being offered.
* **Dismissed.** You can dismiss a recommendation you do not intend to act on. It leaves the
  Portfolio for everyone in the tenant, and the dismissal is recorded in the
  :ref:`Activity log <per-activity-log>`.
* **Superseded.** At the end of a successful refresh, earlier recommendations the run did not
  propose again are retired — unless a plan for one is still live, in which case it stays.


.. _per-recommendations-using:

Working with recommendations
==================================================

**To read a recommendation's evidence**

* On a recommendation, click **Evidence**.

A :ref:`conversation <per-chatting>` opens with the recommendation's evidence and the reasoning
behind its confidence grade. Ask follow-up questions there.

**To see why Pér graded its confidence**

* On a recommendation that shows a grade, click the grade.

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

