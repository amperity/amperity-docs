.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        How an administrator decides who can get into Pér, and how they cut someone off. All of it happens in Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        How an administrator decides who can get into Pér, and how they cut someone off. All of it happens in Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Managing access to Pér


.. _per-managing-access:

==================================================
Managing access to Pér
==================================================

This is how an administrator decides who can get into Pér, and how they cut someone off.

Pér acts in a production tenant on a person's behalf, so who is allowed in is a real control rather
than a formality. Everything in this article is administered in Amperity rather than in Pér.


.. _per-managing-access-where:

Access is administered in Amperity
==================================================

Pér does not manage its own access. Amperity does, on the **Users** page, where the rest of your
user administration already happens.

That keeps one list of people and one place to change it. It also means an administrator does not
have to learn a second permission model to run Pér, and that someone removed from Amperity is
removed from Pér by the same act.

What Pér itself does with access is show you the current state. Its Settings page names the mode
your tenant uses and links out to Amperity; there is nothing to set there.

Who can do what:

* **A** :ref:`User Administrator <per-key-concepts-user-administrator>` **switches the tenant
  between the two modes and grants access to individuals.** Amperity refuses the change to anyone
  else, and says so.
* **Removing someone's access is deliberately easier than giving it.** Anyone who can edit users in
  Amperity can take a Pér grant away.

.. PENDING NC-008: amperity-docs already publishes a "Use Customer Data Agent" row in the policies
   reference, which may not match the two gates the product applies. PO and engineering.


.. _per-managing-access-modes:

Open and managed access
==================================================

A tenant admits people to Pér one of two ways, and the choice is the tenant's.

* **Open.** Anyone authorized for the tenant can enter Pér. Nothing has to be granted per person.
* **Managed.** Only people who have been granted access individually can enter.

Open matches a tenant whose Amperity access list is already the list of people who should be in Pér.
Managed matches one where it is not — a large tenant, a pilot, or a team rolling Pér out to some
people before others.

.. important::

   Neither mode decides what a person can **do**. Access is permission to enter; each person's
   existing Amperity permissions still govern everything that happens afterwards, exactly as they
   do elsewhere in the platform. Granting someone Pér access grants them nothing new in Amperity.

Someone refused under managed access is told that their Amperity administrator has not enabled Pér
access for them, so they know to ask rather than to retry.

See :ref:`Open access <per-key-concepts-open-access>` and
:ref:`Managed access <per-key-concepts-managed-access>`.


.. _per-managing-access-switching:

Turning on managed access
==================================================

Turning on managed access is a reviewed change, not a switch.

This prevents flipping a live tenant to managed access with nobody granted, which would lock
everyone out at once. So instead of flipping the switch, Amperity shows you the people who
currently have access, and the ones you keep are granted access as the mode starts. Everybody else
is shut out.

* **You review a list before anything changes**, and you are told how many people will keep access.
* **Returning to open access** restores entry for everyone authorized for the tenant.
* **The mode applies everywhere Pér can be reached**, not just at the front door: choosing a
  tenant, following a link into one, and opening a chat someone shared with you all consult the
  same check.

.. PARKED-LINK: connect_per_as_mcp_server.rst: restore "connecting Pér to another agent" to the
   list of surfaces that consult the same access check.


.. _per-managing-access-revoking:

Cutting someone off
==================================================

Pér has no revocation of its own. A person is cut off in Amperity.

* **Blocking a person in Amperity revokes all of their access to that tenant.** It overrides
  permissions they hold directly and permissions they inherit from an
  `SSO group mapping <../reference/sso.html#sso-map-groups-to-policies>`__.
* **A blocked person is refused at the door**, whatever credential they are holding. They are not
  left with a working session that happens to be ignored.
* **Blocking a parent tenant covers its sandboxes.** You do not have to block them one by one.
* **Blocking needs a user-administration permission**, and it has to be turned on for your tenant.
  If you cannot see it, your Amperity representative can tell you whether it is.
* **Removing a Pér grant is the narrower move**, and it is the right one when someone should keep
  their Amperity access and lose Pér.

.. important::

   Signing out is not the same as revoking access. If you need to be certain someone is out, block
   them in Amperity rather than relying on them having signed out.

   A block covers the Pér web app. It does not reach Slack or Microsoft Teams, because a turn on
   those surfaces runs on the installation's own connection rather than on the identity of
   whoever asked — Pér does not know which Amperity user is speaking. Who can ask there is
   controlled by who is in the channel. What a blocked person could still see is bounded: those
   surfaces never return individual-level PII and cannot change anything.

.. PENDING NC-036: how a signed-out session behaves in detail, and how long a block takes to show
   up in Pér, are deliberately not stated. PO.

.. PENDING NC-006: blocking a user is documented nowhere else in the Amperity documentation, so
   this section has no link target for it and describes it instead.

.. note::

   Removing someone's access to the tenant in Amperity also clears their Pér grant. If that part
   fails, Amperity tells you so and names the person, so the grant can be removed before their
   tenant access is restored.


.. _per-managing-access-enabling:

Before any of this: the tenant
==================================================

None of the above applies until the tenant itself is enabled for Pér.

A tenant that has not been enabled shows Pér to nobody, no matter what anyone's permissions say.
This is the most common reason for an organization seeing nothing at all, and it is not a
permission problem.

If nobody at your organization can reach Pér, ask your Amperity representative to confirm that your
tenant is enabled. See :ref:`Pér in Public Preview <per-public-preview-prerequisite>`.

.. PENDING NC-023: whether a customer can enable a tenant for Pér, or only Amperity can, is not
   settled. No control in the product sets it. This section deliberately does not say who does.


.. _per-managing-access-using:

Working with Pér access
==================================================

All of these happen in Amperity, on the `Users <../reference/users.html>`__ page. In Pér, the
**Settings** page shows the current mode under **Manage in Amperity** and links out to the same
place.

**To see which mode your tenant uses**

#. In Amperity, open **Users** and find the **Pér user access** section.

**To turn on managed access**

#. In the **Pér user access** section, click **Enable Managed mode**.
#. Review the people listed, who will keep access.
#. Click **Enable Managed mode** to confirm.

**To return to open access**

#. In the **Pér user access** section, click **Return to Open**.
#. Confirm.

**To give one person access**

#. `Edit the user <../reference/users.html#settings-users-edit>`__.
#. Select **Allow Pér access** and save.

This appears only while the tenant uses managed access.

**To take one person's access away**

#. Edit the user.
#. Clear **Allow Pér access** and save.

**To cut someone off entirely**

#. Edit the user.
#. Apply the **Block user** policy and save.

To remove their access to the tenant without blocking them, use
`Revoke tenant access <../reference/users.html#settings-users-revoke>`__ instead.
