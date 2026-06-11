.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Viant DSP
.. |destination-api| replace:: VDP Connect API
.. |plugin-name| replace:: "Viant DSP"
.. |credential-type| replace:: "viant-dsp"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "identifier"
.. |what-send| replace:: audience segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "via"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Viant DSP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Viant DSP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Viant DSP

==================================================
Configure destinations for Viant DSP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-viant-dsp-start
   :end-before: .. term-viant-dsp-end

.. destination-viant-dsp-start

Use Amperity to build audience segments and send them to |destination-name| for use in programmatic advertising campaigns. Amperity syncs hashed identifier data, such as emails, phone numbers, IP addresses, mobile device IDs, or cookie IDs, to first-party audience segments in |destination-name|, where they become targetable in DSP campaigns.

.. destination-viant-dsp-end

.. destination-viant-dsp-api-note-start

.. note:: This destination uses the `VDP Connect API <https://docs.api.viantinc.com/reference/how-to-get-started>`__ |ext_link|.

.. destination-viant-dsp-api-note-end


.. _destination-viant-dsp-howitworks:

How this destination works
==================================================

.. destination-viant-dsp-howitworks-start

Amperity sends audience data to |destination-name| using an incremental workflow. Each run sends only new or changed records. Amperity creates the audience segment in |destination-name| automatically if it does not already exist.

.. destination-viant-dsp-howitworks-end

.. destination-viant-dsp-howitworks-table-start

A |destination-name| destination works like this:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **AUTHENTICATE**

       Amperity authenticates to |destination-name| using an OAuth2 refresh token. Amperity exchanges the refresh token for a short-lived access token, which is used for all API requests in the workflow.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **RESOLVE AUDIENCE SEGMENT**

       Amperity looks up the audience segment by name using the `GET /v1/audiences <https://docs.api.viantinc.com/reference/get-audiences-list>`__ |ext_link| endpoint, paginating through all results until a match is found.

       If the segment does not exist, Amperity creates it using the `POST /v1/audiences <https://docs.api.viantinc.com/reference/create-new-audience-segment>`__ |ext_link| endpoint with the configured account ID, advertiser ID, and identifier type. New segments start with **INACTIVE** status and activate after they accumulate at least 1,000 matched records.

       .. important:: The segment data type cannot be changed after the segment is created. To use a different identifier type, configure a new segment name.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **NORMALIZE AND HASH IDENTIFIERS**

       .. important:: |destination-name| `only accepts SHA256 hashed identifiers <https://docs.api.viantinc.com/reference/prepaing-your-user-data>`__ |ext_link| for email addresses, phone number and physical addresses.

       Amperity normalizes and hashes each value in the **identifier** column before sending it to |destination-name|.

       .. list-table::
          :widths: 30 70
          :header-rows: 1

          * - Identifier type
            - Transform
          * - Email
            - Trims whitespace, converts to lowercase, removes angle-bracket aliases, then SHA-256 hashes.
          * - Phone Number
            - Normalizes to 10-digit US format, strips formatting characters, then SHA-256 hashes.
          * - IP, Cookie, Mobile ID
            - Sent as-is. No hashing required.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **SEND ADDITIONS**

       Amperity sends new audience members to |destination-name| using the `POST /v1/audiences/{id}/data <https://docs.api.viantinc.com/reference/add-audience-data>`__ |ext_link| endpoint in batches of up to 50,000 rows. Batches run in parallel. |destination-name| processes data every 10 minutes and updates segment status after each processing cycle.

       Members already present in |destination-name| from a prior run are counted as cached rows and are not re-sent.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - **SEND DELETIONS AND END WORKFLOW**

       When audience members are removed from the segment in Amperity, Amperity sends a deletion request to |destination-name| using the `PUT /v1/audiences/{id}/data <https://docs.api.viantinc.com/reference/expire-inividual-audience-ids>`__ |ext_link| endpoint.

       .. note:: Deletions are processed asynchronously by |destination-name| and take effect within 24 hours.

       The workflow ends after all additions and deletions are sent.

.. destination-viant-dsp-howitworks-table-end


.. _destination-viant-dsp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-viant-dsp-get-details-table-start

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
             :start-after: .. credential-viant-dsp-refresh-token-start
             :end-before: .. credential-viant-dsp-refresh-token-end

          .. tip:: Contact your Viant account representative to initiate the OAuth2 authorization flow and obtain a refresh token.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required destination settings**

       **Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-account-id-start
             :end-before: .. setting-viant-dsp-account-id-end

       **Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-advertiser-id-start
             :end-before: .. setting-viant-dsp-advertiser-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Required orchestration settings**

       **Audience name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-audience-name-start
             :end-before: .. setting-viant-dsp-audience-name-end

       **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-identifier-type-start
             :end-before: .. setting-viant-dsp-identifier-type-end

       **Audience primary key**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - A query or segment that returns an **identifier** column containing the identifier values to send to |destination-name|. The identifier type must match the **Identifier type** setting.

       .. important:: |destination-name| `only accepts SHA256 hashed identifiers <https://docs.api.viantinc.com/reference/prepaing-your-user-data>`__ |ext_link| for email addresses, phone number and physical addresses.

.. destination-viant-dsp-get-details-end


.. _destination-viant-dsp-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Viant DSP**

.. destination-viant-dsp-credentials-steps-start

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
             :start-after: .. credential-viant-dsp-refresh-token-start
             :end-before: .. credential-viant-dsp-refresh-token-end

.. destination-viant-dsp-credentials-steps-end


.. _destination-viant-dsp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Viant DSP**

.. destination-viant-dsp-add-steps-start

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
          :alt: Add a destination.
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

       **Account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-account-id-start
             :end-before: .. setting-viant-dsp-account-id-end

       **Advertiser ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-advertiser-id-start
             :end-before: .. setting-viant-dsp-advertiser-id-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-audience-name-start
             :end-before: .. setting-viant-dsp-audience-name-end

       **Identifier type** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-viant-dsp-identifier-type-start
             :end-before: .. setting-viant-dsp-identifier-type-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

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

.. destination-viant-dsp-add-steps-end


.. TODO: Add workflow resolutions from existing topics HERE.
