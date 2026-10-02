.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Conversation is how you work with Pér: ask in plain language, follow what it does, and turn the answer into work.

.. meta::
    :content class=swiftype name=body data-type=text:
        Conversation is how you work with Pér: ask in plain language, follow what it does, and turn the answer into work.

.. meta::
    :content class=swiftype name=title data-type=string:
        Chatting with Pér


.. _per-chatting:

==================================================
Chatting with Pér
==================================================

Conversation is how you work with Pér. You ask a question in plain language, Pér reads your
tenant's data to answer it, and it shows you what it is doing as it goes. When the answer implies
work in Amperity, the conversation is also where that work starts.

This is the one place where asking and acting are the same motion. A question does not have to be
restated as a query, then a ticket, then a round of configuration — it stays one thread, and what
comes out of it is a plan you can read. Most of this article is the
:ref:`Understand <per-customer-decision-loop-understand>` stage of the customer decision loop; the
last part of it is the second way into :ref:`Approve <per-customer-decision-loop-approve>`.


.. _per-chatting-what-it-is:

What a conversation is
==================================================

A conversation is a thread of questions and answers against your own customer data, and it keeps.

That is what separates it from a search box. The chat where you worked out why repeat purchase fell
in March is still there in June, with everything it established and everything Pér looked at. You
can pick it up rather than start again.

* **Your chats are yours.** Your list shows the conversations you started. A colleague does not see
  them unless you share one.
* **A chat is named by your first message** until you rename it. Pér does not title your chats
  for you.
* **One answer at a time.** If you send something while a response is still running, Pér says so
  rather than starting a second one.

For what Pér reads to answer you, and under whose access, see
:ref:`How Pér uses your data <per-how-per-uses-your-data>`.


.. _per-chatting-asking:

Asking, and following along
==================================================

Between sending a question and getting an answer, Pér shows its working.

A question worth asking often takes Pér several steps to answer, and a wait you cannot see into is
a wait you cannot judge. So Pér narrates as it goes — and because the work happens on Amperity's
servers rather than in your browser, you do not have to sit and watch it.

How a response behaves:

* **Pér says what it is about to do, before it does it.** Each round of work opens with one plain
  sentence naming the step and why it matters — "First I'll pull customers who purchased in the
  last 12 months" — in business terms rather than tables and columns. Alongside it you see what
  Pér is working on at that moment.
* **The work happens on the server.** You can move to another page, close the chat panel, or reload
  the browser; the answer is still produced and saved. Coming back shows you what you missed and
  then follows along live.
* **Answers are short on purpose.** Pér gives the shortest answer that addresses what you asked,
  and expects you to ask for more. An answer that runs long opens with a one-line version of the
  conclusion so you can decide whether to read the rest.
* **Pér keeps going without asking permission to look things up.** It chains the reads an answer
  needs — resolving an identifier, fetching a related object, pulling a detail — and comes back
  once with the whole picture. It stops to ask only when the choice is genuinely yours: which of
  several things you meant, an ambiguous target, or a change you did not ask for.
* **Sometimes it asks as a choice.** Where a question has a few clear answers, Pér offers them to
  pick from. You can skip the choice and reply in your own words instead.
* **Objects are linked.** Where Pér names something in your tenant, it links to it, so you can open
  it in Amperity.

.. note::

   Pér does not name the tools it calls, and it does not describe how Amperity stores or processes
   your data — those change, and neither is something you can act on. It reports what it found and
   what it did. Your own sources, destinations and bridges are named normally, because they are
   yours.

Two things Pér will not do: it will not hand you a query to run yourself, and it will not work
around a permission you do not have. A read your Amperity access does not allow is reported
immediately, naming the permission that is missing, rather than retried or estimated.


.. _per-chatting-stopping:

Stopping a response
==================================================

You can stop a response that is going the wrong way.

It is worth knowing exactly what stopping does, because a conversation and a plan are different
things and stopping one is not stopping the other.

* **Stopping is recorded on the chat, not on your browser tab.** It takes effect even if you
  started the response somewhere else, or reloaded since.
* **What Pér had already written is kept**, marked as stopped, so the thread still reads in order.
* **A response that runs very long stops itself** and tells you to try again.

.. important::

   Stopping a response does not stop a plan. A plan that is running its own steps is stopped from
   the plan itself — see :ref:`Approving or rejecting a change <per-approvals-using>`.


.. _per-chatting-plans:

Asking Pér to build a plan
==================================================

Ask for something that takes several changes in Amperity, and Pér writes a plan rather than making
the changes one at a time.

This is the point where a conversation becomes work, and it is the second way a plan gets
written — the other is acting on a recommendation. Both produce the same thing, so what you know
about one applies to the other.

A card appears in the conversation with the plan's title and how many steps there are to review.
Open it, read the steps, and approve them there.

.. important::

   Writing a plan changes nothing in Amperity. Nothing in it runs until a person approves it.

For what a plan contains and how its steps are approved, see :ref:`Plans <per-plans>` and
:ref:`How a plan gets written <per-plans-authoring>`.


.. _per-chatting-attachments:

Attaching a file
==================================================

You can bring a document into the conversation and have Pér work from it.

Most real questions arrive with something attached — a brief, an export, a spreadsheet someone
sent you. Pér reads the text out of it and uses it the way your message asks.

What you can attach:

* **Plain text files**, read directly.
* **Documents** — ``.pdf``, ``.docx``, ``.pptx``, ``.xlsx`` and ``.xlsm`` — read on the server and
  turned into text.
* **Older Word and PowerPoint formats** (``.doc``, ``.ppt``) cannot be read. Pér says so and tells
  you which format to save as.

The limits, and what happens at them:

* **One file at a time.** Remove the attached file to attach another.
* **10 MB for a document, 1 MB for a spreadsheet or a text file**, and a ceiling on how much text
  a file can carry however small the file is.
* **A file over a limit is refused by name, before you send.** Nothing is quietly truncated, and
  the message you typed is not lost.

.. important::

   An attached file stays available to later questions in the same chat — but not forever. In a
   long enough conversation the oldest attachments are dropped, and Pér says which ones by name so
   you know it is no longer reading them. Attach the file again, or start a new chat.

Every file you attach is also kept, so you can open it again later without digging through the
thread.

.. note::

   A file is material for Pér to work from, not a set of orders. If it contains instructions
   addressed to Pér, they are not carried out. See
   :ref:`Files you attach <per-how-per-uses-your-data-files>`.


.. _per-chatting-effort:

Choosing how much thinking Pér does
==================================================

You can trade depth against speed.

A one-line lookup and a four-table analysis should not cost the same wait, and only you know which
one you are asking for.

There are three levels:

* **Low effort** — quick, lighter responses.
* **Medium effort** — balanced depth and speed. This is the default.
* **High effort** — deeper, more thorough thinking.

.. note::

   Your choice is remembered in the browser you made it in, not on your account. On another
   computer, Pér starts at the default again.


.. _per-chatting-skills:

Starting a skill
==================================================

A skill is a packaged piece of work you can start by name instead of describing from scratch.

The hard part of asking an agent for analysis is knowing what to ask for. Starting a skill skips
that: it carries its own method, so you get a considered piece of work rather than whatever a cold
question produces.

* **You can start one from the composer**, by name.
* **Pér can start one itself** when what you asked for clearly matches a skill, and it says which
  one it is using — it is never a silent change of mode.
* **Starting one while an answer is still running** puts it in the composer ready for your next
  message, rather than interrupting.

Which skills you have depends on your tenant.


.. _per-chatting-using:

Working in a conversation
==================================================

**To start a conversation**

#. Type your question and click **Ask Pér**.

**To stop a response**

#. Click **Stop generation**.

**To attach a file**

#. Click **+** beside the composer.
#. Choose **Attach a file** and pick the file.
#. Type your message and send it.

To attach a different file, remove the attached one first.

**To change how much thinking Pér does**

#. Click the effort control beside the composer.
#. Choose **Low effort**, **Medium effort** or **High effort**.

**To start a skill**

#. Click **+** beside the composer and choose **Skills**, or type ``/`` in an empty composer.
#. Choose the skill you want.

.. FORWARD-LINK: interface_tour.rst: link where the chat panel sits, and the Plans list, once that
   article exists.

.. FORWARD-LINK: artifacts.rst: link "Every file you attach is also kept" to that article once it
   exists.

.. FORWARD-LINK: skills.rst: link "A skill is a packaged piece of work" and "Which skills you have
   depends on your tenant" to that article once it exists.

.. FORWARD-LINK: chat_history.rst: link "Your chats are yours", renaming, and sharing a chat to
   that article once it exists.

.. PARKED-LINK: per_in_slack.rst, per_in_teams.rst: when those surfaces ship, say here that they
   are read-only — they answer questions but cannot make changes, and a change is made in the Pér
   web app instead.
