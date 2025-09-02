.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Activate audiences using campaigns, journeys, and orchestrations.

.. meta::
    :content class=swiftype name=body data-type=text:
        Activate audiences using campaigns, journeys, and orchestrations.

.. meta::
    :content class=swiftype name=title data-type=string:
        About activations

==================================================
About activations
==================================================

.. activations-overview-start

The **Activations** page consolidates segment-based single-touch campaigns and multi-touch journeys alongside query-based orchestrations into a single workspace. Use the **Activations** page to manage audience activations that are sent from Amperity as campaigns, journeys, or orchestrations to any of your brand's downstream marketing workflows.

.. activations-overview-end


.. _activations-about:

About the Activations page
==================================================

.. activations-about-start

Use the **Activations** page to build audiences for the following activation types:

* **Campaigns** A :doc:`campaign <campaigns>` sends a subset audience to one or more marketing destinations at a specific moment in time and in a single step.

  Common use cases for campaigns include email and SMS, paid media audiences, and loyalty program updates.

* **Journeys** A :doc:`journey <journeys>` automates a sequence of interactions including sending audiences, waiting, and spliting audiences so that members of an audience receives the right message at the right time.

  Journeys are cross-channel time-based programs that use nodes to react to customer behavior.

* **Orchestrations** An :doc:`orchestration <orchestrations>` sends the results of a query to a configured destination.

  Use queries to support a wider variety of destinations than campaigns and journeys. For example, query results can be sent to cloud storage and then be made available to analytics and database platforms like Tableau, Databricks, or Google BigQuery.

.. activations-about-end


.. _activations-what-are-they:

What are activations?
==================================================

.. activations-what-are-they-start

Activations match audiences to individual steps in complex marketing workflows. For example, build an audience that defines the customers to which your brand wants to send offers. A subset of this audience is sent to an email service provider for communication, a smaller, high-value subset of that audience is sent to one or more demand-side platforms for lookalike audience matching. Use journeys to define exits for customers who respond to the offer with a purchase.

Activations can be a single audience matched to a single offer. For example, sending a thank you offer to customers who were in the top 20% of purchases during the previous year. Build a segment that uses the `monetary element of RFM scoring <rfm.html#example-top-20-revenue-during-the-previous-year>`__ to find these customers and then assign that segment to a campaign.

Activations can be complex with audiences split into multiple pathways with a series of offers created for each pathway. For example, `a churn prevention campaign <../user/churn_prevention.html#what-is-a-churn-prevention-campaign>`__.

.. activations-what-are-they-end


.. _activations-howitworks:

How activations work
==================================================

.. activations-howitworks-start

#. **Choose the activation type**

   Selecting **Campaigns** opens the campaigns list and editor; selecting **Journeys** opens the Journeys list and the visual canvas.

#. **Define the audience**

   Designate one or more **segments** and optional **exclusion** segments to determine who enters. For recurring runs, only customers who newly qualify since the last run are included.

#. **Configure destinations and attributes**

   Select one or more downstream destinations and map the attributes each expects. 

#. **Set timing and frequency**

   **Campaigns** and **Journeys** can run once, on a schedule, or on recurrence. **Journeys** can also add **Delay** nodes to pace out the activations.

#. **Launch and monitor**

   Use the **Status** column on the **Activations** tab to track each activation.

.. activations-howitworks-end
