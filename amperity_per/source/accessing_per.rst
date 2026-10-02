.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        How to reach Pér — the address, signing in, choosing a tenant, and what to do when you can't get in.

.. meta::
    :content class=swiftype name=body data-type=text:
        How to reach Pér — the address, signing in, choosing a tenant, and what to do when you can't get in.

.. meta::
    :content class=swiftype name=title data-type=string:
        Accessing Pér


.. _per-accessing-per:

==================================================
Accessing Pér
==================================================

Pér is reached in a web browser, with the Amperity account you already have. There is nothing to
install and no second password to keep.

Most of the trouble people have reaching Pér is one of four things, and they look alike from the
outside: the tenant has not been enabled for Pér, your organization admits people one at a time
and you are not on the list yet, you are on an address that does not serve your tenant, or you
followed a link into a tenant that is not yours. This article is how to tell them apart.


.. _per-accessing-per-web:

The Pér web app
==================================================

Pér runs as a web application, and that is where the whole of it is.

Everything Pér can do happens here: the conversation, the recommendations it gathers, the plans it
writes, the approvals that let those plans run, and the reports it produces. It is worth knowing
that this is one place rather than several, because it means a piece of work you start can be
finished without moving anywhere else.

How to reach it:

* **The address is** ``https://askper.amperity.com``. If you have ``per.amperity.com`` or
  ``amp-agent.amperity.com`` bookmarked, both still work — they send you to the same place.
* **Canadian tenants use a different address**, ``https://per-aws-cc1.amperity.com``.
* **Pér runs in more than one location**, and your tenant is served from one of them. If you open
  an address that does not serve your tenant, Pér sends you to the one that does, keeping the page
  and the tenant you asked for. You do not sign in again on the way.

.. note::

   Because of that last point, the address in your browser may not be the one you typed. That is
   expected, and the address you land on is the one worth bookmarking.

**To open Pér**

#. Go to `Pér <https://askper.amperity.com>`__, or to
   `per-aws-cc1.amperity.com <https://per-aws-cc1.amperity.com>`__ if your tenant is Canadian.
#. Sign in with your Amperity account.


.. _per-accessing-per-signing-in:

Signing in
==================================================

You sign in to Pér with your Amperity account, through the same sign-in Amperity uses.

Pér does not keep its own list of people or its own credentials. That means there is one identity
to manage, one place to change it, and nothing extra to set up before someone can be let in — and
it means whatever your organization already requires in order to sign in to Amperity is what Pér
asks for too.

* **Single sign-on applies.** If your organization signs in to Amperity through its own identity
  provider, Pér signs you in the same way. See
  `How single sign-on works <../reference/sso.html#sso-howitworks>`__.
* **Multi-factor authentication applies**, where your organization has set it up. See
  `Multi-factor authentication <../reference/users.html#settings-users-multifactor-authentication>`__.
* **Who can hold an Amperity account at all** is governed by your tenant's
  `allowed domains <../reference/users.html#settings-users-allow-domains>`__, as it is everywhere
  else in the platform.
* **A session lasts up to seven days.** After that you sign in again.

.. note::

   Signing out is not the same as losing access. Someone who should no longer be able to reach Pér
   is cut off in Amperity — see :ref:`Cutting someone off <per-managing-access-revoking>`.

**To sign out**

#. Open the menu in the top bar and choose **Log out**.

On a narrow window the same control is at the foot of the sidebar.


.. _per-accessing-per-tenant:

Choosing a tenant
==================================================

Pér works in one Amperity tenant at a time, and it shows you only the tenants that have been
enabled for Pér.

That second half is the one worth knowing in advance, because it is the usual explanation for a
tenant you expected to see and cannot. The list in Pér is not your list of Amperity tenants; it is
the part of that list Pér has been turned on for. Nothing is wrong with the tenants that are
missing — they have not been enabled.

* **Pér picks one to start with.** When you arrive without a tenant already chosen, Pér selects one
  for you so you are not met with a list.
* **You can change it at any time** from the tenant picker in the top bar, searching by the
  tenant's name or by its id. Changing tenant reloads the page you are on.
* **The tenant travels in the address.** A Pér link you copy carries the tenant it was in, so
  sending someone a page sends them to the same tenant — provided they can reach it themselves.
* **If the tenant you choose is served from another address**, Pér takes you there rather than
  failing.

.. important::

   Being admitted to a tenant in Pér is permission to enter, nothing more. What you are able to do
   once you are in is governed by your own Amperity permissions, exactly as it is elsewhere in the
   platform. See :ref:`Open and managed access <per-managing-access-modes>`.

.. PENDING NC-008: amperity-docs already publishes a "Use Customer Data Agent" row in the policies
   reference, which may not match the two gates the product applies. PO and engineering. The same
   marker sits in managing_access.rst.

**To switch tenants**

#. In the top bar, open the tenant picker.
#. Type part of the tenant's name or its id, and choose it.


.. _per-accessing-per-cant-get-in:

When you can't get in
==================================================

Four things stop people reaching Pér, and each one has a different answer.

They are easy to confuse, because all four end with a screen instead of the product. Telling them
apart is the difference between asking an administrator for something, asking your Amperity
representative for something else, and simply waiting a minute.

* **Nothing in your list has Pér.** Pér says there are no tenants available, or that it is not
  available for your tenants yet. This means your tenant has not been enabled for Pér, which is
  not a permission problem and cannot be fixed by granting you anything. Ask your Amperity
  representative — see :ref:`Before anyone can use Pér <per-public-preview-prerequisite>`.
* **Your tenant admits people one at a time, and you are not on the list.** Pér says that access
  is not enabled and to ask your Amperity User Administrator to allow Pér access for your user,
  and offers a link into Amperity. Ask the person who administers your users — see
  :ref:`Managing access to Pér <per-managing-access>`.
* **Amperity could not answer.** Pér says the access check is unavailable and to try again
  shortly. This is not a refusal, and nothing about your access has changed. Try again.
* **The link you followed names a tenant that is not yours.** Pér says so, and offers a picker of
  the tenants you can reach. Nothing is chosen for you here on purpose: a link into somebody
  else's tenant should not quietly move you into one of your own. Pick a tenant, or ask whoever
  sent the link which tenant they meant.

.. note::

   The first two look similar and are not. "No tenants available" is about the tenant; "access not
   enabled" is about you. Only the second one can be solved by an administrator in your own
   organization.


.. _per-accessing-per-from-an-agent:

From another agent
==================================================

An agent you already use can read your Pér context directly, rather than being handed a copy of it.

Not all the work happens in Pér, and the context Pér draws on is worth more when it is not
confined to one window. The connection only ever reads, so widening who can see that context never
widens who can act on it.

See :ref:`Connect Pér as an MCP server <per-connect-as-mcp-server>`.

.. PARKED-LINK: per_in_slack.rst, per_in_teams.rst: add Slack and Teams here as further ways in,
   and say that neither can approve a change, so a change is made in the Pér web app instead.
