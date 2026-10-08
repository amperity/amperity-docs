.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        How to use the Database Profile API.

.. meta::
    :content class=swiftype name=body data-type=text:
        How to use the Database Profile API.

.. meta::
    :content class=swiftype name=title data-type=string:
        Database Profile API

==================================================
Database Profile API
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-profile-api-start
   :end-before: .. term-profile-api-end

.. api-profile-learning-lab-start

.. admonition:: Amperity Learning Lab

   Open **Learning Lab** to learn more about how your brand can use the `Database Profile API <https://amperity.com/learning-lab/query-for-profile-information-via-the-api>`__ |ext_link|. Registration is required.

.. api-profile-learning-lab-end


.. _profile-api-howitworks:

How the Database Profile API works
==================================================

.. profile-api-howitworks-start

Use the `Database Profile API <explorer-database-profile-api_>`__ to access customer profile indexes in your Amperity tenant. Any collection of customer profile attributes that can be included in a customer 360 table can be accessed from a `Database Profile API <explorer-database-profile-api_>`__ endpoint.

Each endpoint is defined by a query that you build in the **Queries** page, after which it may be generated as an index within the `Database Profile API <explorer-database-profile-api_>`__. A query defines an index, which is set of fields that exists within your unified customer profiles.

.. note:: The maximum number of fields for an index is 30.

Use `Database Profile API <explorer-database-profile-api_>`__ endpoints to support use cases, such as:

* Loyalty programs
* Personalize the experience for omnichannel customers that log into your website
* Using extended profile attributes with downstream systems, such as Braze, Cordial, and Salesforce Marketing Cloud
* Most recent purchases, favorite products, or other aspects of your product catalog
* Real-time personalization for websites
* Product suggestions

.. profile-api-howitworks-end


.. _profile-api-howitworks-endpoints:

Database Profile API endpoints
--------------------------------------------------

.. profile-api-howitworks-endpoints-start

For every `Database Profile API <explorer-database-profile-api_>`__ endpoint, including its request parameters, response schema, and examples, see the `Database Profile API reference <explorer-database-profile-api_>`__. You can also send requests to each endpoint from that page.

.. profile-api-howitworks-endpoints-end

.. profile-api-howitworks-endpoints-which-policies-start

.. admonition:: What policies users need?

   The `Database Profile API <explorer-database-profile-api_>`__ requires the following policies to be assigned to users within your tenant:

   #. **Allow Profile API administration** This policy allows users to use the **Destinations** page to manage endpoints in your tenant's `Database Profile API <explorer-database-profile-api_>`__.
   #. **Allow API key administration** This policy allows users to use the **Users and Activity** page to manage API keys and tokens required by Amperity APIs.

   These policies may be assigned to the same user.

.. profile-api-howitworks-endpoints-which-policies-end


.. _profile-api-howitworks-indexes:

Indexes
--------------------------------------------------

.. profile-api-howitworks-indexes-start

An index defines a list of customer profile attributes that can be accessed from a `Database Profile API <explorer-database-profile-api_>`__ endpoint.

The fields that are available from an index are defined by a query.

* The attribute associated with the :ref:`profile ID field <profile-api-howitworks-profile-id-field>` must contain a unique identifier.
* All attributes associated with `filter fields <explorer-database-profile-api_>`__ should have unique names

Add an index from the **Profile API** tab on the **Destinations** page. Click the **Add index** button to configure the index settings.

.. profile-api-howitworks-indexes-end


.. _profile-api-howitworks-queries:

Queries
--------------------------------------------------

.. profile-api-howitworks-queries-start

Each index is associated with a single query. The query must have a field that has a unique identifier and at least one other field that can be returned by the request to the `Database Profile API <explorer-database-profile-api_>`__ endpoint.

.. note:: The maximum number of fields for an index is 30.

The field with the unique identifier is the :ref:`profile ID field <profile-api-howitworks-profile-id-field>`.

.. tip:: Do not use non-hashed email addresses as a unique value for an index.

Other fields may be configured as `filter fields <explorer-database-profile-api_>`__. These fields may be included in the request to filter the request to the :ref:`GET /indexes/{id}/profiles <profile-api-howitworks-endpoints>` endpoint.

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

.. note:: A request made to the Database Profile API must have an exact match to a profile ID field value within the index. For example: "Dennis" must match with an uppercase "D" and "Dennis " must match with both an uppercase "D" *and* a trailing character.

.. profile-api-howitworks-profile-id-field-end


.. _profile-api-howitworks-index-ids:

Index IDs
--------------------------------------------------

.. profile-api-howitworks-index-ids-start

Each index has an ID, which requests to that index use. The index ID is available from:

* The **Profile API** tab on the **Destinations** page. For each endpoint, open the actions menu, and then select "Copy ID". 

   .. image:: ../../images/api-profile-destinations-list-index-ids.png
      :width: 500 px
      :alt: Copy the index ID for an endpoint in the Database Profile API.
      :align: left
      :class: no-scaled-link

* Returned by the :ref:`GET /indexes <profile-api-howitworks-endpoints>` endpoint.

.. profile-api-howitworks-index-ids-end

.. profile-api-howitworks-index-ids-tip-start

.. tip:: You can copy the URL of the :ref:`GET /indexes/{id}/profiles <profile-api-howitworks-endpoints>` endpoint from the **Profile API** tab on the **Destinations** page. From the |fa-kebab| menu for an endpoint, select **Copy URL**.

   The copied URL has the correct values for the selected endpoint's **{tenant}** and **{index-id}** request parameters.

.. profile-api-howitworks-index-ids-tip-end


.. _profile-api-enable:

Configure the Database Profile API
==================================================

.. profile-api-enable-api-start

The `Database Profile API <explorer-database-profile-api_>`__ must be configured for use in Amperity. This is done in a series of steps:

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

Build a query that has the attributes you need to enable your downstream workflows. You can use any aspect of your unified customer profiles to define an index.

.. profile-api-enable-build-query-end

.. note:: The maximum number of fields for an index is 30.


.. _profile-api-enable-add-api-key:

Add API key
--------------------------------------------------

An API key enables your downstream use cases to read data from the `Database Profile API <explorer-database-profile-api_>`__.

**To add an API key for the Database Profile API**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab. Under **API keys** click **Add API key**.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - From the **Add API key** dialog, add the name for the API key, select the **Profile API Data Access** option, and then click **Save**.

       .. image:: ../../images/api-keys-add-access-token-profile.png
          :width: 500 px
          :alt: Generate an API key.
          :align: left
          :class: no-scaled-link


.. _profile-api-enable-generate-access-token:

Generate an access token
--------------------------------------------------

Access tokens that enable authentication to Amperity APIs are managed directly from the **Settings** page in Amperity.

**To generate access tokens**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Settings** page, and then select the **Security** tab.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Under **API keys** find the API key for which you want to generate an access token, and then from the **Actions** menu select **Get token**.

       .. image:: ../../images/api-keys-generate-access-token.png
          :width: 500 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Select the number of days this token allows access to the API, after which it will expire. For example, 3 days:

       .. image:: ../../images/api-keys-set-token-expiration.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       Use the **Rotate key secret** option to rotate an existing secret when generating an access token. This will force all previously provisioned tokens that are associated with the current API key to expire in 30 days.

       Click **Generate token**. The token is generated, and then is automatically copied to your clipboard.

       .. image:: ../../images/api-keys-token-saved-to-clipboard.png
          :width: 240 px
          :alt: Generate an access token.
          :align: left
          :class: no-scaled-link

       .. important:: You are the only person who have access to the newly generated access key. Amperity does not save the access key anywhere and it will disappear when you close this dialog. Store the access key in a safe place.


.. _profile-api-enable-add-index:

Add an index
--------------------------------------------------

.. api-profile-add-index-start

An index must be defined for each query that is used to generate an endpoint for the `Database Profile API <explorer-database-profile-api_>`__.

.. api-profile-add-index-end

**To add an index for the Database Profile API**

.. api-profile-add-index-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Profile API** tab on the **Destinations** page. Click the **Add Index** button. This button is located to the right of the **Profile API** section header.

       This opens the **Add Index** dialog box.

       Give the index a name that describes how it is used by downstream workflows. The name of an index must be unique and may not contain any of the following characters: ``\``, ``/``, ``:``, ``"``, ``*``, ``?``, ``<``, ``>``, or ``|``.

       Use a description to help other users in your tenant know what use cases this index enables.

       .. note:: The name of the index is informational only. Indexes are listed alphabetically by name. Index names are not used within requests.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Select the query that is used to generate the fields in the index, choose the field in that index that is used as the profile ID field, and then choose additional filtering fields.

       Define the run options, either as part of a scheduled workflow or manually.

       Save the index.

.. api-profile-add-index-steps-end


.. _profile-api-enable-generate-endpoint:

Generate the endpoint
--------------------------------------------------

.. profile-api-enable-generate-endpoint-start

An index must be generated to make it available from the `Database Profile API <explorer-database-profile-api_>`__.

.. note:: The user interface for the Database Profile API shows a spinner icon--|notification-running|--when an index is being refreshed.

**To generate an index for a Database Profile API endpoint**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
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
          :alt: Step two.
          :align: center
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

After the index has generated, validate the endpoint to verify that it is in the list of indexes, and then has the data that is required by your workflow.

The most direct way to validate the endpoints is to use cURL commands to access the `Database Profile API <explorer-database-profile-api_>`__ endpoints.

.. important:: The steps to validate the endpoint may be different, depending on the downstream application or toolkit being used to enable your use case. For example, :ref:`Braze Connected Content <profile-api-usecase-braze-validate-connected-content>` has its own syntax--Liquid--for building the interface that interacts with the endpoint in your tenant's Database Profile API.

.. profile-api-enable-validate-endpoint-end


.. _profile-api-enable-build-usecase:

Build into use cases
--------------------------------------------------

.. profile-api-enable-build-usecase-start

After you have verified that a specific endpoint is accessible and that it has the data you expect it to contain, you can start building that endpoint into your workflows. See the :ref:`list of use cases <profile-api-usecases>` for some ideas as starting points.

The `Database Profile API <explorer-database-profile-api_>`__ is accessed using cURL, Postman, or any other mechanism that can access a REST API with the access token that is required by the request.

.. profile-api-enable-build-usecase-end


.. _profile-api-enable-run-as-workflow:

Run as part of a workflow
--------------------------------------------------

.. profile-api-enable-run-as-workflow-start

A `Database Profile API <explorer-database-profile-api_>`__ index can be configured to run as part of a scheduled workflow when the schedule is set to **Run after courier group** and an active courier group is selected from the dropdown menu.

.. profile-api-enable-run-as-workflow-end


.. _profile-api-usecases:

Use cases
==================================================

.. profile-api-usecases-start

The `Database Profile API <explorer-database-profile-api_>`__ can support any number of potential use cases. All you need to do is define the use case, identify the requirements for building that use case for your downstream workflow, and then access the customer profile data using the `Database Profile API <explorer-database-profile-api_>`__ endpoints.

The following sections describe some ways to use the `Database Profile API <explorer-database-profile-api_>`__:

* :doc:`Braze Connected Content <api_profile_braze>`
* :ref:`Hashed email profiles <profile-api-usecase-hashed-email-address-profiles>`
* :ref:`Loyalty profiles <profile-api-usecase-loyalty-profiles>`
* :ref:`Movable Ink Studio <profile-api-usecase-moveable-ink-studio>`
* :ref:`Server-side JavaScript in Salesforce Marketing Cloud <profile-api-usecase-ssjs-ssmc>`
* :ref:`Wireless access points <profile-api-usecase-hashed-email-address-profiles-wireless>`

.. 
.. * :ref:`MetaRouter <profile-api-usecase-metarouter>`
.. * :ref:`Recent purchases <profile-api-usecase-recent-purchases>`
.. * :ref:`Website personalization <profile-api-usecase-website-personalization>`
.. 

.. TODO: Cordial does not support token-based access to the Database Profile API. https://support.cordial.com/hc/en-us/articles/115005857328-Get-JSON-Feeds-getJson-method

.. profile-api-usecases-end


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
* Is browser and device independent
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

This use case uses a combination of `Database Profile API <explorer-database-profile-api_>`__ endpoints:

#. An endpoint that has a unified customer profile that :ref:`uses a hashed email address <profile-api-usecase-hashed-email-address-profiles>` as the lookup key.
#. An endpoint that has wireless access points unique identifiers as the lookup key. For example, this endpoint could be built using a query similar to:

   .. code-block:: sql

      SELECT
        wireless_access_point_id
        ,location_ID
        ,location_name
      FROM Locations_Table

For example: A customer logs into the secure wireless that is offered by your hotel or resort using their email address.

A hashed version of that email address is built, and then is used as the lookup key for the endpoint in your `Database Profile API <explorer-database-profile-api_>`__ that has the hashed email profile. The unique ID for the wireless access point is used to look up the hotel or resort.

Use the `Database Profile API <explorer-database-profile-api_>`__ to update the welcome screen. For example:

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

Movable Ink Studio
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

Use Amperity unified customer profiles as values for variables defined by AMPscript. Use `Server-Side JavaScript (SSJS) <https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ssjs_serverSideJavaScript.html>`__ |ext_link| to return data from a `Database Profile API <explorer-database-profile-api_>`__ endpoint, and then make that data available to AMPscript.

The following example shows how replace a variable with an email address from a `Database Profile API <explorer-database-profile-api_>`__ endpoint just before sending a message.

Use AMPscript to return a value from the subscriber/data extension that is defined within the message template. For example, email:

.. code-block:: html

   %%[
     SET @Email = email
   ]%%

Load the values from the `Database Profile API <explorer-database-profile-api_>`__ endpoint using SSJS. This will make those values available to AMPscript variables:

.. code-block:: html

   <script runat="server">

     Platform.Load("core", "1.1.1");
     var email = Variable.GetValue("@Email");

     //Set up Database Profile API call
     var url = 'https://tenant.amperity.com/api/indexes/{id}';
     var contentType = 'application/json';
     var payload = '{"key":"' + email + '"}';
     var names = ["X-Amperity-Tenant", "Authorization"];
     var values = ["$tenant-id", "Bearer $ACCESS-TOKEN"];
     var res = HTTP.Get(url, contentType, payload, names, values);

     //Process results from Database Profile API call
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

Use the ``Variable.SetValue("@$FIELD",objResp.attributes.value.$FIELD);`` function to declare the list of fields that are available to SSJS from the `Database Profile API <explorer-database-profile-api_>`__ endpoint.

.. profile-api-usecase-ssjs-ssmc-end
