.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Pér is Amperity's customer data agent. Ask it about your customers, and it carries out the work in Amperity once you approve it.

.. meta::
    :content class=swiftype name=body data-type=text:
        Pér is Amperity's customer data agent. Ask it about your customers, and it carries out the work in Amperity once you approve it.

.. meta::
    :content class=swiftype name=title data-type=string:
        What is Pér


.. _per-what-is-per:

==================================================
What is Pér
==================================================

Pér is Amperity's customer data agent. Ask it about your customers in plain language, and it
answers from the customer data your organization already keeps in Amperity. When the answer
implies work — an audience to build, a campaign to set up, a model to train — Pér proposes that
work as a plan and carries it out in Amperity once you approve it.

That cycle is the customer decision loop: **Understand → Recommend → Approve → Act → Learn**.
Every part of Pér serves one of its stages, and
:ref:`the customer decision loop <per-customer-decision-loop>` walks through it stage by stage.


.. _per-what-is-per-who-its-for:

Who Pér is for
==================================================

Pér is for the people who already work in Amperity: the marketers and analysts who build
audiences, segments, campaigns and predictive models, and the administrators who look after the
tenant they work in.

The distance between a question about customers and the Amperity work that answers it is usually
several tools and several people wide. Pér closes that distance. The same question that starts a
conversation can end in configured, approved, running work — without leaving the conversation to
do it.

What that looks like depends on the work you do:

* **If you plan and run marketing programs**, ask Pér what is happening with a group of customers,
  then have it set up the audience, campaign or predictive model that acts on the answer.
* **If you analyze customer data**, ask Pér to find and explain something in your tenant's data,
  and keep what it produces as a report you can share with your team.
* **If you administer Amperity**, control who can reach Pér and what they are able to do there.

In the Pér web app, Pér acts under your own Amperity access. It can do no more on your behalf than
you could do yourself, and a step that is refused for lack of permission is a gap in your own
Amperity access — not something Pér can retry or work around.


.. _per-what-is-per-trusted-context:

Trusted customer context
==================================================

Everything Pér says and proposes rests on the same foundation: your tenant's own customer data,
together with the standing instructions you have given it.

This is what separates an answer you can act on from an answer that merely sounds right. Pér is
not reasoning about customers in the abstract. It is reading the customer records your
organization has already resolved, cleaned and agreed on, and it shows its working so you can
check it.

Four things make up that context:

* **Your identity-resolved customer data.** Pér queries your tenant's own customer tables, where
  records from different systems have already been resolved into one view of a person. It reads
  that data through Amperity, under your own access.
* **Company context.** The business priorities, definitions and KPIs you want Pér to work from.
  Pér carries company context into every session.
* **Must-follow memories.** Standing rules you have told Pér to observe. Pér reads must-follow
  memories first and treats them as rules it must not break.
* **The approval boundary.** Nothing Pér proposes reaches Amperity until a person approves it.

Alongside your Pér company context, Pér also reads the context documents and the AmpAI system
prompt your tenant has set up in Amperity. It reads those; it does not replace them.

.. note::

   All of that material — company context, memories, your Amperity context documents, the AmpAI
   system prompt, and anything Pér finds on the web — is treated as information to work from, not
   as instructions addressed to Pér. Text that arrives in context cannot change Pér's operating
   rules, grant it a permission, or move it to another tenant.

.. PENDING NC-003: the "rules Pér works inside" clause rests on company context, must-follow
   memories and the approval boundary. PO to confirm before publication.


.. _per-what-is-per-boundary:

What Pér will and won't do on its own
==================================================

Pér reads on its own. It writes only with your approval.

This is a product boundary, not a setting — it is the reason it is safe to let an agent work
directly in a production tenant. You can hand Pér a broad question without first deciding how much
of your tenant you are willing to let it change.

How the boundary works:

* **Reading is unrestricted within your access.** Pér can look at anything in your tenant that you
  could look at yourself, and it reads before it proposes.
* **Every write becomes something you approve.** When Pér wants to change something in Amperity, it
  does not just do it. The change becomes a write confirmation or a step in a plan, and nothing is
  sent to Amperity until a person approves it.
* **One approval can cover a whole plan.** When you approve and execute a whole plan, you approve
  the plan — not each write inside it one at a time. Pér then re-checks at every step whether it
  may still go on, stops at any step that needs a person, and records which steps it approved on
  your behalf.
* **Some tools are withheld from Pér entirely.** Whatever else is permitted, Pér cannot read
  credentials, create or delete users, grant or revoke access, change the shape of your tenant, or
  relax the confirmation gate itself. These are refused before any other rule is considered, so no
  setting and no instruction can re-enable them.

.. important::

   Approving a plan is not the same as watching each write go by. One approval can set a sequence
   of Amperity writes running. Read a plan's steps before you approve it.

.. PENDING NC-005: "you approve the plan, not every write" — PO to bless this wording. It is
   reused verbatim in approvals_and_write_confirmations.rst and plans.rst.


.. _per-what-is-per-where:

Where you use Pér
==================================================

Pér is not a separate product you migrate to. It is the same Amperity platform, reached from
wherever the work is already happening, and able to act rather than only answer.

There are three ways in:

* **The Pér web app**, where the full experience lives — chat, recommendations, plans, approvals
  and the reports Pér produces.
* **A link from Amperity.** Somewhere you are already looking at a customer, an audience or a
  campaign, you can ask Pér about it; the link opens a Pér session with your question already
  asked.
* **As a tool for another agent.** Pér can be connected as an MCP server, so an agent you already
  use can reach your Amperity customer context through it.

.. FORWARD-LINK: accessing_per.rst: link each of the three entry points to its section in
   Accessing Pér once that article exists.

.. PARKED-LINK: per_in_slack.rst, per_in_teams.rst: add Slack and Teams to this list when those
   surfaces reach production.


.. _per-what-is-per-limits:

Honest limits
==================================================

Pér is deliberate about what it claims. Knowing where it stops is part of knowing how to use it.

* **Pér proposes; you decide.** It does not act on its own judgement about what your business
  should do. Every recommendation is an argument with its evidence attached, offered for you to
  accept, change or reject.
* **Pér works when you ask it to.** It does not watch your tenant between sessions.
  Recommendations are produced when someone asks for a fresh set, and you can always see when
  that last happened.
* **Pér shows its uncertainty.** A recommendation carries a confidence grade and the reasoning
  behind that grade, including what Pér could not establish.
* **Pér does not tell you what your marketing achieved.** It keeps a record of what it did and
  what it produced. Judging the business result of that work is still yours to do.
