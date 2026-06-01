.. /downloads/markdown/


.. |destination-name| replace:: Attentive Events


Attentive Events
==================================================

The |destination-name| destination fires custom events and upserts subscriber attributes in Attentive the moment a customer qualifies for a journey activation step. A single activation can fire an event, write attributes, or do both in one send.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API key**

The Attentive API key used to authenticate requests. The key must have the ``events:write`` and ``attributes:write`` scopes. Generate an API key in the Attentive platform under **Settings > API**.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Operation**

Determines what Amperity sends on each activation. One of:

* **event** — Fires a named custom event. Requires **Event type name**.
* **attribute** — Upserts custom subscriber attributes. Does not fire an event.
* **event_and_attribute** — Upserts attributes first, then fires the event in the same send. Requires **Event type name**.

**Event type name** (Required when operation includes an event)

The name of the custom event in Attentive, exactly as it appears on the journey trigger. The value is case-sensitive.

**Required payload fields**

At least one of the following must be included in the activation node payload:

**email** The subscriber's email address.

**phone_number** The subscriber's phone number in E.164 format, such as ``+12065550100``.
