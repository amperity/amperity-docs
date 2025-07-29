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
        Configure Amperity to send campaigns to Listrak.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Listrak.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Listrak

==================================================
Configure campaigns for Listrak
==================================================

.. campaign-listtrak-about-start

|destination-name| is an automation platform for email marketing. Use the `Listrak Email API <https://api.listrak.com/email>`__ |ext_link| to manage audiences in |destination-name|.

.. campaign-listtrak-about-end

.. campaign-listtrak-context-start

Amperity can manage `email <https://api.listrak.com/email>`__ |ext_link| lists in |destination-name|.

Amperity automatically adds a field attribute to all email lists that are sent to |destination-name|. This field is located inside a field group named "Amperity Message Attributes" within |destination-name|.

.. note:: Use SFTP to manage `Customer lists <https://www.listrak.com/product-team/customer-schema>`__ |ext_link|, `Product lists <https://www.listrak.com/product-team/product-schema>`__ |ext_link|, `Order lists <https://www.listrak.com/product-team/order-schema>`__ |ext_link|, and `Order item lists <https://www.listrak.com/product-team/order-items-schema>`__ |ext_link|.

   Work with your |destination-name| representatives to determine which of these sets will be useful for your workflows within |destination-name|, and then verify that attributes sent from Amperity are mapped correctly to the appropriate data schema within |destination-name|.

.. campaign-listtrak-context-end


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

       You must configure this destination for email or SMS:

       **Email client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-listrak-email-client-id-secret-start
             :end-before: .. credential-listrak-email-client-id-secret-end

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

          (Applies to Email **and** SMS lists.)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-listrak-list-name-start
             :end-before: .. setting-listrak-list-name-end

          .. note::  Lists are available from the **Contacts** page within the |destination-name| user interface.

             |destination-name| prefers to use a single list for managing email addresses and phone numbers, which are named "Master List" by default within |destination-name|. This is the name of the list that is most often managed when data is sent to |destination-name| from Amperity.

             If you are not sure which list (or lists) should be managed by Amperity, work with your Listrak representative to determine the best approach for list management.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Audience configuration**

       Use a query or a segment to build an audience to send to |destination-name|. The **email** or **phone** field must be part of the audience. You may append additional profile attributes to the query or segment.

.. campaign-listrak-get-details-end


.. _campaign-listrak-sftp:

Customers, products, and orders
==================================================

.. campaign-listrak-sftp-start

Configure Amperity to additional data sets---customers, products, orders, and order items---to |destination-name| using SFTP.

.. note:: This option uses the SFTP destination that is built into Amperity and should follow the steps and requirements that are outlined in the |destination-name| `file import guide <https://help.listrak.com/en/articles/1669274-file-import-guide>`__ |ext_link|.

You can send the following sets of data to |destination-name|.

#. `Customers <https://www.listrak.com/product-team/customer-schema>`__ |ext_link|
#. `Products <https://www.listrak.com/product-team/product-schema>`__ |ext_link|
#. `Orders <https://www.listrak.com/product-team/order-schema>`__ |ext_link|
#. `Order items <https://www.listrak.com/product-team/order-items-schema>`__ |ext_link|

Work with your |destination-name| representatives to determine which of these sets will be useful for your workflows within |destination-name|, and then verify that attributes sent from Amperity are mapped correctly to the appropriate data schema within |destination-name|.

.. campaign-listrak-sftp-end


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
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
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
          :alt: Step 1.
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
          :alt: Step 2.
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
          :alt: Step 3.
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
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **List name**
          |checkmark-required| **Required**

          (Applies to Email **and** SMS lists.)

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
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-listrak-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
