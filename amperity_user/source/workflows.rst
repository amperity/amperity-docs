.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Monitor workflows that use orchestrations to send query results to various destinations.

.. meta::
    :content class=swiftype name=body data-type=text:
        Monitor workflows that use orchestrations to send query results to various destinations.

.. meta::
    :content class=swiftype name=title data-type=string:
        Monitor workflows

==================================================
Monitor workflows
==================================================

.. workflows-static-intro-start

Sending data from Amperity is a combination of three things: building a query, linking the results of that query to an orchestration that sends the results to a destination, and then monitoring the workflow to ensure that your data safely makes it downstream.

This is part three of a series of topics that describes how this works.

* Build :doc:`queries <queries>` using Presto SQL. A SELECT statement, along with standard clauses, operators, and functions, is all you need to return data that support any use case.
* An :doc:`orchestration <orchestrations>` connects the results of your query to a workflow that sends those results to its destination.
* A workflow manages the process of sending that data to the selected destination.

  .. note:: Each workflow is monitored by Amperity. You may see notifications about the state of the workflow within the **Queries** and **Destinations** pages. Depending on the type of notification, you may be directed to a workflow actions page that will actively help you troubleshoot issues within that workflow.

.. workflows-static-intro-end

.. workflows-howitworks-start

You can view workflows from the **Workflows** page, from which you configure the audience and sub-audiences that will be associated with the campaign, the downstream locations to which the campaign will be sent, and the time at which the campaign is to begin.

.. workflows-howitworks-end

.. workflows-howitworks-steps-start

The following sections describe what you should do to monitor the health of each query result that you send downstream from Amperity.

.. workflows-howitworks-steps-end

.. workflows-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0


   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - Ensure that each query results match the requirements and/or use case(s) that are required in the downstream application. 

       For example, you may need to update a query to match changes required by the destination. This might be due to a change in the scope of the use case, such as a request to add columns to the "Yearly_Revenue_by_Month" query to support an additional visualization element in your Domo dashboard.

       You may need to update a query to ensure the results match specific requirements by the destination.

       For example, you started with 6 data sources and used those to get your downstream use cases running. And then added a few more data sources. One of these sources has "messy records" that changed some of the data in your customer 360 database, which causes your Google Ads or DV360 orchestration to fail. Google Ads or DV360 requires phone numbers to use a "+11231234567" format and requires that first name, last name, zip code, and country be available to the the "Contact Info" upload key. An orchestration will fail when the data that is sent to Google Ads or DV360 doesn't match the formatting requirements.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - Ensure that all of your orchestrations are running successfully. You can monitor this from the **Workflows** page.

       .. include:: ../../amperity_reference/source/workflows.rst
          :start-after: .. workflows-howto-resolve-errors-start
          :end-before: .. workflows-howto-resolve-errors-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 600 px
          :alt: The Workflow page, showing a workflow with errors.
          :align: left
          :class: no-scaled-link

       When you discover an orchestration that has failed, open workflow actions:

       .. include:: ../../amperity_reference/source/workflows.rst
          :start-after: .. workflows-howto-resolve-errors-steps-start
          :end-before: .. workflows-howto-resolve-errors-steps-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Troubleshoot orchestration failures caused by incorrect settings in Amperity *or* in the downstream system.

       For example, the name of a data extension must be unique within Salesforce Marketing Cloud, should use underscores ( _ ) instead of spaces, and may not contain *any* of the following characters:

       ::

          ! @ # $ % ^ * ( ) = { } [ ] \ . < > / " : ? | , &

       The name of the data extension is configured in the data template, which means you can troubleshoot this type of failure directly.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Notifications show a status for individual steps within workflows that are related to queries and orchestrations. The status can be "Running", "Completed", "Alert", and "Error".

       .. important:: All notifications within your tenant are specific to your tenant and reflect how your tenant is configured. The names of tables, databases, queries, orchestrations, and destinations will appear in the notifications.

          If there is an error, such as a processing error related to a specific column within a custom table, the notification will contain the names you used for that custom table and also for the columns within that table.

       A warning is shown when the workfow was able to complete all steps, but detected issues with at least one step within the workflow.

       An error is shown when the workfow was unable to complete all steps.

       A notification will describe the issues related to warnings and errors, with specific information about what caused them. For errors, you should open the **Workflows** page and review the error. A list of suggested workflow actions will be available.

       .. tip:: If you are unable to resolve an error, please contact Amperity support.

.. workflows-howitworks-callouts-end
