.. /downloads/markdown/


.. |destination-name| replace:: Listrak Messaging


Listrak Messaging
==================================================

The |destination-name| destination triggers a transactional email or SMS message the moment a customer qualifies for a journey activation step. Profile attributes are passed as per-send personalization overrides to the configured message template. This destination sends to contacts who are already subscribed in Listrak.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Email client ID** (Required for email channel)

The client ID from your Listrak email API integration. In Listrak, navigate to **Account Settings > API Keys** and select the **Email** integration.

**Email client secret** (Required for email channel)

The client secret from your Listrak email API integration.

**SMS client ID** (Required for SMS channel)

The client ID from your Listrak SMS API integration. In Listrak, navigate to **Account Settings > API Keys** and select the **SMS** integration.

**SMS client secret** (Required for SMS channel)

The client secret from your Listrak SMS API integration.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Channel**

The messaging channel for this destination. One of: **email** or **sms**.

**List ID** (Required for email channel)

The Listrak email list ID. In Listrak, open **List Manager** and note the list ID for the list that contains your subscribed contacts.

**Transactional message ID**

The ID of the transactional message template to trigger. In Listrak, navigate to the **Transactional** section of the configured list (email) or phone list (SMS) and note the message ID.

**Sender code ID** (Required for SMS channel)

The Listrak SMS sender code ID. In Listrak, navigate to **SMS > Short Codes** and note the sender code ID.

**Phone list ID** (Required for SMS channel)

The Listrak SMS phone list ID. In Listrak, navigate to the SMS phone list and note its ID.

**Required payload fields**

**email** (Required for email channel) The recipient's email address. Must match a subscribed contact in the configured Listrak list.

**phone** (Required for SMS channel) The recipient's phone number. Must match a subscribed contact in the configured Listrak phone list.
