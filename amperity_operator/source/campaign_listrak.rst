.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Listrak
.. |plugin-name| replace:: "Listrak"
.. |credential-type| replace:: "listrak"
.. |required-credentials| replace:: "email client ID and secret"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "list"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns with email lists to Listrak.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns with email lists to Listrak.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Listrak

==================================================
Configure campaigns for Listrak Email
==================================================

.. include:: ../../amperity_operator/source/destination_listrak.rst
   :start-after: .. destination-listrak-about-start
   :end-before: .. destination-listrak-about-end

.. include:: ../../amperity_operator/source/destination_listrak.rst
   :start-after: .. destination-listrak-context-start
   :end-before: .. destination-listrak-context-end


.. _campaign-listrak-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-listrak-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       You must configure this destination for email lists:

       **Email client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-email-client-id-secret-start
             :end-before: .. credential-listrak-email-client-id-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-client-id-secret-location-start
             :end-before: .. credential-listrak-client-id-secret-location-end

       **About Listrak allowlists**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-allowlist-start
             :end-before: .. credential-listrak-allowlist-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **List name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-list-name-start
             :end-before: .. setting-listrak-list-name-end

          .. note::  Lists are available from the **Contacts** menu within the |destination-name| user interface. Open the **Contacts** menu, and then choose **List Manager**.

             .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-listrak-default-list-name-start
                :end-before: .. setting-listrak-default-list-name-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Audience configuration**

       Use a query or a segment to build an audience to send to |destination-name|. The **email** field must be part of the audience. You may append additional profile attributes to the query or segment.

.. campaign-listrak-get-details-end


.. _campaign-listrak-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Listrak**

.. campaign-listrak-credentials-steps-start

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

       You must configure this destination for email or SMS:

       **Email client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-email-client-id-secret-start
             :end-before: .. credential-listrak-email-client-id-secret-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-client-id-secret-location-start
             :end-before: .. credential-listrak-client-id-secret-location-end

.. campaign-listrak-credentials-steps-end


.. _campaign-listrak-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Listrak**

.. campaign-listrak-add-steps-start

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
          :alt: Add 
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

       **List name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-list-name-start
             :end-before: .. setting-listrak-list-name-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Field group**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-field-group-start
             :end-before: .. setting-listrak-field-group-end

          .. note::  Field groups are available from the **Contacts** menu within the |destination-name| user interface. Under **Email Contacts** open **Profile Fields**.

       **Segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-segment-name-start
             :end-before: .. setting-listrak-segment-name-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-listrak-add-steps-end


.. _campaign-listrak-sftp:

Customers, products, and orders
==================================================

.. include:: ../../amperity_operator/source/destination_listrak.rst
   :start-after: .. destination-listrak-sftp-start
   :end-before: .. destination-listrak-sftp-end
