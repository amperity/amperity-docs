.. https://docs.amperity.com/ampiq/


.. |what-access| replace:: RFM attributes
.. |what-choose| replace:: **L12M frequency**, **L12M monetary**, or **L12M recency**
.. |what-find| replace:: "L12M"


.. meta::
    :description lang=en:
        An RFM score is an approximation that measures individual scores for recency, frequency, and monetary, along with a combined score.

.. meta::
    :content class=swiftype name=body data-type=text:
        An RFM score is an approximation that measures individual scores for recency, frequency, and monetary, along with a combined score.

.. meta::
    :content class=swiftype name=title data-type=string:
        Approximate RFM

==================================================
Approximate RFM
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-rfm-start
   :end-before: .. term-rfm-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-whatis-start
   :end-before: .. attribute-rfm-whatis-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-start
   :end-before: .. attribute-rfm-end


.. _attribute-rfm-examples:

Examples
==================================================

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-examples-start
   :end-before: .. attribute-rfm-examples-end


.. _attribute-rfm-scoring:

RFM scores
==================================================

.. attribute-rfm-scoring-start

Each RFM score is split into ten percentile groups. The lowest percentile is 1 and the highest percentile is 10. Each percentile represents 10% of the customers who belong to that segment.

* 10 represents the 90-100th percentile and the customers who have the highest recency, frequency, or monetary scores.
* 9 represents the 80-90th percentile
* 8 represents the 70-80th percentile
* 7 represents the 60-70th percentile
* 6 represents the 50-60th percentile
* 5 represents the 40-50th percentile
* 4 represents the 30-40th percentile
* 3 represents the 20-30th percentile
* 2 represents the 10-20th percentile
* 1 represents the 0-10th percentile and the customers who have the lowest recency, frequency, or monetary scores.

.. tip:: Combine percentiles to build larger groups of customers. For example 9 and 10 together represent the "top 20%" while 8, 9, and 10 represent the "top 30%".

.. attribute-rfm-scoring-end


.. _attribute-rfm-individual:

Recency, frequency, and monetary
==================================================

.. include:: ../../shared/attributes.rst
   :start-after: .. attributes-use-in-segments-start
   :end-before: .. attributes-use-in-segments-end


.. _attribute-rfm-recency:

L12M Recency
--------------------------------------------------

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-recency-start
   :end-before: .. attribute-rfm-recency-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-recency-find-start
   :end-before: .. attribute-rfm-recency-find-end


.. _attribute-rfm-frequency:

L12M Frequency
--------------------------------------------------

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-frequency-start
   :end-before: .. attribute-rfm-frequency-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-frequency-find-start
   :end-before: .. attribute-rfm-frequency-find-end


.. _attribute-rfm-monetary:

L12M Monetary
--------------------------------------------------

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-monetary-start
   :end-before: .. attribute-rfm-monetary-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-monetary-find-start
   :end-before: .. attribute-rfm-monetary-find-end


.. _attribute-rfm-score:

Combined score
==================================================

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-score-start
   :end-before: .. attribute-rfm-score-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-score-tip-start
   :end-before: .. attribute-rfm-score-tip-end

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-score-context-start
   :end-before: .. attribute-rfm-score-context-end


.. _attribute-rfm-conditions:

Available operators
==================================================

.. include:: ../../amperity_reference/source/attribute_rfm.rst
   :start-after: .. attribute-rfm-individual-conditions-start
   :end-before: .. attribute-rfm-individual-conditions-end
