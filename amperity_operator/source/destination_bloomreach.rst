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

.. destination-bloomreach-start

Use Amperity to manage customer profiles in |destination-name|. Build a query or segment, and then send customer data to |destination-name| for segmentation, campaigns, and personalization. Customer profiles are identified by a Bloomreach hard identifier such as email, cookie, Google Analytics ID, or external ID.

.. destination-bloomreach-end

.. destination-bloomreach-api-note-start

.. note:: This destination uses the `Bloomreach Engagement API <https://documentation.bloomreach.com/engagement/reference/>`__ |ext_link|.

.. destination-bloomreach-api-note-end

.. destination-bloomreach-import-replace-start

.. note:: New imports replace existing imports in |destination-name| that have the same import name. Use a unique import name for each orchestration or campaign to avoid overwriting data unintentionally.

.. destination-bloomreach-import-replace-end

.. destination-bloomreach-import-limit-start

.. caution:: Bloomreach limits each project to 25 active import definitions. When the limit is reached, Amperity automatically deletes the oldest Amperity-created import to make room for the new one. If all 25 imports were created outside of Amperity, the send will fail with a message asking the user to delete unused imports in Bloomreach to free a slot.

.. destination-bloomreach-import-limit-end

.. destination-bloomreach-attribute-limit-start

.. caution:: Bloomreach allows at most 255 attributes per customer. The connector adds a segment-membership attribute to every customer, so a single orchestration or campaign can send at most 254 attributes. A send with more than 254 attributes fails with an error before any data is sent.

.. destination-bloomreach-attribute-limit-end

.. destination-bloomreach-async-start

.. note:: |destination-name| processes imports asynchronously after Amperity sends the data. Amperity reports rows as succeeded once the import is triggered. There is no import status tracking. To confirm a send or troubleshoot missing customer data, check the import in the |destination-name| dashboard.

.. note:: Attributes accumulate across all imports in a Bloomreach project. If a project exceeds 255 attributes, Bloomreach discards the over-limit import; Amperity does not track this cumulative total, so the failure appears only in the |destination-name| dashboard.

.. destination-bloomreach-async-end


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

       **Import name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-bloomreach-import-name-start
             :end-before: .. setting-bloomreach-import-name-end

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

       **Import name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-bloomreach-import-name-start
             :end-before: .. setting-bloomreach-import-name-end

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
