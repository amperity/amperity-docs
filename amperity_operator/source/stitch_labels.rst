.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Apply labels to help prevent over- and under-clustering of Stitch results.

.. meta::
    :content class=swiftype name=body data-type=text:
        Apply labels to help prevent over- and under-clustering of Stitch results.

.. meta::
    :content class=swiftype name=title data-type=string:
        Stitch labels

==================================================
Stitch labels
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-stitch-labels-start
   :end-before: .. term-stitch-labels-end

**Over-clustering**
   .. include:: ../../shared/terms.rst
      :start-after: .. term-overcluster-start
      :end-before: .. term-overcluster-end

   .. include:: ../../shared/terms.rst
      :start-after: .. term-precision-start
      :end-before: .. term-precision-end

**Under-clustering**
   .. include:: ../../shared/terms.rst
      :start-after: .. term-undercluster-start
      :end-before: .. term-undercluster-end

   .. include:: ../../shared/terms.rst
      :start-after: .. term-recall-start
      :end-before: .. term-recall-end


.. _stitch-labels-table-schema:

Table schema
==================================================

.. stitch-labels-table-schema-start

The schema for a Stitch labels table is a CSV file. It must contain the following fields:

* **row_id** A sequential ordering of rows in the Stitch labels table, starting at 1.
* **label_id** A string that must match the label_id for another row in the Stitch labels table. This string does not need to be unique, but it must be unique enough to allow the **label_id** / **partition_id** pairs to be uniquely identifiable within the table.
* **partition_id** An integer (1 or 2) that identifies if two rows in the Stitch labels table should match (1 and 1) or be split (1 and 2).
* **datasource** The name of the domain table from which the customer record originated. 
* **semantic** The semantic tag associated with the value. The recommended semantic is **pk**, as this is the Amperity ID for individual customer records. The **pk** value must be unique within the Stitch labels table.

  .. note:: You may use other semantic values for Stitch labels, such as **email** or a foreign key, as long as the :ref:`associated blocking strategy is configured for Stitch <configure-stitch-advanced-clustering-blocking>`.

     #. The **:email** blocking strategy must be configured before using **email** as a semantic value.
     #. The **:fk** blocking strategy must be configured before using a foreign key as a semantic value.

     These blocking strategies are configured by default, but should be verified before using email addresses or foreign keys as semantic values for Stitch labels.
* **value** The value for the field in the domain table.

For example:

.. code-block:: none

   row_id,label_id,partition_id,datasource,semantic,value
   1,JCurrie,1,Table:One,email,justin.c@email.com
   2,JCurrie,2,Table:Two,email,j.currie@mail.com


A Stitch labels table is intended to fine-tune results. If too many entries exist in a Stitch labels table, the solution may be to tune Stitch itself before adding more entries to the labels table. You may use more than one Stitch labels table.

.. stitch-labels-table-schema-end


.. _stitch-labels-match-vs-split:

Match vs. split
--------------------------------------------------

.. stitch-labels-match-vs-split-start

The combination of **label_id** and **partition_id** identifies which rows in the Stitch labels table should match or be split.

For example:

.. code-block:: mysql

   -------- ---------- -------------- -------------- ----------- --------------------
    row_id   label_id   partition_id   datasource     semantic    value
   -------- ---------- -------------- -------------- ----------- --------------------
    1        TSmith     1              Table:One      pk          123a-456b-789c
    2        TSmith     1              Table:Two      pk          456a-789b-123c
   -------- ---------- -------------- -------------- ----------- --------------------

This tells Stitch that TSmith, despite having different values in different data sources, should be matched to the same customer record.

Whereas the following table tells Stitch that JCurrie, despite having the same value in different data sources, should be split into two customer records:

.. code-block:: mysql

   -------- ---------- -------------- -------------- ----------- --------------------
    row_id   label_id   partition_id   datasource     semantic    value
   -------- ---------- -------------- -------------- ----------- --------------------
    1        JCurrie    1              Table:One      email       justin.c@email.com
    2        JCurrie    2              Table:Two      email       j.currie@mail.com
   -------- ---------- -------------- -------------- ----------- --------------------

.. stitch-labels-match-vs-split-end


.. _stitch-labels-how-they-work:

How Stitch labels work
--------------------------------------------------

.. stitch-labels-how-they-work-start

The Stitch labels table does not require all of the possible combinations of semantic values to be specified. If any two rows in the Stitch labels table indicate that a customer record should be merged or split, it won't matter about any of the other semantic values matching (or not matching) elsewhere. Stitch will force the outcome to be what the Stitch labels table indicates.

* Records labeled with the same **label-id** and the same **partition-id** will be merged into the same cluster. All records associated with these two records will be merged into the same cluster.
* Records labeled with the same **label-id** and a different **partition-id** will be split into different clusters based on the **partition-id**. Other records associated with these two records may be split (or may not be split), depending on the outcome of the Stitch clustering analysis for each individual customer record.

A Stitch labels table can have as many rows as required, but each individual row in the table must have a **label_id** that matches another **label_id** in another row in the table. More than one Stitch labels table may be used.

.. stitch-labels-how-they-work-end


.. _stitch-labels-add-table:

Add a Stitch labels table
==================================================

.. stitch-labels-add-table-start

A Stitch labels table is a CSV file that is maintained as a local file, and then uploaded as a feed to Amperity.

#. Use the :doc:`split clusters <stitch_qa_split_clusters>` query in the Stitch QA folder in the **Queries** page to look for examples of overclustering and underclustering.
#. Use the **SQL Query Editor** to run a query similar to:

   .. code-block::
      :linenos:

      SELECT
        *
      FROM Unified_Coalesced
      WHERE amperity_id IN ('123a-456b-789c','234d-567e-891f')

   where "'123a-456b-789c','234d-567e-891f'" represents the pair of Amperity IDs in the overcluster or undercluster.

   This query will return all of the rows associated with those Amperity IDs. Examine the results to understand if the customer records were merged or split correctly.
   
   .. tip:: Use the Unified Preprocessed Raw table instead of the Unified Coalesced table to compare normalized values used by Stitch instead of the values in the source tables.
   
#. Add instances of incorrectly merged and/or split customer records to a CSV file with the correct schema for Stitch labels.
#. Ingest the CSV file as a feed.
#. Select **row_id** field as primary key.
#. Add semantic values to each field that matches the name of the column in the CSV file, with the exception of the **semantic** column, which must be associated with a profile (PII) semantic.

   The semantic tags for Stitch labels are: **sl/label-id**, **sl/partition-id**, **sl/datasource**, **sl/semantic**, and **sl/value**.

   For example, the **label_id** column should be assigned the **sl/label-id** semantic and a row with **email** should be assigned the **sl/semantic** semantic.
#. Activate the feed and examine the results in the domain table.
#. Run Stitch.
#. Run the Customer 360.
#. Re-run the split clusters Stitch QA query and verify that the customer record were merged or split correctly.

.. stitch-labels-add-table-end

.. _stitch-labels-examples:

Examples
==================================================

.. stitch-labels-examples-start

The following examples show overclustering and underclustering, and how to apply the desired outcome using a Stitch labels table.

.. stitch-labels-examples-end

.. stitch-labels-examples-note-start

.. note:: This topic uses similar examples as the ones in the :doc:`Stitch nicknames <stitch_nicknames>` topic to show how to use Stitch labels instead of nicknames to help Stitch evaluate records so they are grouped correctly.

   If the match/mismatch is only due to issues with given names, you should consider using nicknames instead of labels to resolve the issue.

.. stitch-labels-examples-note-end


.. _stitch-labels-example-name-conflict:

Name conflict
--------------------------------------------------

.. stitch-labels-example-name-conflict-start

Teaninau and Teeyon are phonetically similar names, but are not obvious nicknames and after examining the merged customer records it is unclear that these individuals should be part of the same customer record. They may be related, as there are some shared details. If the customer records are merged, and you are sure they should not be part of the same customer record, add an entry to the Stitch labels table to ensure that Teaninau and Teeyon are always split into two customer records:

.. code-block:: none

   row_id,label_id,partition_id,datasource,semantic,value
   1,TeaninauTeeyon,1,Table:One,pk,123a-456b-789c
   2,TeaninauTeeyon,2,Table:Two,pk,234d-567e-891f

If the customer records are split, and you are sure they should be part of the same customer record, add an entry to the Stitch labels table to ensure that Teaninau and Teeyon are always merged into a single customer record:

.. code-block:: none

   row_id,label_id,partition_id,datasource,semantic,value
   1,TeaninauTeeyon,1,Table:One,pk,123a-456b-789c
   2,TeaninauTeeyon,1,Table:Two,pk,234d-567e-891f

.. stitch-labels-example-name-conflict-end


.. _stitch-labels-example-gender-mismatch:

Gender mismatch from typo
--------------------------------------------------

.. stitch-labels-example-gender-mismatch-start

Adam and Ada are not the same name and it is unlikely that Ada is a nickname for Adam. Add an entry to the Stitch labels table to ensure that Adam and Ada are always split into two customer records:

.. code-block:: none

   row_id,label_id,partition_id,datasource,semantic,value
   1,AdamAda,1,Table:One,pk,123a-456b-789c
   2,AdamAda,2,Table:Two,pk,234d-567e-891f

.. stitch-labels-example-gender-mismatch-end


.. _stitch-labels-example-likely-nickname:

Likely nickname
--------------------------------------------------

.. stitch-labels-example-likely-nickname-start

Ty and Tylian were split into two customer records, but after examining the split customer records and noticing they share other details (email address and phone number), it's very likely that Ty is a nickname for Tylian. Add an entry to the Stitch labels table to ensure that Ty and Tylian are always merged into a single customer record:

.. code-block:: none

   row_id,label_id,partition_id,datasource,semantic,value
   1,TyTylian,1,Table:One,pk,123a-456b-789c
   2,TyTylian,2,Table:Two,pk,234d-567e-891f

.. stitch-labels-example-likely-nickname-end
