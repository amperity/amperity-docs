.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Provision the resources that Bring Your Own Compute uses by hand, for brands that prefer to create them themselves or want to review what Amperity provisions.

.. meta::
    :content class=swiftype name=body data-type=text:
        Provision the resources that Bring Your Own Compute uses by hand, for brands that prefer to create them themselves or want to review what Amperity provisions.

.. meta::
    :content class=swiftype name=title data-type=string:
        Manual provisioning

.. _compute-manual:

==================================================
Manual provisioning
==================================================

.. compute-manual-start

Amperity provisions the resources that Bring Your Own Compute (BYOC) uses automatically through the integration wizard. This topic is for brands that prefer to provision those resources by hand, or that want to review exactly what Amperity creates before running production workloads. The steps below are organized by compute environment.

.. compute-manual-end


.. _compute-databricks-manual:

Databricks
==================================================

.. compute-databricks-manual-start

Amperity provisions the resources in this section automatically through the integration wizard. The steps below describe the same resources for brands that prefer to create them by hand, or that need to review exactly what Amperity provisions. Run the SQL in a Unity Catalog-enabled SQL warehouse or notebook as a user with the required privileges.

Throughout, ``<tenant>`` is your Amperity tenant family identifier, ``<sp-application-id>`` is the application (client) ID of the service principal, and Amperity provides the exact IAM role ARNs, bucket or container URLs, and external IDs for your tenant. Use these names exactly -- Amperity's compute service expects this naming.

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
