.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Customer.io
.. |plugin-name| replace:: "Customer.io"
.. |credential-type| replace:: "customerio"
.. |required-credentials| replace:: "API Key" and "Region"
.. |what-send| replace:: customer profile attributes
.. |where-send| replace:: a |destination-name| workspace
.. |filter-the-list| replace:: "cus"


.. meta::
    :description lang=en:
        Configure Amperity to send customer profile attributes to a Customer.io workspace.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer profile attributes to a Customer.io workspace.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Customer.io

====================================================
Configure destinations for Customer.io
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-customerio-start
   :end-before: .. term-customerio-end

.. destination-customerio-start

The Customer.io connector sends |what-send| from Amperity into |where-send|, keeping each person's profile current so |destination-name| can use unified customer data for messaging and segmentation.

Each row in the query results is one person profile. The field selected by the **Person ID field** setting supplies the person's Customer.io identifier (the ``userId`` that Customer.io upserts each profile on); every other column is sent as a profile attribute (trait), using the column name and value as-is and preserving its type -- string, number, or boolean. Customer.io accepts arbitrary attributes, so there is no fixed set of recognized attribute names.

Amperity syncs profiles incrementally: only the rows whose attributes changed since the last successful run are sent, and unchanged rows are reported as sent from cache. Each row is upserted -- a new person is added, an existing person is updated.

.. destination-customerio-end

.. destination-customerio-api-note-start

.. note:: This destination uses the `Customer.io Pipelines API <https://docs.customer.io/integrations/api/cdp/>`__ |ext_link|, sending each profile with ``POST /identify``.

.. destination-customerio-api-note-end

.. destination-customerio-beta-start

.. admonition:: Beta

   The Customer.io connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-customerio-beta-end

.. destination-customerio-prereq-start

.. important:: Get the **Pipelines API key** from your Customer.io workspace under **Account Settings > API Credentials**. This is the Pipelines API key, not the App API key -- they are different credential types. Also confirm which region hosts the workspace (**us** or **eu**); Customer.io has no cross-region fallback, so the **Region** credential must match the workspace's region.

.. note:: A successful connection test upserts a fixed synthetic profile named ``amperity-test-connection`` into the workspace. This is harmless and idempotent -- repeated tests update the same profile rather than creating new ones -- and is Customer.io's own recommended way to validate credentials, because the Pipelines API has no dedicated health-check endpoint.

.. note:: Amperity sends one request per changed profile and paces the requests to stay well under Customer.io's rate limit, so a large send takes proportionally longer.

.. destination-customerio-prereq-end


.. _destination-customerio-get-details:

Get details
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-customerio-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       |checkmark-required| **Required**

       Both credential fields are required. No call can be made without them.

       **API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-customerio-api-key-start
             :end-before: .. credential-customerio-api-key-end

       **Region**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-customerio-region-start
             :end-before: .. credential-customerio-region-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration setting**

       **Person ID field**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-customerio-person-id-field-start
             :end-before: .. setting-customerio-person-id-field-end


.. destination-customerio-get-details-end


.. _destination-customerio-credentials:

Configure credentials
====================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Customer.io**

.. destination-customerio-credentials-steps-start

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

       |checkmark-required| **Required**

       Both credential fields are required.

       **API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-customerio-api-key-start
             :end-before: .. credential-customerio-api-key-end

       **Region**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-customerio-region-start
             :end-before: .. credential-customerio-region-end

.. destination-customerio-credentials-steps-end


.. _destination-customerio-add:

Add destination
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Customer.io**

.. destination-customerio-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

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
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Person ID field**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-customerio-person-id-field-start
             :end-before: .. setting-customerio-person-id-field-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. destination-customerio-add-steps-end


.. _destination-customerio-validation:

Data validation
====================================================

.. destination-customerio-validation-start

Amperity sends every changed row, except for rows it cannot build a valid request for. A row is reported as failed, and the run continues, when any of the following is true:

* The field selected by the **Person ID field** setting is empty for that row, so the person cannot be addressed in Customer.io.
* Customer.io rejects that row's request as malformed -- for example, the profile exceeds Customer.io's per-request payload limit (32 KB) or its per-person attribute limits (attribute name up to 150 bytes, value up to 1000 bytes, up to 300 attributes per person). These limits are published by Customer.io and enforced on Customer.io's side, not by Amperity.
* Customer.io returns a rate-limit or temporary server error for that row.

Failed rows are reported in the destination's run details. When a run produces many failures, only the first distinct error messages are shown; the failed-row count still reflects every failure.

Some conditions stop the entire run instead of failing individual rows:

* The query results have no column mapped to the **Person ID field** -- caught before any data is sent.
* Customer.io rejects the API key. Because the same key is used for every request, the run stops immediately rather than failing every row in turn. Confirm the connected credential uses the Pipelines API key, from **Account Settings > API Credentials**, and not the App API key.

.. destination-customerio-validation-end
