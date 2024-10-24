.. 
.. /markdown
.. 




Stitch benchmarking
==================================================

This topic contains content groupings for cards that explain Stitch benchmarks.

The title in this topic is the title of a card. The **xxxx-desc** is the visible description. The **xxxxx-more** is the "show more" content.


Size of largest cluster
==================================================

**size-of-largest-desc**

   The percentage of stitched records that belong to the largest Amperity ID cluster.

**size-of-largest-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may be an indication of overclustering records into Amperity IDs. On the other hand, a lower than expected value may indicate underclustering.Show less

   Current tooltip: This test computes the percentage of a tenant's stitched records that are associated the largest Amperity ID. A larger percentage implies many records are being clustered into the same Amperity ID, usually because of bogus PII values. If, upon inspection, the largest cluster looks good, you may ignore this test.


Shared name and phone
==================================================

**shared-name-phone-desc**

   The count of unique name and phone combinations that appear in more than one Amperity ID cluster divided by those that appear in just one cluster.

**shared-name-phone-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may indicate underclustering of records into Amperity IDs. On the other hand, a lower than expected value may indicate overclustering.Show less

   Current tooltip: This test computes, for every (name, phone) combination, a ratio of how many such combinations appear in multiple Amperity IDs, vs. only one Amperity ID. A large ratio implies that the same (name, phone) are being spread across multiple Amperity IDs more than we'd expect, which may indicate under-clustering.


Small supersized clusters
==================================================

**small-supersized-desc**

   The count of supersized clusters that contain fewer than 1000 records.

**small-supersized-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: Supersized components are the main cause of underclustering. Small ones are easier to address.Show less


   Current tooltip: This test computes a count of how many medium-large (< 1000 recod) components there are in Stitch output. Counter-intuitively, because of how Stitch works, a large count implies many records were not compared to each other during Stitch, which means the pipeline may have missed potential connections and under-clustered records.


Large supersized clusters
==================================================

**large-supersized-desc**

   The count of supersized clusters that contain more than 1000 records.

**large-supersized-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: Supersized components are the main cause of underclustering. Large ones are harder to address.Show less


   Current tooltip: This test computes a count of how many very large (> 1000 recod) components there are in Stitch output. Counter-intuitively, because of how Stitch works, a large count implies many records were not compared to each other during Stitch, which means the pipeline may have missed potential connections and under-clustered records.


Many NULL records
==================================================

**many-null-records-desc**

   The percentage of stitched records that contain sparse data, which occurs when email addresses, physical addresses, and phone numbers have NULL values.

**many-null-records-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may result in overclustering and a lower than expected value may result in underclustering.

   Current tooltip: This test computes the percentage of records fed to Stitch that are sparse, which is defined as having null email and given name. A larger percentage means that the PII being fed into Stitch is less rich than we'd expect, and usually implies a problem with data capture or semantic tagging.


Shared name and email address
==================================================

**shared-name-email-desc**

   The count of unique name and email address combinations that appear in more than one Amperity ID cluster divided by those that appear in just one cluster.

**shared-name-email-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may indicate underclustering of records into Amperity IDs. On the other hand, a lower than expected value may indicate overclustering.Show less

   Current tooltip: This test computes, for every (name, email) combination, a ratio of how many such combinations appear in multiple Amperity IDs, vs. only one Amperity ID. A large ratio implies that the same (name, email) are being spread across multiple Amperity IDs more than we'd expect, which may indicate under-clustering.


Shared name and physical address
==================================================

**shared-name-address-desc**

   The count of unique name and physical address combinations that appear in more than one Amperity ID cluster divided by those that appear in just one cluster.

**shared-name-address-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may indicate underclustering of records into Amperity IDs. On the other hand, a lower than expected value may indicate overclustering.Show less

   Current tooltip: This test computes, for every (name, address) combination, a ratio of how many such combinations appear in multiple Amperity IDs, vs. only one Amperity ID. A large ratio implies that the same (name, address) are being spread across multiple Amperity IDs more than we'd expect, which may indicate under-clustering.


More than 3 given names
==================================================

**given-names-desc**

   The percentage of Amperity ID clusters with more than 3 given names.

**given-names-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may indicate overclustering of records into Amperity IDs. On the other hand, a lower than expected value may indicate underclustering.Show less


   Current tooltip: This test computes the percentage of Amperity IDs with more than three given names. A larger percentage implies that, with a relatively high frequency, different given names are ending up in the same Amperity ID, which may indicate that records have been over-clustered.


More than 3 surnames
==================================================

**surnames-desc**

   The percentage of Amperity ID clusters with more than 3 surnames.

**surnames-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may indicate overclustering of records into Amperity IDs. On the other hand, a lower than expected value may indicate underclustering.Show less


   Current tooltip: This test computes the percentage of Amperity IDs with more than three surnames. A larger percentage implies that, with a relatively high frequency, different surnames are ending up in the same Amperity ID, which may indicate that records have been over-clustered.


More than 5 postal codes
==================================================

**postal-codes-desc**

   The percentage of Amperity ID clusters with addresses in more than 5 postal codes.

**postal-codes-more**

   COMBINE INTO ONE COHESIVE PARAGRAPH:

   Current show more: A higher than expected value may indicate overclustering of records into Amperity IDs. On the other hand, a lower than expected value may indicate underclustering.

   Current tooltip: This test computes the percentage of Amperity IDs with more than five postal codes. A larger percentage implies that, with a relatively high frequency, different addresses are ending up in the same Amperity ID, which may indicate that records have been over-clustered.
