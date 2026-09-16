.. /downloads/markdown/


.. |destination-name| replace:: Amazon Ads
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |duration| replace:: (in seconds)
.. |duration-value| replace:: "0" - "34,300,800"


Amazon Ads
==================================================

Amazon Ads is an online advertising platform that supports a variety of advertising options, including sponsored, search, display, video, and audio.


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

**Audience name** (Required at orchestration)

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-ads-audience-description-start
   :end-before: .. setting-amazon-ads-audience-description-end

**Audience description** (Required at orchestration)

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-ads-audience-description-start
   :end-before: .. setting-amazon-ads-audience-description-end

**DSP advertiser**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-ads-dsp-advertiser-start
   :end-before: .. setting-amazon-ads-dsp-advertiser-end

**AMC instance**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-ads-amc-instance-start
   :end-before: .. setting-amazon-ads-amc-instance-end

**Membership duration**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-ads-membership-duration-start
   :end-before: .. setting-amazon-ads-membership-duration-end

**Enable consent signals?**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-amazon-ads-enable-consent-signals-start
   :end-before: .. setting-amazon-ads-enable-consent-signals-end

Consent signals are prioritized: 1. Use "tcf" for European Transparency and Consent Framework (TCF) consent signals. 2. Use "gpp" for Global Privacy Protocol (GPP) consent signals. 3. Use "amzn_user_data" and "amzn_ad_storage" for Amazon Consent Signal (ACS) consent signals.

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
 