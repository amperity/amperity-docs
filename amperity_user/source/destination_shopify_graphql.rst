.. https://docs.amperity.com/user/


.. |destination-name| replace:: Shopify (GraphQL)
.. |what-send| replace:: audiences


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Shopify (GraphQL).

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Shopify (GraphQL).

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Shopify (GraphQL)

==================================================
Send query results to Shopify (GraphQL)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-shopify-start
   :end-before: .. term-shopify-end

.. include:: ../../amperity_operator/source/destination_shopify_graphql.rst
   :start-after: .. destination-shopify-graphql-api-note-start
   :end-before: .. destination-shopify-graphql-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

.. sendto-shopify-graphql-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. sendto-shopify-graphql-beta-end

.. sendto-shopify-graphql-steps-to-send-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - :ref:`Build a query <sendto-shopify-graphql-build-query>`


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - :ref:`Add orchestration <sendto-shopify-graphql-add-orchestration>`


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - :ref:`Run orchestration <sendto-shopify-graphql-run-orchestration>`

.. sendto-shopify-graphql-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-shopify-graphql-build-query:

Build query
==================================================

.. sendto-shopify-graphql-build-query-start

Build a query that returns the **email** field for the audience members to send to |destination-name|. Amperity matches each row to a Shopify customer by email and applies the customer tag to the matching customers.

The following example shows a query that returns email addresses from the **Customer 360** table:

.. code-block:: sql

   SELECT
     email
   FROM Customer_360

.. note:: Shopify must already contain a customer whose email matches a row. A row that Shopify cannot match by email is reported as a failed row.

.. sendto-shopify-graphql-build-query-end


.. _sendto-shopify-graphql-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-shopify-graphql-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
