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

   The user group to which Amperity will send data. This group must exist in |destination-name| and must have permission to view and interact with the contact list.


**List name**

   **Required**

   The name of the contact list in |destination-name| that will be managed by Amperity


**Audience primary key**

   **Required**

   Set to "email".


**Verbose logging?**

   Enable to return log details when |destination-name| rejects adding contacts to the contact list.

   When this setting is enabled, a list of rejected contacts is returned by the response from ActiveCampaign. For each rejected contact, a contact identifier is provided along with a string that describes the reason why the contact was rejected.
