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

The Data Import Key from your Braze dashboard. This key is found under **Partner Integrations > Technology Partners > Amperity**.

**Instance**

The Braze REST API instance identifier for your account (for example: "US-01", "US-02", "EU-01", or "JP-01"). This is in your Braze dashboard URL or account settings.


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

**Cohort Name**

The name of the cohort to create or update in Braze. This name appears in the Braze dashboard under **Segments**.

**User ID Field**

The name of the column in your query or segment results that contains the Braze user identifier. Defaults to ``external_id``. If your Braze users are identified by email or a custom field, set this value to match the column name in your query results.

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
