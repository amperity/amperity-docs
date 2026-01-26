.. https://docs.amperity.com/user/


.. |destination-name| replace:: Adobe Target
.. |what-send| replace:: profile parameters
.. |where-send| replace:: |destination-name|
.. |attributes-sent| replace:: profile parameters for the |destination-name| profile store.
.. |allow-for-what| replace:: profile parameter updates
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Send profile parameters to Adobe Target.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send profile parameters to Adobe Target.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send profile parameters to Adobe Target

=================================================
Send profile parameters to Adobe Target
=================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-target-start
   :end-before: .. term-adobe-target-end

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-overview-start
   :end-before: .. destination-adobe-target-overview-end

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-api-note-start
   :end-before: .. destination-adobe-target-api-note-end


.. _destination-adobe-target-profile-parameters:

What are profile parameters?
==================================================

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-profile-parameters-start
   :end-before: .. destination-adobe-target-profile-parameters-end

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-profile-parameters-pii-caution-start
   :end-before: .. destination-adobe-target-profile-parameters-pii-caution-end


.. _destination-adobe-target-activities:

Personalization and optimization activities
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-activities-start
   :end-before: .. destination-adobe-target-activities-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _destination-adobe-target-build-query:

Build a query
==================================================

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-build-dataset-query-start
   :end-before: .. destination-adobe-target-build-dataset-query-end

.. destination-adobe-target-build-query-build-query-select-all-start

If your customer 360 database has configured an `Adobe Target table <../operator/destination_adobe_target.html#adobe-target-table>`__ then the query can select all rows from that table.

.. code-block:: sql

   SELECT * FROM Adobe_Target_Profile_Parameters

.. destination-adobe-target-build-query-build-query-select-all-start-end

.. destination-adobe-target-build-query-build-query-consolidate-start

If the mapping is done in a query open the **Query** page and add a query for sending profile properties to |destination-name|.

.. destination-adobe-target-build-query-build-query-consolidate-end

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-build-dataset-query-tips-start
   :end-before: .. destination-adobe-target-build-dataset-query-tips-end

.. admonition:: What is the thirdPartyId profile property?

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-adobe-target-identifier-thirdpartyid-start
      :end-before: .. setting-adobe-target-identifier-thirdpartyid-end

**Example query**

.. include:: ../../amperity_operator/source/destination_adobe_target.rst
   :start-after: .. destination-adobe-target-build-dataset-query-example-start
   :end-before: .. destination-adobe-target-build-dataset-query-example-end
