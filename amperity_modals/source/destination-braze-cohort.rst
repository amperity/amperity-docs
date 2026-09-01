.. /downloads/markdown/


.. |destination-name| replace:: Braze Cohorts
.. |what-send| replace:: audience lists
.. |where-send| replace:: |destination-name|


Braze Cohorts
==================================================

|destination-name| allows you to send a list of user IDs from Amperity to Braze using the `User cohort <https://www.braze.com/docs/partners/isv_partners/cohort_import/>`__ |ext_link| endpoint, after which they are automatically added to a named cohort. You can then use that cohort with Braze campaigns and canvases.

This destination only syncs user ID lists into cohorts. It does not sync profile attributes, events, or purchase data. To send customer profile attributes to Braze, use the `Braze destination <https://docs.amperity.com/operator/destination_braze.html>`__ |ext_link|.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Client Data Import Key**

Required. The Data Import Key from your Braze dashboard. This key is found under **Partner Integrations > Technology Partners > Amperity**.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Business user access**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-allow-start
   :end-before: .. setting-common-business-user-access-allow-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-restrict-pii-start
   :end-before: .. setting-common-business-user-access-restrict-pii-end

**Instance**

Required. Select the `Braze instance <https://www.braze.com/docs/user_guide/administrative/access_braze/braze_instances>`__ |ext_link| where your account is provisioned. May be one of "US-01", "US-02", "US-03", "US-04", "US-05", "US-06", "US-07", "EU-01", "EU-02", "AU-01", "JP-01", "ID-01", or "KR-01".

**User identifier field**

Required. The field in the audience that supplies the Braze user identifier. This must be ``external_id``, which the audience is required to return.

**List name** (Required at orchestration)

Required. The name of the cohort to create or update in Braze, which appears in the Braze dashboard under **Segments**. This setting is configured on the orchestration or campaign rather than on the destination, so one destination can maintain a separate cohort for each audience you send.

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
