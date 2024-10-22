.. 
.. /markdown
.. 

.. |destination-name| replace:: Meta Offline Events
.. |what-send| replace:: offline events
.. |where-send| replace:: |destination-name|


Meta Offline Events
==================================================

.. TODO: Sync this with the updated events topics.

Send offline events to |destination-name| to help your brand track offline conversions that result from your marketing campaigns. Offline events may be matched with audiences in Facebook, Facebook Messenger, Instagram, and WhatsApp.

Transaction events that occurred within the previous seven days *and* contain positive values for product quantity may be sent to |destination-name| using the |ext_facebook_conversions_api_offline_events|.

The first time transaction events are sent to |destination-name|, seven days of data is sent, after which Amperity should be configured to send daily updates, which will maintain a 7-day rolling window of transaction events.


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
