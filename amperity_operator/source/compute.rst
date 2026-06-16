.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Run Amperity workloads on a Databricks or Snowflake account that is owned and managed by your brand.

.. meta::
    :content class=swiftype name=body data-type=text:
        Run Amperity workloads on a Databricks or Snowflake account that is owned and managed by your brand.

.. meta::
    :content class=swiftype name=title data-type=string:
        About compute

==================================================
About compute
==================================================

.. compute-about-start

Amperity runs data processing workloads -- such as Stitch, customer profile (database) generation, customer attribute (CDT) builds, queries, and segmentation -- on compute resources. By default, these workloads run on compute that is managed by Amperity.

**Bring your own compute (BYOC)** allows your brand to run Amperity workloads on a data platform that is owned and managed by your brand, such as Databricks. Compute runs within your brand's account, against data that is stored in your brand's :ref:`storage location <storage-configure-location>`, while Amperity continues to manage the control plane: the user interface, workflow orchestration, and managed connectors.

.. compute-about-end

.. compute-about-note-start

.. note:: Bring your own compute pairs with :ref:`bring your own storage <storage-configure-location>`. Together they keep both the storage and the processing of your brand's data within infrastructure that your brand owns and manages.

.. compute-about-note-end


.. _compute-what-runs-where:

What runs on your compute
==================================================

.. compute-what-runs-where-start

When bring your own compute is enabled for Databricks, the following workloads run on your brand's Databricks account:

* Source transformations -- customer attributes (CDTs) -- and domain tables
* Stitch, which runs on an on-demand Spark cluster
* Customer profile (database) generation
* Queries and segments

The following capabilities continue to run on Amperity-managed compute:

* Activation, including campaigns and journeys, and workflow orchestration
* Bridge and data ingest
* Real-time profiles and the Profile API
* Predictive models, AmpIQ, and the AI Assistant
* Control-plane operations: the user interface, monitoring, and managed connectors

.. compute-what-runs-where-end

.. compute-what-runs-where-note-start

.. note:: A tenant uses a single primary compute provider and a single SQL dialect; routing workloads across more than one compute provider is not supported. Bring your own compute is enabled for the full set of supported workloads, not selected on a per-workload basis.

.. compute-what-runs-where-note-end


.. _compute-databricks:

Run Amperity workloads on your own Databricks
==================================================

.. compute-databricks-start

.. note:: Running Amperity workloads on Databricks is in public preview. Functionality is added in phases, and bring your own compute is enabled for your tenant by Amperity.

Configure a tenant to run Amperity workloads on a Databricks workspace that is owned and managed by your brand. Amperity connects to your workspace using a service principal, provisions the `Unity Catalog <https://docs.databricks.com/aws/en/data-governance/unity-catalog/>`__ |ext_link| objects that it needs, and runs compute against data in your storage location.

Amperity does not require unmanaged access to your infrastructure. You provision or approve the workspace; Amperity is granted only the permissions it needs to orchestrate supported workloads; jobs are initiated from Amperity and execute in your workspace; and results, metadata, and logs flow back to Amperity for monitoring and support.

.. compute-databricks-end


.. _compute-databricks-prerequisites:

Account prerequisites
--------------------------------------------------

.. compute-databricks-prerequisites-start

Before you connect Amperity to your Databricks workspace, verify the following.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Prerequisite
     - Description

   * - **Bring your own storage**
     - Your Amperity tenant must be configured to use a :ref:`storage location <storage-configure-location>` that is owned and managed by your brand. Databricks is where compute happens; both the source and the destination for business data remain in your storage location.

   * - **Unity Catalog**
     - Your workspace must be enabled for `Unity Catalog <https://docs.databricks.com/aws/en/data-governance/unity-catalog/>`__ |ext_link|. Amperity creates a catalog for its workloads and does not require a default (managed) storage location to be set on the metastore.

   * - **Account administrator**
     - The person who completes the integration must be a Databricks *account* administrator (not only a workspace administrator). Account-administrator access is required to read the account ID, create a service principal, and generate access tokens.

   * - **Region**
     - Your Databricks workspace and your Amperity storage location should be in the same cloud region. Running compute and storage in different regions causes slower jobs, additional networking charges, and harder troubleshooting.

   * - **Network capacity**
     - The workspace network must have enough available IP addresses for Stitch to start on-demand Spark clusters. Databricks assigns two IP addresses per node, so size the subnet for the largest cluster a Stitch run will use.

.. compute-databricks-prerequisites-end

.. compute-databricks-prerequisites-warning-start

.. important:: Bring your own compute is enabled by Amperity for your tenant. If the **Databricks** option does not appear under **Settings** > **Integrations**, contact `Amperity Support <https://support.amperity.com/>`__ |ext_link| to enable it.

.. compute-databricks-prerequisites-warning-end


.. _compute-databricks-ansi-mode:

Configure ANSI mode
--------------------------------------------------

.. compute-databricks-ansi-mode-start

Databricks SQL warehouses run with an `ANSI mode <https://docs.databricks.com/aws/en/sql/language-manual/parameters/ansi_mode>`__ |ext_link| setting that changes how SQL resolves data types. For example, ``COALESCE(<integer>, <string>)`` returns a string when ANSI mode is off, but coerces numerically -- or raises an error -- when ANSI mode is on.

Amperity expects **ANSI mode to be off** so that type resolution matches how Amperity analyzes and builds SQL. For Databricks accounts created on or after October 19, 2022, ANSI mode is on by default, so this setting must be changed deliberately during onboarding.

.. compute-databricks-ansi-mode-end

.. compute-databricks-ansi-mode-steps-start

#. Check the current value:

   .. code-block:: sql

      SET ANSI_MODE;

#. If ANSI mode is on, set it off at the warehouse or account level:

   .. code-block:: sql

      SET spark.sql.ansi.enabled = false;

.. compute-databricks-ansi-mode-steps-end

.. compute-databricks-ansi-mode-warning-start

.. warning:: Changing ANSI mode after onboarding can change the results of existing queries and customer attributes. Review the `Databricks ANSI mode documentation <https://docs.databricks.com/aws/en/sql/language-manual/parameters/ansi_mode>`__ |ext_link| before adjusting this setting.

.. compute-databricks-ansi-mode-warning-end


.. _compute-databricks-integration:

Integration steps
--------------------------------------------------

.. compute-databricks-integration-start

Amperity provisions all of the Databricks resources that it needs automatically. You provide a small number of connection details, and Amperity creates the service principal, storage credentials, external locations, catalog, volumes, cluster policy, and SQL warehouse for you.

.. compute-databricks-integration-end

**To connect Amperity to your Databricks workspace**

.. compute-databricks-integration-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - **Gather workspace details**

       Sign in to your Databricks account as an account administrator and collect the following values.

       * **Workspace URL**, in the form ``https://<workspace>.cloud.databricks.com`` (AWS) or ``https://<workspace>.azuredatabricks.net`` (Azure). Find it in the Databricks account console under **Workspaces**.
       * **Account ID**, a UUID found in the account console under the user menu.
       * **Workspace ID** (AWS only), a numeric value found in the workspace console under the user menu.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - **Generate access tokens**

       Amperity needs a short-lived account access token and a workspace access token to complete provisioning. Generate them using the `Databricks CLI <https://docs.databricks.com/aws/en/dev-tools/cli/>`__ |ext_link|.

       #. Generate an account access token:

          .. code-block:: bash

             databricks auth login --host https://accounts.cloud.databricks.com --account-id <account-id>
             databricks auth token --host https://accounts.cloud.databricks.com --account-id <account-id>

       #. Generate a workspace access token:

          .. code-block:: bash

             databricks auth login --host <workspace-url>
             databricks auth token --host <workspace-url>

       .. important:: OAuth tokens are valid for one hour. If provisioning fails with an authorization error, the token may have expired. Generate fresh tokens and try again.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - **Add the workspace in Amperity**

       #. In Amperity, go to **Settings** > **Integrations**.
       #. In the **Databricks** section, click **Add workspace**.
       #. Enter the **Workspace URL**, **Account ID**, **Account access token**, **Workspace access token**, and -- on AWS -- the **Workspace ID**.

          .. note:: On Microsoft Azure, you may also provide an optional **Access Connector ID**, in the form ``/subscriptions/.../accessConnectors/...``, when the workspace uses an Azure managed identity for storage access.

       #. Click to start provisioning.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - **Wait for provisioning to finish**

       Amperity provisions resources in your workspace and reports the current step and status as it works. Provisioning creates:

       * A service principal with OAuth credentials
       * Storage credentials for your tenant data and for Amperity build artifacts
       * External locations for data and artifact access
       * A Unity Catalog catalog and a default schema for Amperity compute
       * A volume for compute artifacts (the bootstrap JAR) and a volume for cluster logs
       * A cluster policy for compute jobs and a SQL warehouse
       * Grants that scope the service principal to only the resources above

       Provisioning takes a few minutes. Leave the page open until it reports that it is complete.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - **Run workloads on Databricks**

       After provisioning completes, configure Amperity to run workloads on the connected workspace.

       #. Open **Stitch** settings and select **Run on Databricks**, then select the integration you just created.
       #. Run Stitch, build customer profiles, and run queries as usual. These workloads now run on your Databricks account.

.. compute-databricks-integration-steps-end


.. _compute-databricks-sync:

Re-sync a workspace
--------------------------------------------------

.. compute-databricks-sync-start

Use **Sync** to re-apply the provisioning pipeline to a connected workspace -- for example, after an Amperity update adds a new Unity Catalog resource or grant. Syncing:

* Provisions any new Unity Catalog resources
* Re-applies grants for the existing service principal
* Keeps the existing service principal and *does not* rotate its credentials

To sync, open the workspace row under **Settings** > **Integrations** > **Databricks**, click **Sync**, and provide a current **Workspace access token** (and, on Azure, the optional **Access Connector ID**).

.. compute-databricks-sync-end


.. _compute-databricks-debugging:

Debugging steps
--------------------------------------------------

.. compute-databricks-debugging-start

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Symptom
     - Resolution

   * - The **Databricks** option does not appear under **Settings** > **Integrations**.
     - Bring your own compute is not yet enabled for your tenant. Contact `Amperity Support <https://support.amperity.com/>`__ |ext_link|.

   * - Provisioning fails with an authorization or access-denied error.
     - The account or workspace access token expired. OAuth tokens last one hour -- generate fresh tokens (Step 2) and try again.

   * - Provisioning fails while creating the catalog, with a cloud-storage "forbidden" or invalid-credential-trust-policy error.
     - The IAM role trust policy that grants Databricks access to your storage is still propagating. Amperity retries automatically; if the error persists, re-run provisioning after a few minutes.

   * - Catalog creation fails because the metastore has no managed storage location.
     - Amperity sets a managed location at the catalog level and does not require a metastore default. If you see this error, confirm your tenant is on a current Amperity release and contact Support.

   * - A Databricks workload fails and Amperity shows a generic "Workload failed, see run output for details" message.
     - The detailed error is written to the Databricks run output. Open the corresponding run in your Databricks workspace -- the Stitch run name has the form ``st-<timestamp>-<random>`` -- to see the underlying error and stack trace.

   * - A multipart table (for example, a CRT) fails to mount.
     - Multipart tables are not supported as native Databricks tables. This is a known limitation; do not build multipart tables on Databricks compute.

   * - A Stitch job fails partway through with an S3 ``403`` (access denied).
     - This usually indicates a storage-credential propagation or token-expiry issue. Re-sync the workspace and re-run the job.

   * - Stitch fails to start with an "insufficient free addresses in subnet" error.
     - The workspace network does not have enough available IP addresses for the Spark cluster. Work with your cloud or Databricks administrator to add or migrate to a larger subnet, or use a larger node type so the job needs fewer nodes, then re-run.

.. compute-databricks-debugging-end


.. _compute-databricks-security:

Security and access
--------------------------------------------------

.. compute-databricks-security-start

Bring your own compute follows a least-privilege model and a shared responsibility model.

.. _compute-databricks-shared-responsibility:

**Shared responsibility model.** When workloads run in your brand's Databricks account, responsibility for security is shared between Amperity and your brand.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Amperity is responsible for
     - Your brand is responsible for

   * - * Creating and scoping the service principal, storage credentials, external locations, catalog, and grants to the minimum required.
       * Storing the service principal secret securely and not returning it after creation.
       * Orchestrating supported workloads and providing recommended compute-sizing guidance.
       * The Amperity control plane: the user interface, workflow orchestration, and managed connectors.
     - * Security of your Databricks account and workspace, including user and administrator access.
       * Network and access controls on the workspace, such as IP access lists and token lifetimes.
       * Provisioning and scaling compute capacity -- cluster and warehouse policies, cloud quotas, and subnet capacity -- to meet Amperity's workload requirements.
       * Security and access controls on your storage location, including any PII redaction or column-level permissions.
       * Reviewing the resources and grants Amperity provisions, and the ANSI mode setting, before running production workloads.

.. note:: Activation and downstream delivery run on Amperity-managed compute, not on your Databricks account. Confirm the :ref:`boundaries of what runs where <compute-what-runs-where>` with your Amperity representative.

* **Scoped service principal.** Amperity creates a dedicated service principal per tenant. It is granted access only to the catalog, schemas, external locations, and volumes that Amperity provisions for that tenant. It has no access to other catalogs or data in your workspace.

* **Scoped storage credentials.** Storage credentials are scoped to your tenant's storage location. The service principal cannot reach storage outside the locations Amperity provisions, and Amperity build artifacts are mounted **read-only**.

* **Credential management.** The service principal's OAuth secret is stored by Amperity in a secrets manager and is never returned after creation. Syncing a workspace does not rotate the credential. Review the `Databricks recommendations for service principals and tokens <https://docs.databricks.com/aws/en/admin/users-groups/service-principals>`__ |ext_link|, including token lifetimes and IP access lists.

* **Audit logging.** Activity is logged in both systems. `Audit logging in Amperity <https://docs.amperity.com/reference/settings.html#about-activity-logs>`__ records user actions and workflow history; Databricks records `account and workspace audit events <https://docs.databricks.com/aws/en/admin/account-settings/audit-logs>`__ |ext_link| for activity performed by the service principal.

* **Do not embed secrets in configuration.** Do not place encryption keys, credentials, or other secrets in customer-attribute (CDT) definitions or query text, where they can appear in logs. Reference secrets by credential instead.

.. compute-databricks-security-end


.. _compute-databricks-manual:

Set up Databricks resources manually
--------------------------------------------------

.. compute-databricks-manual-start

Amperity provisions the resources in this section automatically through the integration wizard. The steps below describe the same resources for brands that prefer to create them by hand, or that need to review exactly what Amperity provisions. Run the SQL in a Unity Catalog-enabled SQL warehouse or notebook as a user with the required privileges.

Throughout, ``<tenant>`` is your Amperity tenant identifier, ``<sp-application-id>`` is the application (client) ID of the service principal, and Amperity provides the exact IAM role ARNs, bucket or container URLs, and external IDs for your tenant.

.. compute-databricks-manual-end

.. compute-databricks-manual-steps-start

#. **Create a service principal.** In the Databricks account console, create a service principal for Amperity compute and generate a client secret (OAuth). Note the application (client) ID and secret; the secret is shown only once. Assign the service principal to the target workspace with the ``USER`` role.

#. **Create storage credentials.** In the Databricks UI (**Catalog** > **External Data** > **Credentials**) or with the REST API, create two storage credentials:

   * ``amperity_cred_<tenant>`` for your tenant storage location, referencing the Amperity-provided IAM role (AWS) or managed identity / service principal (Azure) for read/write access.
   * ``amperity_artifact_cred_<tenant>`` for the Amperity artifact bucket, referencing the Amperity-provided artifact role.

   Record the external ID that Databricks generates for each credential and provide it to Amperity so the IAM role trust policy can be updated.

#. **Create external locations.** In the Databricks UI (**Catalog** > **External Data** > **External Locations**) or with the REST API, create two external locations:

   * ``amperity_ext_<tenant>`` at your tenant storage URL, using ``amperity_cred_<tenant>`` (read/write).
   * ``amperity_artifact_ext_<tenant>`` at the Amperity artifact URL, using ``amperity_artifact_cred_<tenant>``, set to **read-only**.

#. **Create the compute catalog and schema.** Create a catalog with an explicit managed location, plus a default schema. The managed location avoids any dependency on a metastore default storage location.

   .. code-block:: sql

      CREATE CATALOG IF NOT EXISTS `amperity_<tenant>`
        MANAGED LOCATION '<tenant-storage-url>/databricks/amperity_<tenant>/'
        COMMENT 'Catalog for Amperity compute';

      CREATE SCHEMA IF NOT EXISTS `amperity_<tenant>`.`default`
        COMMENT 'Default schema for Amperity compute';

#. **Create the artifact catalog, schema, and volume.** Amperity reads its bootstrap JAR from a read-only external volume in a shared internal catalog.

   .. code-block:: sql

      CREATE CATALOG IF NOT EXISTS `_amperity_internal`
        MANAGED LOCATION '<tenant-storage-url>/databricks/_amperity_internal/'
        COMMENT 'Catalog for Amperity artifacts';

      CREATE SCHEMA IF NOT EXISTS `_amperity_internal`.`default`;

      CREATE EXTERNAL VOLUME IF NOT EXISTS `_amperity_internal`.`default`.`artifacts`
        LOCATION '<amperity-artifact-url>';

#. **Create the cluster-logs volume.** Compute clusters write driver and executor logs to an external volume in your tenant catalog.

   .. code-block:: sql

      CREATE EXTERNAL VOLUME IF NOT EXISTS `amperity_<tenant>`.`default`.`cluster_logs`
        LOCATION '<tenant-storage-url>/databricks/cluster_logs/';

#. **Create the cluster policy and SQL warehouse.** Using the Databricks UI or REST API, create a cluster policy for Amperity Spark jobs (autoscaling, single-user mode, tagged with your tenant and stack) and a PRO SQL warehouse with serverless compute enabled. These cannot be created with SQL.

#. **Grant the service principal access.** Scope the service principal to only the resources above.

   .. code-block:: sql

      -- Tenant data
      GRANT READ FILES, WRITE FILES, CREATE EXTERNAL TABLE, CREATE EXTERNAL VOLUME
        ON EXTERNAL LOCATION `amperity_ext_<tenant>` TO `<sp-application-id>`;

      GRANT USE CATALOG, CREATE SCHEMA, USE SCHEMA, CREATE TABLE, READ VOLUME, SELECT
        ON CATALOG `amperity_<tenant>` TO `<sp-application-id>`;

      GRANT READ VOLUME, WRITE VOLUME
        ON VOLUME `amperity_<tenant>`.`default`.`cluster_logs` TO `<sp-application-id>`;

      -- Artifacts (read-only)
      GRANT READ FILES
        ON EXTERNAL LOCATION `amperity_artifact_ext_<tenant>` TO `<sp-application-id>`;

      GRANT USE CATALOG, CREATE SCHEMA
        ON CATALOG `_amperity_internal` TO `<sp-application-id>`;

      GRANT USE SCHEMA, READ VOLUME
        ON SCHEMA `_amperity_internal`.`default` TO `<sp-application-id>`;

   Grant ``CAN_USE`` on the cluster policy and the SQL warehouse to the service principal using the Databricks UI or REST API.

#. **Register the workspace with Amperity.** Provide Amperity with the service principal application ID and secret, the workspace URL, and the storage-credential external IDs so Amperity can finish binding the integration.

.. compute-databricks-manual-steps-end


.. _compute-snowflake:

Run Amperity workloads on your own Snowflake
==================================================

.. compute-snowflake-start

.. note:: Running Amperity workloads on Snowflake is a private preview. To express interest or to begin onboarding, contact `Amperity Support <https://support.amperity.com/>`__ |ext_link| or your Amperity representative.

Configure a tenant to run Amperity workloads on a Snowflake account that is owned and managed by your brand. Amperity connects to your account using a dedicated service role and user, and provisions the databases, warehouses, and integrations that it needs.

.. compute-snowflake-end


.. _compute-snowflake-prerequisites:

Account prerequisites
--------------------------------------------------

.. compute-snowflake-prerequisites-start

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Prerequisite
     - Description

   * - **Bring your own storage**
     - Your Amperity tenant must be configured to use a :ref:`storage location <storage-configure-location>` that is owned and managed by your brand.

   * - **Account administrator**
     - Onboarding requires a Snowflake user with the ``ACCOUNTADMIN`` role (or equivalent) to create roles, users, warehouses, storage integrations, and external access integrations.

   * - **Spark support**
     - Amperity runs Stitch on Snowflake using Snowpark / Spark. Confirm with Amperity that the required Snowflake capabilities are enabled on your account.

.. compute-snowflake-prerequisites-end


.. _compute-snowflake-integration:

Integration steps
--------------------------------------------------

.. compute-snowflake-integration-start

Snowflake onboarding is performed together with Amperity Support. At a high level:

#. Amperity provides a public key for the service user and the IAM role ARNs used by the storage integrations.
#. Your administrator creates the Snowflake objects described in :ref:`Set up Snowflake resources manually <compute-snowflake-manual>` (or runs the script Amperity provides).
#. Amperity validates the connection, configures workload identity federation for storage access, and registers the account.
#. Your administrator completes the remaining grants and integrations once the storage trust relationship is in place.

Contact `Amperity Support <https://support.amperity.com/>`__ |ext_link| to begin.

.. compute-snowflake-integration-end


.. _compute-snowflake-debugging:

Debugging steps
--------------------------------------------------

.. compute-snowflake-debugging-start

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Symptom
     - Resolution

   * - A workload fails to access storage with an authentication error.
     - Confirm the external access integration and network rule allow egress to the storage and STS endpoints, and that the workload identity federation secret is in place.

   * - A query fails on an identifier that exists in Snowflake.
     - Snowflake identifiers are case-sensitive. Unquoted identifiers are folded to uppercase; quote identifiers to preserve case. Confirm how Amperity creates tables for your account.

   * - Provisioning fails creating roles, warehouses, or integrations.
     - These objects require ``ACCOUNTADMIN`` (or equivalent). Confirm the onboarding user has the required role.

.. compute-snowflake-debugging-end


.. _compute-snowflake-manual:

Set up Snowflake resources manually
--------------------------------------------------

.. compute-snowflake-manual-start

The following objects make up a Snowflake bring-your-own-compute integration. Amperity provides the public key (``<amperity-public-key>``), the artifact role ARN, and the execution role ARN for your tenant. Throughout, ``<TENANT>`` is your Amperity tenant identifier in uppercase.

.. compute-snowflake-manual-end

.. compute-snowflake-manual-steps-start

#. **Create the database, schema, service role, and user.**

   .. code-block:: sql

      CREATE DATABASE IF NOT EXISTS AMPERITY_<TENANT>;
      CREATE SCHEMA   IF NOT EXISTS AMPERITY_<TENANT>.AMP_INTERNAL;

      CREATE ROLE IF NOT EXISTS AMPERITY_SERVICE_<TENANT>;

      CREATE USER IF NOT EXISTS AMPERITY_SVC_USER_<TENANT>
        DEFAULT_ROLE   = AMPERITY_SERVICE_<TENANT>
        RSA_PUBLIC_KEY = '<amperity-public-key>'
        COMMENT        = 'Amperity compute-gateway service account';

      GRANT ROLE AMPERITY_SERVICE_<TENANT> TO USER AMPERITY_SVC_USER_<TENANT>;

#. **Create warehouses.**

   .. code-block:: sql

      CREATE WAREHOUSE IF NOT EXISTS AMPERITY_<TENANT>_WH
        WAREHOUSE_SIZE = 'MEDIUM'
        AUTO_SUSPEND = 60
        AUTO_RESUME = TRUE
        INITIALLY_SUSPENDED = TRUE;

      GRANT USAGE ON WAREHOUSE AMPERITY_<TENANT>_WH TO ROLE AMPERITY_SERVICE_<TENANT>;

      ALTER USER AMPERITY_SVC_USER_<TENANT>
        SET DEFAULT_WAREHOUSE  = AMPERITY_<TENANT>_WH
            DEFAULT_NAMESPACE  = AMPERITY_<TENANT>.AMP_INTERNAL;

#. **Create storage integrations.** Create a read-only integration for Amperity build artifacts and a read/write integration for your tenant storage.

   .. code-block:: sql

      CREATE STORAGE INTEGRATION IF NOT EXISTS AMPERITY_STORAGE_<TENANT>
        TYPE = EXTERNAL_STAGE
        STORAGE_PROVIDER = 'S3'
        ENABLED = TRUE
        STORAGE_AWS_ROLE_ARN = '<amperity-artifact-role-arn>'
        STORAGE_ALLOWED_LOCATIONS = ('<amperity-artifact-url>');

      CREATE STORAGE INTEGRATION IF NOT EXISTS AMPERITY_REPO_STORAGE_<TENANT>
        TYPE = EXTERNAL_STAGE
        STORAGE_PROVIDER = 'S3'
        ENABLED = TRUE
        STORAGE_AWS_ROLE_ARN = '<tenant-execution-role-arn>'
        STORAGE_ALLOWED_LOCATIONS = ('<tenant-storage-url>');

      GRANT USAGE ON INTEGRATION AMPERITY_STORAGE_<TENANT>      TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT USAGE ON INTEGRATION AMPERITY_REPO_STORAGE_<TENANT> TO ROLE AMPERITY_SERVICE_<TENANT>;

#. **Register the account with Amperity.** Provide Amperity with the service user, role, warehouse, and the private key. Amperity validates the connection, reads the Snowflake IAM user and external ID from the storage integration, updates the storage role trust policy, and configures workload identity federation.

#. **Create the remaining objects.** After Amperity configures storage trust, create the stages, federation secret, network rule, and external access integration, and apply the grants.

   .. code-block:: sql

      CREATE STAGE  IF NOT EXISTS AMPERITY_<TENANT>.AMP_INTERNAL.CONFIG;
      CREATE STAGE  IF NOT EXISTS AMPERITY_<TENANT>.AMP_INTERNAL.LOGS;

      CREATE SECRET IF NOT EXISTS AMPERITY_<TENANT>.AMP_INTERNAL.AWS_S3_SECRET
        TYPE = WORKLOAD_IDENTITY_FEDERATION;

      CREATE OR REPLACE NETWORK RULE AMPERITY_<TENANT>.AMP_INTERNAL.CLOUD_STORAGE_NETWORK_RULE
        TYPE = HOST_PORT
        MODE = EGRESS
        VALUE_LIST = (
          'sts.amazonaws.com:443',
          'sts.<aws-region>.amazonaws.com:443',
          's3.<aws-region>.amazonaws.com:443',
          's3.amazonaws.com:443'
        );

      CREATE EXTERNAL ACCESS INTEGRATION IF NOT EXISTS CLOUD_STORAGE_<TENANT>_SPARK_ACCESS
        ALLOWED_NETWORK_RULES = (AMPERITY_<TENANT>.AMP_INTERNAL.CLOUD_STORAGE_NETWORK_RULE)
        ALLOWED_AUTHENTICATION_SECRETS = (AMPERITY_<TENANT>.AMP_INTERNAL.AWS_S3_SECRET)
        ENABLED = TRUE;

      GRANT ALL PRIVILEGES ON DATABASE AMPERITY_<TENANT> TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT USAGE ON SCHEMA AMPERITY_<TENANT>.AMP_INTERNAL TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT EXECUTE SPARK APPLICATION ON ACCOUNT TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT DATABASE ROLE SNOWFLAKE.SPARK_USER TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT ALL ON STAGE AMPERITY_<TENANT>.AMP_INTERNAL.CONFIG TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT ALL ON STAGE AMPERITY_<TENANT>.AMP_INTERNAL.LOGS   TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT READ ON SECRET AMPERITY_<TENANT>.AMP_INTERNAL.AWS_S3_SECRET TO ROLE AMPERITY_SERVICE_<TENANT>;
      GRANT USAGE ON INTEGRATION CLOUD_STORAGE_<TENANT>_SPARK_ACCESS TO ROLE AMPERITY_SERVICE_<TENANT>;

.. compute-snowflake-manual-steps-end
