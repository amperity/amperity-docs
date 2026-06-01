.. /downloads/markdown/


.. |destination-name| replace:: Klaviyo Messaging


Klaviyo Messaging
==================================================

The |destination-name| destination sends a resolved customer profile to Klaviyo the moment a customer qualifies for a journey activation step. Use this destination to track a Klaviyo event to trigger a flow, upsert a profile with current attributes, or remove a profile from a list.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API key**

A Klaviyo private API key with read/write access to Events and Profiles. Generate it in Klaviyo under **Account > Settings > API Keys**. Alternatively, use a Klaviyo OAuth refresh token.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Operation**

The action to perform in Klaviyo. One of:

* **event** — Track a behavioral event. The event metric name is set by the **Target** field. Use to trigger Klaviyo flows.
* **profile_upsert** — Create or update a Klaviyo profile with the attributes sent from the activation node.
* **list_remove** — Remove a profile from a Klaviyo list. The list ID is set by the **Target** field.

**Target** (Required when operation is **event** or **list_remove**)

The Klaviyo event metric name (for **event**) or list ID (for **list_remove**).

**Required schema fields**

**email** The primary identifier for the Klaviyo profile. Required in all payloads.

**external_id** The Amperity ID used as the Klaviyo external ID for cross-system identity linking. Required in all payloads.

**phone_number** E.164 format, such as ``+15551234567``. Required for SMS-enabled profiles.

**klaviyo_profile_id** The Klaviyo internal profile ID. Required when operation is **list_remove**.
