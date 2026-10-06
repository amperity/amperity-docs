.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        A skill is a named piece of work with a method behind it, so you get a considered analysis rather than whatever a cold question produces.

.. meta::
    :content class=swiftype name=body data-type=text:
        A skill is a named piece of work with a method behind it, so you get a considered analysis rather than whatever a cold question produces.

.. meta::
    :content class=swiftype name=title data-type=string:
        Skills


.. _per-skills:

==================================================
Skills
==================================================

A skill is a route Pér already knows. It is a named piece of work with a method behind it — what to
look at, in what order, what to check before drawing a conclusion — so you can ask for it by name
rather than describing it from scratch.

The hard part of asking an agent for analysis is knowing what to ask for. A skill is Amperity's
answer to that for the work customers do most often. Most skills carry you from
:ref:`understanding something <per-customer-decision-loop-understand>` to
:ref:`a recommendation you can act on <per-customer-decision-loop-recommend>` in one run.


.. _per-skills-what-it-is:

What a skill is
==================================================

A skill is a workflow with a method, started by name.

Because it is persistent and repeatable, it is a reliable way to get quality answers that don't
depend on reproducing specific wording.

* **You start one by name**, from the chat input box.
* **Pér can start one itself** when what you asked for clearly matches a skill, and it says which
  one it is using. It is never a silent change of mode.
* **A skill's instructions are Amperity's material**, so Pér follows them for the task the skill
  covers — and stops when you ask it to stop. Where you take the work afterwards is yours.
* **Starting one while an answer is still running** puts it in the chat input box ready for your
  message, rather than interrupting what is in flight.

.. important::

   A skill does not change what Pér can do without asking. Anything a skill does in Amperity is
   still a change you approve, on a confirmation or as a step of a plan. See
   :ref:`Where the boundary sits <per-approvals-boundary>`.


.. _per-skills-availability:

Which skills you have
==================================================

Which skills you can start depends on your tenant, and the list you see is the list you can run.

That matters for two reasons: the set is not the same everywhere, so a colleague at another company
may have a different one; and there is no hidden menu to go looking for. A skill your tenant does
not have is not shown to you as unavailable — it is simply not in the list.

A tenant with none available is told so, rather than shown an empty picker.

.. PENDING NC-013: which skills may carry the Pér story is a PO question. Five are visible to an
   ordinary tenant at the pin; the GTM material's flagship example is an internal-only skill, and
   one of the five is housekeeping rather than a business outcome.


.. _per-skills-available:

The skills available today
==================================================

Five skills are available to an ordinary tenant. Each one says what it produces and what it needs
from you, because that is what decides whether to start it.

Build company context
--------------------------------------------------

Works out what your tenant already has, interviews you about what is ambiguous or missing, shows
you the finished document, and publishes it once you approve. Reach for it when your
:ref:`company context <per-company-context>` is empty or has gone stale, and you would rather be
asked good questions than face a blank page.

1x buyer conversion
--------------------------------------------------

Diagnoses one-time buyers: how large the group is and whether it is growing, what first purchases
tend to predict a second one, what the paths of customers who did return look like, and how much of
the group is realistically addressable. It runs as a conversation and works through those questions
in order, so you can stop when you have what you need.

Aggregate campaign reporting
--------------------------------------------------

Reports one campaign's aggregate results, broken out by calendar month from its first delivery
through to today, with the window each figure covers stated beside it. Partial months are marked as
partial, and any group of metrics it could not compute is named rather than quietly omitted. You
can ask for a different window once you have the first answer.

If Pér cannot establish when the campaign was delivered, it does not pick a window anyway. It
reports what was sent instead — when the sends first and last started, and how many ended in each
state — and says separately that the results cannot be computed without a delivery date.

.. PENDING NC-014: D9 holds all measurement, holdout, incrementality, lift and attribution
   language. This skill is documented as reporting — what it aggregates, over what window, what it
   could not compute, and what it reports instead when the window cannot be anchored.

Set up event propensity
--------------------------------------------------

Turns a business question into a target event, checks that your event tables actually hold usable
data for it, builds competing model variants, validates them, and activates the one you choose. It
stops for you twice: once to confirm the data is fit for the question, and once to pick the winner.

Review memories
--------------------------------------------------

Reads the :ref:`memories <per-memory-reviewing>` available to the conversation and looks for
duplicates and contradictions. It proposes changes and does not make them, and it tells you when
the set it reviewed may not have been complete. Housekeeping rather than analysis, and worth
running when your memory set has grown.


.. _per-skills-using:

Starting a skill
==================================================

**To start a skill**

#. Click **+** beside the chat input box and choose **Skills**, or type ``/`` in the empty box.
#. Choose the skill you want.
#. Answer what it asks you.

**To find a skill**

#. Open the skill picker and start typing.

The picker matches on more than the words shown in the list, so a skill can surface on a term that
is not in its name.
