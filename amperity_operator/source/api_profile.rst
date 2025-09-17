.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        How to use the Profile API.

.. meta::
    :content class=swiftype name=body data-type=text:
        How to use the Profile API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Profile API

==================================================
Profile API
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-profile-api-start
   :end-before: .. term-profile-api-end

.. api-profile-learning-lab-start

.. admonition:: Amperity Learning Lab

   Open **Learning Lab** to learn more about how your brand can use the `Profile API <https://learn.amperity.com/profile-api>`__ |ext_link|. Registration is required.

.. api-profile-learning-lab-end


.. _profile-api-howitworks:

How the Profile API works
==================================================

.. profile-api-howitworks-start

Use the profile endpoints in the Amperity API to access customer profile indexes in your Amperity tenant. Any collection of customer profile attributes that can be included in a customer 360 table can be accessed from a Profile API endpoint.

Each endpoint is defined by a query that you build in the **Queries** page, after which it may be generated as an index within the Profile API. A query defines an index, which is set of fields that exists within your unified customer profiles.

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-maximum-filters-start
   :end-before: .. endpoint-get-profiles-list-maximum-filters-end

Use Profile API endoints to support use cases, such as:

* Loyalty programs
* Personalize the experience for omnichannel customers that log into your website
* Using extended profile attributes with downstream systems, such as Braze, Cordial, and Salesforce Marketing Cloud
* Most recent purchases, favorite products, or other aspects of your product catalog
* Real-time personalization for websites
* Product suggestions

.. profile-api-howitworks-end


.. _profile-api-howitworks-endpoints:

Profile API endpoints
--------------------------------------------------

.. profile-api-howitworks-endpoints-start

The Profile API has the following endpoints:

* :ref:`GET /indexes <profile-api-howitworks-endpoints-get-indexes>`
* :ref:`GET /indexes/{id} <profile-api-howitworks-endpoints-get-indexes-id>`
* :ref:`GET /indexes <profile-api-howitworks-endpoints-get-indexes-id-profiles>`
* :ref:`GET /indexes <profile-api-howitworks-endpoints-get-indexes-id-profiles-id>`

.. profile-api-howitworks-endpoints-end

.. profile-api-howitworks-endpoints-which-policies-start

.. admonition:: What policies users need?

   The Profile API requires the following policies to be assigned to users within your tenant:

   #. **Allow Profile API administration** This policy allows users to use the **Destinations** page to manage endpoints in your tenant's Profile API.
   #. **Allow API key administration** This policy allows users to use the **Users and Activity** page to manage API keys and tokens required by Amperity APIs.

   These policies may be assigned to the same user.

.. profile-api-howitworks-endpoints-which-policies-end


.. _profile-api-howitworks-endpoints-get-indexes:

GET /indexes
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
   :start-after: .. endpoint-get-profile-index-start
   :end-before: .. endpoint-get-profile-index-end

**Base URL**

.. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
   :start-after: .. endpoint-get-profile-index-base-url-start
   :end-before: .. endpoint-get-profile-index-base-url-end

**cURL example**

.. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
   :start-after: .. endpoint-get-profile-index-request-start
   :end-before: .. endpoint-get-profile-index-request-end

**Request parameters**

.. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
   :start-after: .. endpoint-get-profile-index-request-parameters-start
   :end-before: .. endpoint-get-profile-index-request-parameters-end

**Response**

.. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
   :start-after: .. endpoint-get-profile-index-response-200ok-start
   :end-before: .. endpoint-get-profile-index-response-200ok-end

.. include:: ../../amperity_api/source/endpoint_get_profile_index.rst
   :start-after: .. endpoint-get-profile-index-response-parameters-start
   :end-before: .. endpoint-get-profile-index-response-parameters-end


.. _profile-api-howitworks-endpoints-get-indexes-id:

GET /indexes/{id}
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
   :start-after: .. endpoint-get-profile-index-id-start
   :end-before: .. endpoint-get-profile-index-id-end

**Base URL**

.. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
   :start-after: .. endpoint-get-profile-index-id-base-url-start
   :end-before: .. endpoint-get-profile-index-id-base-url-end

**cURL example**

.. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
   :start-after: .. endpoint-get-profile-index-id-request-start
   :end-before: .. endpoint-get-profile-index-id-request-end

**Request parameters**

.. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
   :start-after: .. endpoint-get-profile-index-id-request-parameters-start
   :end-before: .. endpoint-get-profile-index-id-request-parameters-end

**Response**

.. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
   :start-after: .. endpoint-get-profile-index-id-response-200ok-start
   :end-before: .. endpoint-get-profile-index-id-response-200ok-end

.. include:: ../../amperity_api/source/endpoint_get_profile_index_id.rst
   :start-after: .. endpoint-get-profile-index-id-response-parameters-start
   :end-before: .. endpoint-get-profile-index-id-response-parameters-end


.. _profile-api-howitworks-endpoints-get-indexes-id-profiles:

GET /indexes/{id}/profiles
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-start
   :end-before: .. endpoint-get-profiles-list-end

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-maximum-filters-start
   :end-before: .. endpoint-get-profiles-list-maximum-filters-end

**Base URL**

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-base-url-start
   :end-before: .. endpoint-get-profiles-list-base-url-end

**cURL example**

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-request-start
   :end-before: .. endpoint-get-profiles-list-request-end

**Request parameters**

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-request-parameters-start
   :end-before: .. endpoint-get-profiles-list-request-parameters-end

**Response**

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-response-200ok-start
   :end-before: .. endpoint-get-profiles-list-response-200ok-end

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-response-parameters-start
   :end-before: .. endpoint-get-profiles-list-response-parameters-end


.. _profile-api-howitworks-endpoints-get-indexes-id-profiles-id:

GET /indexes/{id}/profiles/{id}
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_api/source/endpoint_get_profile.rst
   :start-after: .. endpoint-get-profile-start
   :end-before: .. endpoint-get-profile-end

**Base URL**

.. include:: ../../amperity_api/source/endpoint_get_profile.rst
   :start-after: .. endpoint-get-profile-base-url-start
   :end-before: .. endpoint-get-profile-base-url-end

**cURL example**

.. include:: ../../amperity_api/source/endpoint_get_profile.rst
   :start-after: .. endpoint-get-profile-request-start
   :end-before: .. endpoint-get-profile-request-end

**Request parameters**

.. include:: ../../amperity_api/source/endpoint_get_profile.rst
   :start-after: .. endpoint-get-profile-request-parameters-start
   :end-before: .. endpoint-get-profile-request-parameters-end

**Response**

.. include:: ../../amperity_api/source/endpoint_get_profile.rst
   :start-after: .. endpoint-get-profile-response-200ok-start
   :end-before: .. endpoint-get-profile-response-200ok-end

.. include:: ../../amperity_api/source/endpoint_get_profile.rst
   :start-after: .. endpoint-get-profile-response-parameters-start
   :end-before: .. endpoint-get-profile-response-parameters-end


.. _profile-api-howitworks-indexes:

Indexes
--------------------------------------------------

.. profile-api-howitworks-indexes-start

An index defines a list of customer profile attributes that can be accused from a Profile API endpoint.

The fields that are available from an index are defined by a query.

* The attribute associated with the :ref:`profile ID field <profile-api-howitworks-profile-id-field>` must contain a unique identifier.
* All attributes associated with :ref:`filter fields <profile-api-howitworks-filter-fields>` should have unique names

Add an index from the **Profile API** tab on the **Destinations** page. Click the **Add index** button to configure the index settings.

.. profile-api-howitworks-indexes-end


.. _profile-api-howitworks-queries:

Queries
--------------------------------------------------

.. profile-api-howitworks-queries-start

Each index is associated with a single query. The query must have a field that contains a unique identifier and at least one other field that can be returned by the request to the Profile API endpoint.

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-maximum-filters-start
   :end-before: .. endpoint-get-profiles-list-maximum-filters-end

The field with the unique identifier is the :ref:`profile ID field <profile-api-howitworks-profile-id-field>`.

.. tip:: Do not use non-hashed email addresses as a unique value for an index.

Other fields may be configured as :ref:`filter fields <profile-api-howitworks-filter-fields>`. These fields may be included in the request to filter the request to the :ref:`GET /indexes/{id}/profiles <profile-api-howitworks-endpoints-get-indexes-id-profiles>` endpoint.

All fields in the query are returned by a request to the **GET /indexes/{id}/profiles** endpoint.

.. profile-api-howitworks-queries-end


.. _profile-api-howitworks-profile-id-field:

Profile ID field
--------------------------------------------------

.. TODO: Shared with Movable Ink. No reference links.

.. profile-api-howitworks-profile-id-field-start

A profile ID is a unique identifier for individual customer profiles. Use the **GET /indexes/{id}/profiles** endpoint to access customer profiles using 1:1 lookups to enable personalization scenarios.

A request to the **GET /indexes/{id}/profiles** endpoint returns a unique profile identified by the profile ID and any filter fields included in the request.

The value for the lookup key must be a unique identifier. For example:

* A loyalty program ID
* A hashed email address that is generated after a customer logs into a website using their email address

  .. important:: Do not use non-hashed email addresses as a lookup key.

* A customer ID
* A unique identifier used by a downstream workflow, such as the "external_id" field in Braze

.. TODO: Is this note still true?

.. note:: A request made to the Profile API must have an exact match to a profile ID field value within the index. For example: "Dennis" must match with an uppercase "D" and "Dennis " must match with both an uppercase "D" *and* a trailing character.

.. profile-api-howitworks-profile-id-field-end


.. _profile-api-howitworks-filter-fields:

Filter fields
--------------------------------------------------

.. TODO: Shared with Movable Ink. No reference links.

.. profile-api-howitworks-filter-fields-start

Filter fields allow requests to the **GET /indexes/{id}/profiles** endpoint to be filtered on each field that is included in the request. Use filter fields to support use cases with multiple matching fields, such as "Get all profiles associated with a reservation ID".

Filter fields must be defined in the query and the name of the filter field is the same as the name of the field in the query.

.. profile-api-howitworks-filter-fields-end

.. profile-api-howitworks-filter-fields-example-start

For example, to return a profile for "Daniel Kulhman":

.. code-block:: none

   filter[first_name]=Daniel \
   &filter[last_name]=Kulhman

A complete request for "Daniel Kulhman" is similar to:

.. code-block:: bash

   curl --request GET \
        'https://tenant.amperity.com/api/indexes/{id}/profiles \
        &filter[first_name]=Daniel \
        &filter[last_name]=Kulhman' \
        --header 'amperity-tenant: {tenant}' \
        --header 'api-version: 2025-07-31' \
        --header 'Authorization: Bearer {token}'

.. profile-api-howitworks-filter-fields-example-end


.. _profile-api-howitworks-index-ids:

Index IDs
--------------------------------------------------

.. profile-api-howitworks-index-ids-start

The index ID is a unique identifier for an index. To make a request to an endpoint add the index ID to the end of the request URL:

::

   https://tenant.amperity.com/api/indexes?index-id={id}

The index ID is available from:

* The **Profile API** tab on the **Destinations** page. For each endpoint, open the actions menu, and then select "Copy ID". 

   .. image:: ../../images/api-profile-destinations-list-index-ids.png
      :width: 500 px
      :alt: Copy the index ID for an endpoint in the Amperity Profile API.
      :align: left
      :class: no-scaled-link

* Returned by the :ref:`GET /indexes <profile-api-howitworks-endpoints-get-indexes>` endpoint.

.. profile-api-howitworks-index-ids-end

.. profile-api-howitworks-index-ids-tip-start

.. tip:: You can copy the URL of the :ref:`GET /indexes/{id}/profiles <profile-api-howitworks-endpoints-get-indexes-id-profiles>` endpoint from the **Profile API** tab on the **Destinations** page. From the |fa-kebab| menu for an endpoint, select **Copy URL**.

   The copied URL contains the correct values for the selected endpoint's **{tenant}** and **{index-id}** request parameters.

.. profile-api-howitworks-index-ids-tip-end


.. _profile-api-howitworks-access-tokens:

Access token
--------------------------------------------------

.. profile-api-enable-api-jwt-start

Amperity uses a `JSON Web Token (JWT) <https://jwt.io/>`__ |ext_link| for authentication to the Profile API.

The access token is self-generated from the Amperity user interface and authorizes requests to all indexes in the Profile API for your tenant. A self-generated access token ensures that only your team has access to the token and supports organizational security policies like periodic access token rotation.

.. image:: ../../images/api-keys-generate-access-token.png
   :width: 500 px
   :alt: Copy the tenant ID for use in the header request.
   :align: left
   :class: no-scaled-link

The access token must be provided within each request made to the Profile API.

.. profile-api-enable-api-jwt-end


.. _profile-api-howitworks-tenant-id:

Tenant ID
--------------------------------------------------

.. profile-api-howitworks-tenant-id-start

The tenant ID is a unique identifier for your tenant. To make a request to an index you must include the tenant ID in the URL of the request.

The tenant ID is available from the **Profile API** list. For the index, open the actions menu, and then select "Copy tenant ID".

.. image:: ../../images/api-keys-copy-tenant-id.png
   :width: 500 px
   :alt: Copy the tenant ID for use in the header request.
   :align: left
   :class: no-scaled-link

.. profile-api-howitworks-tenant-id-end


.. _profile-api-rate-limit:

Rate limit
==================================================

.. include:: ../../amperity_api/source/rate_limits.rst
   :start-after: .. rate-limits-profile-start
   :end-before: .. rate-limits-profile-end


.. _profile-api-enable:

Configure the Profile API
==================================================

.. profile-api-enable-api-start

The Profile API must be configured for use in Amperity. This is done in a series of steps:

#. :ref:`profile-api-enable-build-query`
#. :ref:`profile-api-enable-add-api-key`
#. :ref:`profile-api-enable-generate-access-token`
#. :ref:`profile-api-enable-add-index`
#. :ref:`profile-api-enable-generate-endpoint`
#. :ref:`profile-api-enable-copy-tenant-id`
#. :ref:`profile-api-enable-validate-endpoint`
#. :ref:`profile-api-enable-build-usecase`
#. :ref:`profile-api-enable-run-as-workflow`

.. profile-api-enable-api-end


.. _profile-api-enable-build-query:

Build a query
--------------------------------------------------

.. profile-api-enable-build-query-start

Build a query that contains the attributes you need to enable your downstream workflows. You can use any aspect of your unified customer profiles to define an index.

.. profile-api-enable-build-query-end

.. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
   :start-after: .. endpoint-get-profiles-list-maximum-filters-start
   :end-before: .. endpoint-get-profiles-list-maximum-filters-end


.. _profile-api-enable-add-api-key:

Add API key
--------------------------------------------------

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-api-token-add-profile-start
   :end-before: .. api-keys-api-token-add-profile-end


.. _profile-api-enable-generate-access-token:

Generate an access token
--------------------------------------------------

.. include:: ../../amperity_reference/source/api.rst
   :start-after: .. api-keys-access-tokens-generate-start
   :end-before: .. api-keys-access-tokens-generate-end


.. _profile-api-enable-add-index:

Add an index
--------------------------------------------------

.. api-profile-add-index-start

An index must be defined for each query that is used to generate an endpoint for the Profile API.

.. api-profile-add-index-end

**To add an index for the Profile API**

.. api-profile-add-index-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Open the **Profile API** tab on the **Destinations** page. Click the **Add Index** button. This button is located to the right of the **Profile API** section header.

       This opens the **Add Index** dialog box.

       Give the index a name that clearly describes how it is used by downstream workflows. The name of an index must be unique and may not contain any of the following characters: ``\``, ``/``, ``:``, ``"``, ``*``, ``?``, ``<``, ``>``, or ``|``.

       Use a description to help other users in your tenant know what use cases this index enables.

       .. note:: The name of the index is informational only. Indexes are listed alphabetically by name; index names are not used within requests.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Select the query that is used to generate the fields in the index, choose the field in that index that is used as the profile ID field, and then choose additional filtering fields.

       Define the run options, either as part of a scheduled workflow or manually.

       Save the index.

.. api-profile-add-index-steps-end


.. _profile-api-enable-generate-endpoint:

Generate the endpoint
--------------------------------------------------

.. profile-api-enable-generate-endpoint-start

An index must be generated to make it available from the Profile API.

.. note:: The user interface for the Profile API shows a spinner icon--|notification-running|--when an index is being refreshed.

**To generate an index for a Profile API endpoint**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Manually. Open the **Actions** menu for the index, and then select **Run**.

       .. image:: ../../images/api-profile-destinations-list-run.png
          :width: 500 px
          :alt: Run the index manually.
          :align: left
          :class: no-scaled-link

       **Run** does one of the following actions:

       #. Generates the index if it was not generated on save.
       #. Regenerates the index and refreshes the data that is available at that endpoint.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - After a courier group completes.

       .. image:: ../../images/api-profile-add-index-dialog-schedule-after-courier-group.png
          :width: 500 px
          :alt: Configure an endpoint to regenerate after a courier group run.
          :align: left
          :class: no-scaled-link

       This option regenerates the index and refreshes the data that is available at that endpoint. This option is recommended for indexes that depend on upstream data refreshes and will ensure that the index is regenerated at the same frequency as the upstream data refresh.

.. profile-api-enable-generate-endpoint-end


.. _profile-api-enable-copy-tenant-id:

Copy the tenant ID
--------------------------------------------------

.. profile-api-enable-copy-tenant-id-start

The tenant ID is a unique identifier for your tenant. To make a request to an index you must include the tenant ID in the URL of the request.

The tenant ID is available from the **Profile API** list. For the index, open the actions menu, and then select "Copy tenant ID".

.. profile-api-enable-copy-tenant-id-end


.. _profile-api-enable-validate-endpoint:

Validate the endpoint
--------------------------------------------------

.. profile-api-enable-validate-endpoint-start

After the index has generated, validate the endpoint to verify that it is in the list of indexes, and then contains the data that is required by your workflow.

The most direct way to validate the endpoints is to use cURL commands to access the Profile API endpoints.

.. important:: The steps to validate the endpoint may be different, depending on the downstream application or toolkit being used to enable your use case. For example, :ref:`Braze Connected Content <profile-api-usecase-braze-validate-connected-content>` has its own syntax--Liquid--for building the interface that interacts with the endpoint in your tenant's Profile API.

.. profile-api-enable-validate-endpoint-end


.. _profile-api-enable-build-usecase:

Build into use cases
--------------------------------------------------

.. profile-api-enable-build-usecase-start

After you have verified that a specific endpoint is accessible and that it contains the data you expect it to contain, you can start building that endpoint into your workflows. See the :ref:`list of use cases <profile-api-usecases>` for some ideas as starting points.

The Amperity Profile API can be accessed using cURL, Postman, or any other mechanism that can access a REST API and provide the access token that is required by the request.

.. profile-api-enable-build-usecase-end


.. _profile-api-enable-run-as-workflow:

Run as part of a workflow
--------------------------------------------------

.. profile-api-enable-run-as-workflow-start

A Profile API index can be configured to run as part of a scheduled workflow when the schedule is set to **Run after courier group** and an active courier group is selected from the dropdown menu.

.. profile-api-enable-run-as-workflow-end


.. _profile-api-response-times:

Index response times
==================================================

.. profile-api-response-times-start

The Profile API supports p95 response times under 100ms at 1000 requests per second. Response times will vary based on the number of attributes and profiles in an index.

The number of rows and filter fields available from a Profile API endpoint determine:

* The length of time it takes to build or rebuild an index
* The response time for requests that are made to an index

As the number of rows and filter fields increase, the performance of that index will decrease. Large indexes with 5 or more filter fields have decreased performance.

.. note::

   .. include:: ../../amperity_api/source/endpoint_get_profiles_list.rst
      :start-after: .. endpoint-get-profiles-list-maximum-filters-start
      :end-before: .. endpoint-get-profiles-list-maximum-filters-end

The size of the index has a greater effect on the length of time required to build or refresh an index than the response times for requests that are made to that index.

.. note:: Response times were measured using traffic across multiple endpoints simultaneously from US-East to US-West. Use these response times as an indicator for the types of response times you will see for your tenant's use of Profile API endpoints.

.. profile-api-response-times-start

.. _profile-api-response-percentiles:

.. profile-api-response-percentiles-start

.. admonition:: About response percentiles

   Response percentiles divide individual response times into groups based on distribution: p95, and p99. Response percentiles are shown in milliseconds (ms).

   * **p950**

     95% of the response times were below this value.

   * **p99**

     99% of the response times were below this value.

.. profile-api-response-percentiles-end


.. _profile-api-response-times-5-columns-0-filters:

5 columns 0 filters
--------------------------------------------------

.. profile-api-response-times-5-columns-0-filters-start

The following table shows response times for a 5 column index with zero filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 0
     - 0
     - 0

   * - **Workflow duration**
     - 2m 43s
     - 3m 40s
     - 26m

   * - **Median latency (ms)**
     - 41 ms
     - 36 ms
     - 60 ms

   * - **P95 latency (ms)**
     - 74 ms
     - 48 ms
     - 84 ms

   * - **P99 latency (ms)**
     - 97 ms
     - 58 ms
     - 110 ms

   * - **Requests per second**
     - 1000
     - 1000
     - 1000

.. profile-api-response-times-5-columns-0-filters-end


.. _profile-api-response-times-5-columns-1-filter:

5 columns 1 filter
--------------------------------------------------

.. profile-api-response-times-5-columns-1-filter-start

The following table shows response times for a 5 column index with 1 filter field and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 1
     - 1
     - 1

   * - **Workflow duration**
     - 2m 25s
     - 3m 19s
     - 29m

   * - **Median latency (ms)**
     - 63 ms
     - 71 ms
     - 68 ms

   * - **P95 latency (ms)**
     - 140 ms
     - 150 ms
     - 240 ms

   * - **P99 latency (ms)**
     - 210 ms
     - 200 ms
     - 380 ms

   * - **Requests per second**
     - 1000
     - 1000
     - 1000

.. profile-api-response-times-5-columns-1-filter-end


.. _profile-api-response-times-5-columns-3-filters:

5 columns 3 filters
--------------------------------------------------

.. profile-api-response-times-5-columns-3-filters-start

The following table shows response times for a 5 column index with 3 filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 3
     - 3
     - 3

   * - **Workflow duration**
     - 3m 2s
     - 4m 59s
     - 34m

   * - **Median latency (ms)**
     - 1000 ms
     - 8300 ms
     - 26000 ms

   * - **P95 latency (ms)**
     - 3500 ms
     - 19000 ms
     - 44000 ms

   * - **P99 latency (ms)**
     - 5300 ms
     - 24000 ms
     - 46000 ms

   * - **Requests per second**
     - 330
     - 40
     - 4

.. profile-api-response-times-5-columns-3-filters-end


.. _profile-api-response-times-10-columns-0-filters:

10 columns 0 filters
--------------------------------------------------

.. profile-api-response-times-10-columns-0-filters-start

The following table shows response times for a 10 column index with zero filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 0
     - 0
     - 0

   * - **Workflow duration**
     - 2m 25s
     - 3m 40s
     - 42m

   * - **Median latency (ms)**
     - 36 ms
     - 29 ms
     - 57 ms

   * - **P95 latency (ms)**
     - 48 ms
     - 52 ms
     - 100 ms

   * - **P99 latency (ms)**
     - 62 ms
     - 110 ms
     - 130 ms

   * - **Requests per second**
     - 1000
     - 1000
     - 1000

.. profile-api-response-times-10-columns-0-filters-end


.. _profile-api-response-times-10-columns-1-filter:

10 columns 1 filter
--------------------------------------------------

.. profile-api-response-times-10-columns-1-filter-start

The following table shows response times for a 10 column index with 1 filter field and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 1
     - 1
     - 1

   * - **Workflow duration**
     - 2m 29s
     - 3m 50s
     - 43m

   * - **Median latency (ms)**
     - 84 ms
     - 72 ms
     - 90 ms

   * - **P95 latency (ms)**
     - 150 ms
     - 200 ms
     - 290 ms

   * - **P99 latency (ms)**
     - 200 ms
     - 320 ms
     - 440 ms

   * - **Requests per second**
     - 1000
     - 1000
     - 1000

.. profile-api-response-times-10-columns-1-filter-end


.. _profile-api-response-times-10-columns-3-filters:

10 columns 3 filters
--------------------------------------------------

.. profile-api-response-times-10-columns-3-filters-start

The following table shows response times for a 10 column index with 3 filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 3
     - 3
     - 3

   * - **Workflow duration**
     - 3m 14s
     - 5m
     - 50m

   * - **Median latency (ms)**
     - 420 ms
     - 6600 ms
     - 27000 ms

   * - **P95 latency (ms)**
     - 1400 ms
     - 15000 ms
     - 40000 ms

   * - **P99 latency (ms)**
     - 2300 ms
     - 19000 ms
     - 43000 ms

   * - **Requests per second**
     - 300
     - 50
     - 5

.. profile-api-response-times-10-columns-3-filters-end


.. _profile-api-response-times-10-columns-5-filters:

10 columns 5 filters
--------------------------------------------------

.. profile-api-response-times-10-columns-5-filters-start

The following table shows response times for a 10 column index with 5 filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 5
     - 5
     - 5

   * - **Workflow duration**
     - 2m 32s
     - 4m 10s
     - 49m

   * - **Median latency (ms)**
     - 390 ms
     - 3000 ms
     - 33000 ms

   * - **P95 latency (ms)**
     - 1500 ms
     - 11000 ms
     - 50000 ms

   * - **P99 latency (ms)**
     - 2200 ms
     - 15000 ms
     - 55000 ms

   * - **Requests per second**
     - 300
     - 40
     - 5

.. profile-api-response-times-10-columns-5-filters-end


.. _profile-api-response-times-30-columns-0-filters:

30 columns 0 filters
--------------------------------------------------

.. profile-api-response-times-30-columns-0-filters-start

The following table shows response times for a 30 column index with zero filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 0
     - 0
     - 0

   * - **Workflow duration**
     - 2m 50s
     - 7m 14s
     - 2h

   * - **Median latency (ms)**
     - 48 ms
     - 36 ms
     - 48 ms

   * - **P95 latency (ms)**
     - 89 ms
     - 91 ms
     - 120 ms

   * - **P99 latency (ms)**
     - 170 ms
     - 160 ms
     - 180 ms

   * - **Requests per second**
     - 1000
     - 1000
     - 1000

.. profile-api-response-times-30-columns-0-filters-end


.. _profile-api-response-times-30-columns-1-filter:

30 columns 1 filter
--------------------------------------------------

.. profile-api-response-times-30-columns-1-filter-start

The following table shows response times for a 30 column index with 1 filter field and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 1
     - 1
     - 1

   * - **Workflow duration**
     - 2m 32s
     - 5m 39s
     - --

   * - **Median latency (ms)**
     - 84 ms
     - 800 ms
     - --

   * - **P95 latency (ms)**
     - 150 ms
     - 3700 ms
     - --

   * - **P99 latency (ms)**
     - 200 ms
     - 6600 ms
     - --

   * - **Requests per second**
     - 1000
     - 700
     - --

.. profile-api-response-times-30-columns-1-filter-end


.. _profile-api-response-times-30-columns-3-filters:

30 columns 3 filters
--------------------------------------------------

.. profile-api-response-times-30-columns-3-filters-start

The following table shows response times for a 30 column index with 3 filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 3
     - 3
     - 3

   * - **Workflow duration**
     - 3m 14s
     - 6m 51s
     - --

   * - **Median latency (ms)**
     - 420 ms
     - 1900 ms
     - --

   * - **P95 latency (ms)**
     - 1400 ms
     - 11000 ms
     - --

   * - **P99 latency (ms)**
     - 2300 ms
     - 15000 ms
     - --

   * - **Requests per second**
     - 300
     - 40
     - --

.. profile-api-response-times-30-columns-3-filters-end


.. _profile-api-response-times-30-columns-5-filters:

30 columns 5 filters
--------------------------------------------------

.. profile-api-response-times-30-columns-5-filters-start

The following table shows response times for a 30 column index with 5 filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 5
     - 5
     - 5

   * - **Workflow duration**
     - 2m 32s
     - 6m 38s
     - --

   * - **Median latency (ms)**
     - 390 ms
     - 3400 ms
     - --

   * - **P95 latency (ms)**
     - 1500 ms
     - 8700 ms
     - --

   * - **P99 latency (ms)**
     - 2200 ms
     - 11000 ms
     - --

   * - **Requests per second**
     - 300
     - 40
     - --

.. profile-api-response-times-30-columns-5-filters-end


.. _profile-api-response-times-30-columns-10-filters:

30 columns 10 filters
--------------------------------------------------

.. profile-api-response-times-30-columns-10-filters-start

The following table shows response times for a 30 column index with 10 filter fields and outputs at 1, 10, and 100 million rows. All response times are in milliseconds.

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - 
     - **1M rows**
     - **10M rows**
     - **100M rows**

   * - **Filter fields**
     - 10
     - 10
     - 10

   * - **Workflow duration**
     - 2m 42s
     - 6m 54s
     - --

   * - **Median latency (ms)**
     - 550 ms
     - 3400 ms
     - --

   * - **P95 latency (ms)**
     - 3800 ms
     - 22000 ms
     - --

   * - **P99 latency (ms)**
     - 9700 ms
     - 26000 ms
     - --

   * - **Requests per second**
     - 150
     - 20
     - --

.. profile-api-response-times-30-columns-10-filters-end


.. _profile-api-usecases:

Use cases
==================================================

.. profile-api-usecases-start

The Profile API can support any number of potential use cases. All you need to do is define the use case, identify the requirements for building that use case for your downstream workflow, and then access the customer profile data using the Profile API endpoints.

The following sections describe some ways to use the Profile API:

* :ref:`Braze Connected Content <profile-api-usecase-braze>`
* :ref:`Hashed email profiles <profile-api-usecase-hashed-email-address-profiles>`
* :ref:`Loyalty profiles <profile-api-usecase-loyalty-profiles>`
* :ref:`Moveable Ink Studio <profile-api-usecase-moveable-ink-studio>`
* :ref:`Server-side JavaScript in Salesforce Marketing Cloud <profile-api-usecase-ssjs-ssmc>`
* :ref:`Wireless access points <profile-api-usecase-hashed-email-address-profiles-wireless>`

.. 
.. * :ref:`MetaRouter <profile-api-usecase-metarouter>`
.. * :ref:`Recent purchases <profile-api-usecase-recent-purchases>`
.. * :ref:`Website personalization <profile-api-usecase-website-personalization>`
.. 

.. TODO: Cordial doesn't support token-based access to the Profile API. https://support.cordial.com/hc/en-us/articles/115005857328-Get-JSON-Feeds-getJson-method

.. profile-api-usecases-end


.. _profile-api-usecase-braze:

Braze Connected Content
--------------------------------------------------

.. profile-api-usecase-braze-start

You can use the Profile API to make extended profile attributes available to Braze using `Connected Content <https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content>`__ |ext_link|.

.. profile-api-usecase-braze-end

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-start

.. important:: Connected Content does not write data to user profiles, which means you can use Connected Content to dynamically populate values into messages without consuming data points.

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-end

.. _profile-api-usecase-braze-validate-connected-content:

.. profile-api-usecase-braze-validate-in-preview-editor-start

.. tip:: You can verify the attributes that are returned by the Profile API endpoint directly in the Connected Content preview editor. Use a block similar to:

   .. code-block:: none

      {% connected_content
        https://{tenant-id}.amperity.com/api/indexes/{id}/profiles?filter[<attribute>]=<value>
      %}


      {{result text}}

   This will return the set of attributes at the "{id}" index for the specified "filter".

.. profile-api-usecase-braze-validate-in-preview-editor-end

.. profile-api-usecase-braze-example-start

Braze uses a feature called Connected Content to define reusable blocks of message content that can then be used across a variety of marketing campaign scenarios.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Build an index that contains the list default user profile attributes, and then extend the profile to include more details from Amperity unified customer profiles.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - Your Profile API access token is a JSON Web Token (JWT) that should be accessible from a safe location and not be embedded directly within your request.

       Use a "connected_content" block to get the access token, and then cache it with enough time to allow the next request to pull data from the index.

       In Braze Connected Content load the access token for the Profile API using a block similar to:

       ::

          {% connected_content
             https://endpoint
             :method post
             :headers {
               "Authorization": "Bearer refresh-token"
             }
             :cache_max_age 900
             :save auth
          %}

       where "https://endpoint" is the URL at which the access token is located, and then "refresh-token" is the access token.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - After the access token is available to Connected Content, use the cached access token to access the index. The type of request to use in this step varies, depending on your use case.

       **To query an index**

       ::

          {% connected_content
             https://{tenant-id}.amperity.com/api/indexes/{id}/profiles?filter[<attribute>]=<value>
             :method post
             :headers {
               "Authorization": "Bearer {{auth.token}}",
               "X-Amperity-Tenant":"socktown",
               "Content-Type":"application/json"
             }
             :body key={{user_id}}
             :save response
          %}
          Hello {{response.attributes.value.first_name}}.


       **To return a list of indexes**

       ::

          {% connected_content
             https://tenant.amperity.com/api/indexes
             :method get
             :headers {
               "Authorization": "Bearer {{auth.token}}",
               "X-Amperity-Tenant": "socktown"
             }
             :body key=external_id
             :content_type application/json
             :save result
          %}


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Add values from the index using the following syntax:

       ::

          {{result.attributes.value.name}}

       where "name" is the name of a field in the index:

       ::

          {{result.attributes.value.given_name}}
          {{result.attributes.value.surname}}
          {{result.attributes.value.phone}}
          {{result.attributes.value.loyalty_id}}
          {{result.attributes.value.loyalty_points}}
          {{result.attributes.value.loyalty_tier}}

       For example:

       ::

          Hello {{result.attributes.value.given_name}}. Your
          {{result.attributes.value.loyalty_tier}} balance is:

          {{result.attributes.value.loyalty_points}}

.. profile-api-usecase-braze-example-end


.. _profile-api-usecase-hashed-email-address-profiles:

Hashed email profiles
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-hashed-email-start
   :end-before: .. term-hashed-email-end

.. profile-api-usecase-hashed-email-address-profiles-start

A hashed email

* Is anonymous
* Is not PII
* Cannot be decrypted
* Is browser- and device-independent
* Enables multi-device, multi-browser, and multi-app tracking
* Can be used to anonymously track users across websites, apps, and devices when the email address used to log into a website, app, or device matches the hashed email

and, most importantly, a hashed email can be used to associate a user to a unified customer profile from which your brand can build personalized workflows.

.. note:: More than one algorithm may be used to hash an email address. Amperity assumes that SHA-256 is the algorithm used for hashing email addresses.

   A workflow that relies on hashed email addresses must use a consistent hashing algorithm at each point in the downstream workflow.

Build a column in a customer 360 table that includes a hashed email address. For example:

.. code-block:: sql

   SELECT
     TO_HEX(SHA256(TO_UTF8(UPPER(TRIM(email))))) AS hashed_email
     ,given_name AS first_name
     ,surname AS last_name
     ,postal AS zip_code
   FROM Merged_Customers

Use the hashed email address as the lookup key for the endpoint, generate the index, and then build workflows that your brand can use to personalize website, app, and browser experiences for your customers.

.. profile-api-usecase-hashed-email-address-profiles-end


.. _profile-api-usecase-hashed-email-address-profiles-wireless:

Wireless access points
++++++++++++++++++++++++++++++++++++++++++++++++++

.. profile-api-usecase-hashed-email-address-profiles-wireless-start

You can use hashed email addresses to associate unified customer profiles to the email addresses that may be used to log into wireless access points.

This use case uses a combination of Profile API endpoints:

#. An endpoint that contains a unified customer profile that :ref:`uses a hashed email address <profile-api-usecase-hashed-email-address-profiles>` as the lookup key.
#. An endpoint that contains wireless access points unique identifiers as the lookup key. For example, this endpoint could be built using a query similar to:

   .. code-block:: sql

      SELECT
        wireless_access_point_id
        ,location_ID
        ,location_name
      FROM Locations_Table

For example: A customer logs into the secure wireless that is offered by your hotel or resort using their email address.

A hashed version of that email address is built, and then is used as the lookup key for the endpoint in your Profile API that contains the hashed email profile. The unique ID for the wireless access point is used to look up the hotel or resort.

Use the Profile API to update the welcome screen. For example:

::

   Thank you {{first_name}} for visiting {{location_name}}.
   We hope you enjoy your stay.

This message could be extended to include promos or offers or any type of additional messaging your brand chooses.

.. profile-api-usecase-hashed-email-address-profiles-wireless-end


.. _profile-api-usecase-loyalty-profiles:

Loyalty profiles
--------------------------------------------------

.. profile-api-usecase-loyalty-profiles-start

You can use loyalty IDs to personalize welcome messages for your customers after they log into your website.

Build a query that includes the unified customer profile data that your brand wants to use to personalize welcome messages. For example:

.. code-block:: sql

   SELECT
     ,amperity_id
     ,mc.given_name AS first_name
     ,mc.surname AS last_name
     ,mc.birthdate
     ,lt.loyalty_id
     ,lt.loyalty_tier
     ,lt.loyalty_points_date
     ,lt.loyalty_points
   FROM Merged_Customers mc
   LEFT JOIN Loyalty_Table lt
   ON mc.amperity_id = lt.amperity_id

Use the loyalty ID as the lookup key for the endpoint, generate the index, and then build workflows that your brand can use to personalize your website for members of your loyalty program.

For example: A customer logs into your website using their loyalty ID, after which the loyalty ID can be used to look up an individual customer in your loyalty profile endpoint and be used to personalize their experience.

For example, a welcome message shown immediately after logging in:

::

   Welcome back {{first_name}}.

   Thank you for being a long-time member of our
   {{loyalty_tier}} program.

   As of {{loyalty_points_date}}, your loyalty points
   total is: {{loyalty_points}}.

This message could be extended to include promos or offers or any type of additional messaging your brand chooses, such as extending the logic to include a message to customers whose birthday falls within the next 30 days:

::

   Welcome back {{first_name}}.

   {{ if birthdate = within the next 30 days }}

   As a special thank you for being a long-time
   member of our {{loyalty_tier}} program, here is
   a {{discount_code_id}} discount code that you
   may use on your next purchase: {{coupon_id}}.

   {{ else }}

   Thank you for being a long-time member of our
   {{loyalty_tier}} program. As of
   {{loyalty_points_date}}, your loyalty points
   total is: {{loyalty_points}}.

   {{ end }}

.. profile-api-usecase-loyalty-profiles-end


.. _profile-api-usecase-moveable-ink-studio:

Moveable Ink Studio
--------------------------------------------------

.. include:: ../../amperity_operator/source/destination_moveableink.rst
   :start-after: .. destination-moveableink-intro-start
   :end-before: .. destination-moveableink-intro-end

.. include:: ../../amperity_operator/source/destination_moveableink.rst
   :start-after: .. destination-moveableink-configure-start
   :end-before: .. destination-moveableink-configure-end


.. _profile-api-usecase-ssjs-ssmc:

Server-side JavaScript in Salesforce
--------------------------------------------------

.. profile-api-usecase-ssjs-ssmc-start

AMPscript is a scripting language used by Salesforce Marketing Cloud to render content on a subscriber-by-subscriber basis in. Embed `AMPscript <https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ampscript.html>`__ |ext_link| variables within HTML emails, text emails, landing pages, SMS messages, and push notifications. These variables are updated at the time a message or notification is sent or shown to a subscriber.

Use Amperity unified customer profiles as values for variables defined by AMPscript. Use `Server-Side JavaScript (SSJS) <https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ssjs_serverSideJavaScript.html>`__ |ext_link| to return data from a Profile API endpoint, and then make that data available to AMPscript.

The following example shows how replace a variable with an email address from a Profile API endpoint just before sending a message.

Use AMPscript to return a value from the subscriber/data extension that is defined within the message template. For example, email:

.. code-block:: html

   %%[
     SET @Email = email
   ]%%

Load the values from the Profile API endpoint using SSJS. This will make those values available to AMPscript variables:

.. code-block:: html

   <script runat="server">

     Platform.Load("core", "1.1.1");
     var email = Variable.GetValue("@Email");

     //Set up Amperity Profile API call
     var url = 'https://tenant.amperity.com/api/indexes/{id}';
     var contentType = 'application/json';
     var payload = '{"key":"' + email + '"}';
     var names = ["X-Amperity-Tenant", "Authorization"];
     var values = ["$tenant-id", "Bearer $ACCESS-TOKEN"];
     var res = HTTP.Get(url, contentType, payload, names, values);

     //Process results from Amperity Profile API call
     var objResp = Platform.Function.ParseJSON(res.Response[0]);
     Variable.SetValue("@AmperityID",objResp.attributes.value.amperity_id);
     Variable.SetValue("@FirstName",objResp.attributes.value.firstname);
     Variable.SetValue("@LastName",objResp.attributes.value.lastname);
     Variable.SetValue("@LifetimeSpend",objResp.attributes.value.lifetimespend);
     Variable.SetValue("@FavoriteBrand",objResp.attributes.value.favoritebrand);
     Variable.SetValue("@LoyaltyPoints",objResp.attributes.value.loyaltypoints);
     Variable.SetValue("@LoyaltyTier",objResp.attributes.value.loyaltytier);

   </script>

Update the **$INDEX-ID**, **$tenant-id**, and **$ACCESS-TOKEN** placeholders for the correct index ID, tenant ID, and access token.

Use the **Variable.SetValue("@$FIELD",objResp.attributes.value.$FIELD);** function to declare the list of fields that are available to SSJS from the Profile API endpoint.

.. profile-api-usecase-ssjs-ssmc-end
