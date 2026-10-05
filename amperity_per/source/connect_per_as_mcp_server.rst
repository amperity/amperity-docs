.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Bring what Pér holds for your tenants into another agent as read-only context, scoped to what you can already see.

.. meta::
    :content class=swiftype name=body data-type=text:
        Bring what Pér holds for your tenants into another agent as read-only context, scoped to what you can already see.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Pér as an MCP server


.. _per-connect-as-mcp-server:

==================================================
Connect Pér as an MCP server
==================================================

Pér can act as a context source for another agent. A client that speaks the
`Model Context Protocol <https://modelcontextprotocol.io/>`__ |ext_link| connects to Pér, signs in
as you, and can then read what Pér holds for the tenants you can already see.

Not all the work happens in Pér. A briefing, a deck, or another team's agent can be built on the
same trusted customer context Pér works from. Because the connection only ever reads, widening who
can see that context never widens who can act on it.

.. PENDING NC-037: there is no published address for this endpoint and no page in Pér that shows
   one, so this article cannot tell a reader how to make the connection. See the last section.

.. PENDING NC-004: which Pér host is published is unsettled, and this article needs one.


.. _per-connect-as-mcp-server-what-it-is:

Context, not control
==================================================

The connection is read-only: there is nothing on the other end that can change anything.

That is important to keep in mind, because connecting an agent to a production system usually raises
the question of what it could do by mistake. Here the answer is nothing. The connection offers no
way to create, change or delete anything in Pér or in Amperity, and nothing an agent asks for
through it can become a change — not even one waiting for approval.

What it offers instead:

* **The tenants your own access covers**, and which of them it is working in by default.
* **A summary of a tenant**, the same material Pér uses to orient itself.
* **The recommendations in the Portfolio**, and the detail behind each one.
* **Recent activity** — what has been happening in the tenant.

.. important::

   This is a different thing from the
   `Amperity MCP server <../api/mcp_overview.html>`__, which lets an agent operate Amperity itself:
   run identity resolution, build segments, run campaigns. That one acts. This one reads what Pér
   holds. Connecting one says nothing about the other.

.. PENDING NC-038: the server also registers tools over surfaces this documentation excludes. The
   article describes what the connection offers in categories and names no tool.


.. _per-connect-as-mcp-server-access:

What the connected agent can see
==================================================

Exactly what you can see. Not more, and not less.

* **It is you, connecting.** The connection carries your own Amperity identity, so the tenants it
  can read are the tenants you are authorized for. A tenant you cannot open in Pér is a tenant it
  cannot read, and asking for one by name is refused.
* **Managed access applies here too.** On a tenant that admits people individually, a person
  without a grant is refused through this connection in the same way they are refused at the front
  door.
* **Nobody else inherits your access.** The connection belongs to the person who made it. Another
  person connecting the same client gets their own view, not yours.

.. important::

   What the agent on the other end does with what it reads is outside Pér's reach. Your customer
   data arrives in that client and is handled under whatever terms govern it. See
   :ref:`What Pér does not cover <per-how-per-uses-your-data-not-covered>`.


.. _per-connect-as-mcp-server-revoking:

Taking it away
==================================================

There is nothing Pér-specific to revoke, because there is nothing Pér-specific that was issued.

The connection is made with the same Amperity access the person already had. So it is removed the
same way all their access is removed, and removing it is not a separate job anyone has to remember.

* :ref:`Cutting the person off in Amperity <per-managing-access-revoking>` **cuts off the
  connection**, on the next check.
* **On a tenant that admits people individually**, removing their grant removes this too.
* **There is no list of connected clients** in Pér, and no way to end one connection while leaving
  the person's other access alone.


.. _per-connect-as-mcp-server-using:

Connecting a client
==================================================

Pér has no page for this. There is nothing to switch on and nothing to copy out of the product, so
setting it up happens entirely in the client you are connecting.

What you need:

* **A client that speaks the Model Context Protocol** over HTTP.
* **The address of Pér's endpoint.** Ask your Amperity representative for it — it is not shown
  anywhere in Pér.
* **A way to sign in.** Clients differ: some run a sign-in of their own, where you authorize the
  connection in a browser as you would any other sign-in; others take an Amperity access token you
  supply. Both end up with the same access — your own.

Once connected, the client works in one tenant by default and can be pointed at any other tenant
you are authorized for.

.. note::

   There is no reference for the endpoint yet. Until there is, your Amperity representative is the
   place to start, and they can tell you whether a particular client is one this has been used with.
