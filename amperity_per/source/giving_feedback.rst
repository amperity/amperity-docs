.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Two ways to tell Amperity what Pér got right or wrong, and what travels with what you send.

.. meta::
    :content class=swiftype name=body data-type=text:
        Two ways to tell Amperity what Pér got right or wrong, and what travels with what you send.

.. meta::
    :content class=swiftype name=title data-type=string:
        Giving feedback


.. _per-giving-feedback:

==================================================
Giving feedback
==================================================

There are two ways to tell Amperity what Pér got right or wrong. You can write the note yourself
with the **Feedback** control, or you can tell Pér in a conversation and have it send the note for
you.

Pér is in :ref:`Public Preview <per-public-preview>`, and what gets reported is what gets fixed.
The answer that was subtly wrong, the step that needed a workaround, the thing you went looking for
and could not find — none of that reaches the people building Pér unless somebody sends it.
Feedback also leaves your tenant, so it is worth knowing what travels with it before you write.


.. _per-giving-feedback-two-ways:

The two ways to send it
==================================================

One route is you writing a note. The other is Pér writing it for you.

That difference is the whole reason only one of them stops to ask. When you write the note, you
have already read it — there is nothing left to check. When Pér writes it, you have not, so Pér
shows you what it is about to send first.

* **The Feedback control sends what you wrote, directly.** You write it, you send it, and it goes.
* **Telling Pér draws a confirmation first.** Ask Pér to pass something on and it writes the note
  and shows it to you as a
  :ref:`write confirmation <per-approvals-card>`. Nothing is sent until you approve it, and Pér
  does not tell you it has been sent before you do.
* **Pér passes your words on as you said them.** It is instructed to carry your feedback through
  rather than rewrite it or soften it, so what the team reads is what you meant.
* **The same point is not filed twice in one conversation.** Ask again in the same chat and Pér
  tells you it has already been sent rather than sending a duplicate.
* **Feedback runs to 5,000 characters.**

.. note::

   Feedback is one of the things the approval boundary covers, along with changes to Amperity,
   your company context and a memory shared with your tenant. See
   :ref:`Where the boundary sits <per-approvals-boundary>`.


.. _per-giving-feedback-what-travels:

What travels with it
==================================================

Feedback does not arrive anonymously, and it does not arrive without context.

That is deliberate — a report nobody can follow up on is a report that goes nowhere. But it means
the note leaves your tenant with more attached than the words you typed, and you should be able to
take that into account when you decide what to put in it.

What goes with every piece of feedback:

* **Who sent it.** Your name and your email address, so the team can come back to you.
* **Where you sent it from.** The tenant you were working in. Feedback sent from the **Feedback**
  control also records the page you were on; feedback sent through a conversation records which
  conversation it came from.
* **A recording of your session in Pér may be attached**, so the team can see what happened rather
  than reconstruct it from a description.

.. PENDING NC-033: whether the docs disclose the session recording is the PO's call. RULED (Sam,
   2026-10-02): say it, and never name the vendor. This is the one sentence to strike if the
   answer changes.

It goes to the Pér team at Amperity, and it is read there.


.. _per-giving-feedback-using:

Sending feedback
==================================================

**To send feedback from anywhere in Pér**

#. Click **Feedback**.
#. Write what you want to say under **Your feedback**.
#. Click **Send feedback**.

**To send feedback from a conversation**

#. Tell Pér what you want passed on to the team.
#. Read the confirmation, which shows the note Pér has written.
#. Click **Execute**.

If the note is not what you meant, reject it and tell Pér what to say instead.

.. PARKED-LINK: per_in_slack.rst, per_in_teams.rst: when those surfaces ship, say here that
   feedback cannot be sent from them, because they cannot show a confirmation — it is sent from
   the Pér web app instead.
