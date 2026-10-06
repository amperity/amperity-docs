.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        One piece of work from a question to something you can hand to somebody — the customer decision loop, once, end to end.

.. meta::
    :content class=swiftype name=body data-type=text:
        One piece of work from a question to something you can hand to somebody — the customer decision loop, once, end to end.

.. meta::
    :content class=swiftype name=title data-type=string:
        Quickstart: your first session


.. _per-quickstart:

==================================================
Quickstart: your first session
==================================================

This walks one piece of work the whole way: a question, a proposal you can check, a plan, the
approvals that let it run, and something you can hand to somebody afterwards.

This article traces the :ref:`customer decision loop <per-customer-decision-loop>` with the product
names attached, so by the end of it the five stages should have stopped being abstract.

**Before you start**

* **Your tenant has to be enabled for Pér**, and you have to be able to get in. See
  :ref:`Accessing Pér <per-accessing-per>`.
* **What you can do inside Pér is your own Amperity access**, not something Pér grants. If you
  cannot read a table in Amperity, Pér cannot read it for you.
* **Nothing in this walk changes your tenant until you approve it.** You can follow it as far as
  the last section and still have changed nothing.


.. _per-quickstart-ask:

Ask something
==================================================

Start by asking Pér a question about your own customers, in your own words.

This tells you what Pér can see, how it reasons about your data, and whether your tenant holds what
you assumed it held — all before you have committed to anything. This is :ref:`Understand
<per-customer-decision-loop-understand>`.

What to expect:

* **Pér says what it is about to do before it does it**, one plain sentence at a time, so a long
  answer is something you can follow rather than wait out.
* **The work happens on Amperity's servers.** You can move to another page or close the browser;
  the answer is still produced, and it is there when you come back.
* **Answers are short on purpose.** Ask for more.

**To ask Pér something**

#. Type your question in the chat panel and click **Ask Pér**.

Good first questions are concrete and about your own data — for example, how many customers bought
twice last year, which segment has grown most since spring, what a particular audience actually
contains.

See :ref:`Chatting with Pér <per-chatting>`, and
:ref:`How Pér uses your data <per-how-per-uses-your-data>` for what it reads and under whose
access.


.. _per-quickstart-recommendation:

Read a recommendation
==================================================

Next, look at something Pér proposes, and at the argument underneath it.

A recommendation is the part of Pér you are meant to be able to disagree with. Reading the
evidence now is the best moment to find a problem with it — far better than finding it after
a campaign has gone out. This is :ref:`Recommend <per-customer-decision-loop-recommend>`.

**This step has a prerequisite the others don't.** Recommendations are produced by a refresh that
somebody asks for, so on a tenant where nobody has asked yet the Portfolio is empty. That is
normal, not a fault.

* **A refresh takes a while**, and a tenant runs one at a time.
* **You can stop one**, and stopping it leaves the Portfolio as it was.
* **It can come back with nothing**, and says so rather than implying something arrived.

Each recommendation carries what it proposes, the evidence for it (including claims, the numbers
behind them, and where in your data they came from), the constraints Pér worked within, and a
confidence grade with the reasoning for that grade, including what Pér could not establish.

**To get a first set of recommendations**

#. Open the **Portfolio**.
#. Click **Retrieve recommendations**, or **Refresh recommendations** if there is already a set.
#. Wait for the run to finish.

**To read the argument behind one**

#. On a recommendation, click **Evidence**.

That opens a conversation about the recommendation rather than a panel, so you can push on it:
ask where a number came from, or have Pér query your data to check it.

See :ref:`Recommendations <per-recommendations>`.


.. _per-quickstart-plan:

Act on it
==================================================

Acting on a recommendation turns it into a plan.

This is the point where an argument becomes a list of proposed concrete changes to your Amperity
tenant, each one waiting for a person. It is where :ref:`Approve
<per-customer-decision-loop-approve>` begins.

* **Pér writes the plan**, reading what it needs to turn the intent into real identifiers,
  tables and settings. This takes a few seconds.
* **Nothing runs.** Writing a plan runs none of it.
* **One plan per recommendation.** Acting on one that already has a plan waiting opens that plan
  rather than writing a second.
* **It can come back with no plan.** A recommendation that does not yet map to a change in
  Amperity produces none, and Pér says so rather than inventing steps.

**To act on a recommendation**

#. Click **Propose plan**, or **View plan** if one is already waiting.
#. Wait while Pér writes it, then read the steps.

See :ref:`Plans <per-plans>` and :ref:`How a plan gets written <per-plans-authoring>`.


.. _per-quickstart-approve:

Approve the steps
==================================================

Read the plan, then approve it — a step at a time, or all at once.

This is the only point in the process where actual changes are made in your Amperity tenant. It
spans :ref:`Approve <per-customer-decision-loop-approve>` and :ref:`Act
<per-customer-decision-loop-act>`.

* **A step that only reads runs itself.** It changes nothing, so it needs no approval — unless
  it is there so you can read a long job's results, in which case it waits for you.
* **A step that changes something shows a write confirmation**, naming the operation, the object
  and the values that will be sent. Read it; it is deliberately specific rather than reassuring.
* **Your permission is checked again at the moment you approve**, not only when the step was
  written. A change you are not permitted to make is refused, and Pér names the permission that
  is missing rather than working around it.
* **A plan stops short of sending.** A campaign it creates is left a draft and a journey it
  creates is left paused. Scheduling the send stays yours.
* **A plan moves while you are signed in with Pér open**, and picks up again on your next visit.
* **What happened is recorded.** Plan steps that ran, plans reverted and steps retried all reach
  the :ref:`Activity log <per-activity-log>`.

You can also approve the whole plan at once. When you approve and run a whole plan, you
approve the plan — not each write inside it one at a time. Pér then re-checks at every step
whether it may still go on, stops at any step that needs a person, and records which steps it
approved on your behalf.

.. important::

   Approving a plan is not the same as watching each write go by. One approval can set a sequence
   of Amperity writes running, and a write that has run cannot be undone from Pér. Read a plan's
   steps before you approve it — and on a first session, approve them one at a time.

.. PENDING NC-005: "you approve the plan, not every write" — PO to bless this wording. It is the
   same sentence used in what_is_per.rst, customer_decision_loop.rst, plans.rst and
   approvals_and_write_confirmations.rst.

**To approve one step**

#. Read the step's confirmation.
#. Click **Run step**.

**To approve and run the whole plan**

#. Read every step.
#. Click **Approve & run all** at the top of the plan.

See :ref:`Approvals and write confirmations <per-approvals>`.


.. _per-quickstart-artifact:

Keep what you found
==================================================

Finish by asking Pér to write up what happened, and share it.

A piece of work goes beyond a plan concluding; it is only finished when the people who have to act
on it can read it without you in the room. This is :ref:`Learn <per-customer-decision-loop-learn>`.

* **You ask for it.** A plan does not produce a write-up on its own — a report exists because
  somebody asked Pér for one.
* **It needs no approval**, because publishing one changes nothing in Amperity.
* **It is private until you share it**, and sharing is to everyone in your tenant rather than to
  named people.
* **Asking for a change rewrites the same artifact** rather than making a second one.

**To have Pér write something up**

#. In the conversation, ask for a readout, a one-pager or a summary of what was done.

**To share it**

#. On the artifact, click **Share with your team**.

Two more things worth doing on a first session, now that you have something to compare them to:

* **Tell Pér what to remember.** Anything you had to explain once — how your business defines a
  term, a rule it should always work inside — can be kept, so you do not explain it again. See
  :ref:`Memory <per-memory>` and :ref:`Company context <per-company-context>`.

.. PARKED-LINK: notifications.rst: restore the "Check your notifications" bullet to this list.

See :ref:`Artifacts <per-artifacts>`.


.. _per-quickstart-next:

Where to go next
==================================================

* :ref:`Chatting with Pér <per-chatting>` — attaching a file, starting a skill, and how much
  thinking to ask for.
* :ref:`Approvals and write confirmations <per-approvals>` — the approval boundary in full,
  including what Pér cannot do whatever you approve.
* :ref:`Plans <per-plans>` — what a plan carries, and what happens when a step fails.
* :ref:`Company context <per-company-context>` — the fastest way to make recommendations better.
* :ref:`Interface tour <per-interface-tour>` — what every other part of the window is for.
