.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Shopify (GraphQL)
.. |destination-api| replace:: Shopify GraphQL Admin API
.. |plugin-name| replace:: "Shopify (GraphQL)"
.. |credential-type| replace:: "shopify"
.. |required-credentials| replace:: "Shop name" and "Access token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "Shopify"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Shopify (GraphQL).

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Shopify (GraphQL).

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Shopify (GraphQL)

==================================================
Configure campaigns for Shopify (GraphQL)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-shopify-start
   :end-before: .. term-shopify-end

.. campaign-shopify-graphql-start

Use Amperity to activate a campaign audience into |destination-name|. Build a query or segment that includes the **email** field, and then send it to |destination-name|.

A Shopify segment is defined by a query rather than by a member list, so there is no list to push an audience into. Instead, Amperity activates an audience as a Shopify customer tag: it matches customers by email, applies the tag to members of the audience, and removes the tag from customers that leave the audience. In Shopify, build a customer segment on the condition that the customer tag is present -- for example, ``customer_tags CONTAINS <tag>`` -- to act on the audience.

The customer tag identifies the audience, so changing the tag name sends the entire audience again under the new tag. Only the **email** match key is used -- Amperity applies the tag and does not write any other profile attributes. Each run sends only the additions and removals since the previous run, not the full audience.

.. campaign-shopify-graphql-end

.. campaign-shopify-graphql-api-note-start

.. note:: This destination uses the `Shopify GraphQL Admin API <https://shopify.dev/docs/api/admin-graphql>`__ |ext_link|.

.. campaign-shopify-graphql-api-note-end

.. campaign-shopify-graphql-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. campaign-shopify-graphql-beta-end

.. campaign-shopify-graphql-scope-start

.. note:: Sending an audience requires the ``write_customers`` access scope on the Shopify app. Pulling data does not. A credential without this scope fails the send.

.. campaign-shopify-graphql-scope-end

.. campaign-shopify-graphql-existing-customers-start

.. note:: Shopify must already contain a customer whose email matches an audience member. Amperity applies the tag to customers that already exist; an audience member that Shopify cannot match by email is reported as a failed row.

.. campaign-shopify-graphql-existing-customers-end

.. campaign-shopify-graphql-partial-failure-start

.. caution:: A run can partially succeed. An individual audience member is counted as a failed row -- while the rest of the run completes -- when the member's row has no email, when no Shopify customer matches the email, when more than one Shopify customer matches the email, or when Shopify rejects the tag for that customer (for example, the customer is already at Shopify's limit of 250 tags).

.. campaign-shopify-graphql-partial-failure-end

.. campaign-shopify-graphql-unmatched-chunk-start

.. important:: If none of the first 100 audience members match a Shopify customer, Amperity stops the send rather than reporting the entire audience as failed rows. This usually means that none of those members are customers of this store. Verify that the audience members shop with this store, and contact Amperity support if they do.

.. campaign-shopify-graphql-unmatched-chunk-end

.. campaign-shopify-graphql-idempotent-start

.. note:: Re-running a send is safe. Applying a tag that a customer already has, or removing a tag that a customer does not have, makes no change in Shopify.

.. campaign-shopify-graphql-idempotent-end

.. campaign-shopify-graphql-limits-start

.. note:: Amperity looks up one customer and applies or removes one tag per audience member, and paces the send to stay within Shopify's API rate limits. Time a representative audience before sending to a large store.

.. campaign-shopify-graphql-limits-end


.. _campaign-shopify-graphql-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-shopify-graphql-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Shop name**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-shopify-shop-name-start
             :end-before: .. credential-shopify-shop-name-end

       **Access token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-shopify-access-token-start
             :end-before: .. credential-shopify-access-token-end

       .. tip::

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-shopify-find-credentials-start
             :end-before: .. credential-shopify-find-credentials-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Audience primary key**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Customer tag**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-shopify-graphql-audience-tag-start
             :end-before: .. setting-shopify-graphql-audience-tag-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A campaign that is configured to use the sub-audience editor, or a one-time campaign that is configured to use a query or segment.

.. campaign-shopify-graphql-get-details-end


.. _campaign-shopify-graphql-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Shopify (GraphQL)**

.. campaign-shopify-graphql-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Shop name**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-shopify-shop-name-start
             :end-before: .. credential-shopify-shop-name-end

       **Access token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-shopify-access-token-start
             :end-before: .. credential-shopify-access-token-end

.. campaign-shopify-graphql-credentials-steps-end


.. _campaign-shopify-graphql-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Shopify (GraphQL)**

.. campaign-shopify-graphql-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add destination
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **Customer tag** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-shopify-graphql-audience-tag-start
             :end-before: .. setting-shopify-graphql-audience-tag-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. campaign-shopify-graphql-add-steps-end
