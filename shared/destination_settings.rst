.. 
.. shared settings for destinations
.. 



**LOREM IPSUM**

.. TODO: Placeholder content for testing and validation.

.. setting-lorem-ipsum-long-start

Lorem ipsum dolor sit amet, duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. setting-lorem-ipsum-long-end

.. setting-lorem-ipsum-short-start

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. setting-lorem-ipsum-short-end

.. setting-lorem-ipsum-alt-start

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

.. setting-lorem-ipsum-alt-end




**COMMON**

This section contains destination settings that are identical across more than one destination.


**Audience primary key**

Applies to: ActiveCampaign, Cordial, Criteo, HubSpot, Klaviyo, Listrak, Microsoft Ads, Oracle Eloqua, Pinterest, and Sailthru.

.. setting-common-audience-primary-key-start

The primary key for the audience. Set to "email".

.. setting-common-audience-primary-key-end






**ACTIVECAMPAIGN**

This section contains destination settings that are unique to ActiveCampaign.

**Audience primary key**

See common settings.

**Group name**

.. setting-active-campaign-group-name-start

The user group to which Amperity will send data. This group must exist in |destination-name| and must have permission to view and interact with the contact list.

.. setting-active-campaign-group-name-end

**List name**

.. setting-active-campaign-list-name-start

The name of the contact list in |destination-name| that will be managed by Amperity.

.. setting-active-campaign-list-name-end

**Verbose logging**

.. setting-active-campaign-verbose-logging-start

Enable to return log details when |destination-name| rejects adding contacts to the contact list.

When this setting is enabled, a list of rejected contacts is returned by the response from ActiveCampaign. For each rejected contact, a contact identifier is provided along with a string that describes the reason why the contact was rejected.

.. setting-active-campaign-verbose-logging-end
