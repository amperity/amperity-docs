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

.. idres-summary-about-start

xxxxx:

* :ref:`Summary tab <idres-summary-tab>`
* :ref:`Benchmark tab <idres-benchmark-tab>`
* :ref:`Deduplication tab <idres-deduplication-tab>`

.. idres-summary-about-end


.. _idres-summary-tab:

Summary
==================================================

.. idres-summary-tab-start

xxxxx

.. idres-summary-tab-end

.. image:: ../../images/mockup-idres-summary-tab.png
   :width: 600 px
   :alt: The Summary tab for identity resolution
   :align: left
   :class: no-scaled-link

.. idres-summary-tab-about-start

The **Summary** tab shows

* The number of unique customer profiles assigned an Amperity ID
* The last time a full Stitch run completed
* A graph for viewing how identity resolution affects customer profiles over time
* The percentage of profiles associated with deterministic, probabilistic, and transitive matching strategies
* The complexity of customer profiles based on the number of records in profiles, sorted by 1, 2, 3, 4, 5-10, 11-15, 16-20, 21-25, and 26+ records

.. idres-summary-tab-about-end


.. _idres-summary-tab-identity-changes:

Identity changes over time
--------------------------------------------------

.. idres-summary-tab-identity-changes-start

<about>

.. idres-summary-tab-identity-changes-end

.. image:: ../../images/mockup-idres-identity-changes.png
   :width: 600 px
   :alt: Identity changes over time
   :align: left
   :class: no-scaled-link

.. idres-summary-tab-identity-changes-table-start

<intro>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - **Added**
     - description
   * - **Deleted**
     - description
   * - **Merged**
     - description
   * - **Recognized**
     - description
   * - **Split**
     - description
   * - **Split + merged**
     - description
   * - **Unchanged**
     - description

.. idres-summary-tab-identity-changes-table-end

.. idres-summary-tab-identity-changes-context-start

<context>

.. idres-summary-tab-identity-changes-context-end

.. image:: ../../images/mockup-idres-identity-changes-hover.png
   :width: 600 px
   :alt: Hover over the graph to view detailed dentity changes over time
   :align: left
   :class: no-scaled-link


.. _idres-summary-tab-matching-strategies:

Matching strategies
--------------------------------------------------

.. idres-summary-tab-matching-strategies-start

xxxxx

* :ref:`Deterministic matching <idres-summary-tab-matching-strategy-deterministic>`
* :ref:`Probabilistic matching <idres-summary-tab-matching-strategy-probabilistic>`
* :ref:`Transitive matching <idres-summary-tab-matching-strategy-transitive>`

.. idres-summary-tab-matching-strategies-end


.. _idres-summary-tab-matching-strategy-deterministic:

Deterministic matching
++++++++++++++++++++++++++++++++++++++++++++++++++

<term>

.. image:: ../../images/mockup-idres-matching-deterministic.png
   :width: 200 px
   :alt: Deterministic matching
   :align: left
   :class: no-scaled-link

.. idres-summary-tab-matching-strategy-deterministic-context-start

<context>

.. idres-summary-tab-matching-strategy-deterministic-context-end


.. _idres-summary-tab-matching-strategy-probabilistic:

Probabilistic matching
++++++++++++++++++++++++++++++++++++++++++++++++++

<term>

.. image:: ../../images/mockup-idres-matching-probabilistic.png
   :width: 200 px
   :alt: Probabilistic matching
   :align: left
   :class: no-scaled-link

.. idres-summary-tab-matching-strategy-probabilistic-context-start

<context>

.. idres-summary-tab-matching-strategy-probabilistic-context-end


.. _idres-summary-tab-matching-strategy-transitive:

Transitive matching
++++++++++++++++++++++++++++++++++++++++++++++++++

<term>

.. image:: ../../images/mockup-idres-matching-transitive.png
   :width: 200 px
   :alt: Transitive matching
   :align: left
   :class: no-scaled-link

.. idres-summary-tab-matching-strategy-transitive-context-start

<context>

.. idres-summary-tab-matching-strategy-transitive-context-end


.. _idres-summary-tab-identity-complexity:

Identity complexity
--------------------------------------------------

.. idres-summary-tab-identity-complexity-start

xxxxx

.. idres-summary-tab-identity-complexity-end

.. image:: ../../images/mockup-idres-identity-complexity.png
   :width: 600 px
   :alt: Review the complexity of the identity graph broken down by number of records in profiles
   :align: left
   :class: no-scaled-link

.. idres-summary-tab-identity-complexity-table-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - **Deterministic only**
     - description

   * - **Probabilistic only**
     - description

   * - **Deterministic and probabilistic**
     - description

   * - **Deterministic and transitive**
     - description

   * - **Probabilistic and transitive**
     - description

   * - **All strategies**
     - description

.. idres-summary-tab-identity-complexity-table-end


.. _idres-benchmark-tab:

Benchmark
==================================================

.. idres-benchmark-tab-about-start

xxxxx

.. idres-benchmark-tab-about-end



.. _idres-deduplication-tab:

Deduplication
==================================================

.. idres-deduplication-tab-about-start

xxxxx

.. idres-deduplication-tab-about-end

