.. 
.. /markdown
.. 

.. |destination-name| replace:: ActiveCampaign
.. |audience-primary-key| replace:: "email"


ActiveCampaign
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-active-campaign-start
   :end-before: .. term-active-campaign-end


Requirements
==================================================

.. TODO: This destination has the following requirements.

#. The API key and base URL for your |destination-name| account.

   Learn more about the `ActiveCampaign REST API <https://developers.activecampaign.com/reference/url>`__.

#. .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-list-name-start
      :end-before: .. setting-active-campaign-list-name-end

   Learn more about |destination-name| `contacts lists <https://help.activecampaign.com/hc/en-us/articles/360000030559-How-to-create-a-list-in-ActiveCampaign>`__.

#. .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-group-name-start
      :end-before: .. setting-active-campaign-group-name-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-group-name-access-start
      :end-before: .. setting-active-campaign-group-name-access-end

   Learn more about |destination-name| `user groups <https://help.activecampaign.com/hc/en-us/articles/115000090164#setting-user-permissions-create-user-groups-0-0>`__.

#. .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-email-required-start
      :end-before: .. setting-active-campaign-email-required-end


Settings
==================================================

.. TODO: Configure the following settings.

**Group name**

   **Required**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-group-name-start
      :end-before: .. setting-active-campaign-group-name-end


**List name**

   **Required**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-list-name-start
      :end-before: .. setting-active-campaign-list-name-end


**Audience primary key**

   **Required**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-audience-primary-key-start
      :end-before: .. setting-common-audience-primary-key-end


**Verbose logging?**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-active-campaign-verbose-logging-start
      :end-before: .. setting-active-campaign-verbose-logging-end


**Business user access**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-business-user-access-allow-start
      :end-before: .. setting-common-business-user-access-allow-end

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-common-business-user-access-restrict-pii-start
      :end-before: .. setting-common-business-user-access-restrict-pii-end
