.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        What Public Preview means for Pér: what is included, what depends on your setup, and what is not claimed yet.

.. meta::
    :content class=swiftype name=body data-type=text:
        What Public Preview means for Pér: what is included, what depends on your setup, and what is not claimed yet.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pér in Public Preview


.. _per-public-preview:

==================================================
Pér in Public Preview
==================================================

Pér is in Public Preview. It is a working product, used on real Amperity tenants to do real work,
and it is still moving.

This article says what that means in practice: what you can rely on now, what depends on your own
setup, and what this documentation does not claim yet. If you are deciding how much of your
process to build on Pér, read this first.

.. PENDING NC-001: "Public Preview" is a lifecycle label. It needs stakeholder sign-off before
   this collection publishes (O5).


.. _per-public-preview-what-it-means:

What Public Preview means
==================================================

Public Preview means Pér is available and supported, and that it is still being built.

The practical difference from a finished product is the rate of change. Capabilities arrive.
Screens are rearranged and controls are renamed. Something you learned last month may be
somewhere else this month, or may work better than it did.

Two things are not subject to that change, because they are the shape of the product rather than
features of it:

* **Pér works from your tenant's own data, under your own access.** It reads what you could read
  and acts as you could act.
* **A person approves before anything is written to Amperity.** This is a boundary, not a setting,
  and nothing in Public Preview relaxes it.

This documentation is written against the product as it is, and describes behavior rather than
layout wherever it can — so that what you read stays true when a screen is rearranged. Where it
describes something you cannot find, the usual explanation is your tenant's own configuration.
The next two sections are about that.


.. _per-public-preview-prerequisite:

Before anyone can use Pér
==================================================

An Amperity tenant has to be enabled for Pér before anyone in it can use Pér at all.

This is worth knowing first because it explains the most common way of encountering nothing: not a
permission problem, not a missing feature, but a tenant that has not been turned on. Tenants are
enabled for Pér one at a time, and until yours is, the people in it do not see Pér.

If nobody at your organization can reach Pér, confirm with your Amperity representative that your
tenant is enabled for Pér.

Once a tenant is enabled, :ref:`who gets in <per-managing-access-modes>` is a separate choice. A
tenant can admit anyone already authorized for it, or admit people one at a time — and either way,
each person's existing Amperity permissions govern what they are able to do once they are in.

.. FORWARD-LINK: accessing_per.rst: link the ways into Pér from this section once that article
   exists. The managed-access half was resolved in chunk 4.

.. PENDING NC-023: who can enable a tenant for Pér — the customer or Amperity — is not settled.
   This section deliberately does not say.


.. _per-public-preview-included:

What's included
==================================================

Everyone in an enabled tenant gets the whole of the customer decision loop.

That is the point of the preview: not a sample of the product, but the working cycle end to end,
on your own data.

* **Conversation with Pér** about your customer data, including what Pér can find on the web.
* **Recommendations**, gathered in the Portfolio, each with its evidence and its confidence.
* **Plans, approvals and write confirmations** — the whole approval path, including approving a
  plan and letting it run.
* **Artifacts** — the reports Pér writes and the files you give it, shareable with your team.
* **Notifications**, for work that finishes after you have moved on.
* **Memory and company context**, so Pér carries what you have told it between sessions.
* **The Activity log**, the record of what Pér did.
* **System settings**, for your tenant's configuration and integration status.

.. FORWARD-LINK: all WORKING WITH PÉR, CONTEXT AND SKILLS and SETTINGS articles: link every item
   in this list, in one pass, in the closing run — NOT as each target lands. Linking some bullets
   and not others reads as omissions. Ruled 2026-10-02; recorded as NC-021(d).


.. _per-public-preview-config:

What depends on your setup
==================================================

Some of Pér works for everyone but gives you different things depending on what you have.

Separating these out matters, because "I don't have that" and "that isn't built" look identical
from the outside and call for completely different responses.

These depend on your tenant's data, your connected tools, or your permissions:

* **How good Pér's recommendations are.** Pér reasons from your tenant's data and your company
  context. A tenant with rich history and a well-stated company context gets sharper proposals
  than one without.
* **Skills.** Which packaged pieces of work you can start by name depends on your tenant.
* **App integrations.** The tools Pér can reach beyond Amperity depend on what has been connected.
* **Data connections.** Some destinations need connection details that Amperity does not already
  hold, and Pér can only use what has been supplied.
* **Connecting Salesforce Marketing Cloud**, which needs an account you authorize.
* **Pér as an MCP server.** Available to any enabled tenant, but you connect the agent that uses
  it.
* **Managing access**, which requires the Amperity policy that administers users.

.. FORWARD-LINK: skills.rst, app_integrations.rst, data_connections.rst, connect_sfmc.rst,
   connect_per_as_mcp_server.rst, managing_access.rst: link every item in one pass in the closing
   run, not as each target lands — same reason as the list above. NC-021(d).


.. _per-public-preview-not-claimed:

What this documentation doesn't claim
==================================================

Being clear about what is not here is part of being trustworthy about what is.

An honest account of a preview is more useful than an enthusiastic one, particularly if you are
deciding what to depend on.

* **Pér does not tell you what your marketing achieved.** It keeps a record of what it did and
  what it produced. Judging the business result of that work is still yours.
* **Pér does not watch your tenant between sessions.** It does not act on its own, and it does not
  start a new round of the loop by itself. Each turn begins when a person begins it.
* **This documentation names no dates.** It describes Pér as it works now, and is updated as Pér
  changes.

.. PENDING NC-015: D10 bars launch, GA and availability dates.

.. PENDING NC-016: D5 holds all pricing, consumption, credit and amp-spend claims. This section
   deliberately says nothing about cost; do not add it without a PO ruling.
