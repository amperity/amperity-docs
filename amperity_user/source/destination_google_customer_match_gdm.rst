.. https://docs.amperity.com/user/


.. |destination-name| replace:: Google Customer Match (GDM)
.. |what-send| replace:: audiences


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Google Customer Match (GDM)

==================================================
Send query results to Google Customer Match (GDM)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-customer-match-gdm-start
   :end-before: .. term-google-customer-match-gdm-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-api-note-start
   :end-before: .. destination-google-customer-match-gdm-api-note-end

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-behavior-start
   :end-before: .. destination-google-customer-match-gdm-behavior-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

.. sendto-google-customer-match-gdm-steps-to-send-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - :ref:`Build a query <sendto-google-customer-match-gdm-build-query>`


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - :ref:`Add orchestration <sendto-google-customer-match-gdm-add-orchestration>`


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - :ref:`Run orchestration <sendto-google-customer-match-gdm-run-orchestration>`

.. sendto-google-customer-match-gdm-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-google-customer-match-gdm-build-query:

Build query
==================================================

.. sendto-google-customer-match-gdm-build-query-start

Build a query that returns the column matching the **Match identifier** configured on the destination.

.. include:: ../../amperity_operator/source/destination_google_customer_match_gdm.rst
   :start-after: .. destination-google-customer-match-gdm-data-shape-start
   :end-before: .. destination-google-customer-match-gdm-data-shape-end

The following example returns email addresses for a destination whose match identifier is **email**:

.. code-block:: sql

   SELECT
     email
   FROM Customer_360
   WHERE email IS NOT NULL

Amperity hashes **email** and **phone** values before sending them; do not hash them in the query. A member whose identifier value is missing or cannot be parsed is dropped and reported as a failed row.

.. sendto-google-customer-match-gdm-build-query-end


.. _sendto-google-customer-match-gdm-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-google-customer-match-gdm-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
