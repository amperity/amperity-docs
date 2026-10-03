.. PENDING D3: this article ships when use-case feasibility is enabled for production tenants. At
   the pin it is limited to one family of tenants.

.. https://docs.amperity.com/per/


.. meta::
    :description lang=en:
        Give Pér the list of things your team wants to do with customer data, and it assesses which of them your tenant can support today.

.. meta::
    :content class=swiftype name=body data-type=text:
        Give Pér the list of things your team wants to do with customer data, and it assesses which of them your tenant can support today.

.. meta::
    :content class=swiftype name=title data-type=string:
        Use-case feasibility


.. _per-use-case-feasibility:

==================================================
Use-case feasibility
==================================================

Give Pér the list of things your team wants to do with customer data, and it works through them
one by one against your tenant as it actually is.

The expensive version of this conversation is a quarter of meetings and a spreadsheet nobody
trusts. The cheap version is Pér reading your tenant and grading the list against what is really
there. It is the :ref:`Understand <per-customer-decision-loop-understand>` stage done at the scale
of a roadmap, and it ends in :ref:`Recommend <per-customer-decision-loop-recommend>` — not a
verdict list, but an order to do things in.


.. _per-use-case-feasibility-what:

What a feasibility run tells you
==================================================

Each use case comes back with a verdict, a score, an estimate of its impact, and where it belongs
in a sequence.

A list of verdicts is less useful than it looks: everything blocked for the same missing thing is
really one piece of work. So the run groups what it found into an order — what has to exist first,
what you could ship next week, and what belongs further out.

* **Every use case gets a verdict**: ready, partial or blocked.
* **It is graded against your tenant**, through the same Amperity reads Pér uses everywhere else,
  rather than against a generic picture of what a tenant usually has.
* **Pér also surfaces opportunities that were not on your list**, where your data supports
  something nobody asked for.
* **The results are sequenced**: foundations that unblock other things, quick wins that are ready
  or nearly ready, and a roadmap for the rest.

.. note::

   A verdict is Pér's assessment, not a measurement. It is a careful reading of your tenant by
   something that read your tenant — worth taking seriously, and worth checking where it matters.
   See :ref:`Correcting what Pér concluded <per-use-case-feasibility-refine>`.

.. PENDING NC-052: the reads are real, and the verdict, score and impact rating are Pér's
   judgement over them against a standard catalogue. The article frames every one as an
   assessment. PO to confirm the framing.


.. _per-use-case-feasibility-input:

Giving Pér your list
==================================================

You upload the list, Pér shows you how it read it, and you correct that before anything runs.

Most use-case lists are a spreadsheet somebody maintains, with columns named whatever made sense
at the time. The mapping step is where a misreading is cheap to fix — afterwards it would mean
grading the wrong column for every row in the file.

* **The list is a spreadsheet or a CSV.**
* **Pér reads it and shows you what it made of each column** — which one holds the use case's
  name, its description, the line of business, the fields it refers to, and who asked for it.
* **You change any of that before starting.** The mapping you confirm is what the run uses.
* **A confirmed mapping is used once.** Starting another run means uploading the list again.


.. _per-use-case-feasibility-results:

Reading the results
==================================================

The results page opens with what Pér concluded overall, then shows the sequence, then every use
case.

It is arranged that way on purpose: the counts tell you the shape of the problem, the sequence
tells you what to do about it, and the table is for the argument you are going to have about one
particular row.

* **A summary and a set of counts** — how many use cases, how many ready, partial and blocked,
  how many are missing a source, and how many are quick wins.
* **The sequence**: **Foundation** first, because other things depend on it; then **Quick wins**,
  ready or nearly so; then **Roadmap**.
* **A table of every use case**, with its verdict, score, impact and classification, which you can
  filter and sort.
* **Opportunities Pér found that were not on your list.**
* **The table exports** as a CSV, for the conversation that happens outside Pér.


.. _per-use-case-feasibility-refine:

Correcting what Pér concluded
==================================================

You can change what a run concluded by saying so in the chat beside the results.

Pér read the data; you know the business. A verdict that is wrong because Pér could not know
something should be correctable in a sentence rather than by re-running everything — and the
corrected version is what everyone else sees afterwards.

* **Ask in the chat beside the results.** You can correct a use case, change its classification,
  add one Pér did not have, or dismiss an opportunity.
* **Each change waits for your approval.** A correction edits a saved analysis, so it arrives as a
  confirmation naming exactly what will change, the same as anywhere else in Pér. See
  :ref:`Approvals and write confirmations <per-approvals>`.
* **Corrections only apply to the run you are looking at.** Pér will not change a different
  analysis from this conversation, because nothing in a use case's identity says which run it
  belongs to and a wrong guess would be invisible.
* **The page updates as you go.**


.. _per-use-case-feasibility-limits:

One run at a time
==================================================

A tenant runs one feasibility analysis at a time.

A run reads a great deal of the tenant, and two at once would compete for the same answers. The
limit is per tenant rather than per person, which is the part worth knowing if a colleague starts
one first.

* **While a run is going, nobody in the tenant can start another.** The page says one is in
  progress and offers to show it to you.
* **You can cancel a run.**
* **A run interrupted by something on Pér's side is reported as failed** rather than left looking
  busy forever.
* **A tenant that is not set up for feasibility analysis is told so**, and told to ask an Amperity
  administrator to set up its data connection.

.. PENDING NC-053: the refusal names a "data connection" that nothing else in the product or the
   documentation defines, and it is not the Data connections settings page. Engineering to say
   what a customer should understand by it.


.. _per-use-case-feasibility-using:

Using feasibility
==================================================

**To run a feasibility analysis**

#. Open **Use-Case Feasibility**.
#. Click **Upload use-case list** and choose your file.
#. Check how Pér has read each column, and correct anything it has wrong.
#. Start the run.

Pér works through the list and the page fills in as it goes.

**To correct a use case**

#. Open the run.
#. In the chat beside the results, say what is wrong and what it should be.
#. Read the confirmation Pér shows you, and approve it.

**To export the results**

#. Open the run.
#. Click **Export CSV**.
