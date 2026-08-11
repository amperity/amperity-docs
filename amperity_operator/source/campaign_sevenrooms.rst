.. https://docs.amperity.com/operator/


.. |destination-name| replace:: SevenRooms
.. |destination-api| replace:: SevenRooms API
.. |plugin-name| replace:: "SevenRooms"
.. |credential-type| replace:: "sevenrooms"
.. |required-credentials| replace:: "Client ID and Client Secret"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "Seven"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to SevenRooms.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to SevenRooms.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for SevenRooms

==================================================
Configure campaigns for SevenRooms
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sevenrooms-start
   :end-before: .. term-sevenrooms-end

.. campaign-sevenrooms-start

Use Amperity to activate an audience into |destination-name|. Build a campaign that includes the **email** field, and then send it to |destination-name|.

SevenRooms builds its guest segments from client tags, so Amperity activates an audience as a named client tag applied to matching guest profiles. Amperity matches guest profiles by email, applies the tag to members of the audience, and removes the tag from guest profiles that leave the audience. Amperity also writes profile attributes -- such as phone number, first name, and last name -- onto the matching guest profiles. Each run sends only the additions, removals, and attribute changes since the previous run, not the full audience.

A SevenRooms client tag is addressed as ``group:tag``. The **Tag group** is set once per destination and the **Tag name** identifies the audience; together they form the tag that Amperity applies. Changing either one sends the entire audience again under the new tag.

.. campaign-sevenrooms-end

.. campaign-sevenrooms-api-note-start

.. note:: This destination uses the `SevenRooms API <https://api-docs.sevenrooms.com>`__ |ext_link|.

.. campaign-sevenrooms-api-note-end

.. campaign-sevenrooms-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. campaign-sevenrooms-beta-end

.. campaign-sevenrooms-existing-clients-start

.. note:: SevenRooms must already contain a guest profile that matches an audience member's email within the venue group. Amperity applies tags and writes attributes to guest profiles that already exist; an audience member that SevenRooms cannot match is reported as a failed row.

.. campaign-sevenrooms-existing-clients-end

.. campaign-sevenrooms-partial-failure-start

.. caution:: A run can partially succeed. Individual audience members that SevenRooms rejects -- for example, a member with no matching guest profile or a field value that is not valid for a guest profile -- are counted as failed rows while the rest of the run completes.

.. campaign-sevenrooms-partial-failure-end

.. campaign-sevenrooms-limits-start

.. note:: Amperity sends one request per audience member, at a conservative rate of approximately 10 requests per second. This rate is an Amperity-side limit, not a published |destination-api| limit.

.. campaign-sevenrooms-limits-end


.. _campaign-sevenrooms-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-sevenrooms-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Client ID and Client Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sevenrooms-client-id-start
             :end-before: .. credential-sevenrooms-client-id-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sevenrooms-client-secret-start
             :end-before: .. credential-sevenrooms-client-secret-end

       .. tip::

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sevenrooms-find-credentials-start
             :end-before: .. credential-sevenrooms-find-credentials-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Base URL**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-base-url-start
             :end-before: .. setting-sevenrooms-base-url-end

       **Venue Group ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-venue-group-id-start
             :end-before: .. setting-sevenrooms-venue-group-id-end

       **Tag group**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-tag-group-start
             :end-before: .. setting-sevenrooms-tag-group-end

       **Audience primary key**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Tag name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-tag-name-start
             :end-before: .. setting-sevenrooms-tag-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A campaign that outputs the **email** field and any profile attributes to send to the |destination-name| audience.

.. campaign-sevenrooms-get-details-end


.. _campaign-sevenrooms-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for SevenRooms**

.. campaign-sevenrooms-credentials-steps-start

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

       **Client ID and Client Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sevenrooms-client-id-start
             :end-before: .. credential-sevenrooms-client-id-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sevenrooms-client-secret-start
             :end-before: .. credential-sevenrooms-client-secret-end

.. campaign-sevenrooms-credentials-steps-end


.. _campaign-sevenrooms-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for SevenRooms**

.. campaign-sevenrooms-add-steps-start

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

       **Base URL**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-base-url-start
             :end-before: .. setting-sevenrooms-base-url-end

       **Venue Group ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-venue-group-id-start
             :end-before: .. setting-sevenrooms-venue-group-id-end

       **Tag group**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-tag-group-start
             :end-before: .. setting-sevenrooms-tag-group-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end

       **Tag name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sevenrooms-tag-name-start
             :end-before: .. setting-sevenrooms-tag-name-end


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

.. campaign-sevenrooms-add-steps-end
