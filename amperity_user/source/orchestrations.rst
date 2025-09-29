.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Send data from Amperity to any destination using orchestrations.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send data from Amperity to any destination using orchestrations.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data anywhere

==================================================
Send data anywhere
==================================================

.. orchestrations-static-intro-start

Sending data from Amperity is a combination of three things: building a query, linking the results of that query to an orchestration that sends the results to a destination, and then monitoring the workflow to ensure that your data safely makes it downstream.

This is part two of a series of topics that describes how this works.

* Build :doc:`queries <queries>` using Presto SQL. A SELECT statement, along with standard clauses, operators, and functions, is all you need to return data that support any use case.
* An orchestration connects the results of your query to a workflow that sends those results to its destination.
* A :doc:`workflow <workflows>` manages the process of sending that data to the selected destination.

  .. note:: Each workflow is monitored by Amperity. You may see notifications about the state of the workflow within the **Queries** and **Destinations** pages. Depending on the type of notification, you may be directed to a workflow actions page that will actively help you troubleshoot issues within that workflow.

.. orchestrations-static-intro-end

.. orchestrations-howitworks-steps-start

The following sections describe the steps you will follow to use an orchestration to send the results of a query to a destination.

.. orchestrations-howitworks-steps-end

.. orchestrations-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0


   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - An orchestration connects the results of a query to a workflow that sends those results to a destination.

       Open the **Destinations** page, scroll down, and then click the **Add Orchestration** button to open the **New Orchestration** dialog box.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - The **New Orchestration** dialog box is a series of picklists. Configuring the orchestration to use a query, and then select the name of the query for which you want to send results.

       .. image:: ../../images/mockup-orchestrations-select-query-123.png
          :width: 650 px
          :alt: Select the query that returns the results that is sent.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - Each orchestration is configured to send query results to a single destination. This destination must already be configured for your tenant, along with a data template that defines how the results are formatted for this destination.

       For example, these query results is sent to a dashboard in Domo. Choose the "Domo S3" destination and the "Domo S3 CSV Files for Dashboards" data template.

       .. image:: ../../images/mockup-orchestrations-select-destination-template-123.png
          :width: 650 px
          :alt: Choose one or more segments to exclude customers from this campaign.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - Each data template has a series of settings that may be configured from an orchestration. 

       When you select the data template, the template-specific settings are shown, many of which are preconfigured with the correct configuration settings.

       In this example, query results are sent to a customer-managed Amazon S3 bucket, from which the data is loaded to Domo as a `DataSet <https://domohelp.domo.com/hc/en-us/articles/360042926274-Adding-a-DataSet-Using-a-Connector>`__ |ext_link|. No updates are required for the template-specific settings because the data template has already configured them with the correct settings.

       .. image:: ../../images/mockup-orchestrations-select-template-settings-123.png
          :width: 540 px
          :alt: Configure the data template for Amazon S3 settings.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - A good dashboard should always have updated data, which means this orchestration should send data on a regular basis.

       .. image:: ../../images/mockup-orchestrations-select-automatic-or-manual-123.png
          :width: 540 px
          :alt: Choose the "cooling down" lifecycle status.
          :align: left
          :class: no-scaled-link

       .. tip:: The first time you send data to a destination you should use a "Manual" workflow, but after you have verified that it worked correctly you can set it to "Automatic".


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: center
          :class: no-scaled-link
     - Review all settings, and then click **Save**.

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 540 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

.. orchestrations-howitworks-callouts-end
