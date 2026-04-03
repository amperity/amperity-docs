.. https://docs.amperity.com/infrastructure/

:orphan:



.. meta::
    :description lang=en:
        A reference for Amperity cloud infrastructure.

.. meta::
    :content class=swiftype name=body data-type=text:
        A reference for Amperity cloud infrastructure.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Amperity cloud infrastructure

==================================================
Cloud infrastructure
==================================================

.. infrastructure-about-start

Amperity runs on Amazon AWS or Microsoft Azure cloud infrastructure. This topic consolidates information about cloud infrastructure settings and options:

* :ref:`Amperity API base URLs <infrastructure-api-base-url>`
* :ref:`IP addresses for allowlists <infrastructure-allowlists>`
* :ref:`Microsoft Azure-specific settings <infrastructure-microsoft-azure>`
* :ref:`Regions for storage and cloud infrastructure <infrastructure-regions>`
* :ref:`SFTP hostnames <infrastructure-hostnames>`
* :ref:`Snowflake account locator IDs <infrastructure-snowflake>`

.. infrastructure-about-end


.. _infrastructure-api-base-url:

Base URLs for Amperity API
==================================================

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. api-amperity-base-url-start
   :end-before: .. api-amperity-base-url-end

.. admonition:: Base URLs and sandboxes

   .. include:: ../../amperity_api/source/base_url.rst
      :start-after: .. api-amperity-base-url-sandboxes-start
      :end-before: .. api-amperity-base-url-sandboxes-end


.. _infrastructure-api-base-url-aws:

Amazon AWS
--------------------------------------------------

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-aws-start
   :end-before: .. base-url-aws-end

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-tenant-id-start
   :end-before: .. base-url-tenant-id-end


.. _infrastructure-api-base-url-australia:

Base URLs in Australia
++++++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-aws-australia-start
   :end-before: .. base-url-aws-australia-end


.. _infrastructure-api-base-url-azure:

Microsoft Azure
--------------------------------------------------

.. include:: ../../amperity_api/source/base_url.rst
   :start-after: .. base-url-azure-start
   :end-before: .. base-url-azure-end


.. _infrastructure-allowlists:

IP addresses for allowlists
==================================================

.. TODO: Keep the start and end strings just like they are.

.. send-data-to-amperity-ip-allowlists-start

You can add Amperity services to allowlists that may be required by upstream systems. The IP address that should be added to the allowlist for the upstream system depends on the service to which that upstream system connects.

.. send-data-to-amperity-ip-allowlists-end

.. send-data-to-amperity-ip-allowlists-important-start

.. important:: Amperity does not maintain allowlists for connections that are made to Amperity services from upstream systems.

.. send-data-to-amperity-ip-allowlists-important-end

.. send-data-to-amperity-ip-allowlists-warning-start

.. warning:: Using an IP allowlist is not recommended. Many issues can arise when an IP address is on an allowlist within Amazon AWS or Microsoft Azure because both services use their own internal networks for routing.

   * Amazon AWS recommends against using allowlists on the SourceIP condition because it `denies access to AWS services that make calls on your behalf <https://aws.amazon.com/premiumsupport/knowledge-center/iam-restrict-calls-ip-addresses/>`__ |ext_link|
   * Microsoft Azure suggests that using IP allowlists for shared access signature (SAS) tokens is only recommended for use with IP addresses that are located outside of Microsoft Azure.

.. send-data-to-amperity-ip-allowlists-warning-end

**When connecting to your Amperity tenant**

.. send-data-to-amperity-ip-allowlists-amperity-start

Most connections are made directly to your Amperity tenant. Use one of the following Amperity IP addresses for an allowlist that is required by an upstream system. The specific IP address to use depends on the location in which your tenant is hosted:

* On Amazon AWS use "52.42.237.53"
* On Amazon AWS (Canada) use "3.98.199.97"
* On Microsoft Azure use "104.46.106.84" for production and "20.81.91.210" for failover
* On Microsoft Azure (EU) use "20.123.127.54"

.. send-data-to-amperity-ip-allowlists-amperity-end

**When connecting to the attached SFTP site**

.. send-data-to-amperity-ip-allowlists-sftp-start

Some connections are made directly to the SFTP site that is included with your Amperity tenant. The specific IP address to use depends on the location in which your tenant is hosted:

* On Amazon AWS use "52.11.51.214"
* On Amazon AWS (Australia) use "3.44.64.64/29"
* On Amazon AWS (Canada) use "52.60.229.171"
* On Microsoft Azure use "20.36.236.80"
* On Microsoft Azure (EU) use "51.104.139.110"

.. send-data-to-amperity-ip-allowlists-sftp-end

.. send-data-to-amperity-ip-allowlists-tip-start

.. tip:: Alternatives to using an allowlist include: 

   #. Cross-account roles within Amazon AWS, which requires using an Amazon Resource Name (ARN) for the role with cross-account access.
   #. Using Azure Data Share.

   Discuss these options with your Amperity representative prior to making a decision to allowlist IP addresses.

.. send-data-to-amperity-ip-allowlists-tip-end


.. _infrastructure-microsoft-azure:

Microsoft Azure subnet IDs
==================================================

.. infrastructure-microsoft-azure-start

Microsoft Azure has specific settings for subnet IDs when using `Amperity Bridge for Databricks <../operator/bridge_databricks.html>`__.

.. infrastructure-microsoft-azure-end

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-sync-with-amperity-subnet-ids-start
   :end-before: .. bridge-databricks-sync-with-amperity-subnet-ids-end

**Azure East US 2**

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-sync-with-amperity-subnet-ids-az-prod-east-us-2-start
   :end-before: .. bridge-databricks-sync-with-amperity-subnet-ids-az-prod-east-us-end

**Azure North Europe**

.. include:: ../../amperity_operator/source/bridge_databricks.rst
   :start-after: .. bridge-databricks-sync-with-amperity-subnet-ids-az-prod-en1-north-europe-start
   :end-before: .. bridge-databricks-sync-with-amperity-subnet-ids-az-prod-en1-north-europe-end


.. _infrastructure-regions:

Regions for storage
==================================================

.. infrastructure-regions-storage-start

Amperity storage is hosted in :ref:`Amazon AWS <infrastructure-regions-storage-aws>` or :ref:`Microsoft Azure <infrastructure-regions-storage-azure>`.

.. infrastructure-regions-storage-end

.. infrastructure-regions-storage-note-start

.. note:: Regions for storage are ony necessary when configuring a new tenant to u`use customer-hosted storage <../operator/storage.html>`__ instead of Amperity-hosted storage.

.. infrastructure-regions-storage-note-end


.. _infrastructure-regions-storage-aws:

Amazon AWS
--------------------------------------------------

.. infrastructure-regions-storage-aws-start

Amperity is hosted in one of the following Amazon AWS regions:

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Australia, primary (Sydney)
     - **ap-southeast-2**
   * - Australia, backup (Melbourne)
     - **ap-southeast-4**
   * - Canada (Central)
     - **ca-central-1**
   * - US West (Oregon)
     - **us-west-2**

`Cross-region transfer costs <https://aws.amazon.com/s3/pricing/>`__ |ext_link| will apply when Amazon S3 storage is configured in different region than the one in which your Amperity tenant is hosted and will increase latency.

.. infrastructure-regions-storage-aws-end


.. _infrastructure-regions-storage-azure:

Microsoft Azure
--------------------------------------------------

.. infrastructure-regions-storage-azure-start

Amperity is hosted in one of the following Microsoft Azure regions:

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - US East 2
     - **eastus2**
   * - North Europe
     - **northeurope**

`Cross-region transfer costs <https://azure.microsoft.com/en-us/pricing/details/bandwidth/>`__ |ext_link| will apply when Azure Blob Storage is configured in different region than the one in which your Amperity tenant is hosted and will increase latency.

.. infrastructure-regions-storage-azure-end


.. _infrastructure-hostnames:

SFTP hostnames
==================================================

.. TODO: Keep the start and end strings just like they are.

.. about-tenant-sftp-start

Every Amperity tenant includes an SFTP site with a hostname of ``<tenant>.sftp.amperity.com``. For example, if your company name is **Socktown**, then your tenant's SFTP hostname is ``socktown.sftp.amperity.com``. The hostname is always all lowercase.

The SFTP site is provisioned by an Amperity administrator after the initial tenant creation. As such, the SFTP site is not immediately available, but this is not a long process. When the SFTP site is ready, Amperity uses SnapPass to send you the connection details. If you wish to use RSA key-based authentication, please provide the public key to your Amperity administrator when requesting SFTP access.

.. about-tenant-sftp-end

.. about-tenant-sftp-older-tenants-start

.. important:: The hostname for the SFTP site is always ``<tenant-name>.sftp.amperity.com``. Some older tenants may still be using the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. about-tenant-sftp-older-tenants-end

.. about-tenant-sftp-provisioned-start

Once provisioned, you may configure the SFTP site to support any desired SFTP workflow. External customer processes can be configured to connect to the site using SFTP, after which they can add data to or pick up data from the site to support any upstream or downstream workflow.

.. include:: ../../shared/file-formats.rst
   :start-after: .. formats-sftp-data-retention-start
   :end-before: .. formats-sftp-data-retention-end

The hostname for the SFTP site is always **[tenant-name].sftp.amperity.com**. Some older tenants may use the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. about-tenant-sftp-provisioned-end


.. _infrastructure-hostnames-australia:

SFTP hostnames in Australia
--------------------------------------------------

.. about-tenant-sftp-australia-start

In Australia, for tenants running on Amazon AWS use ``sftp-aws-apse2.amperity.com``.

.. about-tenant-sftp-australia-end


.. _infrastructure-snowflake:

Snowflake account locator IDs
==================================================

.. infrastructure-snowflake-note-start

.. note:: Snowflake account locator IDs are used with `Amperity Bridge for Snowflake <../operator/bridge_snowflake.html>`__.

.. infrastructure-snowflake-note-end

.. include:: ../../amperity_operator/source/bridge_snowflake.rst
   :start-after: .. bridge-snowflake-sync-amperity-configure-snowflake-account-locator-start
   :end-before: .. bridge-snowflake-sync-amperity-configure-snowflake-account-locator-end

