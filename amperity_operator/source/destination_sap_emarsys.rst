.. https://docs.amperity.com/operator/


.. |destination-name| replace:: SAP Emarsys
.. |destination-api| replace:: Emarsys API
.. |plugin-name| replace:: "emarsys"
.. |credential-type| replace:: "emarsys"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: contact lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "emar"


.. meta::
    :description lang=en:
        Configure Amperity to send contact lists to SAP Emarsys.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send contact lists to SAP Emarsys.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for SAP Emarsys

==================================================
Configure destinations for SAP Emarsys
==================================================

.. destination-sap-emarsys-about-start

|destination-name| is an omnichannel customer engagement platform for personalizing customer interactions across channels for the purpose of increasing customer engagement and lifetime value.

.. destination-sap-emarsys-about-end

.. destination-sap-emarsys-configure-start

Use contact lists in |destination-name| as an alternative to segments when selecting the recipient source for a campaign.

You can configure Amperity to maintain contact lists in |destination-name| using the |destination-api|. Amperity updates the contact list in |destination-name| to match the audience sent from Amperity. Amperity:

#. Adds contact lists when they don't exist in |destination-name|. The name of a contact list is case-sensitive.
#. Updates contact attributes and profile information for contacts already in a contact list to match what is sent from Amperity.
#. Adds contacts to a contact list when they don't exist in |destination-name|.
#. Removes contacts from a contact list when they don't exist in the audience sent from Amperity.

.. destination-sap-emarsys-configure-end


.. _destination-sap-emarsys-howitworks:

How this destination works
==================================================

.. destination-sap-emarsys-howitworks-start

Amperity uses a combination of endpoints maintain contact lists in |destination-name|.

.. destination-sap-emarsys-howitworks-end

.. image:: ../../images/howitworks-sap-emarsys.png
   :width: 600 px
   :alt: Listrak SMS connector
   :align: left
   :class: no-scaled-link

.. destination-sap-emarsys-howitworks-table-start

A |destination-name| destination works like this:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **START WORKFLOW**

       After the workflow is started, Amperity:

       #. Gets the value for **{listId}** for the contact list from |destination-name|.

       #. Amperity builds the audience list for the query or segment.

       #. Amperity validates the audience list.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **CREATE CONTACT LIST?**

       If the contact list does not exist, Amperity uses the `Create a Contact List <https://dev.emarsys.com/docs/core-api-reference/enmevkj1fi016-create-a-contact-list>`__ |ext_link| endpoint to create the list.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **UPDATE CONTACTS**

       The `Update Contacts <https://dev.emarsys.com/docs/core-api-reference/f8ljhut3ac2i1-update-contacts>`__ |ext_link| endpoint to update contact attributes and profile information to match what is sent from Amperity.

       Amperity uses the same endpoint to upsert contact attributes and profile information to contacts that exist in the audience sent from Amperty, but do not exist for the contact in the contact list in |destination-name|.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **ADD CONTACTS**

       The `Add Contacts to a Contact List <https://dev.emarsys.com/docs/core-api-reference/e6v1un6ph06f3-add-contacts-to-a-contact-list>`__ |ext_link| endpoint to add any contacts that exist in the audience sent from Amperity, but do not exist in the contact list in |destination-name|.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - **REMOVE CONTACTS**

       The `Remove Contacts from a Contact List <https://dev.emarsys.com/docs/core-api-reference/4ir8e6fgq3570-remove-contacts-from-a-contact-list>`__ |ext_link| endpoint to remove any contacts that exist in |destination-name|, but do not exist in the audience sent from Amperity.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - **END WORKFLOW**

       The workflow ends when all attributes are updated for existing contacts, contacts are added, and contacts are removed from the contact list.

       When the workflow is finished the updated and added attributes are available immediately in |destination-name|.

.. destination-sap-emarsys-howitworks-table-end


.. _destination-sap-emarsys-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-sap-emarsys-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **OAuth credential settings**

       Configure the client ID and client secret for |destination-name| to allow Amperity to use OAuth while managing client lists.

       **Client ID and secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. setting-sap-emarsys-client-id-and-secret-start
             :end-before: .. setting-sap-emarsys-client-id-and-secret-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-sap-emarsys-list-exists-start
          :end-before: .. setting-sap-emarsys-list-exists-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Profile attributes and custom fields**

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-sap-emarsys-contact-identifier-start
          :end-before: .. setting-sap-emarsys-contact-identifier-end

.. destination-sap-emarsys-get-details-end


.. _destination-sap-emarsys-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for SAP Emarsys**

.. destination-sap-emarsys-credentials-steps-start

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

       Configure the client ID and client secret for |destination-name| to allow Amperity to use OAuth while managing client lists.

       **Client ID and secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. setting-sap-emarsys-client-id-and-secret-start
             :end-before: .. setting-sap-emarsys-client-id-and-secret-end

.. destination-sap-emarsys-credentials-steps-end


.. _destination-sap-emarsys-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for SAP Emarsys**

.. destination-sap-emarsys-add-steps-start

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
          :alt: Add 
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

       **Contact identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sap-emarsys-contact-identifier-start
             :end-before: .. setting-sap-emarsys-contact-identifier-end


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

.. destination-sap-emarsys-add-steps-end


.. _destination-sap-emarsys-attributes-and-fields:

Profile attributes and custom fields
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-sap-emarsys-attributes-and-fields-start
   :end-before: .. setting-sap-emarsys-attributes-and-fields-end
