.. 
.. /markdown
.. 

.. |destination-name| replace:: ActiveCampaign
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: CSV files
.. |where-send| replace:: |destination-name|


ActiveCampaign
==================================================

|destination-name| is an automation platform for email and SMS marketing.


Credentials
==================================================

Amperity requires the `ActiveCampaign REST API key <https://developers.activecampaign.com/reference/authentication>`__ |ext_link| and `base URL <https://developers.activecampaign.com/reference/url>`__ |ext_link| to send audiences to |destination-name|.


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

**Group name**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-active-campaign-group-name-start
   :end-before: .. setting-active-campaign-group-name-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-active-campaign-group-name-access-start
   :end-before: .. setting-active-campaign-group-name-access-end

**List name**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-active-campaign-list-name-start
   :end-before: .. setting-active-campaign-list-name-end

**Audience primary key**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-audience-primary-key-start
   :end-before: .. setting-common-audience-primary-key-end

**Verbose logging?**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-active-campaign-verbose-logging-start
   :end-before: .. setting-active-campaign-verbose-logging-end
