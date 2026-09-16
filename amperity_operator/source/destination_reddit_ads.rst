.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Reddit Ads
.. |destination-api| replace:: Reddit Ads API
.. |plugin-name| replace:: "Reddit"
.. |credential-type| replace:: "reddit"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audience segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "red"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Reddit Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Reddit Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Reddit Ads

==================================================
Configure destinations for Reddit Ads
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-reddit-ads-start
   :end-before: .. term-reddit-ads-end

.. destination-reddit-ads-start

Use Amperity to build audience segments and send them to |destination-name| as custom audiences for ad targeting. Amperity normalizes and SHA-256 hashes email addresses before sending them to |destination-name|, where they are matched to Reddit accounts and made available for campaign targeting.

.. destination-reddit-ads-end

.. destination-reddit-ads-api-note-start

.. note:: This destination uses the `Reddit Ads API v3 <https://ads-api.reddit.com/docs/v3/>`__ |ext_link|.

.. destination-reddit-ads-api-note-end


.. _destination-reddit-ads-howitworks:

How this destination works
==================================================

.. destination-reddit-ads-howitworks-start

Amperity sends audience data to |destination-name| using an incremental workflow. Each run sends only additions and removals since the previous run. Amperity creates the custom audience in |destination-name| automatically on the first run and reuses it on subsequent runs.

.. destination-reddit-ads-howitworks-end

.. destination-reddit-ads-howitworks-table-start

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
     - **RESOLVE CUSTOM AUDIENCE**

       Amperity searches the ad account for a custom audience that matches the configured name. The search is case-insensitive and compares exact names across all audiences in the account.

       If no matching audience is found, Amperity creates a new **CUSTOMER_LIST** custom audience using the `POST /api/v3/ad_accounts/{id}/custom_audiences <https://ads-api.reddit.com/docs/v3/operations/Create%20Custom%20Audience>`__ |ext_link| endpoint. When no list name is configured, the audience name defaults to "Amperity - " followed by the segment name.

       The Reddit audience ID is stored internally and used on subsequent runs. If the audience is deleted in |destination-name| and recreated, Amperity detects the mismatch and rebuilds the full membership on the next run.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **NORMALIZE AND HASH EMAILS**

       |destination-name| requires email normalization to values in the **email** column before hashing email addresses. Amperity:

       #. Converts to lowercase and trims whitespace.
       #. Strips ``+alias`` suffixes from the local part (``user+tag@example.com`` becomes ``user@example.com``).
       #. Removes dots from the local part (``f.i.r.s.t@example.com`` becomes ``first@example.com``).
       #. SHA-256 hashes the result.

       Rows with a missing or unparseable email address are counted as failed rows.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **SEND ADDITIONS**

       Amperity sends new audience members to |destination-name| using the `PATCH /api/v3/custom_audiences/{id}/users <https://ads-api.reddit.com/docs/v3/operations/Update%20Custom%20Audience%20Users>`__ |ext_link| endpoint with action type **ADD**, in batches of up to 2,500 rows with five concurrent requests.

       Additions are always sent before removals to preserve the 1,000-user minimum audience threshold required by |destination-name|.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - **SEND REMOVALS AND END WORKFLOW**

       Audience members removed from the segment in Amperity are sent to |destination-name| using the same endpoint with action type **REMOVE**, in batches of up to 2,500 rows with five concurrent requests.

       The workflow ends after all additions and removals are sent.

.. destination-reddit-ads-howitworks-table-end


.. _destination-reddit-ads-sftp:

Send audiences via SFTP
==================================================

.. destination-reddit-ads-sftp-start

You can also send audience data to |destination-name| as a CSV file using SFTP. Contact your Reddit Ads representative for SFTP credentials and file format requirements, and then configure Amperity to connect to |destination-name| using the :doc:`SFTP <destination_sftp>` destination.

.. destination-reddit-ads-sftp-end


.. _destination-reddit-ads-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-reddit-ads-get-details-table-start

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
             :start-after: .. credential-reddit-ads-refresh-token-start
             :end-before: .. credential-reddit-ads-refresh-token-end

          .. tip:: Contact your Reddit Ads representative to initiate the OAuth2 authorization flow and obtain a refresh token.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required destination settings**

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-ad-account-id-start
             :end-before: .. setting-reddit-ads-ad-account-id-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional orchestration settings**

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-list-name-start
             :end-before: .. setting-reddit-ads-list-name-end

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
     - A query or segment that returns an **email** column. Amperity normalizes and hashes email addresses before sending them to |destination-name|.

.. destination-reddit-ads-get-details-end


.. _destination-reddit-ads-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Reddit Ads**

.. destination-reddit-ads-credentials-steps-start

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
             :start-after: .. credential-reddit-ads-refresh-token-start
             :end-before: .. credential-reddit-ads-refresh-token-end

.. destination-reddit-ads-credentials-steps-end


.. _destination-reddit-ads-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Reddit Ads**

.. destination-reddit-ads-add-steps-start

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

       **Ad account ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-ad-account-id-start
             :end-before: .. setting-reddit-ads-ad-account-id-end

       **List name** (Optional)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-reddit-ads-list-name-start
             :end-before: .. setting-reddit-ads-list-name-end

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

.. destination-reddit-ads-add-steps-end


.. TODO: Add workflow resolutions from existing topics HERE.
