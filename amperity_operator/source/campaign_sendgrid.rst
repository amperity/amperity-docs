.. https://docs.amperity.com/operator/


.. |destination-name| replace:: SendGrid
.. |destination-api| replace:: SendGrid Marketing Contacts API
.. |plugin-name| replace:: "SendGrid"
.. |credential-type| replace:: "sendgrid"
.. |required-credentials| replace:: "API Key"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "send"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to SendGrid.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to SendGrid.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for SendGrid

==================================================
Configure campaigns for SendGrid
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sendgrid-start
   :end-before: .. term-sendgrid-end

.. campaign-sendgrid-start

Use Amperity to manage audience lists in |destination-name|. Build a campaign using the **email** field, and then send the results of that campaign to |destination-name|.

Amperity adds and removes contacts on a named SendGrid marketing list, keyed on email. Each run sends only the additions and removals since the previous run, not the full audience. Email addresses are lowercased before they are sent, and contacts are matched case-insensitively. If the named list does not already exist, Amperity creates it.

Amperity sends only the email address for each contact. You can include the **external_id** field in your campaign and it is accepted by the schema, but it is not sent to |destination-name| in this phase.

.. campaign-sendgrid-end

.. campaign-sendgrid-api-note-start

.. note:: This destination uses the `SendGrid Marketing Contacts API <https://www.twilio.com/docs/sendgrid/api-reference>`__ |ext_link|.

.. campaign-sendgrid-api-note-end

.. campaign-sendgrid-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. campaign-sendgrid-beta-end

.. campaign-sendgrid-async-start

.. note:: |destination-name| adds contacts asynchronously: Amperity submits each batch as an import job and waits for it to finish processing. Contact removals are submitted as a separate job that |destination-name| does not report status for, so Amperity reports removals as succeeded once they are submitted, not confirmed. To verify a send, check the contacts in the |destination-name| dashboard.

.. campaign-sendgrid-async-end

.. campaign-sendgrid-partial-failure-start

.. caution:: A run can partially succeed. If |destination-name| rejects individual contacts during an import (for example, invalid email addresses), those contacts are counted as failed rows while the rest of the run completes.

.. campaign-sendgrid-partial-failure-end

.. campaign-sendgrid-limits-start

.. note:: Amperity sends contacts at a conservative rate of approximately three requests per second and in batches of up to 10,000 contacts. This rate is an Amperity-side limit, not a published |destination-api| limit.

.. campaign-sendgrid-limits-end


.. _campaign-sendgrid-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-sendgrid-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sendgrid-api-key-start
             :end-before: .. credential-sendgrid-api-key-end

       .. tip:: 

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sendgrid-api-find-key-start
             :end-before: .. credential-sendgrid-api-find-key-end

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

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sendgrid-list-name-start
             :end-before: .. setting-sendgrid-list-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A campaign that outputs the fields that must be mapped to the |destination-name| audience.

.. campaign-sendgrid-get-details-end


.. _campaign-sendgrid-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for SendGrid**

.. campaign-sendgrid-credentials-steps-start

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

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-sendgrid-api-key-start
             :end-before: .. credential-sendgrid-api-key-end

.. campaign-sendgrid-credentials-steps-end


.. _campaign-sendgrid-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for SendGrid**

.. campaign-sendgrid-add-steps-start

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

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-sendgrid-list-name-start
             :end-before: .. setting-sendgrid-list-name-end


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

.. campaign-sendgrid-add-steps-end
