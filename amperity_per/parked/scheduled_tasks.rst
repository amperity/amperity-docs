.. PENDING D3: this article ships when scheduled tasks are enabled for production tenants. At the
   pin the Tasks surface is off for every production tenant.

.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        A scheduled task is a request Pér answers on a cadence you set. Tasks are private to you, and a run can only read.

.. meta::
    :content class=swiftype name=body data-type=text:
        A scheduled task is a request Pér answers on a cadence you set. Tasks are private to you, and a run can only read.

.. meta::
    :content class=swiftype name=title data-type=string:
        Scheduled tasks


.. _per-scheduled-tasks:

==================================================
Scheduled tasks
==================================================

A scheduled task is a question you only have to ask once. You write the request, choose how often
Pér should answer it, and Pér answers it on that cadence and leaves the answer waiting for you.

Much of the work of knowing your customers is the same question asked again on Monday. A task
takes the asking off you and leaves you the reading, which is the part worth your time. It serves
the :ref:`Understand <per-customer-decision-loop-understand>` stage of the customer decision loop,
and only that stage: a run can look, and cannot change anything.

.. note::

   A *task* on this page is a scheduled task — a request of your own that repeats. It is not a
   :ref:`step of a plan <per-key-concepts-step>`, which is a single change waiting for your
   approval.


.. _per-scheduled-tasks-what:

What a task is
==================================================

A task is two things: the request you want answered, and how often you want it answered.

The request has to stand on its own. A run opens with nothing behind it, so everything the request
depends on — the period it covers, the objects it concerns, what you want produced — belongs in
the request itself rather than in something you said earlier.

* **It runs on a cadence** — hourly, daily, weekly or monthly — at a time you set, in a timezone
  you choose. You pick the cadence; you never write out a schedule.
* **It carries a short name**, which is how you recognise it later. The name is a label for the
  list, not the instruction.
* **It can be paused**, and started again. A paused task keeps everything it has.
* **Pér describes the schedule back to you in words**: when it runs, when it runs next, and when
  it last ran.
* **A run answers rather than asks.** Nobody is there to clarify, so Pér takes the most reasonable
  reading of an ambiguous request and answers that, instead of waiting for a reply that will not
  come.


.. _per-scheduled-tasks-private:

A task is yours
==================================================

A task belongs to the person who created it, and to nobody else.

A standing question says something about what you are watching, and that is yours to share or
not. What you can hand round is the result.

* **Nobody else can see, edit, run or delete your task.** To anyone else in your tenant, your task
  reads exactly as a task that does not exist.
* **A run acts as you.** What it can reach is what you can reach.
* **Results land in a conversation belonging to the task**, not in the chat where you set it up.
* **What a task produces can still be shared.** The report it keeps up to date can go to everyone
  in your tenant while the task itself stays private.


.. _per-scheduled-tasks-read-only:

What a run may do
==================================================

A run reads. It does not change anything in Amperity.

This is the approval boundary holding at the one moment nobody is there to approve. Pér does not
change anything in Amperity on its own, and a scheduled run is no exception — which is what makes
a task something you can set and then leave alone.

* **Only reading is offered.** Anything that would change Amperity is withheld from the run
  rather than offered and refused later.
* **Every read is checked against your own Amperity access**, object by object, and not only
  against the tenant's. A run cannot reach something you could not reach yourself.
* **A run cannot edit your company context, save a memory, author or run a plan, send feedback,
  or create another task.**
* **A run signs in as the tenant, not as you.** Scheduled work happens with nobody signed in, so
  it uses one read-only Amperity token the tenant holds. That token can read; it cannot create,
  change, activate, send or delete. See :ref:`Setting up scheduled tasks
  <per-scheduled-tasks-setup>`.

.. important::

   Because each read is checked against your own access, a task stops being able to reach anything
   you lose access to in Amperity. The run says which permission was missing rather than quietly
   returning less.

See :ref:`How Pér uses your data <per-how-per-uses-your-data>` for what Pér reads in an ordinary
session, and :ref:`Approvals and write confirmations <per-approvals-boundary>` for where the
boundary sits everywhere else.


.. _per-scheduled-tasks-results:

Where results go
==================================================

Each run writes its answer into the task's own conversation, and tells you it is there.

A result that arrives while you are doing something else has to be findable afterwards. And a
report you get every week is more useful as one document that keeps changing than as fifty
documents you have to compare.

* **The answer is posted into the task's conversation**, which Pér creates for the task and names
  after it. You open it from the task.
* **New results raise a marker beside Tasks**, and the task list gathers them together until you
  open them.
* **Pér emails you when a run settles**, where it has an address for you. The email says whether
  the run finished, finished with gaps, or failed, and links back into Pér. It carries neither the
  answer nor the error — both stay in Pér.
* **Pér says what it made of its own run.** A run that succeeded but could not do everything the
  task asked is reported as having finished with gaps; one that could not do it at all is reported
  as failed, even though it produced an answer.
* **A task keeps one artifact up to date.** Rather than producing a new report each time, a run
  updates the :ref:`artifact <per-artifacts>` the last successful run produced.
* **Deleting a task deletes its run history and its conversation**, and cannot be undone.

.. PENDING NC-047: the email channel is best-effort — a notification that cannot be sent is
   dropped, and the address comes from the owner's own session rather than from Amperity, so a
   person whose session carries no address gets none. PO to confirm it is documented as a feature.

.. note::

   A finished run is not a :ref:`notification <per-notifications>`. Notifications tell you that
   work you approved has finished. A task's results reach you through the task list and by email.


.. _per-scheduled-tasks-timing:

When runs happen, and when they don't
==================================================

The cadence decides when a task runs. Three things change that, and all three are worth knowing
before you build a routine on one.

* **You can run a task yourself at any time**, including while it is paused. A run you start by
  hand does not move the schedule.
* **Missed runs are not made up.** If Pér was unavailable while a task came due more than once, it
  runs once when Pér is available again, not once for each occurrence it missed. A task you start
  again after pausing waits for its next occurrence rather than running the one it missed.
* **A schedule Pér cannot read pauses the task** rather than failing over and over. The task shows
  that its schedule needs attention, and editing the task sets a new one.


.. _per-scheduled-tasks-using:

Using scheduled tasks
==================================================

**To create a task**

#. Open **Tasks**.
#. Click **New task**.
#. Give it a **Name** — a few words naming what it does.
#. Under **What should Pér do?**, write the request in full, as though nothing had been said
   before it.
#. Choose how often it should run, and the **Timezone** those times are in.
#. Choose whether Pér should email you after each run.
#. Click **Create task**.

**To create a task from a conversation**

#. Ask Pér to do something on a repeating basis — every Monday, each morning, monthly.
#. Read the card Pér shows you, then click **View task** to open it.

The task is created as you ask for it, with no confirmation, because creating one changes nothing
in Amperity. What it does when it runs is still bounded by :ref:`what a run may do
<per-scheduled-tasks-read-only>`.

**To pause a task, or start it again**

#. Open the task.
#. Click **Pause**, or **Enable**.

**To run a task now**

#. Open the task.
#. Click **Run now**.

**To share what a task produced**

#. Open the task.
#. Under **Artifacts**, find the one you want to share.
#. Click **Share with team**.

Sharing an artifact does not share the task. See :ref:`Artifacts <per-artifacts-sharing>`.

**To delete a task**

#. Open the task.
#. Click **Delete**, then confirm.

The task, its run history and its conversation are all removed, and cannot be brought back.


.. _per-scheduled-tasks-setup:

Setting up scheduled tasks
==================================================

Before anyone in a tenant can schedule a task, the tenant needs one read-only Amperity token.

Scheduled work runs with nobody signed in, so it cannot borrow a person's sign-in the way the rest
of Pér does. It needs an identity belonging to the tenant — which is exactly why that identity can
only read, and why creating it takes an administrator.

* **It takes the Administrator policy in Amperity.** Someone who holds it generates the token from
  Pér's own settings. Pér creates the Amperity key and gives it the access it needs; there is
  nothing to choose.
* **Amperity staff cannot do this for you.** Setting up scheduled tasks on a customer's tenant has
  to be done by an administrator at that customer, from their own Amperity account.
* **The token is stored encrypted and never shown**, so there is nothing to copy or keep.
* **It expires after 90 days.** Renewing it is the same action that created it.

.. PENDING NC-046: the product states the token's access to PII two ways — the setup page says it
   cannot view PII, while the access Amperity gives it says it can. Reported to the PO; until that
   is settled this article says only that the token can read and cannot change anything.

.. PENDING NC-049: the access Pér attaches to the key has a name in Amperity, but Amperity never
   offers it in the policy list, so naming it here would send an administrator looking for
   something they cannot find. PO to confirm the wording.

**To set up scheduled tasks for your tenant**

#. Open **Settings**.
#. Choose **Automations**.
#. Click **Generate token**.

Pér reports what it did and when the token expires. To renew it later, return to the same page and
click **Rotate token**.

See :ref:`Managing access to Pér <per-managing-access>` for who holds which policy in Amperity.
