.. /downloads/markdown/


.. |destination-name| replace:: Cordial Send


Cordial Send
==================================================

The |destination-name| destination triggers a Cordial automation template send for a single contact the moment a customer qualifies for a journey activation step. Profile attributes are upserted to the contact record in Cordial at the time of send. Custom attributes in the payload are passed as template variables.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API key**

The Cordial API key used to authenticate requests. In Cordial, navigate to **Settings > API Keys** and create or copy an API key with permission to send automations and upsert contacts.

**API URL**

Your Cordial tenant API base URL, such as ``https://api.cordial.io``. This value is provided by Cordial when your account is provisioned.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Contact identifier field**

The field used to identify the contact in Cordial. One of: **email**, **phone**, or **custom_key**.

**Custom key name** (Required when contact identifier field is **custom_key**)

The attribute name used as the contact's custom identifier in Cordial. The payload must include a field with this name.

**Include subscribe status** (Optional)

When enabled, the send payload includes a ``subscribeStatus: "subscribed"`` value in the contact's ``channels`` object. Use when you want the send to opt in a contact who is not yet subscribed.

**Required payload fields**

**template-key** The unique key of the published Cordial automation template to trigger. In Cordial, navigate to **Automation** and open the template to find its key.

**email** (Required when contact identifier field is **email**) The recipient's email address.

**phone** (Required when contact identifier field is **phone**) The recipient's phone number.
