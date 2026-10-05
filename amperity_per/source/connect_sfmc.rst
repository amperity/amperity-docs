.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Connect Pér to Salesforce Marketing Cloud so it can look things up in your account and, with your approval, change them.

.. meta::
    :content class=swiftype name=body data-type=text:
        Connect Pér to Salesforce Marketing Cloud so it can look things up in your account and, with your approval, change them.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Salesforce Marketing Cloud


.. _per-connect-sfmc:

==================================================
Connect Salesforce Marketing Cloud
==================================================

Connecting Salesforce Marketing Cloud lets Pér work in your Salesforce account: look up what is there, and — once you approve — change it.

With this connection, the same conversation covers both platforms, and the things Pér tells you about Salesforce are things it looked up rather than inferred.

The connection is also the one in Pér that belongs to a person rather than to a tenant, which
changes who has to do what.


.. _per-connect-sfmc-two-halves:

A tenant connection, and your own sign-in
==================================================

Setting this up is two separate jobs: someone connects the tenant to a Business Unit once, and then
each person who wants to use it signs in to Salesforce as themselves.

One person setting it up will not automatcally connect everyone else. Pér does not get a shared Salesforce account that sees everything, it gets your account.

* **The tenant connection is made once.** It points Pér at one Salesforce Business Unit, and
  everyone in the tenant shares it. It needs no special permission — anyone who can reach Pér can
  make it, and anyone who can reach Pér can take it away.
* **The address has to be assembled.** Salesforce does not display the address Pér needs
  ready-made; someone with access to your Salesforce setup builds it from the installed package
  that authorizes Pér. The setup panel in Pér walks through it, and
  `Salesforce's own setup guide <https://developer.salesforce.com/docs/marketing/mce-mcp/guide/mce-mcp-setup.html>`__
  |ext_link| is the fuller reference.
* **Then each person signs in.** Signing in is per person and takes one click once the tenant
  connection exists.
* **A tenant can connect several Business Units**, up to five. Past the first, each one needs a
  label, because the label is the only thing that tells them apart afterwards.


.. _per-connect-sfmc-what-per-can-do:

What Pér can do once you are connected
==================================================

Pér gets Salesforce tools in conversation, scoped to your own Salesforce login — and a Salesforce
change is approved exactly the way an Amperity change is.

* **What it can reach is what you can reach.** Pér acts as you in Salesforce, so your own
  permissions there decide what it can see and what it can do. A colleague with narrower Salesforce
  access gets narrower answers from Pér, in the same tenant, on the same day.
* **Looking things up needs no approval**, the same as reading in Amperity.
* **Changing something needs approvals.** A Salesforce change Pér proposes — creating something,
  updating something, deleting something, sending something — arrives as a
  :ref:`write confirmation <per-approvals-card>` and runs only when a person approves it.

.. important::

   The :ref:`approval boundary <per-approvals-boundary>` does not stop at Amperity. There is no
   mode in which Pér changes your Salesforce account without a person approving the change first.

This connection and :ref:`Data connections <per-data-connections>` are two halves of one job.
This one authorizes Pér to act in Salesforce as you. Data connections supplies the subdomain that
identifies your account, which a destination needs before Pér can read what it reports back. A
destination reads as ready only when both are in place.


.. _per-connect-sfmc-staying-connected:

Staying connected, and coming apart
==================================================

A connection can lapse, so Pér checks rather than trusting what it last saw.

* **Every visit re-checks.** If your sign-in has expired while you were away, you are asked to sign
  in again rather than told you are connected when you are not.
* **You can disconnect yourself** without affecting anybody else. The tenant connection stays, and
  you can sign in again whenever you want.
* **Changing a Business Unit's address disconnects everyone** using it. They are not locked out —
  each of them signs in again — but nobody is connected until they do.

.. caution::

   Removing a Business Unit is not the same as disconnecting yourself. It removes the connection
   for the whole tenant, disconnects everyone using it, and cannot be undone — setting it up again
   means assembling the address again.


.. _per-connect-sfmc-using:

Working with the connection
==================================================

All of these are on the **Salesforce Marketing Cloud** card, reached from **Settings** →
:ref:`App integrations <per-app-integrations>` → **MCP connections**.

**To connect a Business Unit**

#. Click **Set up**.
#. Paste the **MCP server URL** from your Salesforce installed package, and give it a **Label**.
#. Click **Continue**, and sign in to Salesforce when you are sent there.

**To connect yourself to a Business Unit someone else set up**

#. Click **Sign in with Salesforce**.

**To check that your connection still works**

#. Click **Test connection**.

**To disconnect yourself**

#. Click **Disconnect**.

**To rename a Business Unit or point it somewhere else**

#. Click **Edit**.
#. Change the **Label**, the **MCP server URL**, or both.
#. Click **Save**.

**To remove a Business Unit for the whole tenant**

#. Click **Remove**.
#. Confirm.

**To add another Business Unit**

#. Click **Add another Business Unit** and set it up as above.

A connected Business Unit says so, and says how many Salesforce tools Pér has through it.
