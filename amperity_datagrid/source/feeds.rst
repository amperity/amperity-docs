.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use feeds to define the schema for any data source that is pulled to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use feeds to define the schema for any data source that is pulled to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure feeds

==================================================
Configure feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end


.. _feeds-set-primary-key:

Set the primary key
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-primary-key-start
   :end-before: .. term-primary-key-end

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-configure-set-primary-key-start
   :end-before: .. feeds-configure-set-primary-key-end

**To set the primary key**

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-configure-set-primary-key-steps-start
   :end-before: .. feeds-configure-set-primary-key-steps-end

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-records-mismatch-tip-start
   :end-before: .. domain-tables-records-mismatch-tip-end


.. _feeds-apply-semantic-tags:

Apply semantic tags
==================================================

.. feeds-apply-semantic-tags-start

Semantic tags must be defined for every feed that will provide profile data to Stitch. This ensures that data from rich sources of profile data are brought into Amperity in a consistent manner, which improves the outcome of the Stitch process.

Each group of semantic tags--:ref:`customer profile semantic tags <semantics-profile>`, :ref:`interaction semantic tags <semantics-profile>`, and :ref:`key semantic tags <semantics-profile>`--allow for a range of options.

.. feeds-apply-semantic-tags-end


.. _feeds-apply-semantic-tags-profile:

Customer profiles
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-start
   :end-before: .. term-pii-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pii-semantic-start
   :end-before: .. term-pii-semantic-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-profile-start
   :end-before: .. semantics-profile-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-profile-table-about-start
   :end-before: .. semantics-profile-table-about-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-profile-table-start
   :end-before: .. semantics-profile-table-end


.. _feeds-apply-semantic-tags-keys:

Keys
--------------------------------------------------

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-keys-start
   :end-before: .. semantics-keys-end

.. feeds-apply-semantic-tags-keys-table-about-start

The following table describes the keys that are used to tag data:

.. feeds-apply-semantic-tags-keys-table-about-end

.. feeds-apply-semantic-tags-keys-table-start

.. list-table::
   :widths: 175 25 25 350
   :header-rows: 1

   * - Semantic Name
     - Datatype
     - Icon
     - Description

   * - **bk-[label]**
     - String
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-bk-start
          :end-before: .. term-bk-end

       .. tip:: A foreign key can be :ref:`labeled as a blocking key <semantics-key-blocking-label-fk>` to force Stitch to score all records that match on the blocking key, but without assigning them a 5.0 score.

   * - **ck**
     - String
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-ck-start
          :end-before: .. term-ck-end

       .. include:: ../../amperity_datagrid/source/semantics.rst
          :start-after: .. semantics-key-customer-tip-start
          :end-before: .. semantics-key-customer-tip-end

   * - **fk-[namespace]**
     - String
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-foreign-key-start
          :end-before: .. term-foreign-key-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-fk-start
          :end-before: .. term-fk-end

       .. include:: ../../amperity_datagrid/source/semantics.rst
          :start-after: .. semantics-key-foreign-context-start
          :end-before: .. semantics-key-foreign-context-end

       .. include:: ../../amperity_datagrid/source/semantics.rst
          :start-after: .. semantics-key-foreign-tip-start
          :end-before: .. semantics-key-foreign-tip-end

       .. include:: ../../amperity_datagrid/source/semantics.rst
          :start-after: .. semantics-key-foreign-note-trivial-duplicates-start
          :end-before: .. semantics-key-foreign-note-trivial-duplicates-end

   * - **pk**
     - String
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-primary-key-start
          :end-before: .. term-primary-key-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-pk-start
          :end-before: .. term-pk-end

       .. include:: ../../amperity_datagrid/source/semantics.rst
          :start-after: .. semantics-key-primary-tip-start
          :end-before: .. semantics-key-primary-tip-end

   * - **sk**
     - String
     - 
     - .. include:: ../../shared/terms.rst
          :start-after: .. term-separation-key-start
          :end-before: .. term-separation-key-end

       .. include:: ../../shared/terms.rst
          :start-after: .. term-sk-start
          :end-before: .. term-sk-end

       .. include:: ../../amperity_datagrid/source/semantics.rst
          :start-after: .. semantics-key-separation-important-start
          :end-before: .. semantics-key-separation-important-end

.. feeds-apply-semantic-tags-keys-table-end


.. _feeds-apply-semantic-tags-product-catalogs:

Product catalogs
--------------------------------------------------

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-product-catalog-start
   :end-before: .. semantics-product-catalog-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-product-catalog-table-with-ampiq-start
   :end-before: .. term-unified-product-catalog-table-with-ampiq-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-product-catalog-table-about-start
   :end-before: .. semantics-product-catalog-table-about-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-product-catalog-table-start
   :end-before: .. semantics-product-catalog-table-end


.. _feeds-apply-semantic-tags-itemized:

Transactions
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-itemized-transactions-semantic-start
   :end-before: .. term-itemized-transactions-semantic-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-itemized-transactions-start
   :end-before: .. semantics-itemized-transactions-end

.. feeds-apply-semantic-tags-itemized-important-start

.. important:: This collection of semantic tags is used by Amperity to build the :doc:`Unified Itemized Transactions table <table_unified_itemized_transactions>`. Each semantic tag is directly associated with a column in that table. For example, values identified by the **is-cancellation**, **item-cost**, and **order-id** semantic tags are added to the **is_cancellation**, **item_cost**, and **order_id** columns, respectively.

   .. include:: ../../shared/terms.rst
      :start-after: .. term-unified-itemized-transactions-table-start
      :end-before: .. term-unified-itemized-transactions-table-end

   Carefully review the data in the **Unified Itemized Transactions** table, including column values that are calculated from values in other columns in this table or the :doc:`Unified Transactions table <table_unified_transactions>`, to verify their accuracy and to ensure that associated semantic tags have been applied correctly.

.. feeds-apply-semantic-tags-itemized-important-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-itemized-transactions-table-about-start
   :end-before: .. semantics-itemized-transactions-table-about-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-itemized-transactions-table-start
   :end-before: .. semantics-itemized-transactions-table-end


.. _feeds-select-last-updated:

Select last updated field
==================================================

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-set-last-updated-field-start
   :end-before: .. feeds-set-last-updated-field-end

**To set the last updated field**

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-set-last-updated-field-steps-start
   :end-before: .. feeds-set-last-updated-field-steps-end

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-records-mismatch-tip-start
   :end-before: .. domain-tables-records-mismatch-tip-end


.. _feeds-make-available-to-stitch:

Make available to Stitch
==================================================

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-make-available-to-stitch-start
   :end-before: .. feeds-make-available-to-stitch-end

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-make-available-to-stitch-tip-start
   :end-before: .. feeds-make-available-to-stitch-tip-end

**To make data available to Stitch**

.. include:: ../../amperity_reference/source/feeds.rst
   :start-after: .. feeds-make-available-to-stitch-steps-start
   :end-before: .. feeds-make-available-to-stitch-steps-end
