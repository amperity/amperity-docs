.. PENDING D3: this article ships when account linking is enabled for production tenants and a
   link changes what Pér does. At the pin a link is recorded and nothing reads it.

.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Linking records that a chat account and an Amperity user are the same person. One link covers one workspace, and you can unlink at any time.

.. meta::
    :content class=swiftype name=body data-type=text:
        Linking records that a chat account and an Amperity user are the same person. One link covers one workspace, and you can unlink at any time.

.. meta::
    :content class=swiftype name=title data-type=string:
        Linked accounts


.. _per-linked-accounts:

==================================================
Linked accounts
==================================================

Linking is a way to record that an account in a chat workspace and an Amperity user are the same person.

Everywhere else, Pér knows who is asking. On a chat surface it does not: the whole workspace
reaches Pér through one shared connection, and nothing in a channel message says which Amperity
user sent it. A link is the record that closes that gap — your Amperity user on one side, your
account in that workspace on the other.

.. important::

   A link is a record, not a grant. It gives nobody access to anything, and it does not yet change
   what Pér answers or who it answers as. See
   :ref:`What linking does not do <per-linked-accounts-limits>`.

.. PENDING NC-051: nothing consumes a link at the pin — the only readers are the linking flow
   itself and the settings tile. The article is written to say so plainly. Ruled by Sam,
   2026-10-02; the un-park condition requires a consumer before this ships.


.. _per-linked-accounts-what:

What a link is
==================================================

One link joins one chat account to one Amperity user, for one workspace.

Linking is deliberately a thing you do rather than something inferred from a matching email
address. A guess would be wrong occasionally and invisible when it was, so Pér asks instead.

* **It covers one workspace.** If your tenant has more than one chat workspace set up, each is
  linked separately, and Pér never picks one for you — even when there is only one to pick.
* **You start it in Pér and finish it in the chat platform.** Pér sends you to sign in there, and
  brings you back to a screen that names the account about to be linked.
* **That screen reads the account from the link itself**, not from the address bar, so what it
  shows you is what gets linked.
* **A chat account already linked to a different Amperity user cannot be taken over.** Only that
  person can unlink it first.
* **Each link shows where it came from** — the account, the workspace, the tenant, and when it was
  made. The account's name is read fresh each time rather than stored.


.. _per-linked-accounts-limits:

What linking does not do
==================================================

Linking does not change what Pér will answer, or what anyone can reach. A link is a record Pér keeps. It is not a credential, and it is
not a permission.

* **It does not change what Pér answers on a chat surface.** Those answers are still produced
  through the workspace's shared connection, on the same terms for everyone in the channel.
* **It does not carry your Amperity access into chat.** Nothing about a linked account makes Pér
  show you something it would not show a colleague in the same channel.
* **It grants nothing.** Linking gives you no access you did not already have, and gives nobody
  else any access to you.
* **Your own Amperity access still governs the Pér web app**, where you are signed in as yourself.
  See :ref:`Accessing Pér <per-accessing-per>`.


.. _per-linked-accounts-removal:

When a link goes away
==================================================

A link lasts until you remove it, or until the workspace it covers stops being connected.

* **You can unlink at any time**, and link again afterwards.
* **An unfinished link expires.** The link Pér gives you is single-use, and one left sitting has
  to be started again.
* **Cancelling partway leaves nothing behind.**
* **A link is removed when its workspace is no longer set up for Pér**, or when that workspace is
  claimed for a different Amperity tenant. Anyone who had linked an account there links it again
  once the workspace is set up afresh.


.. _per-linked-accounts-using:

Using linked accounts
==================================================

Linked accounts is a setting of your own rather than your tenant's: what you link is yours, and
changing it changes nothing for anyone else.

**To link a chat account**

#. Open **Settings**.
#. Find **Linked accounts**, and the workspace you want to link.
#. Click **Link**.
#. Sign in to the chat platform when it asks.
#. Read the account named on the confirmation screen, and confirm it.

Pér tells you whether the link was made. If it was not — the link had expired, or that account
belongs to someone else — it says which.

**To unlink a chat account**

#. Open **Settings**.
#. Find the account under **Linked accounts**.
#. Click **Unlink**, then confirm.

Pér stops associating that account with your Amperity user. You can link it again at any time.
