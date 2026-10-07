.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        A memory is a standing note Pér carries between sessions, so you only have to say something once.

.. meta::
    :content class=swiftype name=body data-type=text:
        A memory is a standing note Pér carries between sessions, so you only have to say something once.

.. meta::
    :content class=swiftype name=title data-type=string:
        Memory


.. _per-memory:

==================================================
Memory
==================================================

A memory is a standing note Pér carries between sessions: a preference you would rather not repeat,
a rule you want held to, a fact about your business that keeps coming up, or a correction you do not
want to make twice.

It is also where the strongest standing instruction you can give Pér lives: a must-follow memory.
This is one of the three things, along with your :ref:`company context <per-company-context>` and
the approval boundary, that make up the rules Pér works inside. This is the :ref:`Learn
<per-customer-decision-loop-learn>` stage of the customer decision loop, and it is the part of it
you control directly.

.. PENDING NC-003: the "rules Pér works inside" clause rests on company context, must-follow
   memories and the approval boundary. PO to confirm. Same clause as what_is_per.rst,
   key_concepts.rst and company_context.rst.


.. _per-memory-what-it-is:

What a memory is
==================================================

A memory is a short note with two choices attached: who it applies to, and how hard it binds.

Everything else about a memory — where it came from, how often it has been used, what kind of thing
it is — Pér works out and shows you.

* **Scope** says who it applies to. **Personal — only you** keeps it to your own conversations.
  **Tenant — shared with everyone here** puts it in front of everyone in your tenant, and Pér may
  act on it in their work as well as yours.
* **Enforcement** says how hard it binds. A **Guideline** shapes what Pér does without tying its
  hands. **Must follow** is read first and treated as a rule Pér must not break.

A memory can be written by hand or saved out of a conversation, and the list tells you which it was.
Memories do not expire — one you wrote a year ago is still in force until you archive it.


.. _per-memory-how-many:

How many Pér can hold
==================================================

Memories share a limited space in what Pér reads, so a focused set works better than a large one.

Pér reads them in priority order: must-follow memories first, then rules and corrections, then
preferences and facts. When there are more memories than that space allows, the lower-priority ones
are left out — which means an old preference you no longer care about can crowd out a newer one you
do.

.. important::

   Archive what you no longer need. Keeping the set small is what keeps the memories you rely on in
   play.

.. PENDING NC-030: the limited space is a token cap on the pinned band, and overflow is dropped.
   The article states the behaviour without naming a figure. PO to confirm the wording.


.. _per-memory-what-per-does:

What Pér does with memories
==================================================

Pér tells you when it uses a memory, and keeps a count of how often each one has mattered.

If Pér does something you did not expect, you want to know whether a memory caused it; if a memory
you wrote is doing nothing, you want to know that too.

* **Pér says when it applies one**, naming the memory, in the conversation where it applied.
* **The list records how often each memory has been cited**, and when it last changed. A memory
  that has never been cited is a memory to look at again.
* **Pér works out what kind of thing a memory is** — a rule, a correction, a preference, a fact —
  from how you wrote it. There is no kind to set, and the kind is what decides priority within an
  enforcement level. Writing a rule as a rule rather than as a mild preference is what makes it
  read like one.

.. note::

   The level you choose, **Guideline** or **Must follow**, is the control you hold over this. If a
   memory has to hold, make it **Must follow** rather than relying on how it is worded.


.. _per-memory-approving:

Approving a memory Pér proposes
==================================================

Pér can offer to save a memory, and you decide whether it does.

* **By default Pér asks every time.** A proposed memory arrives as a
  :ref:`write confirmation <per-approvals-card>` showing the title, the scope, the enforcement
  level, the body, and the kind Pér chose with its reason for choosing it. Nothing is saved until
  you approve it.
* **You can let your personal memories save without asking.** That is the other setting, and it
  covers memories about you alone. Where Pér had to ask you something in order to answer — how to
  read the numbers in your data, say — it asks again before remembering your answer, even with this
  setting on.
* **A memory shared with your tenant always asks**, under either setting, because everyone in your
  tenant can read it and Pér may act on it in their work.
* **Saving automatically is the same save.** It answers the same confirmation rather than taking
  another route, so the checks for a duplicate title, the redaction, and the record of the change
  are identical. Only who approves it differs.

See :ref:`Where the boundary sits <per-approvals-boundary>` for how this fits the rest of what Pér
asks you to approve.


.. _per-memory-limits:

What Pér won't keep
==================================================

Three things a memory will not do:

* **Recognized contact details and credentials are stripped before a memory is saved.** Email
  addresses, phone numbers, card numbers and some key and token formats are removed, whether Pér
  proposed the memory or you typed it. The check matches known patterns rather than catching
  everything, so treat it as a backstop: a memory is a note about how to work, not a place to keep a
  customer record or a password.
* **Two memories in the same scope cannot share a title.** A clash is reported so you can decide
  which one you meant, rather than quietly merged into one.
* **You can turn memory off for yourself.** Pér stops saving new memories and stops using the ones
  you have. Nothing is deleted — your memories stay where they are, and turning it back on brings
  them back into play. With memory off there is nothing left to approve, so the setting for saving
  memories automatically is switched off too.


.. _per-memory-reviewing:

Reviewing what you have
==================================================

A memory set accumulates, and some of it goes stale. Reviewing it is part of using it.

Nothing expires on its own, so this is maintenance somebody has to do.

* **Archiving is not deleting.** An archived memory moves to its own tab and stops being used. You
  can restore it later.
* **Changes are recorded in the** :ref:`Activity log <per-activity-log>`. A personal memory's
  entry deliberately leaves its title out, so maintaining your own memories does not publish them.
* **The** :ref:`Review memories <per-skills>` **skill reads the memories available to a
  conversation and looks for duplicates and contradictions.** It proposes changes; it does not make
  them. It also tells you when the set it looked at may not have been complete.


.. _per-memory-using:

Working with memories
==================================================

Memory settings are your own, and need no particular permission.

**To write a memory**

#. Open **Settings** and choose **Memory**.
#. Click **Add memory**.
#. Give it a **Title** and a **Body**, and choose its **Scope** and **Enforcement**.
#. Click **Create**.

Write the body so it says what to do and why, not just what you prefer. A memory that explains
itself is one you can judge later.

**To change how Pér saves memories it proposes**

#. Open **Settings** and choose **Memory**.
#. Under **When Pér proposes a memory**, choose **Ask me before saving each one** or **Save
   personal memories automatically**.

A memory shared with your tenant asks either way.

**To archive a memory**

#. Open **Settings** and choose **Memory**.
#. Find the memory and click **Archive**.

**To restore an archived memory**

#. Open **Settings** and choose **Memory**.
#. Open the **Recently archived** tab.
#. Find the memory and click **Restore**.

**To turn memory off**

#. Open **Settings** and choose **Memory**.
#. Turn off **Save and use memories automatically**.

Your existing memories stay where they are.

A memory cannot be saved from Slack or Microsoft Teams. Both surfaces answer only and cannot show a
confirmation, so a memory is saved from the Pér web app instead.
