.. /downloads/markdown/


.. |destination-name| replace:: Braze
.. |what-send| replace:: API-triggered campaigns
.. |where-send| replace:: |destination-name|


Braze Real-Time API-Triggered Campaign
==================================================

Send an API-triggered |destination-name| campaign to a single recipient as soon as Amperity sees the customer interaction that should trigger it, using the `send triggered campaign messages <https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/>`__ |ext_link| endpoint. Each real-time point becomes one recipient. The same request can update that user's |destination-name| profile attributes and pass trigger properties to the campaign for personalization.

Use this connector when Amperity decides that the campaign should go out. For a campaign that |destination-name| triggers itself, off a custom event or an attribute change, use the **Braze Real-Time Action-Based Campaign** connector instead. To send customer profile attributes on a schedule rather than in real time, use the `Braze destination <https://docs.amperity.com/operator/destination_braze.html>`__ |ext_link|.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API key**

Required. The |destination-name| REST API key for your account. The key must have the **campaigns.trigger.send** permission, and also **users.track** if you map any user attributes.

Create or find a REST API key in the |destination-name| dashboard under **Settings > API Keys**. A REST API key is scoped to a single |destination-name| instance, so the key must belong to the same instance you configure for this destination.


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

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-braze-instance-start
   :end-before: .. setting-braze-instance-end


Activate node settings
==================================================

The rest of the configuration for this connector belongs to the journey that sends to it. Add this destination to an **Activate** node, then configure the following fields on that node. Two nodes may send to the same destination with different campaigns, identifiers, and attributes.

**Campaign API identifier**

Required. The API identifier of the campaign to trigger, found on that campaign's **Settings** tab in |destination-name|. The campaign must be an API-triggered campaign; |destination-name| rejects a trigger request for any other campaign type.

**Braze user identifier**

Required. The identifier |destination-name| matches the recipient on. May be "external_user_id" or "email". |destination-name| accepts only one identifier per recipient, so this choice decides which one Amperity sends.

**Identifier attribute**

The Amperity attribute that supplies the value for the identifier selected above. Leave this unset to send the Amperity profile ID as the "external_user_id".

**Only send to users who already exist in Braze**

Enabled by default, so that a customer |destination-name| does not recognize is skipped. Clear this option only if you want |destination-name| to create a new user profile for an unrecognized recipient.

**Braze user attributes**

Attributes written to the |destination-name| user profile alongside the send. |destination-name| sorts each name into one of its own standard profile fields or into a new custom attribute by exact, case-sensitive match, so "first_name" updates the standard field while "First_Name" creates a custom attribute. |destination-name| identity fields, such as "external_id" and "braze_id", cannot be set here; use the **Identifier attribute** field instead.

**API trigger properties**

Attributes sent as `trigger properties <https://www.braze.com/docs/api/objects_filters/trigger_properties_object/>`__ |ext_link| for this send. Reference these in the campaign's message body to personalize it. Trigger properties apply to a single send and are not stored on the |destination-name| user profile.
