.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        A landing page for the collection of content about DataGrid and AmpID.

.. meta::
    :content class=swiftype name=body data-type=text:
        A landing page for the collection of content about DataGrid and AmpID.

.. meta::
    :content class=swiftype name=title data-type=string:
        Start here

==================================================
Start here
==================================================

.. start-here-start

Start here to learn how to configure Amperity for all of your use cases.  Use DataGrid to pull all of your customer data from any source-–online, offline, historical, streaming-–without requiring schema planning or ETL. Use DataGrid to send sends results of any size and type to any of your downstream applications and workflows.

.. start-here-end


.. _start-here-about:

About this topic collection
==================================================

.. start-here-about-start

The left-side navigation (from top to bottom) in this topic collection uses a verb-based approach to loosely organize around the series of actions that you may do when configuring Amperity.

.. note:: This left-to-right configuration workflow is most common whenever you add new data sources to Amperity.

   This is because that workflow typically requires adding couriers, applying semantic tags, making domain tables available to Stitch, refactoring your customer 360 database (or other databases, as needed), and then making those results available to queries and/or segments, depending on the types of downstream workflows you need to support.

   As you do these steps, you will move from the top toward the bottom of the left-side navigation in Amperity. For example: **Sources** > **Stitch** > **Customer 360**, and so on.

The left-side navigation has sections for the following activities:

.. TODO: Need to add links to topics in the following list.

#. Using a sandbox to make configuration changes, validating those changes in the sandbox, and then promoting those changes to your production tenant.
#. Managing data sources, including ensuring semantic tags are applied to raw data, and ensuring that data tables that are made available to the Stitch process are in the right shapes for your business requirements.
#. Running Stitch and validating those results.
#. Building your customer 360 database and managing any other databases and tables that are required to support your business requirements.
#. Managing destinations, including configuring them so that data analysts and marketers in your organization can use Amperity to build queries and send data to downstream workflows and/or define audiences and campaigns that can be sent to a variety of marketing channels.
#. Configuring certain end-to-end workflows to run on a defined schedule.

.. start-here-about-end


.. _start-here-tenant:

About your Amperity tenant
==================================================

.. start-here-tenant-start

Customers use Amperity in many different ways:

* **AmpID** for identity resolution and management
* **Amp360** for complete customer profiles
* **AmpIQ** for customer intelligence and activation
* **DataGrid** as a power grid for customer data

A tenant is an instance of Amperity that supports all of these combinations from a common starting state:

* An empty **Sources** page that is ready to be configured to pull data to Amperity from any location.
* A **Stitch** page shows the results of processing all of the data that was pulled to Amperity.
* A **Customer 360** page, in which a database is built using the output of the Stitch process as the starting point.
* A **Queries** page that runs queries against the customer 360 to return subsets of data.
* An empty **Destinations** page that is ready to be configured to send results of queries made in the Segments page to any downstream process.

Customers who use AmpIQ will have the following additional pages:

* A **Segments** page that builds segments against the customer 360 for use with campaigns.
* A **Metrics** page that contains a series of metrics cards that track core business outcomes.
* A **Campaigns** page that allows you to define campaigns, and then send messages or offers specific group of customers or recipients

.. start-here-tenant-end


.. _start-here-tenant-sftp:

Included SFTP site
--------------------------------------------------

.. start-here-tenant-sftp-start

Every Amperity tenant includes an SFTP site with a hostname of ``<tenant>.sftp.amperity.com``. For example, if your company name is **ACME**, then your tenant's SFTP hostname is ``acme.sftp.amperity.com``. (The hostname is always all lowercase.)

.. note:: The SFTP site is provisioned by an Amperity administrator *after* the initial tenant creation. As such, the SFTP site is not immediately available, but this is not a long process. When the SFTP site is ready, Amperity will use SnapPass to send you the connection details. If you wish to use RSA key-based authentication, please provide the public key to your Amperity administrator when requesting SFTP access.

Once this site is provisioned, you may configure the SFTP site as an SFTP source or an SFTP destination to support any desired workflow. External customer processes can be configured to connect to the site using SFTP, after which they can add data to or pick up data from the site to support any external workflow.

.. caution:: The SFTP server has a 30-day limit on data and after 30 days, data may be moved automatically to an archive location. This location is still accessible to Amperity in case it becomes necessary to reuse it.

.. important:: The hostname for the SFTP site is always ``<tenant-name>.sftp.amperity.com``. Some older tenants may still be using the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. start-here-tenant-sftp-end


.. _start-here-log-in-amperity:

Log in to Amperity
==================================================

.. start-here-log-in-amperity-start

You must provide your credentials to Amperity in order to log in.

.. start-here-log-in-amperity-end

**To log in to Amperity**

.. start-here-log-in-amperity-steps-start

#. Open https://app.amperity.com in your web browser. Google Chrome is recommended.
#. When prompted, provide your Amperity credentials.

   .. note:: Most credentials are configured to use some form of single sign-on (SSO), but may be configured to use usernames and passwords, depending on how user access is configured for your tenant.
#. Click **LOG IN**.

.. start-here-log-in-amperity-steps-end


.. _start-here-tenant-browsers:

Supported browsers
--------------------------------------------------

.. start-here-tenant-browsers-start

Amperity works best with Google Chrome and works fine with Chromium-based browsers, such as Brave.

Amperity is not supported from Firefox, Safari, Internet Explorer, or from mobile/tablet devices.

.. start-here-tenant-browsers-end


About sandbox workflows
==================================================

.. include:: ../../amperity_reference/source/sandboxes.rst
   :start-after: .. sandboxes-about-sandbox-workflows-start
   :end-before: .. sandboxes-about-sandbox-workflows-end

