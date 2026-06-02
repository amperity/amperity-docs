.. /downloads/markdown/


.. |destination-name| replace:: Cheetah Digital Standard Data Load


Cheetah Digital Standard Data Load
==================================================

The |destination-name| destination loads profile data into a Cheetah Digital (Marigold Engage Plus) recipient list the moment a customer qualifies for real-time activation. Use this destination to keep recipient data current for campaigns that run on Cheetah Digital's own schedule.


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

The activation node payload must include the following field:

**form_id** The API post ID of the recipient list in Cheetah Digital. All profile attributes and custom attributes in the activation node payload are loaded as name-value pairs into this list. Obtain the API post ID from your Cheetah Digital account manager or the Cheetah Digital platform.
