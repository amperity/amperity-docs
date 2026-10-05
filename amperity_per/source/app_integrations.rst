.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        The hub for connecting Pér to the other systems your team works in.

.. meta::
    :content class=swiftype name=body data-type=text:
        The hub for connecting Pér to the other systems your team works in.

.. meta::
    :content class=swiftype name=title data-type=string:
        App integrations


.. _per-app-integrations:

==================================================
App integrations
==================================================

App integrations is where Pér is connected to the other systems your team works in.

Everything Pér knows about your customers comes from Amperity, but plenty of what happens to those
customers happens somewhere else. This page is both the short list of what Pér can reach beyond
Amperity and the way in to setting each one up.


.. _per-app-integrations-mcp-connections:

What you can connect
==================================================

Pér can be connected to other systems in three ways.

* **Systems Pér reaches out to.** Connecting one lets Pér look things up there and, with your
  approval, change them. Today that is
  :ref:`Salesforce Marketing Cloud <per-connect-sfmc>`.
* **Pér as something another agent reaches into.** Pér can also be
  :ref:`connected as a context source <per-connect-as-mcp-server>` for an agent somewhere else.
  That direction only ever reads.
* **Places Pér answers in.** Pér can be added to Slack and to Microsoft Teams, where it answers
  questions in a channel. Setting either one up is described with the surface itself, in
  :ref:`Setting up the Slack app <per-in-slack-setup>` and
  :ref:`Setting up the Teams app <per-in-teams-setup>`.

The systems Pér reaches out to are set up under **MCP connections** on this page. Connecting Pér as
a context source is set up in the other agent's own client rather than here. Slack and Microsoft
Teams have their own entries beside **MCP connections**.

Setting up an MCP connection needs no special permission. Anyone who can reach Pér can set one up
and anyone who can reach Pér can take it away, so a connection is worth agreeing on rather than
assuming. Slack and Teams are different: both need Amperity permission to administer API keys, and
Teams also needs a Microsoft directory administrator.

.. PARKED-LINK: connect_databricks.rst: when Databricks ships it becomes a second system Pér
   reaches out to, so the "Today that is Salesforce Marketing Cloud" sentence above changes.


.. _per-app-integrations-using:

Opening App integrations
==================================================

**To open App integrations**

#. Open **Settings**.
#. Choose **App integrations**.
#. Choose **MCP connections**.
