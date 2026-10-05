.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        The record of what Pér has done in your tenant: the recommendations it made, the plan steps that were carried out, and the settings changes behind them.

.. meta::
    :content class=swiftype name=body data-type=text:
        The record of what Pér has done in your tenant: the recommendations it made, the plan steps that were carried out, and the settings changes behind them.

.. meta::
    :content class=swiftype name=title data-type=string:
        Activity log


.. _per-activity-log:

==================================================
Activity log
==================================================

The Activity log is the record of what Pér has done in your tenant: the recommendations it made,
the plan steps that were approved and carried out, and the handful of settings changes that shape
how it works.

Pér acts in a production tenant, which makes "what did it do, and on whose say-so" a question
somebody eventually asks — usually somebody who was not in the conversation that started it. The
Activity log answers this. It is also one of the three things that carry forward into
the :ref:`Learn <per-customer-decision-loop-learn>` stage of the customer decision loop, alongside
:ref:`memories <per-memory>` and :ref:`artifacts <per-artifacts>`.

The log belongs to the tenant rather than to you. Everyone who can reach Pér sees the same entries.


.. _per-activity-log-what-it-records:

What it records
==================================================

The log records work that changed something or retired something, not everything Pér said.

Three kinds of thing reach it the Activity log:

**Plans and their steps**

* A :ref:`plan <per-plans>` approved and run, and each step approved and run.
* A step that was approved, and a step that was rejected.
* A plan :ref:`reverted <per-plans-changing>` before any of its steps ran.
* A fresh attempt proposed for a :ref:`step that failed <per-plans-failure>`.

**Recommendations**

* A :ref:`recommendation that was dismissed <per-recommendations-lifecycle>`.

**Settings that change how Pér works**

* An edit to your :ref:`company context <per-company-context>`, however it was made.
* A :ref:`memory <per-memory>` created, edited, archived or restored.
* A change to the :ref:`word Pér uses for your customers <per-system-settings-customer-name>`.

.. note::

   Writing an entry is best-effort everywhere except one place: if the log write fails, the work it
   describes still stands. Reverting a plan is the exception — its entry is written as part of the
   revert itself, so a plan cannot be abandoned without the log saying so.


.. _per-activity-log-reading:

Reading an entry
==================================================

Every entry answers three questions: who acted, what happened, and how it turned out.

* **Who acted.** Each entry is marked as Pér acting on its own, Pér acting on an approval somebody
  gave it, or a person acting directly. The middle mark is the one worth looking for on anything
  that changed your tenant: it means a person approved the change before it ran.
* **What happened.** A title, and a short account of the work underneath it. A long account is
  shortened to its first lines, and you can open it.
* **How it turned out.** Most entries carry an outcome — a step that succeeded, a recommendation
  that was dismissed, a plan that was reverted. Not every entry has one.

Entries are grouped by day, newest first, with today and yesterday named rather than dated and a
count beside each day.


.. _per-activity-log-limits:

What the log does not tell you
==================================================

The log is deliberately narrow, and has four specific edges worth knowing:

* **It does not always say who.** A settings change names the person who made it. Plan work and
  recommendation work does not: the entry records that a step was approved and run, not which
  person approved it.
* **A personal memory keeps its title out of it.** Maintaining your own memories does not publish
  them to everyone in the tenant. A memory shared with the tenant is named.
* **A one-off change you approved in conversation is not here.** A
  :ref:`write confirmation <per-approvals-card>` settles on its own card and in the conversation it
  happened in, and that conversation is the record of it. The Activity log covers plan steps,
  reverts, retries, dismissed recommendations and settings changes.
* **There is nothing to filter or search.** It is one list, newest first, and that is all it is.

.. important::

   Taken together, the first and third points mean the Activity log is not a complete audit trail
   of every change Pér made on your behalf, and was not built as one. For a particular change, the
   :ref:`conversation it happened in <per-chat-history>` and the plan it belonged to are the fuller
   record.

Amperity keeps its own, separate `activity logs <../reference/activity_logs.html>`__ covering
everything that happens across the platform. They are a broader record than this one, and they are
where to look for work that did not come from Pér.

.. PENDING NC-028: the Activity log does not record one-off confirmed writes, and names the person
   only on settings changes. Flagged for the PO; approvals_and_write_confirmations.rst depends on
   the same facts.


.. _per-activity-log-using:

Opening the Activity log
==================================================

**To open the Activity log**

#. Open **Settings**.
#. Choose **Activity log**.

Each entry is marked **Agent**, **Agent (approved)** or **User** — Pér acting on its own, Pér
acting on an approval you gave it, and a person acting directly.

If Pér has not done anything in your tenant yet, the page says so rather than showing an
empty list.
