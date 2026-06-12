.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Iterable
.. |destination-api| replace:: Iterable API
.. |plugin-name| replace:: "Iterable"
.. |credential-type| replace:: "iterable"
.. |required-credentials| replace:: "API Key" and "Base URL"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "ite"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send data to Iterable.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Iterable.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Iterable

==================================================
Configure destinations for Iterable
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-iterable-start
   :end-before: .. term-iterable-end

.. destination-iterable-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** or **userId** field, and then send the results of that query to |destination-name| or build a segment that matches specific criteria, and then send the identifiers for customers who belong to that audience. You may extend the audience using custom attributes.

.. destination-iterable-end

.. destination-iterable-api-note-start

.. note:: This destination uses the `Iterable API <https://api.iterable.com/api/docs>`__ |ext_link|.

.. destination-iterable-api-note-end


.. _destination-iterable-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-iterable-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-iterable-api-key-start
             :end-before: .. credential-iterable-api-key-end

       **Base URL**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-iterable-base-url-start
             :end-before: .. credential-iterable-base-url-end

       .. tip::

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-iterable-api-find-key-start
             :end-before: .. credential-iterable-api-find-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **User identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-iterable-user-identifier-start
             :end-before: .. setting-iterable-user-identifier-end

       **Audience name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-iterable-audience-name-start
             :end-before: .. setting-iterable-audience-name-end

       **Update existing profiles only?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-iterable-update-existing-only-start
             :end-before: .. setting-iterable-update-existing-only-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A query that outputs the fields that must be mapped to the |destination-name| audience.

.. destination-iterable-get-details-end


.. _destination-iterable-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Iterable**

.. destination-iterable-credentials-steps-start

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

       **API Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-iterable-api-key-start
             :end-before: .. credential-iterable-api-key-end

       **Base URL**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-iterable-base-url-start
             :end-before: .. credential-iterable-base-url-end

.. destination-iterable-credentials-steps-end


.. _destination-iterable-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Iterable**

.. destination-iterable-add-steps-start

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

       **User identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-iterable-user-identifier-start
             :end-before: .. setting-iterable-user-identifier-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-iterable-audience-name-start
             :end-before: .. setting-iterable-audience-name-end

       **Update existing profiles only?**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-iterable-update-existing-only-start
             :end-before: .. setting-iterable-update-existing-only-end


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

.. destination-iterable-add-steps-end


.. _destination-iterable-extended-profile-attributes:

Extended profile attributes
==================================================

.. destination-iterable-extended-profile-attributes-start

You can extend audiences that are sent to |destination-name| by including extended profile attributes.

The following SQL query shows how to return results that include custom data fields for |destination-name|:

.. code-block:: sql
   :linenos:

   SELECT
     email
     ,given_name AS firstName
     ,surname AS lastName
     ,city
     ,state
     ,postal AS zipCode
     ,phone AS phoneNumber
     ,birthdate
   FROM Customer360

.. note:: |destination-name| custom data fields are stored in the ``dataFields`` object and can be used for personalization and segmentation. Review the `user profile fields <https://support.iterable.com/hc/en-us/articles/208013936-User-Profile-Fields>`__ |ext_link| that are supported by |destination-name|.

.. destination-iterable-extended-profile-attributes-end
