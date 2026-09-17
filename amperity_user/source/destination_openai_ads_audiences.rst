.. https://docs.amperity.com/user/


.. |destination-name| replace:: OpenAI Audiences
.. |what-send| replace:: audiences


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to OpenAI Audiences.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to OpenAI Audiences.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to OpenAI Audiences

==================================================
Send query results to OpenAI Audiences
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-openai-ads-audiences-start
   :end-before: .. term-openai-ads-audiences-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-beta-start
   :end-before: .. destination-openai-ads-audiences-beta-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-api-note-start
   :end-before: .. destination-openai-ads-audiences-api-note-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-behavior-start
   :end-before: .. destination-openai-ads-audiences-behavior-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

.. sendto-openai-ads-audiences-steps-to-send-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - :ref:`Build a query <sendto-openai-ads-audiences-build-query>`


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - :ref:`Add orchestration <sendto-openai-ads-audiences-add-orchestration>`


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - :ref:`Run orchestration <sendto-openai-ads-audiences-run-orchestration>`

.. sendto-openai-ads-audiences-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-openai-ads-audiences-build-query:

Build query
==================================================

.. sendto-openai-ads-audiences-build-query-start

Build a query that returns the column matching the **Match identifier** configured on the destination.

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-data-shape-start
   :end-before: .. destination-openai-ads-audiences-data-shape-end

The following example returns email addresses for a destination whose match identifier is **email**:

.. code-block:: sql

   SELECT
     email
   FROM Customer_360
   WHERE email IS NOT NULL

Amperity hashes raw **email** and **phone** values before sending them; do not hash them in the query. Choose the **email_sha256** or **phone_number_sha256** match identifier only when your query already returns a correctly normalized SHA-256 digest. A member whose identifier value is missing or cannot be used is dropped and reported as a failed row.

.. sendto-openai-ads-audiences-build-query-end


.. _sendto-openai-ads-audiences-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-openai-ads-audiences-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
