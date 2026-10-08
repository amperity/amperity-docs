.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use the Database Profile API to make extended profile attributes available to Braze using Connected Content.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use the Database Profile API to make extended profile attributes available to Braze using Connected Content.

.. meta::
    :content class=swiftype name=title data-type=string:
        Braze Connected Content

.. _profile-api-usecase-braze:

==================================================
Braze Connected Content
==================================================

.. profile-api-usecase-braze-start

You can use the `Database Profile API <explorer-database-profile-api_>`__ to make extended profile attributes available to Braze using `Connected Content <https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content>`__ |ext_link|.

.. profile-api-usecase-braze-end

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-start

.. important:: Connected Content does not write data to user profiles, which means you can use Connected Content to dynamically populate values into messages without consuming data points.

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-end

.. _profile-api-usecase-braze-validate-connected-content:

.. profile-api-usecase-braze-validate-in-preview-editor-start

.. tip:: You can verify the attributes that are returned by the Database Profile API endpoint directly in the Connected Content preview editor. Use a block similar to:

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
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Build an index that has the list default user profile attributes, and then extend the profile to include more details from Amperity unified customer profiles.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Your `Database Profile API <explorer-database-profile-api_>`__ access token is a JSON Web Token (JWT) that should be accessible from a safe location and not be embedded directly within your request.

       Use a "connected_content" block to get the access token, and then cache it with enough time to allow the next request to pull data from the index.

       In Braze Connected Content load the access token for the `Database Profile API <explorer-database-profile-api_>`__ using a block similar to:

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
          :alt: Step three.
          :align: center
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
          :alt: Step four.
          :align: center
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
