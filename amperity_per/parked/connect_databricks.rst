.. PENDING D3: this article ships when the Databricks connection is enabled for production
   tenants. At the pin it is limited to one tenant.

.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Connecting Databricks lets Pér query your Databricks workspace directly, alongside what it reads from Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Connecting Databricks lets Pér query your Databricks workspace directly, alongside what it reads from Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Databricks


.. _per-connect-databricks:

==================================================
Connect Databricks
==================================================

Connecting Databricks gives Pér a second place to look: your own Databricks workspace, queried
directly.

It may be the case that you want Pér to reason about information has not been brought into Amperity yet, and until it is, Pér can only tell you what it cannot see. With this connection it can answer from Databricks as well, including telling you which of those tables are worth bringing in.
That is the :ref:`Understand <per-customer-decision-loop-understand>` stage reaching past
Amperity's own edges.


.. _per-connect-databricks-what:

What the connection gives Pér
==================================================

One connection for the whole tenant, made once, that Pér queries as a service principal of yours.

This is a connection to a data platform rather than to a marketing tool, so it behaves differently
from the others: there is nothing for each person to sign in to, and nothing personal about what
Pér sees through it.

* **It is tenant-wide.** One connection serves everyone in the tenant. There is no per-person
  sign-in and no per-person view.
* **Pér connects as a service principal**, not as any individual, so what Pér can read is decided
  entirely by what that service principal has been granted in Databricks.
* **It can see which of your Databricks tables are already bridged into Amperity**, which is what
  lets Pér talk about the two platforms as one picture rather than two.
* **Setting it up needs no special permission in Pér.** Anyone who can reach Pér can make the
  connection, and anyone who can reach Pér can remove it — so it is worth agreeing on rather than
  assuming.


.. _per-connect-databricks-reach:

What Pér can and can't reach
==================================================

Setup checks the credential and the warehouse. It cannot check whether the service principal has been granted anything to read — so a connection can pass every check Pér is able to run and still return nothing.

* **Setup verifies the credential and the warehouse.** Pér asks Databricks for a token and runs a
  real check against the warehouse you named. A failure here stops the connection being saved.
* **Setup cannot verify your catalog grants.** They are per-catalog and the check cannot read
  them. Until they are in place Pér will not recommend anything from Databricks.
* **A stopped warehouse is started by the check**, which takes a few minutes. That wait is the
  check doing its job, not a hang.

.. important::

   If Pér seems to know nothing about your Databricks data after a successful setup, the grants
   are the first thing to look at — not the connection.

Where a plan needs Databricks tables brought into Amperity, Pér adds a step that works out which
bridge covers them and waits for a person to confirm it. That step reads bridge configuration and
never the data behind it, and if none of the tables are bridged yet it says so rather than going
ahead. See :ref:`Plans <per-plans>`.


.. _per-connect-databricks-prerequisites:

Before you start
==================================================

Everything Pér asks for comes from Databricks, so it is worth collecting first.

Setup is one screen and one chance: the client secret is not shown again afterwards, so an
incomplete attempt means going back to Databricks for a new one.

You need a Databricks service principal, and its:

* **workspace host** — just the host from your workspace's address, with no scheme and no path
* **client ID**
* **client secret**, issued for that service principal and scoped at least to SQL
* **SQL warehouse ID**, for the warehouse you want Pér to query

And the service principal needs, in Databricks:

* to be **added to the workspace**
* **CAN USE** on that SQL warehouse
* **USE SHARE** on the metastore — without it Pér cannot see which tables are already bridged into
  Amperity
* **USE CATALOG**, **USE SCHEMA** and **SELECT** on every catalog you want Pér to use


.. _per-connect-databricks-using:

Working with the connection
==================================================

Both of these are on the **Databricks** card, reached from **Settings** →
:ref:`App integrations <per-app-integrations>` → **MCP connections**.

**To connect Databricks**

#. Click **Set up**.
#. Enter the **Workspace host**, **Client ID**, **Client secret** and **SQL warehouse ID**.
#. Click **Test connection** to check them without saving, if you want to.
#. Click **Continue**.

Pér checks the credential and the warehouse before storing anything. A connected workspace says so
on the card, and names the host it is connected to.

**To remove the connection**

#. Click **Delete**, then confirm.

This removes the connection for the whole tenant, not just for you. Setting it up again means
another client secret, since the first one is not shown twice.
