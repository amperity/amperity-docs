.. /downloads/markdown/


.. |destination-name| replace:: SFMC Transactional Messaging


SFMC Transactional Messaging
==================================================

The |destination-name| destination triggers a transactional email, SMS, or push message through Salesforce Marketing Cloud the moment a customer qualifies for a journey activation step. Use this destination for order confirmations, loyalty status updates, password resets, and other individually triggered transactional messages personalized with Amperity-known profile attributes.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Subdomain**

The Salesforce Marketing Cloud (SFMC) API authentication subdomain — the portion of your tenant URL before ``.auth.marketingcloudapis.com``. For example, if your auth URL is ``mc1a2b3c4d5e6f7g8h9.auth.marketingcloudapis.com``, the subdomain is ``mc1a2b3c4d5e6f7g8h9``. Not a secret value.

**Client ID**

The client ID from your SFMC installed package. Not a secret value. In SFMC, navigate to **Setup > Platform Tools > Apps > Installed Packages** and open or create a Server-to-Server API integration component.

**Client secret**

The client secret from your SFMC installed package.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Channel**

The messaging channel for this destination. One of: **email**, **sms**, or **push**.

**Required payload fields**

**definition_key** The send definition key from the SFMC Transactional Messaging send definition. In SFMC, transactional send definitions are created under **Email Studio > Transactional Sending** (email) or **MobileConnect** (SMS).

**contact_key** The SFMC subscriber key that identifies the recipient. Required for email and SMS. For push, provide either **contact_key** or **to**, but not both.

**to** The recipient address. For SMS: phone number in E.164 format, such as ``+15551234567``. For push: the push registration identifier. For push, provide either **contact_key** or **to**, but not both.
