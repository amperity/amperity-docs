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
        Configure Amperity to send data to SendGrid.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to SendGrid.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for SendGrid

==================================================
Configure destinations for SendGrid
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sendgrid-start
   :end-before: .. term-sendgrid-end

.. destination-sendgrid-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** field, and then send the results of that query to |destination-name| or build a segment that matches specific criteria, and then send the email addresses for customers who belong to that audience.

Amperity adds and removes contacts on a named SendGrid marketing list, keyed on email. Each run sends only the additions and removals since the previous run, not the full audience. Email addresses are lowercased before they are sent, and contacts are matched case-insensitively. If the named list does not already exist, Amperity creates it.

Amperity sends only the email address for each contact. You can include the **external_id** field in your query and it is accepted by the schema, but it is not sent to |destination-name| in this phase.

.. destination-sendgrid-end

.. destination-sendgrid-api-note-start

.. note:: This destination uses the `SendGrid Marketing Contacts API <https://www.twilio.com/docs/sendgrid/api-reference>`__ |ext_link|.

.. destination-sendgrid-api-note-end

.. destination-sendgrid-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-sendgrid-beta-end

.. destination-sendgrid-async-start

.. note:: |destination-name| adds contacts asynchronously: Amperity submits each batch as an import job and waits for it to finish processing. Contact removals are submitted as a separate job that |destination-name| does not report status for, so Amperity reports removals as succeeded once they are submitted, not confirmed. To verify a send, check the contacts in the |destination-name| dashboard.

.. destination-sendgrid-async-end

.. destination-sendgrid-partial-failure-start

.. caution:: A run can partially succeed. If |destination-name| rejects individual contacts during an import (for example, invalid email addresses), those contacts are counted as failed rows while the rest of the run completes.

.. destination-sendgrid-partial-failure-end

.. destination-sendgrid-limits-start

.. note:: Amperity sends contacts at a conservative rate of approximately three requests per second and in batches of up to 10,000 contacts. This rate is an Amperity-side limit, not a published |destination-api| limit.

.. destination-sendgrid-limits-end


.. _destination-sendgrid-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-sendgrid-get-details-table-start

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
     - A query that outputs the fields that must be mapped to the |destination-name| audience.

.. destination-sendgrid-get-details-end


.. _destination-sendgrid-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for SendGrid**

.. destination-sendgrid-credentials-steps-start

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

.. destination-sendgrid-credentials-steps-end


.. _destination-sendgrid-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for SendGrid**

.. destination-sendgrid-add-steps-start

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

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

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

.. destination-sendgrid-add-steps-end
