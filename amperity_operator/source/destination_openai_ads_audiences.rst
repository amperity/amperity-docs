.. https://docs.amperity.com/operator/


.. |destination-name| replace:: OpenAI Audiences
.. |destination-api| replace:: OpenAI Advertiser API
.. |plugin-name| replace:: "OpenAI Audiences"
.. |credential-type| replace:: "openai-ads-audiences"
.. |required-credentials| replace:: "API key"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "openai"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to OpenAI Audiences.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to OpenAI Audiences.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for OpenAI Audiences

==================================================
Configure destinations for OpenAI Audiences
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-openai-ads-audiences-start
   :end-before: .. term-openai-ads-audiences-end

.. destination-openai-ads-audiences-beta-start

.. admonition:: Beta

   The OpenAI Audiences connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-openai-ads-audiences-beta-end

.. destination-openai-ads-audiences-start

Use |destination-name| to sync an Amperity audience to an OpenAI custom audience, so you can include, exclude, or bid-adjust those customers in your OpenAI ad campaigns.

Each member is matched to OpenAI users on a single identifier that you choose when you configure the destination: an **email** address, a **phone** number, or a pre-hashed **email_sha256** or **phone_number_sha256** value. Amperity applies SHA-256 hashing to raw email and phone values before sending them; plaintext identifiers never leave Amperity. Email is trimmed and lowercased before hashing, and phone numbers are converted to E.164 format (including the country code) before hashing.

If you already store hashed identifiers, choose the **email_sha256** or **phone_number_sha256** column and Amperity sends the value as supplied, after confirming it is a 64-character SHA-256 digest. Because Amperity cannot re-normalize a value that is already hashed, a pre-hashed identifier only matches if it was hashed the way OpenAI expects: the SHA-256 of a trimmed, lowercased email, or of a phone number in E.164 format. A digest built from a differently formatted value is still a valid 64-character digest, so it passes validation but silently matches no one.

A member whose chosen identifier is missing, or cannot be used — a phone number that does not parse, or a pre-hashed value that is not a 64-character digest — is dropped and reported as a failed row, so that one bad member does not fail the whole run.

.. destination-openai-ads-audiences-end

.. destination-openai-ads-audiences-data-shape-start

The query or segment sent to |destination-name| must return the one column that matches the configured **Match identifier** — an ``email``, ``phone``, ``email_sha256``, or ``phone_number_sha256`` column. Any other column is ignored, not rejected.

That column is also the key Amperity uses to track audience membership, so it must stay fixed: changing the **Match identifier** after the audience exists means recreating the audience. A query that omits the configured column still runs — every member then fails to match and the run reports those rows as failed.

.. destination-openai-ads-audiences-data-shape-end

.. destination-openai-ads-audiences-api-note-start

.. note:: This destination uses the `OpenAI Advertiser API <https://developers.openai.com/ads/api-overview>`__ |ext_link|.

.. destination-openai-ads-audiences-api-note-end

.. destination-openai-ads-audiences-behavior-start

.. important:: |destination-name| updates membership incrementally. Each run sends only the members who joined or left the audience since the last run: new members are added first, then members who left are removed. Members already in the audience are left in place and reported as unchanged. Amperity tracks these membership changes itself, so it never resends the full audience.

.. caution:: A single identifier is sent per member — the **Match identifier** you configure applies to every member of the audience. Because that identifier is also how Amperity tracks membership, it cannot be changed without recreating the audience, and match rates are typically lower than a connector that sends several identifiers per person. OpenAI counts a user matched on either email or phone as one member, but only one identifier column can be sent.

.. note:: Membership is matched in the background. A successful orchestration means OpenAI accepted the members, not that they matched a user or that the audience is usable for targeting yet. OpenAI reports matched-audience sizes only as privacy-preserving ranges and never returns per-member results, so a run cannot confirm that any specific member matched — confirm the audience size in OpenAI Ads Manager.

.. caution:: Amperity resolves the **List name** to an audience on the account, creating one if it does not exist, and reuses it on later runs. OpenAI audiences cannot be deleted, and archiving is permanent: an archived audience cannot be restored, targeted, or written to. If the configured audience was archived, enter a new **List name** and Amperity creates a fresh audience.

.. note:: An OpenAI custom audience needs roughly 25,000 matched users before it can be used for inclusion targeting or bid adjustment. Below that size it can still be used for exclusion, which has no minimum matched size.

.. note:: OpenAI custom audiences are not supported for campaigns that target the European Economic Area (EEA) or Switzerland. Confirm your campaigns target other regions before syncing.

.. note:: If OpenAI rejects a membership batch, Amperity reports that batch's members as failed rows and stops the run without sending the remaining batches. Re-running is safe: Amperity resubmits each batch so an interrupted change resumes rather than being applied twice.

.. destination-openai-ads-audiences-behavior-end


.. _destination-openai-ads-audiences-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-openai-ads-audiences-get-details-table-start

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
             :start-after: .. credential-openai-ads-audiences-api-key-start
             :end-before: .. credential-openai-ads-audiences-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-openai-ads-audiences-find-api-key-start
             :end-before: .. credential-openai-ads-audiences-find-api-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Match identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-match-identifier-start
             :end-before: .. setting-openai-ads-audiences-match-identifier-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-start
             :end-before: .. setting-openai-ads-audiences-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-archived-start
             :end-before: .. setting-openai-ads-audiences-list-name-archived-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A query or segment that returns the one column matching the configured **Match identifier**.

.. destination-openai-ads-audiences-get-details-end


.. _destination-openai-ads-audiences-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for OpenAI Audiences**

.. destination-openai-ads-audiences-credentials-steps-start

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
             :start-after: .. credential-openai-ads-audiences-api-key-start
             :end-before: .. credential-openai-ads-audiences-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-openai-ads-audiences-find-api-key-start
             :end-before: .. credential-openai-ads-audiences-find-api-key-end

.. destination-openai-ads-audiences-credentials-steps-end


.. _destination-openai-ads-audiences-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for OpenAI Audiences**

.. destination-openai-ads-audiences-add-steps-start

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

       **Match identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-match-identifier-start
             :end-before: .. setting-openai-ads-audiences-match-identifier-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-start
             :end-before: .. setting-openai-ads-audiences-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-archived-start
             :end-before: .. setting-openai-ads-audiences-list-name-archived-end

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

.. destination-openai-ads-audiences-add-steps-end
