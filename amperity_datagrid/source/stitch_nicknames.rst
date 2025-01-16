.. https://docs.amperity.com/datagrid/


.. meta::
    :description lang=en:
        Manage the list of nicknames that are used during the Stitch process.

.. meta::
    :content class=swiftype name=body data-type=text:
        Manage the list of nicknames that are used during the Stitch process.

.. meta::
    :content class=swiftype name=title data-type=string:
        Manage nicknames

==================================================
Manage nicknames
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-nicknames-start
   :end-before: .. term-nicknames-end

.. stitch-nicknames-start

Stitch uses given names to identify customer records that should (or should not) be grouped together. Nicknames help Stitch associate variations in given names to the sets of records that uniquely identify your customers.

Amperity pre-loads a set of common nicknames to your tenant in the form of a static CSV file. This file has thousands of nicknames, including all of the most common nicknames, along with many variations.

You can upload your files to extend the list of common nicknames to add and/or remove nicknames as needed for your tenant. You can use any file format -- |format_csv|, |format_json|, |format_psv|, |format_tsv|, |format_parquet|, etc. -- that is supported by Amperity. (This topic uses a CSV file to describe how to manage nicknames.)

.. stitch-nicknames-end


.. _stitch-nicknames-about-pairs:

About nickname pairs
==================================================

.. stitch-nicknames-about-pairs-start

The combination of **canonical_name** and **nickname** fields in a nicknames table identifies the pair of names that are used to associate given names with your customers.

For example:

.. code-block:: mysql

   -------- ----------------  ---------- -------------
    row_id   canonical_name    nickname   update_type
   -------- ----------------  ---------- -------------
    1        Michael           Mike       ADD
    2        Victoria          Vicki      ADD
    3        Victoria          Vickie     ADD
   -------- ----------------  ---------- -------------

Whenever you add a nickname, this tells Stitch that each nickname *should* be associated with the canonical name and that both values can be used to identify the same customer. In this example, "Mike" is added as a nickname for "Michael", while "Vicki" and "Vickie" are added as nicknames for "Victoria".

The following table tells Stitch which nicknames *should not* be associated with the canonical name and *should not* be used to identify the same customer. In this example, "Sally" and "Shelly" should not be nicknames for "Susan", while "Tim" and "Timmy" should not be nicknames for "Thomas".

.. code-block:: mysql

   -------- ----------------  ---------- -------------
    row_id   canonical_name    nickname   update_type
   -------- ----------------  ---------- -------------
    1        Susan             Sally       REMOVE
    2        Susan             Shelly      REMOVE
    3        Thomas            Tim         REMOVE
    4        Thomas            Timmy       REMOVE
   -------- ----------------  ---------- -------------

.. stitch-nicknames-about-pairs-end

.. stitch-nicknames-about-pairs-note-start

.. note:: Add and remove requests can be combined into the same file:

   .. code-block:: mysql

      -------- ----------------  ---------- -------------
       row_id   canonical_name    nickname   update_type
      -------- ----------------  ---------- -------------
       1        Michael           Mike       ADD
       2        Susan             Sally      REMOVE
       3        Victoria          Vicki      ADD
       4        Susan             Shelly     REMOVE
       5        Thomas            Tim        REMOVE
       6        Victoria          Vickie     ADD
       7        Thomas            Timmy      REMOVE
       8        Daniel            Danny      REMOVE
      -------- ----------------  ---------- -------------

   If you add a nickname for a canonical name that does not exist, a new row is added. For example, if "Daniel" does not exist in your nicknames list, row 8 will add "Daniel" and add a nickname for "Danny".

   If a nickname is added *and* removed, Amperity will ignore the remove request and keep the nickname in the list.

.. stitch-nicknames-about-pairs-note-end


.. _stitch-nicknames-semantic-tags:

Upload CSV file
--------------------------------------------------

.. stitch-nicknames-semantic-tags-start

You may upload a file to Amperity that contains a list of nicknames that should be added to or removed from the nicknames file. For example, a CSV file would be similar to:

.. code-block:: none

   row_id,canonical_name,nickname,update_type
   1,Michael,Mike,ADD
   2,Victoria,Vickie,ADD
   3,Thomas,Tim,REMOVE

Add this file to your tenant using a manual upload and a feed named "Nicknames". Name the source after the file type you are using. For example: "CSV".

Apply the following semantic tags:

* **nicknames/canonical-name** to **canonical_name**
* **nicknames/nickname** to **nickname**
* **nicknames/update-type** to **update_type**

and then activate the feed.

.. stitch-nicknames-semantic-tags-end


.. _stitch-nicknames-examples:

Examples
==================================================

.. stitch-nicknames-examples-start

The following examples show how you can use a nicknames table to manage the list of nicknames that are associated with the customers in your database.

.. stitch-nicknames-examples-end

.. stitch-nicknames-examples-important-start

.. important:: Nicknames are a part of how Stitch evaluates records to determine if they match. The presence of nicknames is not enough to ensure that records will match. Records that have given names that are nicknames, but are otherwise very different, are unlikely to match.

.. stitch-nicknames-examples-important-end

.. stitch-nicknames-examples-note-start

.. note:: This topic uses similar examples as the ones in the :doc:`Stitch labels <stitch_labels>` topic to show how to use nicknames instead of Stitch labels to help Stitch evaluate records so they are grouped correctly.

   If the match/mismatch is due to issues unrelated to given names, you should consider using Stitch labels instead of nicknames to resolve the issue.

.. stitch-nicknames-examples-note-end


.. _stitch-nicknames-example-name-conflict:

Name conflicts
--------------------------------------------------

.. stitch-nicknames-example-name-conflict-start

Teaninau and Teeyon are phonetically similar names, but are not obvious nicknames and after examining the merged customer records it may be unclear that these individuals should be part of the same customer record. They may be related, as there are some shared details.

If the customer records are merged, and you believe they should not be part of the same customer record, add an entry to your nicknames table:

.. code-block:: none

   row_id,canonical_name,nickname,update_type
   1,Teaninau,Teeyon,REMOVE

and then upload it to Amperity. Verify the results to see if Teaninau and Teeyon are split into individual groupings.

If the customer records are split, and you believe they should be part of the same customer record, add an entry to your nicknames table:

.. code-block:: none

   row_id,canonical_name,nickname,update_type
   1,Teaninau,Teeyon,ADD

and then upload it to Amperity. Verify the results to see if Teaninau and Teeyon are merged into the same grouping.

.. stitch-nicknames-example-name-conflict-end


.. _stitch-nicknames-example-gender-mismatch:

Gender mismatch from typo
--------------------------------------------------

.. stitch-nicknames-example-gender-mismatch-start

Adam and Ada are not the same name and it is unlikely that Ada is a nickname for Adam.

Add an entry to the nicknames table to decrease the likelihood that Stitch will consider two records as having the same given name:

.. code-block:: none

   row_id,canonical_name,nickname,update_type
   1,Adam,Ada,REMOVE

.. stitch-nicknames-example-gender-mismatch-end


.. _stitch-nicknames-example-likely-nickname:

Likely nickname
--------------------------------------------------

.. stitch-nicknames-example-likely-nickname-start

Ty and Tylian were split into two customer records, but after examining the split customer records and noticing they share other details (email address and phone number), it's very likely that Ty is a nickname for Tylian.

Add an entry to the nicknames table to increase the likelihood that Ty and Tylian are considered matching given names:

.. code-block:: none

   row_id,canonical_name,nickname,update_type
   1,Tylian,Ty,ADD

.. stitch-nicknames-example-likely-nickname-end
