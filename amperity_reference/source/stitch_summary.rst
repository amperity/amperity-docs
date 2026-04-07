.. https://docs.amperity.com/infrastructure/

:orphan:



.. meta::
    :description lang=en:
        A summary of identity resolution, including identity changes over time and how matching strategies combine to identify complex profiles.

.. meta::
    :content class=swiftype name=body data-type=text:
        A summary of identity resolution, including identity changes over time and how matching strategies combine to identify complex profiles.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Amperity cloud infrastructure

==================================================
About identity resolution
==================================================

.. stitch-summary-about-start

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-tab-start
   :end-before: .. term-stitch-tab-end

* :doc:`Summary tab <stitch_summary>`
* :doc:`Benchmark tab <stitch_benchmarks>`
* :doc:`Deduplication tab <stitch_deduplication>`

.. stitch-summary-about-end


.. _stitch-summary-tab:

Summary
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-identity-resolution-start
   :end-before: .. term-identity-resolution-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-summary-tab-start
   :end-before: .. term-stitch-summary-tab-end

.. image:: ../../images/mockup-stitch-summary-tab.png
   :width: 600 px
   :alt: The Summary tab for identity resolution
   :align: left
   :class: no-scaled-link

.. stitch-summary-tab-about-start

The **Summary** tab shows:

#. The number of unique customer profiles assigned an Amperity ID.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-amperity-id-start
      :end-before: .. term-amperity-id-end

#. The last time a full Stitch run completed.
#. A graph for viewing :ref:`how identity changes over time <stitch-summary-tab-identity-changes>`.
#. The percentage of profiles associated with :ref:`deterministic, probabilistic, and transitive matching strategies <stitch-summary-tab-matching-strategies>`.
#. The :ref:`complexity of customer profiles <stitch-summary-tab-identity-complexity>` based on the number of records in profiles, sorted by 1, 2, 3, 4, 5-10, 11-15, 16-20, 21-25, and 26+ records.

.. stitch-summary-tab-about-end


.. _stitch-summary-tab-identity-changes:

Identity changes over time
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-adaptive-identity-start
   :end-before: .. term-adaptive-identity-end

.. image:: ../../images/mockup-stitch-identity-changes.png
   :width: 600 px
   :alt: Identity changes over time
   :align: left
   :class: no-scaled-link

.. stitch-summary-tab-identity-changes-table-start

.. stitch-summary-tab-identity-changes-table-start

Changes, such as **Added**, **Merged**, or **Recognized**, are tracked for each identity graph over a 90-day time period.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - **Added**
     - A new Amperity ID was created and added to an identity graph.

       This type of change occurs when new customer records are added to Amperity.
   * - **Deleted**
     - An Amperity ID was deleted.

       This type of change occurs when records are removed from source data, such as after responding to a compliance processing request.
   * - **Merged**
     - Amperity IDs assigned to two or more profiles in the previous identity graph were combined into a single customer profile and assigned to an Amperity ID that existed in the previous identity graph.

       This type of change occurs when data clarifies connections between accounts that were not previously known to be related.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-stitch-rules-start
          :end-before: .. term-stitch-rules-end

   * - **Recognized**
     - Additional records were appended to a customer profile in an identity graph that was assigned an Amperity ID without a **Merge**, **Split**, or **Split + Merge** operation.

       This type of change occurs during real-time workflows.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-identity-recognition-start
          :end-before: .. term-identity-recognition-end

       Sometimes what is known is an app or website login that uses an email address or a phone number. Sometimes what is known is a durable identifier, such as a loyalty account ID. Sometimes what is known is a machine-issued digital identifier for Google Ads ID, a mobile device ID, or an advertising-related temporal identifier, such as a pixel ID.

   * - **Split**
     - Am Amperity ID assigned to a customer profile from the previous identity graph was split into two or more new customer profiles. New Amperity IDs were assigned to the new customer profiles.

       This type of change occurs when new data clarifies ownership of a shared source identifier, such as a device ID, email address, or phone number.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-stitch-rules-start
          :end-before: .. term-stitch-rules-end

   * - **Split + merged**
     - Multiple Amperity IDs from the previous identity graph were split from existing profiles, and then merged into new customer profiles and assigned new Amperity IDs.

       This type of change occurs when new data provides clarity to sparse records.

       .. include:: ../../shared/terms.rst
          :start-after: .. term-stitch-rules-start
          :end-before: .. term-stitch-rules-end

   * - **Unchanged**
     - An Amperity ID did not change.

.. stitch-summary-tab-identity-changes-table-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-record-pair-start
   :end-before: .. term-record-pair-end

.. image:: ../../images/mockup-stitch-identity-changes-hover.png
   :width: 600 px
   :alt: Hover over the graph to view detailed identity changes over time
   :align: left
   :class: no-scaled-link

.. stitch-summary-tab-identity-changes-hover-start

Hover over individual days in the chart that shows identity changes over time to view statistics for specific days.

.. stitch-summary-tab-identity-changes-hover-end

.. stitch-summary-tab-identity-changes-unchanged-start

.. admonition:: Identity changes are a very small percentage of total customer profiles.

   Enable the **Include unchanged** slider on the right side below the chart to view unchanged customer profiles. Unchanged customer profiles are shown in grey.

   .. image:: ../../images/mockup-stitch-identity-changes-hover-unchanged.png
      :width: 600 px
      :alt: Hover over the graph to view unchanged identities over time
      :align: left
      :class: no-scaled-link

.. stitch-summary-tab-identity-changes-unchanged-end


.. _stitch-summary-tab-matching-strategies:

Matching strategies
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-identity-graph-start
   :end-before: .. term-identity-graph-end

.. stitch-summary-tab-matching-strategies-context-start

An identity graph is built by comparing records, such as those with personally identifiable information (PII), transaction histories, shopping preferences, and loyalty account information, and clustering matching records into individual customer profiles. Each customer profile in an identity graph is assigned an Amperity ID.

Each identity graph is created from a combination of deterministic and probabilistic matching rules that define conditions for when records should be clustered or separated. The **Rules Editor** defines a heirarchy of deterministic and probabilistic matching strategies for each identity graph. Identity resolution attempts to match on a rule starting at the top of the list of rules in the rules heirarchy. The first rule that matches is scored.

* Deterministic matching strategies try to cluster records together when conditions are met. For example, a deterministic strategy for loyalty IDs tries to match records with the same loyalty ID.
* Probabilistic matching strategies try to separate records when conditions are met. For example, a probabilistic strategy for email addresses tries to separate records with different email addresses.

.. stitch-summary-tab-matching-strategies-context-end

.. stitch-summary-tab-matching-strategies-tries-start

.. admonition:: Why does Amperity "try" to match records?

   Amperity is different from traditional data management systems because Amperity does not force record assignment to an identity.

   Amperity uses deterministic and probabilistic matching strategies to define conditions that determine when records can or cannot match. All record pairs are scored. The scores represent the strength or weakness of the relationship between two records.

   * Exact matches are assigned minimum or maximum scores.
   * Fuzzy matches are assigned similarity scores.

   It may not be possible to satisfy all of the rules before applying a score. In these situations the default scoring model may assign a score, a transitive connection may be discovered, or edge analysis identifies records that should or should not cluster together. For example, it is possible for a customer profile in an identity graph to have more than one email because *other records* within the customer profile scored high enough to cluster record pairs *or* additional email addresses were discovered transitively.

   As the data your brand collects changes over time the data your brand makes available to Amperity changes. Amperity adapts and updates the identity graph to reflect the current state of your customer data.

.. stitch-summary-tab-matching-strategies-tries-end

.. stitch-summary-tab-matching-strategies-percentages-start

The **Summary** page, under **Matching strategies**, shows the percentage of total profiles in the identity graph that were discovered using :ref:`deterministic <stitch-summary-tab-matching-strategy-deterministic>`, :ref:`probabilistic <stitch-summary-tab-matching-strategy-probabilistic>`, and :ref:`transitive <stitch-summary-tab-matching-strategy-transitive>` matching.

.. stitch-summary-tab-matching-strategies-percentages-end

.. image:: ../../images/mockup-stitch-matching-strategies.png
   :width: 500 px
   :alt: Deterministic, probabilistic, and transitive matching
   :align: left
   :class: no-scaled-link

.. stitch-summary-tab-matching-strategies-percentages-context-start

Identity graphs can be configured to be more deterministic or less deterministic. Most often an identity graph uses a combination of deterministic and probabilistic rules for identity resolution. In addition to deterministic matching and probabilistic matching, identity resolution discovers transitive connections that lead to more accurate and more complete customer profiles.

.. stitch-summary-tab-matching-strategies-percentages-context-end


.. _stitch-summary-tab-matching-strategy-deterministic:

Deterministic matching
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-deterministic-connection-start
   :end-before: .. term-deterministic-connection-end

.. stitch-summary-tab-matching-strategy-deterministic-context-start

Deterministic matching strategies try to cluster records together when conditions are met. For example, a deterministic strategy for loyalty IDs tries to match records with the same loyalty ID.

.. stitch-summary-tab-matching-strategy-deterministic-context-end


.. _stitch-summary-tab-matching-strategy-probabilistic:

Probabilistic matching
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-probabilistic-connection-start
   :end-before: .. term-probabilistic-connection-end

.. stitch-summary-tab-matching-strategy-probabilistic-context-start

Probabilistic matching strategies try to separate records when conditions are met. For example, a probabilistic strategy for email addresses tries to separate records with different email addresses.

.. stitch-summary-tab-matching-strategy-probabilistic-context-end


.. _stitch-summary-tab-matching-strategy-transitive:

Transitive matching
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-transitive-connection-start
   :end-before: .. term-transitive-connection-end

.. stitch-summary-tab-matching-strategy-transitive-context-start

Transitive connections are discovered during identity resolution.

.. stitch-summary-tab-matching-strategy-transitive-context-end


.. _stitch-summary-tab-match-categories:

About match categories
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../shared/terms.rst
   :start-after: .. term-match-category-start
   :end-before: .. term-match-category-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-match-type-start
   :end-before: .. term-match-type-end


.. _stitch-summary-tab-scoring-record-pairs:

About scoring record pairs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. stitch-summary-tab-scoring-record-pairs-start

Stitch uses a scoring system to determine how strongly two records are matched:

#. Rules-based scoring
#. Default model scoring

.. stitch-summary-tab-scoring-record-pairs-end


.. _stitch-summary-tab-scoring-record-pairs-rules:

Rules-based scoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stitch-summary-tab-scoring-record-pairs-rules-start

Rules-based scoring relies on an ordered list of rules. Each rule defines a condition and an action to take when that condition is met. A condition is a set of criteria that determines if two records can match.

For example:

.. code-block:: none

   cluster records
     when values match for loyalty-id

   separate records
     when values differ for phone

   separate records
     when values differ for email

   cluster records
     when values approximately match for given-name
     and values approximately match for surname

Identity resolution compares two records by starting at the top of the list of rules, and then stepping through the list of rules until a condition is met. When a condition is met the corresponding action is taken. Identity resolution stops comparing two records after the first action is taken, even if additional conditions could be met.

For example, two records with different names, addresses, and phone numbers. Both records have the exact same loyalty ID.

#. Using the order in the example shown above both records will cluster together because of the exact match on loyalty ID.
#. If the "separate records when phone numbers are not the same" was the first rule, these records would be separated because values differ, *even if the loyalty ID is the same*.

The order of rules for rule-based scoring is important and should be carefully considered to ensure the identity graph built from these rules matches the desired business use cases for the identity graph.

Every record that meets the condition for a rule is given a pairwise connection score.

.. stitch-summary-tab-scoring-record-pairs-rules-end

.. term-pairwise-connection-score-start

Every pairwise connection score is two parts separated by a period.

The first part--the record pair score--correlates to the match category, which is a machine learning classifier applied during identity resolution to individual record pairs:

* 5 for exact matches
* 4 for excellent matches
* 3 for high matches
* 2 for moderate matches
* 1 for weak matches
* 0 for non-matches

Identity resolution uses the second part--the record pair strength--to show the quality of the record pair score. This value appears in the Stitch report as a two decimal number. A record pair strength by itself is not a direct indicator of the quality of a pairwise connection score.

.. term-pairwise-connection-score-end

.. stitch-summary-tab-scoring-record-pairs-rules-note-start

.. note:: Use the **Unified Scores** table to review pairwise comparison scoring for an identity graph *or* view scores from the **Pairwise connections** tab in the **Data Explorer**.

.. stitch-summary-tab-scoring-record-pairs-rules-note-end


.. _stitch-summary-tab-scoring-record-pairs-default:

Default model scoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stitch-summary-tab-scoring-record-pairs-default-start

Default model scoring is applied to all records that did not match a rules-based condition. Default model scoring has the following options:

#. **Amperity AI**

.. term-stitch-start

Stitch uses patented algorithms to process massive volumes of data and discovers the hidden connections in your customer profiles that identify unique individuals. Stitch an identity graph in which every unique customer profile is assigned an Amperity ID.

.. term-stitch-end

Use **Amperity AI** model scoring to build an identity graph with deterministic *and* probabilistic matches, along with opportunities to discover transitive connections that lead to more accurate and more complete customer profiles.

A hybrid model--the most common approach--uses a mixture of exact matching and fuzzy matching with cluster and separation rules to precisely tune scoring for an identity graph. Records are matched deterministically *and* probabilistically. Transitive connections are discovered. The identity graph has accurate and complete customer profiles.



A hybrid model--the most common approach--is to use a mixture of exact matching and fuzzy matching for deterministic *and* probabilistic rules to precisely tune scoring for an identity graph. A hybrid model also creates opportunities to discover transitive connections that lead to more accurate and more complete customer profiles.



**No matching model**

.. term-no-matching-model-start

Records are matched only on cluster rules. All records unable to match on a clustering rule are not included in a cluster.

.. term-no-matching-model-end

Use **No matching model** to build a purely deterministic identity graph that builds customer profiles when cluster rules match. Scores are applied only when records match on a cluster rule.


.. _stitch-summary-tab-identity-complexity:

Identity complexity
--------------------------------------------------

.. stitch-summary-tab-identity-complexity-start

Each identity graph is a combination of deterministic, probabilistic, and transitive connections. As the data your brand collects changes the data your brand makes available to Amperity changes. Amperity adapts and updates the customer profiles and keychains within in the identity graph to relect the current state of your customer data.

.. stitch-summary-tab-identity-complexity-end

.. image:: ../../images/mockup-stitch-identity-complexity.png
   :width: 600 px
   :alt: Review the complexity of the identity graph broken down by number of records in profiles
   :align: left
   :class: no-scaled-link

.. stitch-summary-tab-identity-complexity-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - **Deterministic only**
     - Customer profiles built using only deterministic matching.

   * - **Probabilistic only**
     - Customer profiles built using only probabilistic matching.

   * - **Deterministic and probabilistic**
     - Customer profiles built using a combination of deterministic and probabilistic matching.

   * - **Deterministic and transitive**
     - Customer profiles built using a combination of deterministic and transitive matching.

   * - **Probabilistic and transitive**
     - Customer profiles built using a combination of probabilistic and transitive matching.

   * - **All strategies**
     - Customer profiles built using a combination of deterministic, probabilistic, and transitive matching

.. stitch-summary-tab-identity-complexity-table-end


.. _stitch-summary-howtos:

How-tos
==================================================

.. stitch-summary-howtos-start

xxxxx

.. stitch-summary-howtos-end


Explore semantics
Open settings
View identity complexity
View matching strategies
View identity changes over time


.. _stitch-summary-howto-xxxxx:

xxxxx
--------------------------------------------------

.. stitch-summary-howto-xxxxx-start

xxxxx

.. stitch-summary-howto-xxxxx-end

**To xxxxx**

.. stitch-summary-howto-xxxxx-steps-start

xxxxx

.. stitch-summary-howto-xxxxx-steps-end
