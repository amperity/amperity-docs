.. /downloads/markdown/


.. |destination-name| replace:: Braze
.. |what-send| replace:: custom events and profile attributes
.. |where-send| replace:: |destination-name|


Braze Real-Time Action-Based Campaign
==================================================

Log a custom event and update user profile attributes in |destination-name| as soon as Amperity sees the customer interaction, using the `track users <https://www.braze.com/docs/api/endpoints/user_data/post_user_track/>`__ |ext_link| endpoint. |destination-name| owns the send: configure an action-based campaign or canvas in the |destination-name| dashboard that is entered by the event Amperity logs, or by a change to one of the attributes Amperity writes.

Use this connector when |destination-name| should decide whether the customer is messaged. If Amperity should trigger the campaign directly, use the **Braze Real-Time API-Triggered Campaign** connector instead. To send customer profile attributes on a schedule rather than in real time, use the `Braze destination <https://docs.amperity.com/operator/destination_braze.html>`__ |ext_link|.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API key**

Required. The |destination-name| REST API key for your account. The key must have the **users.track** permission.

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

The rest of the configuration for this connector belongs to the journey that sends to it. Add this destination to an **Activate** node, then configure the following fields on that node. Two nodes may send to the same destination with different event names, identifiers, and attributes.

**Event name**

Required. The name of the custom event logged in |destination-name|. Use this name as the trigger for an action-based campaign or canvas in the |destination-name| dashboard. |destination-name| creates a custom event the first time it receives one, so the name here and the name the campaign listens for must match exactly.

**Event properties**

Attributes sent as properties of the custom event. Reference these in the campaign's message body to personalize it, or use them in the campaign's entry criteria. Event properties belong to a single event and are not stored on the |destination-name| user profile.

**Braze user identifier**

Required. The identifier |destination-name| matches the user on. May be "external_id", "braze_id", "email", or "phone". |destination-name| accepts only one identifier per request, so this choice decides which one Amperity sends. Note that "email" and "phone" are secondary identifiers in |destination-name| and match a user only when no primary identifier is present on the request.

**Identifier attribute**

The Amperity attribute that supplies the value for the identifier selected above. Leave this unset to send the Amperity profile ID as the "external_id".

**Only update users who already exist in Braze**

Enabled by default, so that a customer |destination-name| does not recognize is skipped. Clear this option only if you want |destination-name| to create a new user profile for an unrecognized customer.

**Braze user attributes**

Attributes written to the |destination-name| user profile. |destination-name| sorts each name into one of its own standard profile fields or into a new custom attribute by exact, case-sensitive match, so "first_name" updates the standard field while "First_Name" creates a custom attribute. |destination-name| identity fields, such as "external_id" and "braze_id", cannot be set here; use the **Identifier attribute** field instead.

A campaign may be triggered by a change to one of these attributes rather than by the event name, which lets a single Activate node feed several campaigns.
