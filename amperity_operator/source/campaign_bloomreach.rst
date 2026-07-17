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
        Configure Amperity to send campaigns to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Bloomreach

==================================================
Configure campaigns for Bloomreach
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bloomreach-start
   :end-before: .. term-bloomreach-end

.. campaign-bloomreach-start

Use Amperity to send campaigns to |destination-name|. Build a campaign in Amperity to define the audience and attributes to send, then configure the destination to send customer profiles to |destination-name| for segmentation and personalization. Customer profiles are identified by a Bloomreach hard identifier such as email, cookie, Google Analytics ID, or external ID.

.. campaign-bloomreach-end

.. campaign-bloomreach-api-note-start

.. note:: This destination uses the `Bloomreach Engagement API <https://documentation.bloomreach.com/engagement/reference/>`__ |ext_link|.

.. campaign-bloomreach-api-note-end

.. include:: destination_bloomreach.rst
   :start-after: .. destination-bloomreach-import-replace-start
   :end-before: .. destination-bloomreach-import-replace-end

.. include:: destination_bloomreach.rst
   :start-after: .. destination-bloomreach-import-limit-start
   :end-before: .. destination-bloomreach-import-limit-end

.. include:: destination_bloomreach.rst
   :start-after: .. destination-bloomreach-attribute-limit-start
   :end-before: .. destination-bloomreach-attribute-limit-end

.. include:: destination_bloomreach.rst
   :start-after: .. destination-bloomreach-async-start
   :end-before: .. destination-bloomreach-async-end


.. _campaign-bloomreach-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-bloomreach-get-details-table-start

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
     - A campaign that outputs the fields that must be sent to the |destination-name| customer table.

.. campaign-bloomreach-get-details-table-end


.. _campaign-bloomreach-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Bloomreach**

.. campaign-bloomreach-credentials-steps-start

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

.. campaign-bloomreach-credentials-steps-end


.. _campaign-bloomreach-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Bloomreach**

.. campaign-bloomreach-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add destination
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

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
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end

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
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. campaign-bloomreach-add-steps-end
