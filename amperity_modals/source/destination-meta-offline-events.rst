.. /downloads/markdown/


.. |destination-name| replace:: Meta Events
.. |what-send| replace:: events
.. |where-send| replace:: |destination-name|


Meta Events
==================================================

.. TODO: Sync this with the updated events topics.

Send conversion events to |destination-name| using the Meta `Conversions API <https://developers.facebook.com/docs/marketing-api/conversions-api>`__ |ext_link| to measure and attribute the conversions that result from your advertising, to optimize ad delivery, and to deduplicate server-side events against browser (Pixel) events. Conversions may happen offline (such as a purchase in a physical store) or online (such as a purchase on a website).

The Conversions API is a separate Meta product from custom audiences (Meta Ads Manager), which build targeting audiences using the Meta Marketing API.

Transaction events that occurred within the previous seven days *and* contain positive values for product quantity may be sent to |destination-name| using the Conversions API.

.. include:: ../../amperity_user/source/events_meta_ads_manager.rst
   :start-after: .. events-meta-ads-manager-overview-window-start
   :end-before: .. events-meta-ads-manager-overview-window-end


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Refresh token**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-oauth-refresh-token-start
   :end-before: .. credential-oauth-refresh-token-end


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

**Dataset ID**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-meta-ads-manager-dataset-id-start
   :end-before: .. setting-meta-ads-manager-dataset-id-end

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
