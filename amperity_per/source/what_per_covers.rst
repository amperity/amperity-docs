.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        What Pér covers: what a tenant needs first, what is included, what depends on your setup, and what is not claimed.

.. meta::
    :content class=swiftype name=body data-type=text:
        What Pér covers: what a tenant needs first, what is included, what depends on your setup, and what is not claimed.

.. meta::
    :content class=swiftype name=title data-type=string:
        What Pér covers


.. _per-what-per-covers:

==================================================
What Pér covers
==================================================

Pér is a functional product, used on real Amperity tenants to do real work, and it keeps
developing.

This article says what you can rely on now, what your tenant needs before anyone can use Pér at
all, what depends on your own setup, and what this documentation does not claim. If you are
deciding how much of your process to build on Pér, read this first.


.. _per-what-per-covers-constants:

What doesn't change
==================================================

Capabilities arrive, screens are rearranged and controls are renamed. Two things are the shape of
the product rather than features of it, and they hold throughout:

* **Pér works from your tenant's own data, and never beyond the access it is given.** In the Pér
  web app that access is your own: it reads what you could read and acts as you could act. In
  Slack and Microsoft Teams it is narrower — one workspace connection, no PII, and no ability to
  change anything.
* **A person approves before anything is written to Amperity.** This is a boundary, not a setting,
  and nothing relaxes it.

This documentation is written against the product as it is, and describes behavior rather than
layout wherever it can — so that what you read stays true when a screen is rearranged. Where it
describes something you cannot find, the usual explanation is your tenant's own configuration,
which the sections below describe.


.. _per-what-per-covers-prerequisite:

Before anyone can use Pér
==================================================

An Amperity tenant has to be enabled for Pér before anyone in it can use Pér at all.

If nobody at your organization can reach Pér, confirm with your Amperity representative that your
tenant is enabled for Pér.

Once a tenant is enabled, :ref:`who gets in <per-managing-access-modes>` is a separate choice. A
tenant can admit anyone already authorized for it, or admit people one at a time — and either way,
each person's existing Amperity permissions govern what they are able to do once they are in.

For how someone actually gets in once both of those are settled, see
:ref:`Accessing Pér <per-accessing-per>`.

.. PENDING NC-023: who can enable a tenant for Pér — the customer or Amperity — is not settled.
   This section deliberately does not say.


.. _per-what-per-covers-included:

What's included
==================================================

Everyone in an enabled tenant gets the whole of the customer decision loop.

The end-to-end working cycle includes:

* :ref:`Conversation with Pér <per-chatting>` about your customer data, including what Pér can
  find on the web.
* :ref:`Recommendations <per-recommendations>`, gathered in the Portfolio, each with its evidence
  and its confidence.
* :ref:`Plans <per-plans>`, :ref:`approvals and write confirmations <per-approvals>` — the whole
  approval path, including approving a plan and letting it run.
* :ref:`Artifacts <per-artifacts>` — the reports Pér writes and the files you give it, shareable
  with your team.
* :ref:`Memory <per-memory>` and :ref:`company context <per-company-context>`, so Pér carries what
  you have told it between sessions.
* :ref:`The Activity log <per-activity-log>`, the record of what Pér did.
* :ref:`System settings <per-system-settings>`, for your tenant's configuration and integration
  status.


.. _per-what-per-covers-config:

What depends on your setup
==================================================

Some of Pér works for everyone but gives you different things depending on what you have.

Separating these out matters, because "I don't have that" and "that isn't built" look identical
from the outside and call for completely different responses.

These depend on your tenant's data, your connected tools, or your permissions:

* **How good** :ref:`Pér's recommendations <per-recommendations>` **are.** Pér reasons from your
  tenant's data and your :ref:`company context <per-company-context>`. A tenant with rich history
  and a well-stated company context gets sharper proposals than one without.
* :ref:`Skills <per-skills>`. Which packaged pieces of work you can start by name depends on your
  tenant.
* :ref:`App integrations <per-app-integrations>`. The tools Pér can reach beyond Amperity depend
  on what has been connected.
* :ref:`Data connections <per-data-connections>`. Some destinations need connection details that
  Amperity does not already hold, and Pér can only use what has been supplied.
* :ref:`Connecting Salesforce Marketing Cloud <per-connect-sfmc>`, which needs an account you
  authorize.
* :ref:`Managing access <per-managing-access>`, which requires the Amperity policy that
  administers users.


.. _per-what-per-covers-not-claimed:

What this documentation doesn't claim
==================================================

* **Pér does not tell you what your marketing achieved.** It keeps a record of what it did and
  what it produced. Judging the business result of that work is still yours.
* **Pér does not watch your tenant between sessions.** It does not act on its own, and it does not
  start a new round of the loop by itself. Each turn begins when a person begins it.
* **This documentation names no dates.** It describes Pér as it works now, and is updated as Pér
  changes.
