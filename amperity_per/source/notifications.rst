.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Work you approve often finishes after you have moved on. A notification is how you find out.

.. meta::
    :content class=swiftype name=body data-type=text:
        Work you approve often finishes after you have moved on. A notification is how you find out.

.. meta::
    :content class=swiftype name=title data-type=string:
        Notifications


.. _per-notifications:

==================================================
Notifications
==================================================

Some of what you approve in Pér takes minutes or hours to run in Amperity — training a model,
running a database, running a workflow. It usually finishes long after you have moved on to
something else. A notification is how you find out.

It closes the gap between approving something and knowing whether it worked, without you having to
go back and check. It is also the honest boundary of what Pér keeps an eye on: it tells you when
work you started reaches an end, and nothing more than that. This is the
:ref:`Act <per-customer-decision-loop-act>` stage of the customer decision loop, after you have
stopped watching.


.. _per-notifications-what-raises-one:

What raises one
==================================================

A notification comes from a long-running job in Amperity that a plan step started, reaching an end.

Knowing the trigger is what keeps the feed readable. It is a short list of specific events, not a
stream of everything Pér does.

There are three outcomes:

* **The job finished.** Open the notification to read the results.
* **The job failed.** The notification carries Amperity's own explanation of what went wrong.
* **Pér stopped tracking it.** The job ran too long to keep waiting on.

Each one opens the plan it belongs to, so you land on the step rather than on a list.

* **A failure message is Amperity's, trimmed.** Technical detail beneath the explanation is
  stripped and the text is capped, so one failure cannot crowd out everything else in the feed.
  The step itself carries the full detail and a link into the Amperity workflow — see
  :ref:`When a step fails <per-plans-failure>`.
* **A failed job also stops a plan that was running its own steps.** Nothing further is approved.

.. important::

   Most of what happens in Pér raises no notification. An answer in conversation, a report Pér
   wrote, a fresh set of recommendations, a change you approved on a card — none of these notify
   anyone. Notifications are for work left running in Amperity.


.. _per-notifications-who-sees-what:

Who sees what
==================================================

The feed is your tenant's; whether an entry has been read is yours alone.

That combination explains both of the things people find odd about it — an entry about work you did
not start, and a badge that stays after a colleague says they cleared theirs.

* **Everyone in the tenant sees the same entries.** Work a colleague approved appears in your feed
  too, because it is work in your tenant.
* **Read state is per person.** A colleague opening the feed cannot clear your badge, and you
  cannot clear theirs. That is deliberate: the person who approved the work is the one who needs
  to know it finished.
* **Opening the feed marks what it showed you as read** — only what it showed you. Older entries
  below the most recent are never silently cleared.
* **The count keeps up on its own.** You do not have to reload to see that something arrived.


.. _per-notifications-limits:

What this isn't
==================================================

Nothing is watching your tenant on your behalf.

"Notifications" invites the assumption that something is monitoring, and it is worth being plain
that nothing is.

An entry appears because a job you approved was checked on while someone was in Pér — not because
a scheduler is running in the background. Pér does not watch your tenant between sessions, and
it does not raise an alert about something it noticed on its own. See
:ref:`Where the loop stops <per-customer-decision-loop-limits>` and
:ref:`Steps that take a while <per-plans-waiting>`.

For the record of what Pér actually did — the steps it carried out and the recommendations it
made — the Activity log is the place to look, not the feed.


.. _per-notifications-using:

Working with notifications
==================================================

**To see what has finished**

#. Click **Notifications**.

Entries you have not read are marked. Opening the list marks them read for you.

**To open the work a notification is about**

#. Click the notification.

The plan it belongs to opens at the step it concerns.

.. FORWARD-LINK: activity_log.rst: link "the Activity log" once that article exists.

.. FORWARD-LINK: interface_tour.rst: link where the notifications control sits once that article
   exists.
