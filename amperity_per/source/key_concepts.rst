.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Definitions of the terms used throughout the Pér documentation.

.. meta::
    :content class=swiftype name=body data-type=text:
        Definitions of the terms used throughout the Pér documentation.

.. meta::
    :content class=swiftype name=title data-type=string:
        Key concepts


.. _per-key-concepts:

==================================================
Key concepts
==================================================

These are the terms this documentation uses, and what each one means in Pér.

Several of them are everyday English words with a specific meaning in Pér. For example, A *plan* is
a particular object with a particular lifecycle, not just an intention. A *memory* is something you
asked Pér to keep, not everything it has seen.


.. _per-key-concepts-activity-log:

**Activity log**
   The record of what Pér did in your tenant: the actions it took and the recommendations it
   made. Amperity keeps its own, separate
   `activity logs <../reference/activity_logs.html>`__ covering everything that happens across
   the platform.


.. _per-key-concepts-ai-agent-for-customer-data:

**AI agent for customer data**
   The kind of product Pér is: an agent that works on your customer data, answering questions
   about it and — with your approval — acting on it in Amperity.


.. _per-key-concepts-allow-per-access:

**Allow Pér access**
   The grant that lets one person into Pér when a tenant uses managed access. Given and removed
   in Amperity, on the `Users <../reference/users.html>`__ page.


.. _per-key-concepts-apply-mode:

**apply mode**
   How a memory that Pér proposes gets saved. By default Pér asks every time. You can choose to
   let your personal memories save without asking; a memory shared with your tenant always asks,
   under either setting.


.. _per-key-concepts-auto-run:

**Approve & run all**
   Approving a whole plan at once and letting it run itself. You approve the plan, not each write
   inside it: Pér re-checks at every step whether it may still go on, stops at any step that needs
   a person, and records which steps it approved on your behalf.


.. _per-key-concepts-artifact:

**artifact**
   Something a session leaves behind: a report Pér wrote, or a file you gave it. You can come back
   to an artifact later, export it to PDF, and share it so that everyone in your tenant can open
   it.


.. _per-key-concepts-block-user:

**Block user**
   The Amperity control that revokes all of a person's access to a tenant, overriding any
   permission they hold directly or inherit. Pér has no revocation of its own — blocking happens
   in Amperity.

   .. PENDING NC-006: blocking a user is documented nowhere in amperity-docs, so this entry has
      no link target. Sam's call; three options in collection-plan.md §3.1.


.. _per-key-concepts-company-context:

**company context**
   The business priorities, definitions and measures you want Pér to work from. Company context
   goes into every session. Alongside it, Pér reads the
   `context documents <../reference/ampai.html#ampai-company-context>`__ and the AmpAI system
   prompt your tenant has set up in Amperity; it reads those, and does not replace them.


.. _per-key-concepts-customer-decision-loop:

**customer decision loop**
   The cycle Pér is built around: :ref:`Understand → Recommend → Approve → Act → Learn
   <per-customer-decision-loop>`.


.. _per-key-concepts-guideline:

**Guideline**
   One of the two enforcement levels of a memory. A guideline shapes what Pér does without binding
   it.


.. _per-key-concepts-managed-access:

**Managed access**
   One of the two ways a tenant admits people to Pér: only people granted access individually can
   enter. Set in Amperity, on the `Users <../reference/users.html>`__ page, by a User
   Administrator.


.. _per-key-concepts-mcp-tools:

**MCP tools**
   The Amperity tools Pér calls to read your data and to change things on your behalf. Pér reads
   before it writes, every change becomes something you approve, and some tools are withheld from
   Pér entirely.


.. _per-key-concepts-memory:

**memory**
   Something you have told Pér to remember between sessions — a preference, a rule, a fact or a
   correction. Each memory is either personal to you or shared with everyone in your tenant, and
   is either a **Guideline** or **Must follow**. Memories can be saved from a conversation or
   written by hand, and can be archived and restored. They do not expire.


.. _per-key-concepts-must-follow:

**Must follow**
   One of the two enforcement levels of a memory. Pér reads must-follow memories first and treats
   them as rules it must not break.


.. PARKED-LINK: notifications.rst: restore the **notification** glossary entry and its
   _per-key-concepts-notification anchor.


.. _per-key-concepts-open-access:

**Open access**
   One of the two ways a tenant admits people to Pér: anyone authorized for the tenant can enter.
   Either way a tenant is set up, each person's existing Amperity permissions still govern what
   they are able to do once inside.


.. _per-key-concepts-per:

**Pér**
   Amperity's AI agent for customer data, and the name used throughout this documentation.


.. _per-key-concepts-plan:

**plan**
   A titled, reviewable list of Amperity writes that you approve before any of them runs. A plan
   has steps, flags anything it considers risky, and collects what it produces. Plans are authored
   two ways: by acting on a recommendation, or by asking for one in conversation. A step that
   fails shows what went wrong and can be run again.

   Reverting a plan abandons one that has not started yet, which frees its recommendation to be
   acted on again. It is not a way to undo work that has already run.


.. _per-key-concepts-portfolio:

**Portfolio**
   Where Pér gathers the work it thinks is worth your attention: the recommendations it has made,
   and the plans already under way.


.. _per-key-concepts-recommendation:

**recommendation**
   Something Pér proposes doing, with the argument attached: the claims it rests on, the numbers
   behind them, where in your data they came from, a confidence grade and the reasoning for that
   grade, and what Pér could not establish. Acting on a recommendation authors a plan. Once you
   have acted on one, Pér stops offering it.


.. _per-key-concepts-skill:

**skill**
   A packaged piece of work you can start by name rather than describing from scratch. Which
   skills are available depends on your tenant.


.. _per-key-concepts-step:

**step**
   A single approvable unit inside a plan: one concrete change to your Amperity tenant. Steps are
   what you approve, either one at a time or all at once.

   .. PARKED-LINK: scheduled_tasks.rst: add the step/task disambiguation to this entry once
      scheduled tasks ship, since "task" then becomes a word in this documentation.


.. _per-key-concepts-trusted-customer-context:

**trusted customer context**
   What Pér works from: your identity-resolved customer data, the history in it, the rules you
   have given Pér to work inside, and the predictive intelligence available in your tenant — all
   of it delivered by the Amperity platform. See
   :ref:`Trusted customer context <per-what-is-per-trusted-context>`.

   .. PENDING NC-003: the "rules you have given Pér to work inside" clause rests on company
      context, must-follow memories and the approval boundary. PO to confirm.


.. _per-key-concepts-user-administrator:

**User Administrator**
   The Amperity `policy <../reference/policies.html>`__ held by the people who manage Pér access:
   switching a tenant between open and managed access, and granting or removing access for
   individuals.


.. _per-key-concepts-write-confirmation:

**write confirmation**
   What stands between Pér proposing a change to Amperity and that change happening. Nothing runs
   until a person works through it.
