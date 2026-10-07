.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Where Pér's answers come from: the data it reads, under whose access, what else it carries into a session, and what it can never reach.

.. meta::
    :content class=swiftype name=body data-type=text:
        Where Pér's answers come from: the data it reads, under whose access, what else it carries into a session, and what it can never reach.

.. meta::
    :content class=swiftype name=title data-type=string:
        How Pér uses your data


.. _per-how-per-uses-your-data:

==================================================
How Pér uses your data
==================================================

Pér answers from your organization's own customer data, read out of Amperity at the moment you ask.
Amperity stays the system of record: Pér builds no separate store of your customer data, though what
it read to answer you is kept with the conversation it was asked in. It reads under your own
Amperity access, so it can see exactly what you can see and nothing more.

Every answer Pér gives is as solid as its sources. This article sets out what those
sources are: which of your data Pér reads and under whose access, what else it carries into a
session, what may leave Amperity, and what it is never allowed to reach at all. It is the
:ref:`Understand <per-customer-decision-loop-understand>` stage of the customer decision loop,
described from the data's side rather than the conversation's.


.. _per-how-per-uses-your-data-reads:

Reading your customer data
==================================================

Pér queries your tenant through Amperity's own tools, the same way any other part of the platform
does.

This is what makes an answer checkable. Pér is not reasoning about customers in the abstract and it
is not working from a snapshot taken at some earlier point — it is reading the identity-resolved
customer records your organization has already agreed on, as they are now.

How that works:

* **Under your own access.** In the Pér web app, Pér reads as you, using the access your Amperity
  sign-in gives you. It can do no more on your behalf than you could do yourself.
* **Your policies apply.** Whatever your Amperity policies restrict is restricted for Pér. If your
  policies carry the `Restrict PII access
  <../reference/policies.html#policies-option-restrict-pii>`__ option, Pér does not see that data
  either.
* **A refusal is about your access, not about Pér.** When Amperity declines a read, Pér names the
  permission that is missing and says that you or an administrator needs to grant it. It does not
  retry around it, and it does not estimate the numbers the blocked read would have returned.
* **One tenant, one person.** A session is fixed to the tenant you are working in. Pér cannot move
  itself to another tenant.
* **It reads before it proposes.** Pér is required to look up what it needs rather than guess —
  an identifier, a table, a column, the current state of something it is about to change.
* **It does not invent results.** When a read fails, Pér says so and carries on with what it has,
  rather than filling the gap.

The chat surfaces work differently. In Slack and Microsoft Teams, Pér answers on one connection
belonging to the workspace rather than on the Amperity sign-in of whoever asked, and that connection
is not given access to PII. Values from columns tagged as PII come back redacted, though counts and
other aggregates over them still work. Neither surface can change anything. See
:ref:`Pér in Slack <per-in-slack>` and :ref:`Pér in Teams <per-in-teams>`.

.. note::

   Reading is not something you approve. Changing anything is. See
   :ref:`Approvals and write confirmations <per-approvals>`.


.. _per-how-per-uses-your-data-context:

What else Pér brings to a question
==================================================

Alongside your customer data, Pér carries standing material into every session.

This is the part you control, and it is why Pér's answers get better over time rather than starting
cold each new session. It is also material Pér did not write, which is why it is handled carefully.

What goes in:

* **Your** :ref:`company context <per-company-context>` — the business priorities, definitions
  and measures you want Pér to work from.
* **Your** :ref:`memories <per-memory>` — what you have told Pér to remember between sessions. Pér
  reads must-follow memories first and treats them as rules it must not break.
* **The Amperity context documents and the AI Assistant system prompt** your tenant has set up.
  Pér reads those; it does not replace them.
* **A summary of your portfolio** — the work already proposed and under way.

.. important::

   All of that material is treated as information to work from, not as instructions addressed to
   Pér. Text that arrives in context cannot change Pér's operating rules, hand it a tool, grant it
   a permission, or move it to another tenant. Where such material conflicts with Pér's own rules,
   Pér's rules win, and a directive inside it is not carried out. In such a case, Pér says plainly
   that the material cannot change its rules and gets on with what you asked.

The one exception is a skill's own instructions. A :ref:`skill <per-skills>` is Amperity's
material rather than something found or written at the tenant, so Pér follows it for the task it
covers — and stops when you ask it to stop.


.. _per-how-per-uses-your-data-files:

Files you attach
==================================================

A file you :ref:`attach to a conversation <per-chatting-attachments>` is material for Pér to work
from, not a set of orders.

This matters most for documents that came from outside your organization, which is exactly where an
instruction aimed at an agent would be hidden. Pér reads the file, uses it however your message
asks — summarizing it, analyzing it, quoting it — and treats your message, not the file, as the
thing it is acting on.

If the file contains directives addressed to Pér, such as calling a tool, changing its rules or
contacting someone, Pér does not carry them out. It mentions them instead, where they are relevant.

Every file you attach is also kept as an :ref:`artifact <per-artifacts>`, so you can reopen it
without going back through the conversation.


.. _per-how-per-uses-your-data-web:

Searching the web
==================================================

Pér can look outside Amperity for recent public news. This helps recommendations account for
current events that might affect a campaign, such as a recall or a regulatory change.

Anything leaving your tenant is checked against a fixed rule, enforced on every query rather than
left to judgement.

How it works:

* **Recent news, not general browsing.** The default window is the last 30 days.
* **Only for public questions.** Pér uses it for named external events, industry and regulatory
  news, and disruption coverage. Questions your own data answers — audience sizes, campaign
  results, what is scheduled, how your tenant is configured — are answered from your tenant
  instead.
* **Queries are checked before they leave.** A search Pér sends out may not contain an email
  address; may not contain the characters ``$``, ``%``, ``@`` or ``#``; may not contain numbers
  other than a four-digit year or a quarter such as ``Q3``; and may not contain your tenant's own
  identifier or a term on a blocked list that covers common internal field names. A query that
  breaks any of those rules is refused before it is sent, and Pér is asked to rephrase it in public
  terms.
* **Sources are cited when used.** Pér cites a result it actually relied on, and is told not to
  list sources it read but did not use.

.. important::

   Those rules are what keeps a web search from carrying your customer counts, your revenue figures,
   your audience sizes or your customers' details out of Amperity — not as a matter of care, but
   because the query is rejected. They are structural rules rather than a complete filter: your
   company's own public name, for instance, is meant to go out, because that is what news is about.


.. _per-how-per-uses-your-data-withheld:

What Pér is never allowed to reach
==================================================

A short list of things stays out of reach whatever is asked and whatever is approved.

These are the ones that cannot be re-enabled by a setting, an instruction, or a persuasive request,
because they are refused before any other rule is considered.

On the reading side, Pér cannot retrieve a stored credential, and it cannot read a file off the
server it runs on. Both are refused even though they are reads, and even though your own Amperity
access might otherwise allow them.

On the changing side the list is longer: identity and access, the shape of your tenant, where your
data may be sent, and the confirmation gate itself are all out of reach, whatever is approved. The
full boundary is in :ref:`What Pér can't do, whatever you approve <per-approvals-limits>`.

.. PARKED-LINK: scheduled_tasks.rst: when scheduled tasks ship, add that a scheduled run is
   offered only reading tools, and that each read is checked a second time against the task
   owner's own Amperity access rather than only against the tenant's.


.. _per-how-per-uses-your-data-not-covered:

What this doesn't cover
==================================================

This article describes how Pér reaches your data and what it does with it inside the product.

It is not a statement about where your data is processed, who processes it, how long anything is
retained, or whether any of it is used to train a model. Those are commitments rather than product
behavior, and they belong in your agreement with Amperity. For anything in that category, see your
agreement or ask your Amperity representative.
