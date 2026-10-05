.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        The customer decision loop is the cycle Pér works in: understand, recommend, approve, act, learn.

.. meta::
    :content class=swiftype name=body data-type=text:
        The customer decision loop is the cycle Pér works in: understand, recommend, approve, act, learn.

.. meta::
    :content class=swiftype name=title data-type=string:
        The customer decision loop


.. _per-customer-decision-loop:

==================================================
The customer decision loop
==================================================

Marketing work on customer data follows a shape, whatever the campaign: someone works out what is
happening with a group of customers, proposes what to do about it, agrees on a plan, makes it
happen in the tools, and carries what they learn into the next round.

In brief:
**Understand → Recommend → Approve → Act → Learn**

This is the customer decision loop, and it is what Pér is built around.

Knowing the loop is the quickest way to find your way around Pér, because every part of Pér serves
one of its stages. This documentation is, in effect, a close-up of one stage at a time.


.. _per-customer-decision-loop-understand:

Understand
==================================================

Pér works out what is actually happening with your customers.

Nothing further along the loop is worth anything if this stage is wrong, which is why Pér shows
its work rather than handing you a conclusion. You can follow what it looked at and check it
against what you know.

You do this stage in conversation. Ask a question in plain language and Pér queries your tenant's
own customer data to answer it — the same identity-resolved records your organization already
relies on, read under your own Amperity access. As it works, it says in one line what it is about
to look at and why, so you can follow the shape of the analysis before the answer arrives.

What Pér brings to the question, beyond the data: the company context your tenant has set up, the
memories you have given it, and what it can find on the web.


.. _per-customer-decision-loop-recommend:

Recommend
==================================================

Pér proposes something worth doing, and makes the argument for it.

A recommendation is a proposal with its evidence attached: the claims it rests
on, the numbers behind those claims, and where in your data they came from. It also carries a
confidence grade and the reasoning behind that grade, including what Pér could not establish.
You are meant to be able to disagree with it on the evidence.

Recommendations gather in the Portfolio, which is where Pér puts the work it thinks is worth your
attention. They are drawn from your tenant's data, your company context and your memories,
together with what Pér has already carried out for you and what it has already proposed — so the
Portfolio does not keep re-proposing work you have started.

.. note::

   Pér produces recommendations when someone asks for a fresh set, not continuously. You can see
   when the current set was produced.


.. _per-customer-decision-loop-approve:

Approve
==================================================

Nothing happens in Amperity until a person says so.

Because approval is a real gate rather than a formality, you can let Pér do the work of figuring out
*what* should happen without giving up control of *whether* it happens.

Acting on a recommendation authors a plan: a titled list of steps, each one a concrete change to
your Amperity tenant. You can also ask for a plan directly in conversation, and Pér will author
one. Either way, you read the steps before any of them runs.

When you approve and run a whole plan, you approve the plan — not each write inside it one at
a time. Pér then re-checks at every step whether it may still go on, stops at any step that needs
a person, and records which steps it approved on your behalf.

.. important::

   Read a plan's steps before you approve it. One approval can kick off a sequence of Amperity
   writes, and a write that has run cannot be undone from Pér.

.. PENDING NC-005: "you approve the plan, not every write" — PO to bless this wording. It is the
   same sentence used in what_is_per.rst and is reused in approvals_and_write_confirmations.rst
   and plans.rst.


.. _per-customer-decision-loop-act:

Act
==================================================

The approved steps run in Amperity.

This means the audience now exists, the campaign is configured, and the model is trained. Nothing
is left for you to go and replicate by hand.

Steps run in order, and some of them start work that takes a while, for example, training a model or
running a database. Pér waits for those and carries on when they finish. If a step fails, it says
what went wrong rather than leaving the plan stuck, and you can fix the cause and run that step
again.

Work you approved may finish after you have moved on to something else. When something finishes
after you have moved on, Pér raises a notification so you find out without having to go back and
check.


.. _per-customer-decision-loop-learn:

Learn
==================================================

What happened feeds what Pér does next.

This stage is what makes the second round better than the first — both for you, in having a record
to look back at, and for Pér, in not starting cold.

Three things carry forward:

* **What you told Pér to remember.** Memories persist between sessions, so a preference, a rule or
  a correction only has to be given once.
* **What Pér did.** The Activity log keeps a record of its actions and its recommendations.
* **What Pér produced.** Reports it writes and files you give it are kept as artifacts, which you
  can come back to or share with your team.

The next set of recommendations is drawn with all of that in view, including the steps you have
already carried out and the recommendations already in the Portfolio.


.. _per-customer-decision-loop-limits:

Where the loop stops
==================================================

The loop does not activate or repeat by itself.

That is worth stating plainly, because "loop" can suggest something running in the background on
your behalf. Pér does not watch your tenant, does not act between sessions, and does not start a
new round on its own. Each turn begins when a person begins it.

Nor does Pér close the loop for you on the question of whether the work was worth doing. It keeps
a record of what it did and what it produced; judging the business result of that work is still
yours.

.. PENDING NC-020: what the Learn stage may claim, and whether the loop may be described as
   recurring. Memory, the Activity log and artifacts carry forward and are verified; measurement
   and automatic re-running are barred (D9, rules §7). PO.
