.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        How to run Stitch.

.. meta::
    :content class=swiftype name=body data-type=text:
        How to run Stitch.

.. meta::
    :content class=swiftype name=title data-type=string:
        Run Stitch

==================================================
Run Stitch
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-start
   :end-before: .. term-stitch-end


.. _stitch-add-tables:

Add tables to Stitch run
==================================================

.. include:: ../../amperity_reference/source/stitch_results.rst
   :start-after: .. stitch-run-select-tables-start
   :end-before: .. stitch-run-select-tables-end

.. stitch-add-tables-note-start

.. note:: Only tables with the **Make available to Stitch** setting enabled in the **Feed Editor** will be available in the **Stitch Settings** dialog box.

.. stitch-add-tables-note-end

**To add tables to the Stitch run**

.. include:: ../../amperity_reference/source/stitch_results.rst
   :start-after: .. stitch-run-select-tables-steps-start
   :end-before: .. stitch-run-select-tables-steps-end


.. _stitch-run:

Run Stitch
==================================================

.. include:: ../../amperity_reference/source/stitch_results.rst
   :start-after: .. stitch-run-about-start
   :end-before: .. stitch-run-about-end

.. stitch-run-start

Click the **Run** button on the **Stitch** page to manually start a Stitch run.

.. stitch-run-end

.. include:: ../../amperity_reference/source/stitch_results.rst
   :start-after: .. stitch-run-important-start
   :end-before: .. stitch-run-important-end


.. _stitch-configure:

Configure Stitch
==================================================

.. stitch-configure-start

A list of :doc:`Stitch configuration settings <configure_stitch>` is available from the **Stitch** page. These settings should not be changed until after your first Stitch run and the Stitch QA process has started.

It is not uncommon to make some configuration changes after analyzing how Amperity has processed your data. Common configuration changes include :doc:`adjusting how Amperity handles certain types of semantic tags <semantics>`, :ref:`changing the blocking strategy <configure-stitch-advanced-clustering-blocking>`, adjusting the :ref:`thresholds for match categories <configure-stitch-advanced-clustering-matching-thresholds>`, updating the :ref:`maximum number of allowed trivial duplicates <configure-stitch-advanced-trivial-duplicates>`.

In rare cases, adjustments may be made to how Amperity :ref:`applies the results of blocking <configure-stitch-advanced-clustering-matching-strategy>`.

.. stitch-configure-end
