.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Google Customer Match (GDM)
.. |destination-api| replace:: Google Data Manager API
.. |plugin-name| replace:: "Google Customer Match (GDM)"
.. |credential-type| replace:: "google-customer-match-gdm"
.. |required-credentials| replace:: "refresh token"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "google"
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "540"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Google Customer Match (GDM).

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Google Customer Match (GDM)

======================================================================
Configure destinations for Google Customer Match (GDM)
======================================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-customer-match-gdm-start
   :end-before: .. term-google-customer-match-gdm-end

.. destination-google-customer-match-gdm-beta-start

.. admonition:: Beta

   The Google Customer Match (GDM) connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-google-customer-match-gdm-beta-end

.. destination-google-customer-match-gdm-start

Use |destination-name| to sync an Amperity audience to a Google Customer Match user list, so you can target those customers across Google Search, Shopping, Gmail, YouTube, and Display.

Each member is matched to Google users on a single identifier that you choose when you configure the destination: an **email** address, a **phone** number, or a **mobile-id** (mobile advertising ID). Amperity applies SHA-256 hashing to email and phone values before sending them; plaintext identifiers never leave Amperity. Phone numbers are converted to E.164 format first, and a number with no country code is treated as a US number, so supply non-US numbers already in E.164 format. Mobile advertising IDs are sent as-is, because Google does not accept them hashed.

A member whose chosen identifier is missing or cannot be used — a phone number that does not parse, for example — is dropped and reported as a failed row, so that one bad member does not fail the whole run.

The query or segment sent to |destination-name| must return the one column that matches the configured **Match identifier** — an **email**, **phone**, or **mobile-id** column — and only that column.

.. note:: |destination-name| is a separate connector from Google Customer Match, which sends audiences over an older Google API. This connector uses Google's newer Data Manager platform and authenticates as your own Google account. Existing audiences are not shared between the two connectors.

.. destination-google-customer-match-gdm-end

.. destination-google-customer-match-gdm-data-shape-start

The query behind a **Send to** orchestration is not checked against the connector's schema before it runs, so a query that returns the wrong column is not caught up front. Make sure the query returns:

* Exactly one column, named for the configured **Match identifier** and spelled exactly as Amperity reads it: ``email``, ``phone``, or ``mobile-id``. Note that ``mobile-id`` is hyphenated, not ``mobile_id``.
* No other columns. Any extra column is ignored, not rejected.

That column is also the key Amperity uses to track audience membership, so it must stay fixed: changing the **Match identifier** after the audience exists means recreating the audience. A query that omits the configured column, or returns a different one, still runs — every member then fails to match, the audience is left unchanged, and the run reports every row as failed with no error raised beforehand.

.. destination-google-customer-match-gdm-data-shape-end

.. destination-google-customer-match-gdm-api-note-start

.. note:: This destination uses the `Google Data Manager API <https://developers.google.com/data-manager/api>`__ |ext_link|.

.. destination-google-customer-match-gdm-api-note-end

.. destination-google-customer-match-gdm-behavior-start

.. important:: |destination-name| updates membership incrementally. Each run sends only the members who joined or left the audience since the last run: new members are added, and members who left are removed individually by name. Members already in the audience are left in place and reported as unchanged. Amperity tracks these membership changes itself, so it never resends the full audience.

.. caution:: A single identifier is sent per member — the **Match identifier** you configure applies to every member of the audience. Because that identifier is also how Amperity tracks membership, it cannot be changed without recreating the audience, and match rates are typically lower than a connector that sends several identifiers per person. Per-member consent signals are not sent, so a segment sent to |destination-name| must already exclude anyone who has denied ad personalization or ad user data.

.. note:: Membership changes are applied in the background and can take from minutes to days to take effect. Amperity reports members as delivered once Google accepts them. A successful orchestration means Google accepted the members, not that they are in the audience yet — confirm the audience member count in the Google Ads interface. Google also reports success for removing a member who was not in the audience, so only the member count in Google can confirm a removal. When Google rejects members within a batch, Amperity reports them as failed rows with Google's explanation in the run's error log, and the rest of the batch is still sent.

.. caution:: Amperity can only update an audience it created. If the configured **Audience name** matches an audience that was shared into the account from elsewhere, the run fails with an error that names the audience rather than writing to it.

.. note:: The connected Google account must directly administer the account named in **Customer ID**. Manager account (MCC) setups, where the login reaches the account indirectly through a manager account, are not supported. Google also refuses membership changes when the account is disabled, or when it has campaigns that are missing the required European Union political advertising declaration; both are resolved in the Google account.

.. destination-google-customer-match-gdm-behavior-end


.. _destination-google-customer-match-gdm-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-google-customer-match-gdm-get-details-table-start

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
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

          .. important:: Authentication for |destination-name| *must* be completed within Google, using the **Connect with Google** sign-in flow, before configuring Amperity to send |what-send| to |where-send|. During sign-in, approve access to Google's Data Manager service.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Customer product**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-product-start
             :end-before: .. setting-google-customer-match-gdm-customer-product-end

       **Customer ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-id-start
             :end-before: .. setting-google-customer-match-gdm-customer-id-end

       **Match identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-match-identifier-start
             :end-before: .. setting-google-customer-match-gdm-match-identifier-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-name-start
             :end-before: .. setting-google-customer-match-gdm-audience-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional configuration settings**

       **Audience description**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-description-start
             :end-before: .. setting-google-customer-match-gdm-audience-description-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-membership-duration-start
             :end-before: .. setting-google-customer-match-gdm-membership-duration-end

.. destination-google-customer-match-gdm-get-details-end


.. _destination-google-customer-match-gdm-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Google Customer Match (GDM)**

.. destination-google-customer-match-gdm-credentials-steps-start

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

       .. note:: Amperity provides two Google Customer Match connectors. Select |plugin-name| to sync audiences over Google's Data Manager platform. **Google Customer Match** is the separate connector that uses an older Google API.

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
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-google-customer-match-gdm-credentials-steps-end


.. _destination-google-customer-match-gdm-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Google Customer Match (GDM)**

.. destination-google-customer-match-gdm-add-steps-start

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

       **Customer product**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-product-start
             :end-before: .. setting-google-customer-match-gdm-customer-product-end

       **Customer ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-customer-id-start
             :end-before: .. setting-google-customer-match-gdm-customer-id-end

       **Match identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-match-identifier-start
             :end-before: .. setting-google-customer-match-gdm-match-identifier-end

       **Audience name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-name-start
             :end-before: .. setting-google-customer-match-gdm-audience-name-end

       **Audience description**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-audience-description-start
             :end-before: .. setting-google-customer-match-gdm-audience-description-end

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-google-customer-match-gdm-membership-duration-start
             :end-before: .. setting-google-customer-match-gdm-membership-duration-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-frequency-start
             :end-before: .. setting-common-membership-duration-frequency-end

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

.. destination-google-customer-match-gdm-add-steps-end
