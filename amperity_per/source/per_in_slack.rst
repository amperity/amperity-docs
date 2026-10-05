.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Pér answers questions in Slack channels. The surface reads only, never returns customer PII, and points changes back to the Pér web app.

.. meta::
    :content class=swiftype name=body data-type=text:
        Pér answers questions in Slack channels. The surface reads only, never returns customer PII, and points changes back to the Pér web app.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pér in Slack


.. _per-in-slack:

==================================================
Pér in Slack
==================================================

Pér answers questions in Slack, in the channel where the conversation is already happening.

Slack serves the :ref:`Understand <per-customer-decision-loop-understand>` stage of the customer
decision loop, and deliberately only that. It reads and cannot change anything, so inviting Pér into
a channel is not a choice about what it may change.


.. _per-in-slack-what:

What Pér can do in Slack
==================================================

Pér answers from the same customer data it works from everywhere else, and shows where the answer
came from.

An answer in a channel may be read by people who were not there when it was asked, so it has to
carry enough of its own evidence to be checked by someone who arrives late.

* **It looks things up.** What exists in your tenant, and what state it is in.
* **It can run a query** to answer a question that nothing on the shelf answers.
* **Every answer carries a footer** naming the tenant it answered for, what it used to answer, how
  long it took, and a link to continue in Pér.
* **It will not change anything.** See :ref:`Changes happen in Pér <per-in-slack-read-only>`.


.. _per-in-slack-read-only:

Changes happen in Pér
==================================================

Pér can answer in Slack. It cannot create, edit, delete, run or schedule anything in Amperity
from there.

* **Ask for a change and Pér says so in one sentence**, and tells you to make it in Pér. It does
  not draft the change or describe what approving it would look like.
* **It still does the reading.** Before pointing you to the web app it offers what it can answer
  there and then — the state of the object, what the change would touch.
* **Every answer links back into Pér.** The link is on the footer, put there by Pér rather than
  written into the answer.
* **The link carries no authority.** Following it signs you in as yourself, bounded by your own
  Amperity access. Someone in the channel with no access to that tenant gets a sign-in prompt, not
  a continuation. It is an address, not a key.
* **A thread in a private channel cannot be continued.** Pér records whether the channel was
  public and refuses to reopen a thread from one that was not. The answer in Slack is unaffected.

.. important::

   The approval boundary is not relaxed in Slack — it is moved out of reach. Pér reads your
   tenant's data on its own and does not change anything in Amperity on its own, and in Slack it
   cannot even propose a change. See
   :ref:`Approvals and write confirmations <per-approvals-boundary>`.


.. _per-in-slack-pii:

Slack never shows customer PII
==================================================

Values from columns tagged as PII come back redacted. Counts and other aggregates over them still
work.

A channel transcript is permanent, searchable, and visible to everyone in the channel, including
people who hold no Amperity access at all. That is why this surface cannot carry individual-level
PII, and nothing you can do in Slack changes that.

* **Slack queries run on one connection belonging to the workspace**, not on the Amperity sign-in
  of whoever asked. That connection is not given access to PII.
* **PII values come back as a dash.** The row is returned; the value is not.
* **Aggregates still work.** Counting the customers who have an email address, for example, is
  unaffected — Pér can count what it cannot read.
* **Pér says so rather than telling you to request access**, because PII access cannot be obtained
  from Slack at all.
* **Individual-level PII is available in the Pér web app**, where your own Amperity access
  applies. See :ref:`Accessing Pér <per-accessing-per>`.


.. _per-in-slack-where:

Where Pér answers
==================================================

Pér answers in channels, and only in channels. It answers what was addressed to it, and stays out of
everything else.

* **Mention Pér in a channel it is in, and it answers.**
* **Reply in a thread Pér is already part of, and it may answer** without being mentioned again.
  Whether a reply was meant for Pér is a judgement it makes each time.
* **A new channel message that does not mention Pér is left alone**, however relevant it looks.
* **Pér does not answer in direct messages or group messages.**
* **Pér does not answer in a channel shared with another Slack workspace**, and says so.
* **There is a daily limit on questions** — your own, your workspace's, and across every
  workspace Pér serves. Pér tells you when one has been reached.

.. PENDING NC-048: the Slack setup page tells an administrator that Pér will answer a direct
   message. It will not — direct messages and group messages are both refused. This article
   follows the behavior; the product copy is reported to engineering.

.. PENDING NC-050: the daily limit is real and user-visible, and no figure for it exists to
   publish. D5 holds consumption claims, so this says a limit exists and that Pér tells you when
   you reach it. PO to confirm.

.. note::

   On a tenant that uses managed access, Pér does not answer in Slack at all, because Slack
   carries no verified Amperity identity to check a grant against. It says so, and points you to
   the web app. See :ref:`Managing access to Pér <per-managing-access-modes>`.


.. _per-in-slack-using:

Using Pér in Slack
==================================================

**To ask Pér something in a channel**

#. Invite Pér to the channel, if it is not there already.
#. Mention it, and ask.

**To carry on in Pér**

#. Open the **continue in Pér** link on the answer's footer.
#. Sign in to Amperity if you are not already.

The thread opens in Pér as a conversation of your own, where you can take it further — and where
you can make changes. See :ref:`Chat history, sharing, and export <per-chat-history>`.


.. _per-in-slack-setup:

Setting up the Slack app
==================================================

One Slack workspace is connected to one Amperity tenant, and the connection is made from Pér.

The app answers as the tenant rather than as each person in the workspace, which is why it needs
an Amperity token of the tenant's own — and why that token can only read, and why creating it
takes someone who administers API keys.

* **It takes Amperity permission to administer API keys.** The relevant policies are
  **Allow API key administration** and **API Token Issuer**.
* **Amperity staff cannot do this for you**, on a customer's tenant.
* **Start the install from Pér, not from the Slack directory.** An install begun in Pér is claimed
  for your tenant as it finishes. One begun anywhere else establishes nobody as its owner, and the
  app stays inert until it is finished in Pér.
* **The Amperity token is stored encrypted and never shown.** It expires after 90 days, and
  renewing it is the same action that created it.
* **A new token does not revoke the old one.** The previous token keeps working until it is
  revoked in Amperity.
* **Pér will not store a Slack token that expires**, and refuses an install that came back without
  every permission it needs. In both cases nothing is stored and the install is started again.
* **Enterprise Grid organization-wide installs are not supported.** A standard Slack workspace is.

.. important::

   Moving a workspace to a different Amperity tenant, or claiming a different workspace for this
   one, is not a quiet change. Pér says what it affected, and anyone whose Slack account was
   associated with the old arrangement has to set that up again.

**To add Pér to a Slack workspace**

#. Open **Settings**.
#. Choose **App integrations**, then **Slack**.
#. Click **Generate token**, if no token is stored yet.
#. Click **Add to Slack** and complete the install.

**To renew the Amperity token**

#. Return to the same page.
#. Click **Rotate token**.
#. Revoke the previous token in Amperity if it should stop working.

See :ref:`App integrations <per-app-integrations>` for the rest of what is set up there.
