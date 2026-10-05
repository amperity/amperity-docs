.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        The standing briefing you give Pér: what your business steers by, what it is working toward, and what your own terms mean.

.. meta::
    :content class=swiftype name=body data-type=text:
        The standing briefing you give Pér: what your business steers by, what it is working toward, and what your own terms mean.

.. meta::
    :content class=swiftype name=title data-type=string:
        Company context


.. _per-company-context:

==================================================
Company context
==================================================

Company context is the standing briefing you give Pér. It says what your business steers by, what
it is working toward, the rules it operates under, and what your own words mean when they appear in
your data. You write it once, and Pér reads it in every session.

It is the difference between an agent that knows your data and one that also knows your business.
Pér can see that a segment's revenue fell; only your company context tells it whether that segment
is one you are deliberately winding down. This is the :ref:`Understand
<per-customer-decision-loop-understand>` stage of the customer decision loop, and company context is
one of the three things that make up the rules Pér works inside, along with must-follow memories and
the approval boundary.

.. PENDING NC-003: the "rules Pér works inside" clause rests on company context, must-follow
   memories and the approval boundary. PO to confirm. Same clause as what_is_per.rst and
   key_concepts.rst.


.. _per-company-context-what-goes-in:

What goes in it
==================================================

Four kinds of thing are worth writing down: what you measure, what you are trying to do, the rules
you work under, and what your terms mean.

Pér can already read your data, so there is no need to restate that information. Instead, it is
useful to state what the data *means*. The useful material for company context is the part that
lives in people's heads rather than in a table.

A tenant with nothing written yet starts from a template with four sections:

* **North-star metrics** — the handful of measures your business is actually run on, and how you
  define each one. Two companies rarely mean the same thing by "active customer".
* **Business priorities** — what you are trying to achieve, and over what horizon.
* **Operating rules** — the standing "always" and "never" that any recommendation has to respect.
* **Glossary** — your own terms, your tiers, your channel names, and anything in your data whose
  meaning is not obvious from its name.

.. important::

   Leave current numbers out. Pér reads those live, and a figure written here is out of date the
   moment it changes. Goals and targets are worth stating, because those are things you have
   chosen rather than things Pér can look up.

The template is a starting point, not a form. You can add sections, remove them or rearrange them,
and nothing is checked against a schema when you save.

Company context is one document per tenant, shared by everyone in it, and there is no separate
permission for it — anyone who can reach Pér can read and edit it.


.. _per-company-context-how-per-uses-it:

How Pér uses it
==================================================

Company context goes into every session, and Pér treats company context as reference rather than
instruction.

What this means:

* **Every session.** Company context is part of what Pér reads before answering you in
  conversation, and part of what it reads before working out a fresh set of recommendations. You
  do not have to repeat it, and you do not have to trigger anything for an edit to take hold.
* **Reference, not orders.** Company context is material Pér works *from*. An instruction written
  into it does not become a rule Pér obeys, and it cannot relax the approval boundary or reach
  anything Pér is not allowed to reach. See
  :ref:`Your company context and memories <per-how-per-uses-your-data-context>`.

.. PENDING NC-031: the Company Context page describes itself more narrowly than the behavior —
   it says Pér reads it before refreshing recommendations and that edits take effect on the next
   refresh. The code puts it in every chat turn as well. Docs state the behavior; the page copy is
   the PO's to fix.


.. _per-company-context-from-amperity:

Context Pér reads from Amperity
==================================================

If your tenant already set up context in Amperity, Pér reads that too, and this page shows it to
you.

Plenty of tenants wrote their business context for AmpAI before Pér existed. None of that has to be
written again, and knowing it is already in play saves you duplicating or contradicting
it.

Below your own company context, the page shows two things from Amperity, read-only:

* **Company context documents** — the
  `context documents <../reference/ampai.html#ampai-company-context>`__ configured in your
  Amperity tenant.
* **The AmpAI system prompt** — the standing instructions your tenant gave AmpAI. Amperity's own
  documentation calls this the
  `custom prompt <../reference/ampai.html#ampai-custom-prompt>`__.

Pér reads both alongside the company context you write here. This page does not replace them, and
it cannot edit them — both are edited in Amperity.

.. note::

   The panel appears only when Pér can reach Amperity for your session. A tenant with no context
   documents, or no AmpAI system prompt, is told so rather than shown an empty box.

.. PENDING NC-032: one object, two names. Pér's settings page labels it the AmpAI system prompt;
   Amperity's own UI and documentation call it the custom prompt. The article names it as the page
   the reader is on labels it, and links to the Amperity reference. PO to settle.


.. _per-company-context-uploading:

Adding documents Pér should read
==================================================

The page can also take whole files. These go to Amperity, not into the document above.

The upload control sits beside your company context, but it does not fill it in. Each file you
upload becomes a separate Amperity context document, and shows up in the read-only panel below
rather than in the text you are editing.

The limits:

* **Ten files at a time**, at most.
* **1 MB each.**
* **``.txt``, ``.md``, ``.pdf`` and ``.docx``** only. A file that is too large, or of a format that
  is not supported, is refused by name.

.. note::

   Uploading is not all-or-nothing. Files are created one at a time, so if one fails, the ones
   already created stay created. Check the panel below before uploading the batch again.


.. _per-company-context-editing:

Editing it
==================================================

Company context belongs to the tenant, so editing it is something more than one person does.

With a document everyone shares, it is likely that two people will eventually open it at once. The
page takes this into account.

* **It records who saved it last, and when.**
* **A save by someone else while you are editing asks you to choose.** You can keep your draft or
  take the saved version. Neither is thrown away without you saying so.
* **Edits are recorded in the** :ref:`Activity log <per-activity-log>`.

You do not have to write it yourself:

* **Pér can propose an edit**, which arrives as a
  :ref:`write confirmation <per-approvals-card>` showing what the document would become. Nothing
  changes until you approve it.
* **The** :ref:`Build company context <per-skills-available>` **skill** works out what your tenant
  already has, interviews you about the rest, shows you the finished document, and publishes it
  through that same confirmation.


.. _per-company-context-using:

Working with company context
==================================================

**To write your company context**

#. Open **Settings** and choose **Company context**.
#. Edit the document. A tenant with nothing written yet starts from the template.
#. Click **Save**.

If someone else saved while you were editing, choose **Keep draft** to keep your version or
**Use latest** to take theirs.

**To add documents Pér should read**

#. Open **Settings** and choose **Company context**.
#. Click **Upload documents to Amperity** and pick the files.

They appear under **From Amperity**, not in the document above.

**To have Pér draft your company context**

#. Start the **Build company context** skill in a conversation.
#. Answer what Pér asks about your business.
#. Read the document it proposes, and approve it.
