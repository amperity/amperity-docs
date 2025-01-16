.. /downloads/markdown/


.. |destination-name| replace:: Listrak
.. |audience-primary-key| replace:: "email" or "phone"
.. |what-send| replace:: email and phone lists
.. |where-send| replace:: |destination-name|


Listrak
==================================================

|destination-name| is an automation platform for email and SMS marketing. Use the ActiveCampaign REST API to manage audiences in |destination-name|.

Amperity can manage email and SMS lists in |destination-name| using this destination.

Amperity automatically adds a field attribute to all email and SMS lists that are sent to |destination-name|. This field is located inside a field group named "Amperity Message Attributes" within |destination-name|.

Use SFTP to manage `Customer lists <https://www.listrak.com/product-team/customer-schema>`__ |ext_link|, `Product lists <https://www.listrak.com/product-team/product-schema>`__ |ext_link|, `Order lists <https://www.listrak.com/product-team/order-schema>`__ |ext_link|, and `Order item lists <https://www.listrak.com/product-team/order-items-schema>`__ |ext_link|.

Work with your |destination-name| representatives to determine which of these sets will be useful for your workflows within |destination-name|, and then verify that attributes sent from Amperity are mapped correctly to the appropriate data schema within |destination-name|.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Email client ID and client secret**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-listrak-email-client-id-secret-start
   :end-before: .. credential-listrak-email-client-id-secret-end

**SMS client ID and client secret**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-listrak-sms-client-secret-start
   :end-before: .. credential-listrak-sms-client-secret-end

**Note**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-listrak-allowlist-start
   :end-before: .. credential-listrak-allowlist-end


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

**List name**

(Applies to Email **and** SMS lists.)

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-list-name-start
   :end-before: .. setting-listrak-list-name-end

**Audience primary key**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-audience-primary-key-start
   :end-before: .. setting-common-audience-primary-key-end

**Field group**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-field-group-start
   :end-before: .. setting-listrak-field-group-end

**Segment name**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-segment-name-start
   :end-before: .. setting-listrak-segment-name-end
