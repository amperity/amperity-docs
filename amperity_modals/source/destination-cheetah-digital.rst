.. /downloads/markdown/


.. |destination-name| replace:: Cheetah Digital Advanced Event Trigger


Cheetah Digital Advanced Event Trigger
==================================================

The |destination-name| destination triggers a campaign in Cheetah Digital (Marigold Engage Plus) the moment a customer qualifies for a journey activation step. Amperity calls the Campaign Trigger API directly using username and password authentication.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Username**

The username for your Cheetah Digital account. Not a secret value — visible after saving.

**Password**

The password for your Cheetah Digital account.


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Required payload fields**

The activation node payload must include the following fields:

**cheetah_digital_campaign_id** The ID of the campaign to trigger. Obtain from your Cheetah Digital account manager or the Cheetah Digital platform.

**cheetah_digital_table** The table ID for data import. Obtain from your Cheetah Digital account manager or the Cheetah Digital platform.
