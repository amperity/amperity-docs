.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Pér reads your data on its own, but every change it makes in Amperity waits for a person to approve it.

.. meta::
    :content class=swiftype name=body data-type=text:
        Pér reads your data on its own, but every change it makes in Amperity waits for a person to approve it.

.. meta::
    :content class=swiftype name=title data-type=string:
        Approvals and write confirmations


.. _per-approvals:

==================================================
Approvals and write confirmations
==================================================

Pér reads your tenant's data on its own. It does not change anything in Amperity on its own. When
Pér wants to make a change, that change becomes a write confirmation: a card stating exactly what
is about to happen, which waits for a person to approve it.

This is the approval boundary, and it is the stage of the customer decision loop called
:ref:`Approve <per-customer-decision-loop-approve>`. It lets you use Pér safely in a production
tenant and hand it a broad question: you will always be asked before Pér changes anything in
Amperity.


.. _per-approvals-boundary:

Where the boundary sits
==================================================

The boundary runs between reading and changing.

Knowing which side a request falls on tells you whether Pér will come back with an answer or come
back with something to approve. This rule holds across every part of Pér.

* **Reading is not gated.** Pér can look at anything in your tenant that you could look at
  yourself, and reading never draws a confirmation. It reads before it proposes, so that it can
  check any change against your current data.
* **Pér can ask for a change; it cannot make one.** Pér is given the ability to propose far more
  than it is able to carry out. Asking is what draws the confirmation. Nothing it proposes runs
  until you approve it, and what runs is what you approved and nothing more.
* **The boundary covers more than Amperity.** A confirmation also stands in front of an edit to
  your company context, a memory shared with everyone in your tenant, connection details you
  supply so Pér can reach a destination, and feedback you send to Amperity about Pér.
* **What Pér keeps to itself is not gated.** A report Pér writes for you changes nothing in
  Amperity, so it needs no approval. A memory about you alone follows your own setting: by default
  Pér asks before saving one, and you can choose to let your personal memories save without
  asking. A memory shared with your tenant always asks. With automatic saving on, a personal
  memory still appears in the chat as a card, already marked **Saved**.
* **Amperity holds its own gate.** On a production tenant, Amperity itself keeps changes behind an
  explicit confirmation, and your approval in Pér is what answers it. Pér cannot turn that gate
  off.

.. important::

   The boundary is a product rule, not a setting. There is no mode in which Pér changes your
   Amperity tenant without a person approving the change first.

.. PARKED-LINK: scheduled_tasks.rst: when scheduled tasks ship, say here that a run happens with
   nobody present and so can only read — the boundary holds by withholding every write, not by
   deferring one. It is the one case where Pér acts without a person in the room.

.. PARKED-LINK: use_case_feasibility.rst: when feasibility ships, note that correcting a saved
   analysis in chat is a carded write like any other.


.. _per-approvals-card:

What a write confirmation shows you
==================================================

A write confirmation is a plain statement of one change, written so you can check it.

The card is specific: it names the operation, the object, and the values to enable clear judgment
about the approval.

A confirmation carries:

* **What the change does**, in plain words — creating a segment, updating a campaign, deleting a
  journey.
* **Which object** it acts on, named.
* **The values that will be sent.** A long value is collapsed so the card stays readable, and you
  can open it. On a step of a plan the values sit behind **Details**, because a plan page carries
  many cards at once.
* **A warning, where one is warranted.** A deletion, or anything that reaches real customers, is
  marked as being more serious.
* **Every write it covers.** Some changes only make sense together, and arrive as one confirmation
  covering several writes. The card lists each of them, and approving it approves all of them.
* **Several changes of the same kind, together.** When Pér proposes several changes of the same
  kind in one turn, they arrive as one card with a row for each. You can answer any row on its own,
  or answer the rest together — so approving once here can run more than one change. A deletion
  among them is confirmed again before anything runs.

.. note::

   The same card appears in conversation and on a
   :ref:`step of a plan <per-plans-approving>`. What you are approving, and what you can see
   before approving it, is the same in both places.

.. _per-approvals-whole-plan:

Approving a whole plan at once
==================================================

A :ref:`plan <per-plans>` can be approved as a whole, rather than a step at a time.

A plan of a dozen steps does not need a dozen clicks. When you approve and run a whole plan, you
approve the plan — not each write inside it one at a time. Pér then re-checks at every step whether
it may still go on, stops at any step that needs a person, and records which steps it approved on
your behalf.

What that means in practice:

* **It holds where a person is needed.** A step that is meant to be read before the next one runs
  stops the run and waits for you, and the step's own approval control is still there beside it.
* **It stops on failure.** A step Amperity refuses ends the run rather than carrying on past it.
* **You can stop it.** Work already set running in Amperity cannot be recalled, but nothing further
  is approved, and the run stops at the next step rather than instantly.

.. important::

   Approving a plan is not the same as watching each write go by. One approval can set a sequence
   of Amperity writes running, and a write that has run cannot be undone from Pér. Read a plan's
   steps before you approve it.


.. _per-approvals-limits:

What Pér can't do, whatever you approve
==================================================

Some things stay out of reach however the conversation goes.

These are the parts that hold regardless of settings, instructions, or persuasion:

* **Pér cannot approve on your behalf.** Approving a step and restarting a run are things only a
  person does. If Pér is asked to approve a step itself, the attempt is refused and recorded.
* **Only the person who asked can answer a confirmation card.** A card belongs to the request that
  produced it, in the conversation that produced it. Someone else in your tenant cannot approve or
  reject it, and cannot tell that it exists. A plan is different: a plan is visible to your tenant,
  and another person there can approve a step in it, under their own access.
* **A confirmation does not outlive its conversation.** Delete the conversation and its unapproved
  changes can no longer be run, even from a tab still showing them.
* **Approving twice does not run the change twice.**
* **Permission is checked again at the moment you approve**, not only when the card was drawn. A
  change that was permitted when Pér proposed it, and is not permitted now, is refused.

Some operations are refused before any other rule is considered. Whatever else is permitted,
Pér cannot:

* Read a stored credential
* Read a file off the server it runs on
* Create or delete people
* Grant or revoke access
* Create or delete a sandbox or push configuration to a parent tenant
* Set up a new destination for your data to be sent to
* Roll your tenant's configuration back to an earlier version
* Move itself to another tenant
* Relax the confirmation gate itself

No setting and no instruction re-enables these.

.. note::

   A refusal for lack of permission is about your own Amperity access, not about Pér. Pér names
   the permission that is missing and says that you or an administrator needs to grant it, rather
   than working around it.


.. _per-approvals-record:

What's recorded
==================================================

Every confirmation leaves a trace that says which way it went.

"Who approved what, and when" is the first question asked after anything surprising, and it should
not depend on anyone remembering.

* **The confirmation itself settles.** It stays in the conversation showing whether the change ran,
  was rejected, or failed — and, when it failed, Amperity's own message. A change can also finish
  with a warning: it ran, but something it was meant to set up alongside it did not, and the card
  says what to check.
* **A rejection is recorded as a rejection.** Pér is told the change was not made and must not
  treat it as done.
* **The outcome is written into the conversation**, so the next thing you ask, and the same
  conversation reopened later, read the same history.
* **Plan steps reach the** :ref:`Activity log <per-activity-log>`. A step that was approved and
  run, a plan that was reverted, and a step that was retried each appear there.

.. _per-approvals-using:

Approving or rejecting a change
==================================================

**To approve a change Pér proposes in a** :ref:`conversation <per-chatting>`

#. Read the confirmation: what the change does, the object it names, and the values listed on it.
#. Open any collapsed value you want to check.
#. Click **Run**. Some changes name what they do instead, such as **Create segment**.

The confirmation settles to **Done** when the change has run, and links to the object in Amperity
where there is one to open. A change that finished with a warning reads **Done with warning** and
says what to check.

**To reject a change Pér proposes**

#. Click **Reject**.

Nothing runs, the confirmation settles to **Rejected**, and Pér is told the change was not made.

**To answer a card covering several changes of the same kind**

#. Read each row.
#. Answer a row on its own, or choose **Approve all** or **Reject all**.

Once some rows have been answered, those controls read **Approve remaining** and **Reject
remaining**. A deletion among them asks you to confirm before anything runs.

**To approve one step of a plan**

#. Open the plan and read the step's confirmation.
#. Click **Run step**.

A step that only reads usually runs itself and shows no confirmation — see
:ref:`Approving the steps <per-plans-approving>`. Where one does wait for you, it changes nothing,
so it offers no rejection.

**To approve and run a whole plan**

#. Open the plan and read every step.
#. Click **Approve & run all** at the top of the plan.

**To stop a plan that is running itself**

#. Open the plan.
#. Click **Stop automatic run**.

Work already set running in Amperity continues; nothing further is approved.

A confirmation cannot be answered from Slack or Microsoft Teams. Both surfaces answer only, so a
change is made in the Pér web app instead.
