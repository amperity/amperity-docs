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

.. PENDING NC-039: the page's own lead text names Slack and Teams on every tenant, including the
   ones that have neither. Product copy; this article describes what is actually on the page.


.. _per-app-integrations-mcp-connections:

What you can connect
==================================================

Pér can be connected to other systems in two directions.

* **Systems Pér reaches out to.** Connecting one lets Pér look things up there and, with your
  approval, change them. Today that is
  :ref:`Salesforce Marketing Cloud <per-connect-sfmc>`.
* **Pér as something another agent reaches into.** Pér can also be
  :ref:`connected as a context source <per-connect-as-mcp-server>` for an agent somewhere else.
  That direction only ever reads.

Both directions are set up under **MCP connections** on this page.

Connecting anything here needs no special permission. Anyone who can reach Pér can set a connection
up and anyone who can reach Pér can take it away, so a connection is worth agreeing on rather than
assuming.

.. PARKED-LINK: per_in_slack.rst: add the Slack setup section to this article once Slack ships.

.. PARKED-LINK: per_in_teams.rst: add the Teams setup section to this article once Teams ships.

.. PARKED-LINK: connect_databricks.rst: when Databricks ships it becomes a second system Pér
   reaches out to, so the "Today that is Salesforce Marketing Cloud" sentence above changes.


.. _per-app-integrations-using:

Opening App integrations
==================================================

**To open App integrations**

#. Open **Settings**.
#. Choose **App integrations**.
#. Choose **MCP connections**.
