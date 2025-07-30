.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Users assigned to the DataGrid Administrator policy can configure Stitch settings.

.. meta::
    :content class=swiftype name=body data-type=text:
        Users assigned to the DataGrid Administrator policy can configure Stitch settings.

.. meta::
    :content class=swiftype name=title data-type=string:
        Stitch settings

==================================================
Stitch settings
==================================================

.. settings-about-start

Users assigned to the **DataGrid Administrator** policy can configure Stitch settings.

.. settings-about-end


.. _settings-rules:

Rules
==================================================

.. settings-rules-start

Rules define priority for deterministic identity resolution. Rules are evaluated in order (top-to-bottom) until a rule returns true.

.. settings-rules-end

.. settings-rules-grid-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: About rules
      :link: configure_stitch.html#rules

   .. grid-item-card:: Cluster records
      :link: configure_stitch.html#cluster-records

   .. grid-item-card:: Separate records
      :link: configure_stitch.html#separate-records

   .. grid-item-card:: Rules can be in any order
      :link: configure_stitch.html#rules-can-be-in-any-order

   .. grid-item-card:: Remaining records
      :link: configure_stitch.html#remaining-records

   .. grid-item-card:: Visual vs. Code views
      :link: configure_stitch.html#visual-vs-code-views

.. settings-rules-grid-end


.. _settings-general:

General settings
==================================================

.. settings-general-start

Modify general settings after analyzing data in your tenant to improve data quality and clustering results.

.. settings-general-end

.. settings-general-grid-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: Allowed empty tables
      :link: configure_stitch.html#allowed-empty-tables

   .. grid-item-card:: Days of recorded history
      :link: configure_stitch.html#days-of-recorded-history

   .. grid-item-card:: Force Stitch to run
      :link: configure_stitch.html#force-stitch-to-run

   .. grid-item-card:: Ignore jitter alerts
      :link: configure_stitch.html#ignore-jitter-alerts

   .. grid-item-card:: One-to-one Stitch
      :link: configure_stitch.html#one-to-one-stitch

   .. grid-item-card:: Skip unified changes
      :link: configure_stitch.html#skip-unified-changes

   .. grid-item-card:: Skip unified scores
      :link: configure_stitch.html#skip-unified-scores

   .. grid-item-card:: Stable IDs
      :link: configure_stitch.html#stable-ids

.. settings-general-grid-end


.. _settings-bad-values:

Bad values
==================================================

.. settings-bad-values-start

Bad values are ignored by Stitch during identity resolution.

.. settings-bad-values-end

.. settings-bad-values-grid-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: Rules for automatic detection
      :link: configure_stitch.html#rules-for-automatic-detection

   .. grid-item-card:: Values to ignore
      :link: configure_stitch.html#values-to-ignore

.. settings-bad-values-grid-end


.. _settings-advanced:

Advanced settings
==================================================

.. settings-advanced-start

Use advanced settings to modifiy specific behaviors and data preferences.

.. settings-advanced-end

.. settings-advanced-grid-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: Australian phone numbers
      :link: configure_stitch.html#australian-phone-numbers

   .. grid-item-card:: Blocking strategies
      :link: configure_stitch.html#test

   .. grid-item-card:: Business email addresses
      :link: configure_stitch.html#business-email-addresses

   .. grid-item-card:: Case-sensitive foreign keys
      :link: configure_stitch.html#test

   .. grid-item-card:: Clean foreign keys
      :link: configure_stitch.html#clean-foreign-keys

   .. grid-item-card:: Disable bad-values detection
      :link: configure_stitch.html#test

   .. grid-item-card:: Email addresses
      :link: configure_stitch.html#email-addresses

   .. grid-item-card:: Matching strategy
      :link: configure_stitch.html#matching-strategy

   .. grid-item-card:: Matching thresholds
      :link: configure_stitch.html#matching-thresholds

   .. grid-item-card:: Multiple preprocessing profiles
      :link: configure_stitch.html#multiple-preprocessing-profiles

   .. grid-item-card:: Normalize gender
      :link: configure_stitch.html#normalize-gender

   .. grid-item-card:: Staple
      :link: configure_stitch.html#staple

   .. grid-item-card:: Stitch reports
      :link: configure_stitch.html#stitch-reports

   .. grid-item-card:: Graph partitions
      :link: configure_stitch.html#graph-partitions

   .. grid-item-card:: Trivial duplicates
      :link: configure_stitch.html#trivial-duplicates

.. settings-advanced-grid-end
