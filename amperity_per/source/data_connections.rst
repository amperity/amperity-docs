.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Where you supply the connection details a destination needs that Amperity does not carry for it.

.. meta::
    :content class=swiftype name=body data-type=text:
        Where you supply the connection details a destination needs that Amperity does not carry for it.

.. meta::
    :content class=swiftype name=title data-type=string:
        Data connections


.. _per-data-connections:

==================================================
Data connections
==================================================

Data connections is where you supply the handful of connection details a destination needs that
Amperity does not carry for it.

Pér can read what a destination reports back about the work sent to it, which is how it can tell
you what became of a campaign rather than only what was sent. A destination missing the detail that
identifies your account cannot be reached at all, and the symptom is a destination that quietly has
nothing to say. This page is the one place that says which destinations are ready and lets you fill
in what is missing.


.. _per-data-connections-what-goes-in:

What this page is for
==================================================

Most of what Pér knows about a destination comes from Amperity. A few things do not, and those are
what you enter here.

Amperity knows which destinations your tenant has and how they are configured, and Pér reads all of
that. What Amperity does not hold is the identifier a destination's own reporting is addressed to —
there is no field for it in Amperity and no tool that can look it up, so the only way Pér can have
it is for a person to type it in.

* **Only one destination asks for anything here:**
  :ref:`Salesforce Marketing Cloud <per-connect-sfmc>`. Every other destination in your tenant
  works without a visit to this page, and does not appear on it.
* **The detail it asks for is the subdomain** that identifies your Salesforce account.
* **The list comes from Amperity**, and you can pull it again at any time. A tenant that has never
  pulled it sees an empty page that says so.
* **What you enter here survives.** Pulling the list again does not overwrite a value you set.


.. _per-data-connections-ready:

Knowing when a destination is ready
==================================================

The page marks each destination as ready or as still needing something — and "ready" means ready
for you, not ready for the tenant.

This is the one thing on the page that is easy to misread. Two separate things have to be true
before Pér can get a destination's reporting, and only one of them is tenant-wide:

* **The detail on this page has to be filled in.** Anyone can do it, once, for everyone.
* **You have to be signed in to the destination yourself.**
  :ref:`Salesforce Marketing Cloud <per-connect-sfmc>` is connected per person, not per tenant, so
  Pér reaches it as you.

.. important::

   A destination marked ready for you can be marked as still needing something for a colleague who
   has not signed in to it, and nothing is wrong when that happens. If a destination reads as not
   ready and the detail is plainly filled in, the missing half is your own sign-in.

A tenant that has connected more than one Salesforce Business Unit also chooses which one each
destination belongs to. A tenant with one does not see the choice, because there is nothing to
choose.


.. _per-data-connections-per-can-fill-it-in:

Letting Pér fill it in
==================================================

You do not have to come to this page at all. Pér can make the change itself, in conversation.

It is the same change either way, and it is held to the same standard: a detail Pér supplies
arrives as a :ref:`write confirmation <per-approvals-card>` naming the destination and the value,
and nothing is saved until you approve it. See
:ref:`Approvals and write confirmations <per-approvals>`.


.. _per-data-connections-using:

Working with data connections
==================================================

**To fill in what a destination needs**

#. Open **Settings** and choose **Data connections**.
#. Find the destination and enter its **TSSD subdomain**.
#. Click **Save**.

**To pull the destination list from Amperity again**

#. Open **Settings** and choose **Data connections**.
#. Click **Sync destination configuration**.

**To choose which Business Unit a destination belongs to**

#. Open **Settings** and choose **Data connections**.
#. Find the destination and choose its **Business Unit**.
#. Click **Save**.

The **Business Unit** choice appears only when your tenant has connected more than one.

Each destination is marked **Configured** or **Needs configuration**.
