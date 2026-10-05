.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        The page that says which tenant Pér is working in, which destinations it knows about, and what is running right now.

.. meta::
    :content class=swiftype name=body data-type=text:
        The page that says which tenant Pér is working in, which destinations it knows about, and what is running right now.

.. meta::
    :content class=swiftype name=title data-type=string:
        System settings


.. _per-system-settings:

==================================================
System settings
==================================================

System is the page that tells you what Pér is looking at: which tenant, whose account, which
destinations, and whether anything is running right now.

Nearly everything else in Pér assumes you are in the right tenant with the right data in front of
you. When an answer looks wrong, this is the page that tells you whether those assumptions hold —
and it is the page worth having open when you ask your Amperity representative about something.

Nothing here changes how Pér reasons. It is a statement of what is, with one editable setting.


.. _per-system-settings-tenant:

Which tenant, and who you are
==================================================

The first section names the tenant Pér is working in and the account you are signed in as.

Pér can reach more than one tenant, and a question answered against the wrong one looks like a
wrong answer rather than a wrong tenant. This section is how you rule that out in a second, and it
is the quickest thing to check before anything else.

It also carries the identifiers Amperity uses for your tenant and your account. Those are not
things you need day to day; they are there so support has something exact to work from.

There is no permission on this page. Anyone who can reach Pér can open it.

.. note::

   Amperity usage is tracked in Amperity rather than in Pér. The **Settings** page carries an
   **Amps** tile that links out to it; see
   `About Amps consumption <../reference/amps.html>`__.

.. PENDING NC-016: pricing, consumption and amp-spend claims are on hold. This note names the link
   out and claims nothing about what Pér consumes.


.. _per-system-settings-customer-name:

What Pér calls your customers
==================================================

One setting on this page is editable: the word Pér uses for the people in your customer data.

Not every business calls them customers. If yours says guests, members, riders, or fans, setting it
here means Pér uses your word instead of a generic one.

* **It is a tenant setting**, so the word is the same for everyone.
* **Changing it is recorded in the** :ref:`Activity log <per-activity-log>`.

.. PENDING NC-042: the setting is editable and the change reaches the Activity log, both verified.
   Where the word then appears in the product could not be established for an ordinary tenant —
   every place it renders is gated behind a count that no application code writes. The article
   deliberately claims nothing about the effect. PO and engineering.


.. _per-system-settings-integrations:

Which destinations Pér knows about
==================================================

The second section lists the destinations Pér has picked up from Amperity, and when it last looked.

* **Each destination says when it was last synced.**
* **A destination only administrators may use is marked** **Admin only**.
* **The list is searchable** once there is more than one.

A destination that is here but still needs something from you is dealt with on
:ref:`Data connections <per-data-connections>`, not here. This section reports; that page is where
you fill things in.


.. _per-system-settings-diagnostics:

What is running right now
==================================================

The last section says whether Pér is working on a fresh set of recommendations at this moment.

A refresh takes a while, and knowing one is underway explains a Portfolio that is about to
change. When one is running, the section says so and when it started.

The rest of this section describes the server Pér is running on. It is there for Amperity support
rather than for you, and nothing in it changes what Pér does.

.. PENDING NC-040: the page shows raw internal identifiers and runtime details to every user. The
   article describes the rows and names no value, and does not tell readers to quote them.


.. _per-system-settings-using:

Working with System settings
==================================================

**To open System settings**

#. Open **Settings**.
#. Choose **System**.

**To change what Pér calls your customers**

#. Open **Settings** and choose **System**.
#. Beside **Customer**, click **Edit customer name**.
#. Type the word and click **Save**.

**To find a destination in the list**

#. Open **Settings** and choose **System**.
#. Under **Integration status**, type part of the destination's name.

The three sections are **Tenant configuration**, **Integration status** and **Diagnostics**.
