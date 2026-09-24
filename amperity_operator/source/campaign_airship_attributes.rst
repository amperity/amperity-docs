.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Airship Attributes
.. |destination-api| replace:: Airship Attribute Lists API
.. |plugin-name| replace:: "Airship Attributes"
.. |credential-type| replace:: "airship-attributes"
.. |required-credentials| replace:: "Client ID", "Client Secret", "App Key", and "Data Center"
.. |what-send| replace:: attributes
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "airship"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Airship Attributes.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Airship Attributes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Airship Attributes

==================================================
Configure campaigns for Airship Attributes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-airship-attributes-start
   :end-before: .. term-airship-attributes-end

.. campaign-airship-attributes-start

You can configure Amperity to send a campaign audience of customer attributes to |destination-name| using the |destination-api|. Each row is one Airship user profile. The ``airship_identifier`` column is required and holds the identifier Airship matches the row against -- a named user ID, a channel ID, or an email address, depending on the **Identifier type** setting. Every other column becomes an Airship attribute, matched to the attribute in your Airship project whose ID is exactly the column name. Values are sent to Airship as they appear in Amperity; nothing is hashed or transformed. Rows with a blank ``airship_identifier`` are dropped and counted as failed, because Airship has nothing to match them against.

Each campaign send uploads the entire audience to a named Airship attribute list, creating the list on the first send and reusing it after that. The list name prefix selects how empty values are handled: a name beginning ``ua_attributes_`` preserves the attribute values already on each profile, for an incremental send, while ``ua_attributes_snapshot_`` removes attributes left empty by the upload, for a full refresh.

Amperity uploads the attributes as a compressed file, then waits for Airship to finish processing before reporting results. A large list usually finishes within 5 to 10 minutes; Amperity waits up to 30 minutes before timing out. Amperity reports how many rows Airship applied and how many it rejected, along with a sample of any row-level errors.

.. campaign-airship-attributes-end

.. campaign-airship-attributes-api-note-start

.. note:: This destination uses the `Airship Attribute Lists API <https://www.airship.com/docs/developer/rest-api/ua/operations/attribute-lists/>`__ |ext_link|.

.. campaign-airship-attributes-api-note-end

.. campaign-airship-attributes-beta-start

.. admonition:: Beta

   The Airship Attributes connector is currently in beta. Contact your Amperity representative to learn more.

.. campaign-airship-attributes-beta-end

.. campaign-airship-attributes-behavior-start

.. note:: Amperity has three separate Airship destinations, each configured with its own credentials: **Airship** sends CSV files over SFTP, **Airship Attributes** (this destination) sends profile attributes through the Airship REST API, and **Airship Custom Events** sends behavioral events. Attributes enrich a profile for segmentation and personalization; they do not trigger an Airship message or automation on their own.

.. important:: Every attribute you send must already exist in your Airship project before the first send. Create each one in the Airship dashboard under **Audience > Attributes > Attribute List**, with an attribute ID that matches the Amperity column name exactly and a type that matches the data. Airship checks the column headers when the upload arrives and rejects the **entire** upload if any column is not an existing attribute, naming one column at a time. Attributes cannot be created through the API, so this cannot be automated, and Amperity cannot check it in advance. Allow about 10 minutes after creating an attribute before sending values for it.

.. note:: Airship applies each upload as a whole: if Airship rejects the upload, because a column is not an existing attribute or the list fails validation, none of the rows are applied. Individual rows can still fail after an accepted upload, and Amperity reports these separately with a sample of the reasons. A successful send confirms that Airship accepted and applied the file, not that every row reached a profile: Airship counts a row as applied even when its identifier matches no existing user, holding that data for 90 days before discarding it. If a send reports success but you see no change in Airship, confirm that the **Identifier type** matches the identifier your Airship project uses.

.. note:: Airship enforces these limits per attribute list and project: 10 million rows and 101 columns per list (one identifier column plus up to 100 attributes), 1.5 GB per uploaded file, a list name of at most 64 characters, 100 attribute lists per project, and 250 attributes per project. Airship does not publish a request rate limit.

.. campaign-airship-attributes-behavior-end


.. _campaign-airship-attributes-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-airship-attributes-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Client ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-client-id-start
             :end-before: .. credential-airship-attributes-client-id-end

       **Client Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-client-secret-start
             :end-before: .. credential-airship-attributes-client-secret-end

       **App Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-app-key-start
             :end-before: .. credential-airship-attributes-app-key-end

       **Data Center**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-data-center-start
             :end-before: .. credential-airship-attributes-data-center-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-airship-attributes-find-credentials-start
          :end-before: .. credential-airship-attributes-find-credentials-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-attributes-identifier-type-start
             :end-before: .. setting-airship-attributes-identifier-type-end

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-attributes-list-name-start
             :end-before: .. setting-airship-attributes-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-attributes-list-name-prefix-start
             :end-before: .. setting-airship-attributes-list-name-prefix-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A campaign that is configured to use the sub-audience editor or one-time campaign that is configured to use a query or segment.

.. campaign-airship-attributes-get-details-table-end


.. _campaign-airship-attributes-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Airship Attributes**

.. campaign-airship-attributes-credentials-steps-start

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

       **Client ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-client-id-start
             :end-before: .. credential-airship-attributes-client-id-end

       **Client Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-client-secret-start
             :end-before: .. credential-airship-attributes-client-secret-end

       **App Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-app-key-start
             :end-before: .. credential-airship-attributes-app-key-end

       **Data Center**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-attributes-data-center-start
             :end-before: .. credential-airship-attributes-data-center-end

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-airship-attributes-find-credentials-start
          :end-before: .. credential-airship-attributes-find-credentials-end

.. campaign-airship-attributes-credentials-steps-end


.. _campaign-airship-attributes-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Airship Attributes**

.. campaign-airship-attributes-add-steps-start

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

       **Identifier type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-attributes-identifier-type-start
             :end-before: .. setting-airship-attributes-identifier-type-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-attributes-list-name-start
             :end-before: .. setting-airship-attributes-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-attributes-list-name-prefix-start
             :end-before: .. setting-airship-attributes-list-name-prefix-end

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


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. campaign-airship-attributes-add-steps-end
