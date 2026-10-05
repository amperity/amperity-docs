.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Pér answers questions in Microsoft Teams channels. The surface reads only, never returns customer PII, and points changes back to the Pér web app.

.. meta::
    :content class=swiftype name=body data-type=text:
        Pér answers questions in Microsoft Teams channels. The surface reads only, never returns customer PII, and points changes back to the Pér web app.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pér in Teams


.. _per-in-teams:

==================================================
Pér in Teams
==================================================

Pér answers questions in Microsoft Teams, in the channel where the conversation is already
happening.

Teams serves the :ref:`Understand <per-customer-decision-loop-understand>` stage of the customer
decision loop, and deliberately only that. It reads and cannot change anything, so adding Pér to a
channel is not a choice about what it may change.


.. _per-in-teams-what:

What Pér can do in Teams
==================================================

Pér answers from the same customer data it works from everywhere else, and shows where the answer
came from.

An answer in a channel may be read by people who were not there when it was asked, so it has to
carry enough of its own evidence to be checked by someone who arrives late.

* **It looks things up.** What exists in your tenant, and what state it is in.
* **It can run a query** to answer a question that nothing on the shelf answers.
* **Every answer carries a footer** naming the tenant it answered for, what it used to answer, and
  how long it took.
* **While it works, it posts a line and keeps that same line up to date**, rather than showing a
  typing indicator — Teams does not render one in a channel. The line appears only once there is
  real progress to report, so a quick answer leaves nothing stray behind.
* **It will not change anything.** See :ref:`Changes happen in Pér <per-in-teams-read-only>`.


.. _per-in-teams-read-only:

Changes happen in Pér
==================================================

Pér can answer in Teams. It cannot create, edit, delete, run or schedule anything in Amperity
from there.

* **Ask for a change and Pér says so in one sentence**, and tells you to make it in Pér. It does
  not draft the change or describe what approving it would look like.
* **It still does the reading.** Before pointing you to the web app it offers what it can answer
  there and then — the state of the object, what the change would touch.
* **It will not hand you a link.** Pér names the web app and leaves you to open it. Open Pér as
  you normally would, and ask again there.

.. important::

   The approval boundary is not relaxed in Teams — it is moved out of reach. Pér reads your
   tenant's data on its own and does not change anything in Amperity on its own, and in Teams it
   cannot even propose a change. See
   :ref:`Approvals and write confirmations <per-approvals-boundary>`.


.. _per-in-teams-pii:

Teams never shows customer PII
==================================================

Values from columns tagged as PII come back redacted. Counts and other aggregates over them still
work.

A channel transcript is permanent, searchable, and visible to everyone in the channel, including
people who hold no Amperity access at all. That is why this surface cannot carry individual-level
PII, and nothing you can do in Teams changes that.

* **Teams queries run on one connection belonging to the installation**, not on the Amperity
  sign-in of whoever asked. That connection is not given access to PII.
* **PII values come back as a dash.** The row is returned; the value is not.
* **Aggregates still work.** Counting the customers who have an email address, for example, is
  unaffected — Pér can count what it cannot read.
* **Pér says so rather than telling you to request access**, because PII access cannot be obtained
  from Teams at all.
* **Individual-level PII is available in the Pér web app**, where your own Amperity access
  applies. See :ref:`Accessing Pér <per-accessing-per>`.


.. _per-in-teams-where:

Where Pér answers
==================================================

Pér answers in channels, and only in channels. It answers what was addressed to it, and stays out of
everything else.

* **Mention Pér in a channel it is in, and it answers** — including a bare mention with no
  question, which it reads as asking whether it is there.
* **Reply in a thread Pér is already part of, and it may answer** without being mentioned again.
  Whether a reply was meant for Pér is a judgement it makes each time.
* **A new channel post that does not mention Pér is left alone**, however relevant it looks.
* **Pér does not answer in a personal chat or a group chat.**
* **There is a daily limit on questions** — your own, your organization's, and across every
  installation Pér serves. Pér tells you when one has been reached.

.. PENDING NC-048: a chat surface's setup page tells an administrator that Pér will answer a
   direct message. It will not — personal chats and group chats are both refused. This article
   follows the behavior; the product copy is reported to engineering.

.. PENDING NC-050: the daily limit is real and user-visible, and no figure for it exists to
   publish. D5 holds consumption claims, so this says a limit exists and that Pér tells you when
   you reach it. PO to confirm.

.. note::

   On a tenant that uses managed access, Pér does not answer in Teams at all, because Teams
   carries no verified Amperity identity to check a grant against. It says so, and points you to
   the web app. See :ref:`Managing access to Pér <per-managing-access-modes>`.


.. _per-in-teams-using:

Using Pér in Teams
==================================================

**To ask Pér something in a channel**

#. Add Pér to the channel, if it is not there already.
#. Mention it, and ask.

**To carry on in Pér**

#. Open Pér in your browser, and sign in to Amperity.
#. Ask again there.

What you asked in Teams does not travel with you, so a question you want to take further is worth
asking in Pér in its own right. See :ref:`Accessing Pér <per-accessing-per-web>`.


.. _per-in-teams-setup:

Setting up the Teams app
==================================================

One Microsoft 365 directory is connected to one Amperity tenant, and setup has three parts: your
Microsoft administrator's consent, the Teams app added to your organization, and one Amperity
token.

The app answers as the tenant rather than as each person in the directory, which is why it needs
an Amperity token of the tenant's own — and why that token can only read. The Microsoft half is
separate, and the person who can grant it is often not the person setting Pér up.

* **The Amperity half takes permission to administer API keys.** The relevant policies are
  **Allow API key administration** and **API Token Issuer**.
* **The Microsoft half takes a directory administrator** — in Microsoft's terms, Global
  Administrator, Privileged Role Administrator or Cloud Application Administrator. If that is not
  you, Pér gives you a link to send to the person it is.
* **Pér supplies the Teams app package** to download and hand to whoever manages your
  organization's app catalog.
* **A consent request is single-use and times out.** One left unfinished has to be started again
  from the same page.
* **A directory already claimed by another Amperity tenant cannot be taken over** from the setup
  screen.
* **The Amperity token is stored encrypted and never shown.** It expires after 90 days, and
  renewing it is the same action that created it.

.. note::

   Removing Pér from one team does not switch it off for the rest of your organization. Teams
   simply stops sending Pér that team's messages, and every other team is unaffected.

**To grant Microsoft consent**

#. Open **Settings**.
#. Choose **App integrations**, then **Microsoft Teams**.
#. Start the connection, and complete the Microsoft sign-in — or use
   **Send this link to your Microsoft admin** to pass it to someone who can.

**To add the Teams app to your organization**

#. On the same page, click **Download Teams app package**.
#. Give the package to whoever manages your organization's Teams app catalog.

**To connect the Amperity token**

#. Return to the same page once the app is installed.
#. Click **Generate token**.

The page shows where setup has got to: **Not started**, **Consent recorded**, **Added — not
connected**, or **Connected**.

See :ref:`App integrations <per-app-integrations>` for the rest of what is set up there.
