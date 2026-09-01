.. /downloads/markdown/


.. |destination-name| replace:: Salesforce Marketing Cloud
.. |what-send| replace:: data extension rows
.. |where-send| replace:: |destination-name|


SFMC Data Extension Row
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-marketing-cloud-start
   :end-before: .. term-salesforce-marketing-cloud-end

Insert or update a single |destination-name| data extension row as soon as Amperity sees the customer interaction, using the `synchronous data extension rowset <https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc-data_extension_rows_sync>`__ |ext_link| endpoint. Each real-time point becomes one row. |destination-name| upserts on the data extension's primary key, so a point for a customer already in the data extension updates that row rather than adding another.

The data extension is the target of this connector. To enter a customer into a journey, use the **SFMC Journey** connector; to send a transactional message, use the **SFMC Messaging** connector. To load data extensions on a schedule rather than in real time, use the `Salesforce Marketing Cloud destination <https://docs.amperity.com/operator/destination_salesforce_marketing_cloud.html>`__ |ext_link|.

This connector is currently in beta. Contact your Amperity representative to learn more.


Requirements
==================================================

#. The data extension must already exist in |destination-name|. This connector writes rows to a data extension; it does not create one.

#. The data extension must have at least one field marked as a primary key, which is what makes the write an upsert. |destination-name| rejects a row that does not supply every primary key field.

#. The installed package that issues the API credentials must have the **Data Extensions: Read, Write** permission for the business unit that owns the data extension.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**API authentication subdomain**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-salesforce-marketing-cloud-api-subdomain-start
   :end-before: .. credential-salesforce-marketing-cloud-api-subdomain-end

**API client ID and client secret**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-salesforce-marketing-cloud-api-client-secret-start
   :end-before: .. credential-salesforce-marketing-cloud-api-client-secret-end


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

**Account ID**

The ID of the business unit to target, also known as the MID. Leave this unset to target whichever business unit created the installed package that issues the credentials. Set it to write to a different business unit; the installed package must have access to that business unit.


Activate node settings
==================================================

The rest of the configuration for this connector belongs to the journey that sends to it. Add this destination to an **Activate** node, then configure the following fields on that node. Two nodes may send to the same destination and write to different data extensions.

**Data extension external key**

Required. The data extension's external key, found on the data extension's **Properties** tab in **Contact Builder**. This is the external key, not the data extension name; |destination-name| returns an error for a key it cannot resolve.

**Primary key**

Required. The data extension fields that identify the row, mapped to the Amperity attributes that supply their values. These must be primary key fields on the data extension, and a composite primary key needs one entry per field. Map the value your sends key on, such as the subscriber key or email address: a row keyed on anything else is a write that nothing in |destination-name| will read.

**Row columns**

Required. The data extension's field names, mapped to the Amperity attributes or literal values written to them. Names must match the data extension's field names exactly. A column whose attribute is left unset is omitted from the write, which leaves any existing value in that column in place rather than clearing it.
