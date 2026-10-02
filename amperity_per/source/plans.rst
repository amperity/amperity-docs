.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        A plan is a titled, ordered list of changes to Amperity, each one approved before it runs.

.. meta::
    :content class=swiftype name=body data-type=text:
        A plan is a titled, ordered list of changes to Amperity, each one approved before it runs.

.. meta::
    :content class=swiftype name=title data-type=string:
        Plans


.. _per-plans:

==================================================
Plans
==================================================

A plan is where work Pér proposes becomes work that runs: a titled, ordered list of steps, each
step a concrete change to your Amperity tenant, and each one approved by a person before it
happens. A plan also carries the reason it exists, what to watch out for, and what it produced.

A plan is the difference between advice and work. It is durable and resumable — you can leave it,
come back tomorrow, and it is still there with its history — and it is the one place to read
everything Pér intends to do before any of it happens. Plans span two stages of the customer
decision loop: :ref:`Approve <per-customer-decision-loop-approve>`, then
:ref:`Act <per-customer-decision-loop-act>`.


.. _per-plans-what-a-plan-is:

What a plan is
==================================================

A plan gathers everything one piece of work needs into a single object.

There is no second kind of record to learn and no separate place where the detail lives. What will
change, in what order, why, what could go wrong, and what came out of it are all on the plan.

A plan carries:

* **Steps**, in order. Each one is a concrete change to Amperity, stated as the change it is.
* **The reason the plan exists** — the argument for the whole thing, above the steps.
* **Risk flags.** What could go wrong or needs watching once the plan runs, graded **High**,
  **Medium** or **Low**, with the highest first. Where a risk has a measure worth keeping an eye
  on, that is listed beside it.
* **What it created in Amperity**, as objects you can open.
* **A status** — **In progress**, **Complete**, **Failed** or **Abandoned**.

Plans belong to the tenant, not to you. Everyone working in your tenant sees the same list of
plans.

.. FORWARD-LINK: interface_tour.rst: link the Plans list once that article exists.


.. _per-plans-authoring:

How a plan gets written
==================================================

Plans are written two ways, and both produce the same thing.

You can act on a recommendation, or you can ask for a plan in conversation. Either way the steps
are written by Pér's planning agent, so what you learn from one route applies to the other.

* **From a recommendation.** Acting on a recommendation hands it to the planning agent, which
  reads it in full and turns it into concrete changes. See
  :ref:`Acting on a recommendation <per-recommendations-acting>`.
* **From a conversation.** Ask Pér to set up, build or launch something that takes several changes
  in Amperity, or that involves a long-running job, and it writes a plan rather than making the
  changes one at a time. A card appears in the conversation with the plan's title and how many
  steps there are to review.

How plans are written:

* **The smallest correct plan.** Pér prefers the fewest steps that do the job, and a one-step plan
  is a normal outcome. A plan holds at most sixteen steps.
* **Reads only, to make the writes concrete.** While writing a plan, Pér reads what it needs to
  fill in real identifiers, tables and settings. It changes nothing.
* **A single send is a campaign; a sequence is a journey.** When the work is one one-time send, the
  plan creates a campaign. When it is more than one send, has a wait between sends, or branches on
  whether someone opened or clicked, the plan creates a journey instead. A sequence cannot be
  expressed as a campaign, and Amperity rejects one that tries.
* **A plan stops short of sending.** A campaign it creates is left a draft and a journey it creates
  is left paused. Scheduling the send is yours.
* **Pér does not write the content of a send.** It builds the audience, the campaign or the
  journey and the configuration around it; the creative is not its work.
* **A missing destination is stated, not invented.** If a channel the work needs has no destination
  set up in Amperity, Pér writes the smaller plan your existing destinations support and says
  plainly, in that step, what is missing.


.. _per-plans-approving:

Approving the steps
==================================================

A plan moves one step at a time, and each step waits for you.

This is the section to come back to, because it is the part that governs what actually happens in
your tenant. Nothing in a plan runs because the plan exists; it runs because someone approved that
step.

* **The first step waits; the rest unlock in order.** A step that cannot run yet says so rather
  than looking broken.
* **A step that changes something shows a write confirmation** — the same card Pér shows in
  conversation, with the values that will be sent. See
  :ref:`What a write confirmation shows you <per-approvals-card>`.
* **A step that only reads runs itself.** It changes nothing, so it needs no approval and offers no
  rejection; it goes as soon as the step before it finishes.
* **Some steps cover several changes at once.** Where changes only make sense together, they arrive
  as one step and one approval, and the confirmation lists each of them.

You can also approve the whole plan at once. When you approve and execute a whole plan, you
approve the plan — not each write inside it one at a time. Pér then re-checks at every step
whether it may still go on, stops at any step that needs a person, and records which steps it
approved on your behalf. See :ref:`Approving a whole plan at once <per-approvals-whole-plan>`.

.. important::

   Approving a plan is not the same as watching each write go by. One approval can set a sequence
   of Amperity writes running, and a write that has run cannot be undone from Pér. Read a plan's
   steps before you approve it.

.. PENDING NC-005: "you approve the plan, not every write" — PO to bless this wording. It is the
   same sentence used in what_is_per.rst, customer_decision_loop.rst and
   approvals_and_write_confirmations.rst.


.. _per-plans-waiting:

Steps that take a while
==================================================

Some steps start work in Amperity that takes minutes or hours.

Training a model, running a database, running a workflow: a plan that could not wait for those
would not be much use for real work. So a step can launch a job and the plan waits for it.

* **The plan waits, then carries on.** When the job finishes, the next step unlocks.
* **A checkpoint can hold the plan.** Where the results of a long job need reading before the next
  step runs, the step after it waits for a person and says what finished and what to review.
* **The plan moves while you are here.** A plan advances while you are signed in with Pér open, and
  picks up again on your next visit. Where a plan is running itself, only the person who started
  the run carries it on — though anyone visiting Pér lets a finished job be recognized and the next
  step proposed.
* **You find out when a job ends.** Work that finishes after you have moved on raises a
  :ref:`notification <per-notifications>`.

.. important::

   A plan is not work that continues overnight on its own. It resumes when someone returns to Pér.

.. PENDING NC-027: the wording of "the plan moves while you are here" — PO to confirm. The
   behaviour is verified; the sentence is a product-messaging call.


.. _per-plans-failure:

When a step fails
==================================================

Two different things can go wrong, and they are handled differently.

Telling them apart is what decides whether you wait, fix something in Amperity, or run the step
again. A plan never leaves you on a step that has simply stopped with no explanation.

**Amperity refused the change.** Pér reads the refusal, corrects the step and offers it again as
a confirmation for you to approve, saying what was rejected and that it has been corrected. It
tries
this at most twice; after that the step stays as it is, with the error, for a person to deal with.

**You do not have the access the step needs.** This is not corrected and retried, because there is
nothing to correct. The step keeps its message and waits for you to get the access and run it.

**A job Amperity was running failed.** The step shows Amperity's own message, a link to open
that workflow in Amperity, and a line of guidance. A predictive step also lists the usual
causes.

Where the job can safely be run again, the step offers to retry it.

.. note::

   Retrying is not offered for every failure. It covers a step whose launched job failed or was
   abandoned, and only when that job can be identified. A step that made several changes at once is
   not retried automatically, because re-running it would repeat the changes that already
   succeeded — fix the cause in Amperity and run the plan on from a fresh step instead.


.. _per-plans-changing:

Changing or abandoning a plan
==================================================

A plan is not fixed once it is written.

Before you start approving steps, you can have Pér change what a step will do, or put the whole
plan aside. Both have limits, and the second one has a name that invites exactly the wrong
expectation.

**Changing a step.** Ask Pér in :ref:`conversation <per-chatting>` to change a step that has not
run yet — a different audience, another name, a changed offer. A step that has already been
approved, has run, or was rejected cannot be changed, and a changed step still waits for your
approval rather than running.
A plan that is approving its own steps cannot be changed at all; stop the run first.

**Reverting a plan.** Reverting rejects every step of a plan that has not started and returns its
recommendation to the board, so that work can be proposed again. It is offered only while nothing
has progressed past the first step, and only for a plan written from a recommendation. Starting
again creates a new plan.

.. important::

   Reverting is not an undo. It abandons a plan before any of it has run. There is no way to undo
   a change that has already been made in Amperity — that is why the steps are worth reading
   before you approve them.


.. _per-plans-using:

Working with plans
==================================================

**To open a plan**

#. Open **Plans** and choose the plan.

From a conversation, open the plan from the card Pér posted there.

**To approve and run one step**

#. Read the step's confirmation.
#. Click **Execute step**. A step that only reads reads **Run step**.

**To approve and run a whole plan**

#. Read every step first.
#. Click **Approve & execute all** at the top of the plan.

The control may also read **Run all {n} steps** beside the first step.

**To stop a plan that is running itself**

#. Click **Stop automatic run**.

Work already set running in Amperity continues; nothing further is approved.

**To retry a step whose job failed**

#. Read the error on the step, and open the workflow in Amperity if you need the detail.
#. Fix the cause in Amperity.
#. Click **Retry step**.

**To change a step before it runs**

#. In conversation, tell Pér which step to change and what it should do instead.
#. Approve the changed step as you would any other.

**To revert a plan that has not started**

#. Click **Revert to recommendation**.
#. Confirm.

A step you approved and executed, a plan you reverted and a step you retried each appear in the
:ref:`Activity log <per-activity-log>`.
