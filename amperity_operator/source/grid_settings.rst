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

Rules define priority for deterministic identity resolution. Rules are evaluated in order, from top-to-bottom, until a rule returns true.

.. settings-rules-end

.. settings-rules-grid-start

.. grid:: 1 1 2 2
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: About rules
      :link-type: ref
      :link: configure-stitch-rules

   .. grid-item-card:: Cluster records
      :link-type: ref
      :link: configure-stitch-rules-cluster

   .. grid-item-card:: Separate records
      :link-type: ref
      :link: configure-stitch-rules-separate

   .. grid-item-card:: Rules can be in any order
      :link-type: ref
      :link: configure-stitch-rules-order

   .. grid-item-card:: Remaining records
      :link-type: ref
      :link: configure-stitch-rules-remaining

   .. grid-item-card:: Visual vs. Code views
      :link-type: ref
      :link: configure-stitch-rules-code

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
      :link-type: ref
      :link: configure-stitch-general-allowed-empty-tables

   .. grid-item-card:: Days of recorded history
      :link-type: ref
      :link: configure-stitch-general-performance-history

   .. grid-item-card:: Force Stitch to run
      :link-type: ref
      :link: configure-stitch-general-stitch-force

   .. grid-item-card:: Ignore jitter alerts
      :link-type: ref
      :link: configure-stitch-general-stitch-ignore-jitter

   .. grid-item-card:: One-to-one Stitch
      :link-type: ref
      :link: configure-stitch-general-one-to-one

   .. grid-item-card:: Skip unified changes
      :link-type: ref
      :link: configure-stitch-general-stitch-skip-changes

   .. grid-item-card:: Skip unified scores
      :link-type: ref
      :link: configure-stitch-general-stitch-skip-scores

   .. grid-item-card:: Stable IDs
      :link-type: ref
      :link: configure-stitch-general-stitch-stable-id

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
      :link-type: ref
      :link: configure-stitch-bad-values-rules

   .. grid-item-card:: Values to ignore
      :link-type: ref
      :link: configure-stitch-bad-values-ignore

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
      :link-type: ref
      :link: configure-stitch-advanced-profile-australian-phone

   .. grid-item-card:: Blocking strategies
      :link-type: ref
      :link: configure-stitch-advanced-clustering-blocking

   .. grid-item-card:: Business email addresses
      :link-type: ref
      :link: configure-stitch-advanced-profile-business-email

   .. grid-item-card:: Case-sensitive foreign keys
      :link-type: ref
      :link: configure-stitch-advanced-clustering-case-sensitive

   .. grid-item-card:: Clean foreign keys
      :link-type: ref
      :link: configure-stitch-advanced-profile-clean-foreign-keys

   .. grid-item-card:: Disable bad-values detection
      :link-type: ref
      :link: configure-stitch-advanced-bad-values-disable

   .. grid-item-card:: Email addresses
      :link-type: ref
      :link: configure-stitch-advanced-profile-email

   .. grid-item-card:: Matching strategy
      :link-type: ref
      :link: configure-stitch-advanced-clustering-matching-strategy

   .. grid-item-card:: Matching thresholds
      :link-type: ref
      :link: configure-stitch-advanced-clustering-matching-thresholds

   .. grid-item-card:: Multiple preprocessing profiles
      :link-type: ref
      :link: configure-stitch-advanced-profile-multiple-profiles

   .. grid-item-card:: Normalize gender
      :link-type: ref
      :link: configure-stitch-advanced-profile-normalize-gender

   .. grid-item-card:: Staple
      :link-type: ref
      :link: configure-stitch-advanced-staple

   .. grid-item-card:: Stitch reports
      :link-type: ref
      :link: configure-stitch-advanced-reports

   .. grid-item-card:: Graph partitions
      :link-type: ref
      :link: configure-stitch-advanced-profile-supersized-clusters

   .. grid-item-card:: Trivial duplicates
      :link-type: ref
      :link: configure-stitch-advanced-trivial-duplicates

.. settings-advanced-grid-end
