.. destination-braze-cohorts-about-end
.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Braze Cohorts
.. |plugin-name| replace:: "Braze Cohorts"
.. |credential-type| replace:: "braze-cohort"
.. |required-credentials| replace:: "Client Data Import Key"
.. |audience-primary-key| replace:: "external_id"
.. |what-send| replace:: audience lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "braz"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Braze Cohorts.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Braze Cohorts.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Braze Cohorts

==================================================
Configure destinations for Braze Cohorts
==================================================

.. destination-braze-cohorts-intro-start

|destination-name| allows you to send a list of user IDs from Amperity to Braze using the `User cohort  <https://www.braze.com/docs/partners/isv_partners/cohort_import/>`__ |ext_link| endpoint, after which they are automatically added to a named cohort. You can then use that cohort with Braze campaigns and canvases.

.. destination-braze-cohorts-intro-end

.. destination-braze-cohorts-context-start

Amperity manages the full sync process: creating the cohort in Braze if it does not exist, sending user IDs in optimized batches, and reporting results back to your workflow.

.. note:: This destination only syncs user ID lists into cohorts. It does not sync profile attributes, events, or purchase data.

   To send customer profile attributes to Braze, use the :doc:`Braze destination <destination_braze>`.

.. destination-braze-cohorts-context-end


.. _destination-braze-cohorts-about-cohorts:

About Braze Cohorts
==================================================

.. destination-braze-cohorts-about-start

A cohort in Braze is a group of users identified by their user IDs. When you send an audience from Amperity to |destination-name|:

* The cohort is created in Braze if it does not already exist
* The cohort is updated if it already exists
* Only user IDs are sent; no profile attributes or event data
* Users with a NULL value in the ID field are automatically skipped

Cohorts sent from Amperity are available in the Braze dashboard under **Segments**, where you can filter by cohort name to verify users were imported.

.. destination-braze-cohorts-about-end

.. destination-braze-cohorts-internal-id-start

.. note:: Amperity prefixes cohort IDs with ``amperity-`` internally. For example, a cohort named "High Value" creates a cohort ID of ``amperity-High Value``. The cohort name (without the prefix) is what appears in the Braze dashboard.

.. destination-braze-cohorts-internal-id-end


.. _destination-braze-cohorts-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-braze-cohorts-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       The Client Data Import Key for your Braze account. This key is found in the Braze dashboard under **Partner Integrations > Technology Partners > Amperity**.

       .. admonition:: Get the Client Data Import Key

          Log in to the Braze dashboard and navigate to **Partner Integrations > Technology Partners > Amperity** (the exact path may vary by Braze version; sometimes under **Integrations > Technology Partners**).

          Copy the **Data Import Key**. This value is used to configure credentials in Amperity.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Instance**

          The Braze REST API instance for your account. This is a region identifier such as "US-01", "US-02", "EU-01", or "JP-01".

          The Braze instance can be found in your Braze dashboard URL or in account settings. For example, if your URL is ``https://dashboard-03.braze.com``, the instance is "US-03".

          .. list-table::
             :widths: 30 70
             :header-rows: 1

             * - Instance Value
               - API Endpoint Used
             * - US-01
               - ``https://rest.iad-01.braze.com``
             * - US-02
               - ``https://rest.iad-02.braze.com``
             * - US-03 through US-08
               - ``https://rest.iad-0X.braze.com``
             * - JP-01
               - ``https://rest.jp-01.braze.com``
             * - EU formats
               - ``https://rest.fra-0X.braze.eu``


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Cohort settings**

       **Cohort Name**

          The name of the cohort to create or update in Braze. This is how the cohort appears in the Braze dashboard.

          .. note:: Amperity prefixes cohort IDs with ``amperity-``. For example, a name of ``High Value`` creates cohort ID in Braze of ``amperity-High Value``.

       **User ID Field**

          The name of the column in your query or segment results that contains the Braze user identifier. Defaults to ``external_id``. Change this if your dataset uses a different column name.

.. destination-braze-cohorts-get-details-end


.. _destination-braze-cohorts-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Braze Cohorts**

.. destination-braze-cohorts-credentials-steps-start

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
     - In the **Credentials settings** dialog box, do the following:

       From the **Plugin** dropdown, select |destination-name|.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this credential.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Configure the following settings, and then click **Save**.

       **Client Data Import Key**

          The Data Import Key from your Braze dashboard. This key is found under **Partner Integrations > Technology Partners > Amperity** (exact path may vary depending on Braze version).

       **Instance**

          The Braze REST API instance identifier for your account. For example: "US-01", "US-02", "EU-01", or "JP-01". This is in your Braze dashboard URL or account settings.

.. destination-braze-cohorts-credentials-steps-end


.. _destination-braze-cohorts-add:

Add destination
==================================================

.. TODO: Update shared inclusion file for Cohorts

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Braze Cohorts**

.. destination-braze-cohorts-add-steps-start

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
          :alt: Add a destination for Braze Cohorts.
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

       **Cohort Name**

          The name of the cohort to create or update in Braze. This name appears in the Braze dashboard.

       **User ID Field**

          The name of the column in your query or segment results that contains the Braze user identifier to send. Defaults to ``external_id``.

          If your Braze users are identified by email or a custom field, set this value to match the column name in your query results.


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

.. destination-braze-cohorts-add-steps-end


.. _destination-braze-cohorts-build-query:

Build a query
==================================================

.. destination-braze-cohorts-build-query-start

Build a query that returns a list of users matched by their **external_id**, **device_id**, or an **alias**.

* **external_id** and **alias** should be used with known users
* **device_id** should be used with anonymous users

.. destination-braze-cohorts-build-query-end

.. destination-braze-cohorts-build-query-example-start

**SQL example**

.. code-block:: sql

   SELECT
     external_id
   FROM Customer360
   WHERE email IS NOT NULL

.. destination-braze-cohorts-build-query-example-end

.. destination-braze-cohorts-build-query-custom-id-start

**Using a different ID field**

If your Braze users are identified by email or a custom field, return that column and set the **User ID Field** setting to match:

.. code-block:: sql

   SELECT
     c360.email AS external_id
   FROM Customer360 c360

For example associating anonymous web traffic with the **device_id**:

.. code-block:: sql

   SELECT
     web_device_id AS device_id
   FROM Web_Events_Table

.. destination-braze-cohorts-build-query-custom-id-end

.. destination-braze-cohorts-build-query-tips-start

.. tip:: Test with a small audience first (for example, add ``LIMIT 100``) before running a full sync.

.. important:: Users with a **NULL** value in the ID field are automatically skipped and not sent to Braze.

.. destination-braze-cohorts-build-query-tips-end


.. _destination-braze-cohorts-add-orchestration:

Add orchestration
==================================================

.. destination-braze-cohorts-add-orchestration-start

To send cohorts to Braze, add an orchestration that connects your query or segment to the |destination-name| destination.

**To add an orchestration for Braze Cohorts**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Navigate to the **Activations** page and click **Add orchestration**.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - Select the query or segment you built that returns user IDs.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Select the **Braze Cohorts** destination.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - Configure the destination settings:

       * **Cohort Name**—the name of the cohort as it should appear in Braze
       * **User ID Field**—the column name containing user IDs (default: ``external_id``)

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - Set the workflow to **Manual** initially. Click **Save**.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - From the **Activations** page, select your orchestration and click **Run**.

       Monitor status. When complete, the cohort will be available in Braze.

       In the Braze dashboard, navigate to **Segments** and filter by the cohort name to verify users were imported.

.. destination-braze-cohorts-add-orchestration-end


.. _destination-braze-cohorts-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. destination-braze-cohorts-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
          :width: 500 px
          :alt: Review a notifications error.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-b-start
          :end-before: .. workflow-actions-common-table-section-one-b-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The workflow tab, showing a workflow with errors.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`destination-braze-cohorts-workflow-actions-invalid-credentials`
       * :ref:`destination-braze-cohorts-workflow-actions-wrong-instance`
       * :ref:`destination-braze-cohorts-workflow-actions-users-not-appearing`


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. destination-braze-cohorts-workflow-actions-end


.. _destination-braze-cohorts-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. destination-braze-cohorts-workflow-actions-invalid-credentials-start

The Client Data Import Key is incorrect or has expired.

To resolve this error:

#. Log in to the Braze dashboard.
#. Navigate to **Partner Integrations > Technology Partners > Amperity**.
#. Verify the **Data Import Key** is correct and has not expired.
#. Open the **Credentials** page in Amperity and update the credential if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-braze-cohorts-workflow-actions-invalid-credentials-end


.. _destination-braze-cohorts-workflow-actions-wrong-instance:

Wrong instance
--------------------------------------------------

.. destination-braze-cohorts-workflow-actions-wrong-instance-start

A 401 error may occur if the Instance value does not match your account's actual region.

To resolve this error:

#. Verify the instance string matches your Braze account region.
#. The instance can be found in your Braze dashboard URL. For example, if your URL is ``https://dashboard-03.braze.com``, the instance is "US-03".
#. Open the destination settings in Amperity and update the **Instance** value if required.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-braze-cohorts-workflow-actions-wrong-instance-end


.. _destination-braze-cohorts-workflow-actions-users-not-appearing:

Users not appearing in Braze
--------------------------------------------------

.. destination-braze-cohorts-workflow-actions-users-not-appearing-start

Users may not appear in Braze cohorts if the ``external_id`` values in Amperity do not match the IDs in Braze.

To resolve this error:

#. Verify the user ID field configured in Amperity matches how users are identified in your Braze account.
#. Check that your query returns the correct user ID column.
#. Ensure users in Amperity have matching records in Braze.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. destination-braze-cohorts-workflow-actions-users-not-appearing-end
