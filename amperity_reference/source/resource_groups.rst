.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        A resource group represents one or more databases to which users have access and from which data can be sent to downstream workflows.

.. meta::
    :content class=swiftype name=body data-type=text:
        A resource group represents one or more databases to which users have access and from which data can be sent to downstream workflows.

.. meta::
    :content class=swiftype name=title data-type=string:
        Resource groups

==================================================
About resource groups
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-resource-group-start
   :end-before: .. term-resource-group-end


.. _settings-security-resource-groups-all:

"All resource groups"
==================================================

.. settings-security-resource-groups-all-start

Amperity includes one default resource group: "All resource groups".

Users that are granted access to the "All resource groups" resource group are allowed to interact with all of the databases in the **Customer 360** page.

.. settings-security-resource-groups-all-end


.. _settings-security-resource-groups-custom:

Custom resource groups
==================================================

.. settings-security-resource-groups-custom-start

Use a custom resource group to support any combination of team member access to brand-specific databases.

.. note:: Users who are associated with a custom resource group cannot access the **Sources** page. Access to the **Sources** page requires users to have access all data available to the tenant.

   Users who are associated with a custom resource group *may* be able to view the **Stitch** page (depending on their policy), but is not able to view personally identifiable information (PII).

.. settings-security-resource-groups-custom-end

**To add a custom resource group**

.. settings-security-resource-groups-custom-steps-start

#. As a user with **Admin** privileges, open the **Settings** page, and then select **Security**.
#. Next to **Resource Groups**, click **Add Resource Group**.
#. Enter the name of the custom resource group and a description.
#. Click **Save**.

.. settings-security-resource-groups-custom-steps-end


.. _settings-security-resource-groups-assign-users:

Assign users to resource groups
==================================================

.. settings-security-resource-groups-assign-users-start

Assign a user to a policy, and then associate that policy to a resource group. A user may be assigned to more than one policy. A policy may be associated with any resource group.

Assign users to policies and resource groups when they are added to Amperity. This can be done :doc:`using the Amperity UI <users>` or from your identity provider (IdP) when :doc:`managing users with SSO group mappings <sso>`.

.. settings-security-resource-groups-assign-users-end


.. _settings-security-resource-groups-database-permissions:

Database permissions
==================================================

.. settings-security-resource-groups-database-permissions-start

A database may be associated with a single custom resource group. A custom resource group may be associated with more than one database.

.. note:: A database is *always* associated with the "All resource groups" resource group.

A database that is assigned permission to a custom resource group allows users associated with that resource group to:

#. View that database from the **Customer 360** page.
#. View all tables in that database.
#. Configure database exports from that database.
#. Build segments and queries that run against that database.
#. Design campaigns that send the results of segments to downstream workflows.
#. Use destinations to send the results of queries to downstream workflows.

.. note:: Users who are associated with the "All resource groups" resource group are allowed to add and edit databases in the **Customer 360** page and run Spark SQL queries against all of the data in the tenant.

.. settings-security-resource-groups-database-permissionss-end

**To set database permissions for a custom resource group**

.. settings-security-resource-groups-database-permissions-steps-start

#. From the **Customer 360** page, under **All Databases**, click the ellipses menu for a database, and then click **Change Permissions**. This opens the **Permissions** dialog box.
#. Click **Standard Access**, and then select a custom resource group from the dropdown list.
#. Click **Save**.

.. settings-security-resource-groups-database-permissions-steps-end


.. _settings-security-resource-groups-multi-brand-tenants:

Multi-brand tenants
==================================================

.. settings-security-resource-groups-multi-brand-tenants-start

Use a combination of custom resource groups to define how teams in your organization can interact with brand databases in Amperity, where each custom resource represents a brand.

For example, a tenant with multiple brands, a global analytics team, multiple brand-specific teams, and multiple databases can:

#. Configure a policy for the global analytics team and assign the policy to the "All resource groups" resource group.
#. Define a custom resource group for the owners of brand A, and then configure these owners with a policy that is assigned to the brand A resource group.
#. Define a custom resource group for the owners of brand B, and then configure these owners with a policy that is assigned to the brand B resource group.
#. Configure the database for brand A for permissions to the custom resource group associated with brand A.
#. Configure the database for brand B for permissions to the custom resource group associated with brand B.

This will allow members of the global analytics team to access the databases for brands A and B while ensuring that brand owners can only access their brand's database.

.. settings-security-resource-groups-multi-brand-tenants-end
