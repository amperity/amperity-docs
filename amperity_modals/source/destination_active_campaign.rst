.. 
.. /markdown
.. 

.. |destination-name| replace:: ActiveCampaign



ActiveCampaign
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-active-campaign-start
   :end-before: .. term-active-campaign-end


Requirements
==================================================

This destination has the following requirements.

#. The API key for your instance of |destination-name|.
#. The ActiveCampaign API `endpoint URL <https://developers.activecampaign.com/reference/url>`__.

   The |destination-name| API is rate limited to 5 requests per second.
#. The name of a `user group <https://help.activecampaign.com/hc/en-us/articles/115000090164#setting-user-permissions-create-user-groups-0-0>`__ that exists in |destination-name| and has permission to view and interact with the contact list.

   You must log into |destination-name| as a member of the specified user group to have access to the contact list that is managed by Amperity.

#. The name of a `contacts list <https://help.activecampaign.com/hc/en-us/articles/360000030559-How-to-create-a-list-in-ActiveCampaign>`__ in |destination-name|. This can be the name of an existing list or a new list.

#. A query or campaign that outputs from Amperity the fields that map to the contacts in |destination-name|.


Settings
==================================================

Configure the following settings.

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
