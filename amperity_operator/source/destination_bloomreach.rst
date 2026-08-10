.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Bloomreach Engagement
.. |destination-api| replace:: Bloomreach Engagement API
.. |plugin-name| replace:: "Bloomreach"
.. |credential-type| replace:: "bloomreach"
.. |required-credentials| replace:: "API base URL", "Project token", "API key ID", and "API secret"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: customer profiles
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "blo"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send data to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Bloomreach

==================================================
Configure destinations for Bloomreach
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bloomreach-start
   :end-before: .. term-bloomreach-end

.. destination-bloomreach-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-bloomreach-beta-end

.. destination-bloomreach-start

Use Amperity to manage customer profiles in |destination-name|. Build a query or segment, and then send customer data to |destination-name| for segmentation, campaigns, and personalization. Customer profiles are identified by a Bloomreach hard identifier such as email, cookie, Google Analytics ID, or external ID.

.. destination-bloomreach-end

.. destination-bloomreach-api-note-start

This destination uses the `Bloomreach Engagement API <https://documentation.bloomreach.com/engagement/reference/>`__ |ext_link|.

.. destination-bloomreach-api-note-end

.. destination-bloomreach-membership-start

.. important:: |destination-name| has no API for setting segment membership directly. Amperity records membership as ``segment-addition`` and ``segment-deletion`` events that carry the segment name. To act on this membership in |destination-name|--for example, to target it in a campaign--build a segmentation in your |destination-name| project over these events. Until that segmentation exists, the membership data is present in |destination-name| but is not yet usable as a segment.

.. destination-bloomreach-membership-end

.. destination-bloomreach-attribute-limit-start

.. caution:: |destination-name| allows at most 255 attributes per customer. An orchestration or campaign that sends more than 255 attributes fails with an error before any data is sent.

.. destination-bloomreach-attribute-limit-end

.. destination-bloomreach-reporting-start

.. note:: Amperity sends customer updates and segment membership changes to |destination-name| over the batch API and receives a result for each row in the same request. Rows that |destination-name| rejects are reported as failed, and the rejection reason is recorded as an error on the orchestration or campaign run.

.. warning:: Attributes accumulate across everything sent to a |destination-name| project over time. If the project's total number of distinct attributes would exceed |destination-name|'s limit of 255, |destination-name| rejects the over-limit writes and Amperity reports them as errors on the run.

.. destination-bloomreach-reporting-end


.. _destination-bloomreach-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-bloomreach-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API base URL**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-base-url-start
             :end-before: .. credential-bloomreach-base-url-end

       **Project token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-project-token-start
             :end-before: .. credential-bloomreach-project-token-end

       **API key ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-api-key-id-start
             :end-before: .. credential-bloomreach-api-key-id-end

       **API secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-api-secret-start
             :end-before: .. credential-bloomreach-api-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-find-credentials-start
             :end-before: .. credential-bloomreach-find-credentials-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Bloomreach identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-bloomreach-identity-column-start
             :end-before: .. setting-bloomreach-identity-column-end

       **Segment name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-bloomreach-segment-name-start
             :end-before: .. setting-bloomreach-segment-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A query that outputs the fields that must be sent to the |destination-name| customer table.

.. destination-bloomreach-get-details-end


.. _destination-bloomreach-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Bloomreach**

.. destination-bloomreach-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **API base URL**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-base-url-start
             :end-before: .. credential-bloomreach-base-url-end

       **Project token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-project-token-start
             :end-before: .. credential-bloomreach-project-token-end

       **API key ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-api-key-id-start
             :end-before: .. credential-bloomreach-api-key-id-end

       **API secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-api-secret-start
             :end-before: .. credential-bloomreach-api-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-bloomreach-find-credentials-start
             :end-before: .. credential-bloomreach-find-credentials-end

.. destination-bloomreach-credentials-steps-end


.. _destination-bloomreach-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Bloomreach**

.. destination-bloomreach-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add destination
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Bloomreach identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-bloomreach-identity-column-start
             :end-before: .. setting-bloomreach-identity-column-end

       **Segment name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-bloomreach-segment-name-start
             :end-before: .. setting-bloomreach-segment-name-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. destination-bloomreach-add-steps-end
