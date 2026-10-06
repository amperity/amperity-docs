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

Pér makes it simple to ask a question about customers, get answers grounded in data, and do the work
in Amperity that acts on the answers. The same question that starts a conversation can end in
configured, approved, running work, without leaving the conversation to do it.

What that looks like depends on the work you do:

* **If you plan and run marketing programs**, ask Pér what is happening with a group of customers,
  then have it set up the audience, campaign or predictive model that acts on the answer.
* **If you analyze customer data**, ask Pér to find and explain something in your tenant's data,
  and keep what it produces as a report you can share with your team.
* **If you administer Amperity**, control who can reach Pér and what they are able to do there.


.. _per-what-is-per-trusted-context:

Trusted customer context
==================================================

Everything Pér says and proposes is grounded in your Amperity tenant's own customer data,
together with the standing instructions you have given it.

Four things make up that context:

* **Your identity-resolved customer data.** Pér queries your tenant's own customer tables, where
  records from different systems have already been resolved into one view of a person. It reads
  that data through Amperity, and never beyond the access it has been given.
* **The history in that data.** Not only who your customers are, but what they have done.
* **The rules you have given Pér to work inside.** Three things make these up:

  * **Company context** — the business priorities, definitions and KPIs you want Pér to work
    from, carried into every session.
  * **Must-follow memories** — standing rules you have told Pér to observe. Pér reads must-follow
    memories first and treats them as rules it must not break.
  * **The approval boundary** — nothing Pér proposes reaches Amperity until a person approves it.

* **The predictive intelligence available in your tenant.** Where your tenant already has
  predictive models, Pér looks at the audiences they identify and proposes work that acts on them.

Alongside your Pér company context, Pér also reads the context documents and the AmpAI system
prompt your tenant has set up in Amperity.

.. note::

   All of that material — company context, memories, your Amperity context documents, the AmpAI
   system prompt, and anything Pér finds on the web — is treated as information to work from, not
   as instructions addressed to Pér. Received context cannot change Pér's operating
   rules, grant it a permission, or move it to another tenant.

.. PENDING NC-003: the "rules Pér works inside" clause rests on company context, must-follow
   memories and the approval boundary. PO to confirm before publication.


.. _per-what-is-per-boundary:

What Pér will and won't do on its own
==================================================

Pér reads on its own. It writes only with your approval.

This is a boundary, not an adjustable setting, and is why you can let an agent work
directly in a production tenant. You can hand Pér a broad question without first deciding how much
of your tenant you are willing to let it change.

How the boundary works:

* **Reading is unrestricted within your access.** Pér can look at anything in your tenant that you
  could look at yourself, and it reads before it proposes.
* **Every write becomes something you approve.** When Pér wants to change something in Amperity, it
  does not just do it. The change becomes a write confirmation or a step in a plan, and nothing is
  sent to Amperity until a person approves it.
* **One approval can cover a whole plan.** When you approve and run a whole plan, you approve
  the plan — not each write inside it one at a time. Pér then re-checks at every step whether it
  may still go on, stops at any step that needs a person, and records which steps it approved on
  your behalf.
* **Some tools are withheld from Pér entirely.** Whatever else is permitted, Pér cannot read
  credentials, create or delete people, grant or revoke access, change the shape of your tenant,
  or relax the confirmation gate itself. These are refused before any other rule is considered, so
  no setting and no instruction can re-enable them. The full list is in
  :ref:`What Pér can't do, whatever you approve <per-approvals-limits>`.

.. important::

   Approving a plan is not the same as watching each write go by. One approval can set a sequence
   of Amperity writes running, and a write that has run cannot be undone from Pér. Read a plan's
   steps before you approve it.

.. PENDING NC-005: "you approve the plan, not every write" — PO to bless this wording. It is
   reused verbatim in approvals_and_write_confirmations.rst and plans.rst.


.. _per-what-is-per-where:

Where to use Pér
==================================================

You can access Pér via:

* :ref:`The Pér web app <per-accessing-per-web>`, where the full experience lives — chat,
  recommendations, plans, approvals and the reports Pér produces.
* :ref:`Pér in Slack <per-in-slack>` and :ref:`Pér in Teams <per-in-teams>`, where Pér answers in
  the channel where the work is already being discussed. Both answer only; a change is made in the
  Pér web app.

.. PARKED-LINK: connect_per_as_mcp_server.rst: restore the "As a tool for another agent" bullet to
   this list of places Pér is reached from.

For the address, signing in and choosing a tenant, see
:ref:`Accessing Pér <per-accessing-per>`.
