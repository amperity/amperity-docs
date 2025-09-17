.. /downloads/markdown/


Stitch benchmarking
==================================================

Content groupings for cards that explain Stitch benchmarks.

Each H1 is the title of a card. The **xxxx-desc** is the visible description for that card and the **xxxxx-more** is the "show more" content.


Size of largest cluster
==================================================

**size-of-largest-desc**

   The percentage of stitched records that belong to the largest Amperity ID cluster.

**size-of-largest-more**

   A high percentage indicates overclustering, which is often associated with incomplete (or inaccurate) PII values. Review the cluster for accuracy and if it looks good, ignore this test.


Shared name and phone
==================================================

**shared-name-phone-desc**

   The count of unique name and phone combinations that appear in more than one Amperity ID cluster divided by those that appear in just one cluster.

**shared-name-phone-more**

   A large ratio indicates that a unique name and phone combination appears in multiple clusters, which indicates underclustering. Review the clusters for accuracy.



Small supersized clusters
==================================================

**small-supersized-desc**

   The count of supersized clusters that contain fewer than 1000 records.

**small-supersized-more**

   Supersized clusters are the main cause of underclustering. A large count indicates many records were not compared to each other during Stitch and potential connections may have been missed.



Large supersized clusters
==================================================

**large-supersized-desc**

   The count of supersized clusters that contain more than 1000 records.

**large-supersized-more**

   Supersized clusters are the main cause of underclustering. A large count indicates many records were not compared to each other during Stitch and potential connections may have been missed.



Many NULL records
==================================================

**many-null-records-desc**

   The percentage of stitched records that contain sparse data, which occurs when email addresses, physical addresses, and phone numbers have NULL values.

**many-null-records-more**

   A larger percentage of sparse records indicates that the quality of PII that is provided to Stitch is lower than expected. Review data sources that contain PII along with the semantic tags that are applied.



Shared name and email address
==================================================

**shared-name-email-desc**

   The count of unique name and email address combinations that appear in more than one Amperity ID cluster divided by those that appear in just one cluster.

**shared-name-email-more**

   A large ratio indicates that a unique name and email address combination appears in multiple clusters, which indicates underclustering. Review the clusters for accuracy.



Shared name and physical address
==================================================

**shared-name-address-desc**

   The count of unique name and physical address combinations that appear in more than one Amperity ID cluster divided by those that appear in just one cluster.

**shared-name-address-more**

   A large ratio indicates that a unique name and physical address combination appears in multiple clusters, which indicates underclustering. Review the clusters for accuracy.



More than 3 given names
==================================================

**given-names-desc**

   The percentage of Amperity ID clusters with more than 3 given names.

**given-names-more**

   A large percentage indicates that different given names are appearing the same cluster, which indicates overclustering. Review the clusters for accuracy.



More than 3 surnames
==================================================

**surnames-desc**

   The percentage of Amperity ID clusters with more than 3 surnames.

**surnames-more**

   A large percentage indicates that different surnames are appearing the same cluster, which indicates overclustering. Review the clusters for accuracy.


More than 5 postal codes
==================================================

**postal-codes-desc**

   The percentage of Amperity ID clusters with addresses in more than 5 postal codes.

**postal-codes-more**

   A large percentage indicates that different postal codes are appearing the same cluster, which indicates overclustering. Review the clusters for accuracy.
