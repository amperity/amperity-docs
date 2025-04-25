.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Stitch benchmarks are heuristic scores that define the expectations for the quality of customer profiles that are output by Stitch.

.. meta::
    :content class=swiftype name=body data-type=text:
        Stitch benchmarks are heuristic scores that define the expectations for the quality of customer profiles that are output by Stitch.

.. meta::
    :content class=swiftype name=title data-type=string:
        Stitch benchmarks

==================================================
About Stitch benchmarks
==================================================

.. stitch-benchmark-checks-start

Stitch collects data that your brand has provided to Amperity, runs, and then outputs a series of tables that contain the results. There is no "ground truth" dataset for your brand against which Amperity can compare Amperity IDs to validate identity, which prevents using standard error metrics to evaluate the quality of Stitch output.

A benchmark check is a heuristic that defines how often Amperity IDs are expected to meet a certain condition. For example, Amperity expects no more than 0.011% of your Amperity IDs to be associated with more than three given names.

Each benchmark check measures the percentage of Amperity IDs meeting its respective condition and compares the result against the optimal range. A benchmark check result can fall into the optimal range, above the optimal range, or far above the optimal range (high).

For example, it is expected that most, but not all, Amperity IDs should not have more than three given names. Is is possible for an Amperity ID to be correclty associated with more than three given names for valid reasons such as differences in data capture, the presence of typos, use of nicknames, name changes, and so on. A higher than expected rate of Amperity IDs (generally) associated with more than three given names may be an indicator that Stitch is clustering records together too aggressively.

.. stitch-benchmark-checks-end


.. _benchmarks-about-results:

About benchmark results
==================================================

.. TODO: Don't change the reference link name. It is shared with /reference/benchmarks.rst.

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-results-optimal-start
   :end-before: .. stitch-benchmark-results-optimal-end

.. image:: ../../images/mockup-stitch-benchmarks-tab.png
   :width: 600 px
   :alt: The Stitch benchmark status page.
   :align: center
   :class: no-scaled-link


.. _stitch-benchmark-results-optimal:

Optimal
---------------------------------------------------

.. TODO: Don't change the reference link name. It is shared with /reference/benchmarks.rst.

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-results-optimal-start
   :end-before: .. stitch-benchmark-results-optimal-end


.. _stitch-benchmark-results-above-optimal:

Above optimal range
---------------------------------------------------

.. TODO: Don't change the reference link name. It is shared with /reference/benchmarks.rst.

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-results-above-optimal-start
   :end-before: .. stitch-benchmark-results-above-optimal-end


.. _stitch-benchmark-results-high:

High
---------------------------------------------------

.. TODO: Don't change the reference link name. It is shared with /reference/benchmarks.rst.

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-results-high-start
   :end-before: .. stitch-benchmark-results-high-end


.. _benchmarks-review:

Review interpretations
==================================================

.. stitch-benchmark-cards-interpretations-start

Interpretations are provided by each benchmark check. They describe the result and provide an explanation of how to interpret it. For example:

"This score is above the typical range for most brands. A large percentage indicates that different postal codes are appearing in the same cluster, which indicates overclustering."

or:

"This score is far above the typical range for most brands. A large ratio indicates that a unique name and physical address combination appears in multiple clusters, which indicates underclustering."

When a benchmark score is above the optimal range or high it is recommended to review and grade a set of 10 example clusters, after which the benchmark check will make a series of recommendations that can lead to improved benchmark results.

.. stitch-benchmark-cards-interpretations-end


.. _benchmarks-grade:

Grade and calibrate
==================================================

.. stitch-benchmark-cards-grade-and-calibrate-start

All benchmark checks include example Amperity IDs that can be reviewed and graded. You should periodically review and grade examples for benchmark checks with high results. This helps ensure that Stitch is always building the highest quality customer profiles and can lead to incremental improvements over time.

Depending on the outcome of reviewing and grading benchmark check examples, a series of recommendations may be shown. Stitch configuration settings can be updated directly in the benchmark check.

.. stitch-benchmark-cards-grade-and-calibrate-end

.. TODO: Need mockup here that shows one of the review/grade pages.

.. stitch-benchmark-cards-grade-and-calibrate-howitworks-start

.. admonition:: How does Amperity choose which records are available for grading?

   Amperity uses `stratified random sampling <https://en.wikipedia.org/wiki/Stratified_randomization>`__ |ext_link| to select the examples. A fresh set of examples is generated during each Stitch run.

   #. All clusters (or groups of clusters) that are flagged by the check are collected.

      For example, with the **Amperity IDs with many surnames** check, all clusters with more than 3 surnames are collected.

   #. A rules-based approach is used to determine which of these clusters are likely to be "good" identity decisions and which are likely to be "poor" identity decisions.

      The percentage of clusters that are likely to be "good" identity decisions and the percentage likely to be "poor" identity decisions are identified.

      For example: 70% good, 30% poor.

   #. 10 examples are selected at random using the same rate of "good" and "poor" clusters.

      For example, 7 records will represent "good" identity decisions and 3 records will represent "poor".

      Amperity will make a recommendation for when to rate each example as "good", but cannot identify without input which examples in the random sample represent "good" or "poor" identity decisions.

.. stitch-benchmark-cards-grade-and-calibrate-howitworks-end


.. _benchmarks-revisit-benchmarks:

Revisit benchmarks
==================================================

.. benchmarks-revisit-benchmarks-start

You should revisit benchmark scores on a regular basis. The frequency is determined by the current state of your tenant. For example:

#. A newly-configured tenant should have benchmark scores reviewed after every Stitch run. Reduce the frequency when you are satisfied with each benchmark score.
#. Review benchmark scores after adding a data source that contains customer profile data that is used with identity resolution.
#. On a production tenants with consistent data sources you may revisit benchmark scores less frequently.

.. benchmarks-revisit-benchmarks-end


.. _stitch-benchmark-categories:

Benchmark categories
==================================================

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-categories-start
   :end-before: .. stitch-benchmark-categories-end


.. _stitch-benchmark-category-overclustering:

Overclustering
---------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-overcluster-start
   :end-before: .. term-overcluster-end

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-overclustering-start
   :end-before: .. stitch-benchmark-category-overclustering-end


.. _stitch-benchmark-category-many-given-names:

Many given names
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-many-given-names-start
   :end-before: .. stitch-benchmark-category-many-given-names-end


.. _stitch-benchmark-category-many-postal-codes:

Many postal codes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-many-postal-codes-start
   :end-before: .. stitch-benchmark-category-many-postal-codes-end


.. _stitch-benchmark-category-many-surnames:

Many surnames
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-many-surnames-start
   :end-before: .. stitch-benchmark-category-many-surnames-end


.. _stitch-benchmark-category-underclustering:

Underclustering
---------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-undercluster-start
   :end-before: .. term-undercluster-end

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-underclustering-start
   :end-before: .. stitch-benchmark-category-underclustering-end


.. _stitch-benchmark-category-shared-names-and-emails:

Shared names and emails
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-shared-names-and-emails-start
   :end-before: .. stitch-benchmark-category-shared-names-and-emails-end


.. _stitch-benchmark-category-shared-names-and-phones:

Shared names and phones
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-shared-names-and-phones-start
   :end-before: .. stitch-benchmark-category-shared-names-and-phones-end


.. _stitch-benchmark-category-shared-names-and-addresses:

Shared names and addresses
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_reference/source/benchmarks.rst
   :start-after: .. stitch-benchmark-category-shared-names-and-addresses-start
   :end-before: .. stitch-benchmark-category-shared-names-and-addresses-end
