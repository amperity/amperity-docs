.. https://docs.amperity.com/reference/

:orphan:

.. meta::
    :description lang=en:
        Frequently asked questions about AmpAI.

.. meta::
    :content class=swiftype name=body data-type=text:
        Frequently asked questions about AmpAI.

.. meta::
    :content class=swiftype name=title data-type=string:
        AmpAI Privacy FAQ

==================================================
AmpAI Privacy FAQ
==================================================

.. ampai-privacy-start

AmpAI is powered by models that reside on Azure OpenAI Service.

Azure OpenAI Service has the following data sharing policies:

* No data is available to or shared with other customers
* No data is available to OpenAI
* No data is used to improve OpenAI models
* No data is used to improve any Microsoft or 3rd party products or services

You can read more details on the Azure OpenAI Service data and privacy policy `here <https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy?tabs=azure-portal>`__ |ext_link|.

.. ampai-privacy-end


.. _ampai-azure-openai-service-store:

What data does the Azure OpenAI Service store?
==================================================

.. ampai-azure-openai-service-store-start

Azure OpenAI Service does not store any data after the API response is returned. AmpAI's implementation is stateless and all context must be sent to Azure OpenAI Service with each API call.

.. ampai-azure-openai-service-store-end


.. _ampai-amperity:

What data does Amperity store?
==================================================

.. ampai-amperity-start

Amperity stores conversation history in the same secure location as existing tenant data. This data is isolated per tenant and is never aggregated or intermixed between or across tenants.

.. ampai-amperity-end


.. _ampai-azure-openai-service-process:

What data does the Azure OpenAI Service process?
==================================================

.. ampai-azure-openai-service-process-start

There are two types of data Amperity sends to the Azure OpenAI Service:

* Data to improve model performance. This includes database schema information, tables names, fields and descriptions, the current query's SQL, a sample of results from the query, and any errors encountered.
* AmpAI message history. Amperity sends the full message history for a given conversation to Azure OpenAI Service to maintain the context of the conversation.

.. ampai-azure-openai-service-process-end


.. _ampai-azure-openai-service-not-sent:

What data is not sent to Azure OpenAI Service?
==================================================

.. ampai-azure-openai-service-not-sent-start

Amperity sends only the data needed to ensure effective operation of the Azure OpenAI Service and no data is stored at rest in the Azure OpenAI service. In addition, Amperity restricts the use of the service to limit access to data:

* Extensive customer PII. Amperity will send a sample of query results to the Azure OpenAI Service which may contain PII.
* Credentials. Amperity does not send any stored upstream or downstream credentials (usernames and passwords) to Azure OpenAI Service.

.. ampai-azure-openai-service-not-sent-end
