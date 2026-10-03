.. PENDING D3: this article ships when lookalikes are enabled for production tenants. At the pin
   they are off in every production stack.

.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        A lookalike takes a group of customers you already have and finds more who behave like them, with Pér's own account of how far the resemblance went.

.. meta::
    :content class=swiftype name=body data-type=text:
        A lookalike takes a group of customers you already have and finds more who behave like them, with Pér's own account of how far the resemblance went.

.. meta::
    :content class=swiftype name=title data-type=string:
        Lookalikes


.. _per-lookalikes:

==================================================
Lookalikes
==================================================

A lookalike takes a group of customers you already have and finds more who behave like them.

The group you can describe is almost never the whole group worth reaching. Expanding it is only
useful if you can tell how far the resemblance really went — which is why every lookalike carries
its own evidence rather than just a number of customers. It runs
:ref:`Understand → Recommend → Approve <per-customer-decision-loop>`: Pér expands, shows you what
it found, and waits.


.. _per-lookalikes-seed:

What a lookalike is built from
==================================================

It starts from an audience that already exists in your tenant — the seed — and expands outward
from it.

Starting from something you built deliberately is what keeps a lookalike accountable. Pér is not
translating a description into a query here; it is taking a group you already defined and asking
who else behaves like the people in it.

* **You ask for one in conversation.** There is no form. Ask Pér for a cohort, then ask it to find
  more customers like them.
* **The seed is an existing audience.** Pér names it and the definition behind it is read from
  your tenant, so the group expanded from is the group you meant.
* **Each seed customer finds its own matches**, rather than the group being averaged into one
  composite customer who does not exist. A match is always a match to real people.
* **The pool is customers with a profile.** Transactions are compared too, but a transaction has
  no profile to reach, so it is never returned as a match.
* **A tenant with nothing to compare says so.** Where no customer behaviour has been prepared for
  this kind of comparison, Pér says lookalikes cannot be built there rather than showing you an
  empty page.


.. _per-lookalikes-evidence:

How far the resemblance went
==================================================

Every lookalike carries the numbers behind it: what it drew on, how much of the seed it could use,
and how tightly the seed held together.

An expanded audience is easy to produce and hard to trust. The difference between a lookalike and
a longer list is being able to say how alike these people actually are — and being told when the
answer is "not very".

* **How coherent the seed was.** Pér scores whether your seed customers share one pattern before
  anything is expanded. A mixed group is fine, because each pattern finds its own matches. A group
  that shares no pattern at all is not expanded, because the result would be close to random.
* **What it drew on, and how much of it could be used** — the customers available to search, how
  many of your seed matched, and how many of those could be compared at all.
* **How many came back.** If you asked for a size, you get up to that many. If you did not, the
  expansion stops where the resemblance stops rather than filling a quota.
* **A quality floor you set.** Matches below it are dropped, even when that returns fewer
  customers than you asked for.
* **Who the group actually is.** Pér compares the expanded audience against your customer base and
  says what they have in common — and what they do not, which is as useful and more often ignored.

.. important::

   These scores describe behavioural similarity in the data as it stood, not what anyone will do
   next. A lookalike is not a prediction.

.. PENDING NC-056: the explainer on this page calls the figures block a "receipt". Rules §5 keeps
   that word out of this documentation, so the article names it by what it shows. Reported along
   with NC-007 as a product-vocabulary collision.


.. _per-lookalikes-saving:

Saving one
==================================================

Pér expands first and shows you the numbers. Saving is a separate step, and it asks.

A saved lookalike is permanent and other work refers to it afterwards, so the thing you approve
has to be the thing that gets saved — not Pér's summary of it.

* **The confirmation shows the numbers Pér actually found**, taken from the expansion itself
  rather than from anything Pér wrote in the conversation.
* **A save that no longer matches what you were shown is refused**, not quietly recomputed. Both
  the figures and the people behind them have to be the same ones.
* **A confirmation does not wait forever.** The card says how long it is good for, and an expired
  one means expanding again.

.. caution::

   A saved lookalike cannot be deleted. Nothing in Pér removes one, and later work refers to it by
   name. Save the one you mean.

.. PENDING NC-054: two places in the product describe this differently — one says a save can
   happen in the same turn as its own expansion with nobody having read a number, the other
   refuses exactly that and draws the confirmation card. The card is the later behavior and the
   one wired at the pin; this article documents it. Reported to engineering.

.. PENDING NC-055: that a saved lookalike cannot be deleted is code-true and deliberate, and it is
   a permanent constraint on a customer's own tenant. PO to confirm it is stated.


.. _per-lookalikes-activating:

Putting one to work
==================================================

A saved lookalike can be pushed into Amperity as a segment, or taken away as a file.

Expanding an audience is only half of it. The segment is how the work reaches everything else in
Amperity, and the page shows you exactly what it is about to create before you create it.

* **You choose what goes in** — the whole lookalike, seed included, or only the customers the
  expansion found.
* **The definition is on display.** The exact query the segment will use is shown, and you can
  copy it.
* **Pushing creates the segment in Amperity straight away.** The control says so, and it is the
  moment the work leaves Pér.
* **Pushing the same thing twice does not make two segments.** Pér checks what is already live
  first, and tells you when a push went through but it could not record that it had — so you do
  not retry and create a second one.
* **The page says where a lookalike is live**, and whether the segment it created still exists in
  Amperity.
* **It can be downloaded** as a file, either the expansion alone or the seed with it.


.. _per-lookalikes-privacy:

What Pér is given, and what it isn't
==================================================

Pér reasons about the shape of the group. It is not handed the people in it.

That distinction is worth stating because it is not obvious: an agent that can build an audience
sounds like an agent that has read everyone in it, and this one has not.

* **No query, no customer records, no membership list** comes back to Pér from building or reading
  a lookalike. What it gets is counts, a verdict and labels.
* **The page shows you what Pér cannot see**, which is why the definition and the download live
  there rather than in the conversation.


.. _per-lookalikes-using:

Using lookalikes
==================================================

**To build a lookalike**

#. Ask Pér for the group you want to start from, or name an audience you already have.
#. Ask it to find more customers like them.
#. Read what it found.

**To save one**

#. Read the numbers on the confirmation Pér shows you.
#. Approve it.

**To push one into Amperity**

#. Open the lookalike from **Lookalikes**.
#. Under **Activation-ready segment**, choose **Full lookalike** or **Lookalikes only**.
#. Click **Show SQL** if you want to read the definition first.
#. Click **Push to Amperity**.

**To download one**

#. Open the lookalike.
#. Download it, choosing the expansion alone or the seed with it.
