.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Roku Audience
.. |destination-api| replace:: Roku Ads API
.. |plugin-name| replace:: "Roku Audience"
.. |credential-type| replace:: "roku-audience"
.. |required-credentials| replace:: "Refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audience segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "roku"


.. meta::
    :description lang=en:
        Configure Amperity to send data to Roku Audience.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Roku Audience.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Roku Audience

==================================================
Configure destinations for Roku Audience
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-roku-audience-start
   :end-before: .. term-roku-audience-end

.. destination-roku-audience-start

Use Amperity to manage audience segments in |destination-name|. Build a query using the **email** field, and then send the results of that query to |destination-name| or build a segment that matches specific criteria, and then send the email addresses and device identifiers for customers who belong to that audience.

.. destination-roku-audience-end

.. destination-roku-audience-api-note-start

.. note:: This destination uses the `Roku Ads API <https://developer.ads.roku.com/ads/reference/introduction>`__ |ext_link|.

.. destination-roku-audience-api-note-end


.. _destination-roku-audience-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-roku-audience-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-audience-refresh-token-start
             :end-before: .. credential-roku-audience-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-audience-find-refresh-token-start
             :end-before: .. credential-roku-audience-find-refresh-token-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Audience primary key**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Roku Ads account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-audience-account-uid-start
             :end-before: .. setting-roku-audience-account-uid-end

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-audience-list-name-start
             :end-before: .. setting-roku-audience-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-audience-list-name-unique-start
             :end-before: .. setting-roku-audience-list-name-unique-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A query that outputs the fields that must be mapped to the |destination-name| audience.

.. destination-roku-audience-get-details-end


.. _destination-roku-audience-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Roku Audience**

.. destination-roku-audience-credentials-steps-start

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

       **Refresh token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-audience-refresh-token-start
             :end-before: .. credential-roku-audience-refresh-token-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-roku-audience-find-refresh-token-start
             :end-before: .. credential-roku-audience-find-refresh-token-end

.. destination-roku-audience-credentials-steps-end


.. _destination-roku-audience-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Roku Audience**

.. destination-roku-audience-add-steps-start

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

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Roku Ads account ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-audience-account-uid-start
             :end-before: .. setting-roku-audience-account-uid-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-audience-list-name-start
             :end-before: .. setting-roku-audience-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-roku-audience-list-name-unique-start
             :end-before: .. setting-roku-audience-list-name-unique-end


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

.. destination-roku-audience-add-steps-end
