.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Recommended Actions turns your unified customer data into a prioritized list of marketing actions, each with the opportunity it addresses, the customer segment it targets, and its expected impact.

.. meta::
    :content class=swiftype name=body data-type=text:
        Recommended Actions turns your unified customer data into a prioritized list of marketing actions, each with the opportunity it addresses, the customer segment it targets, and its expected impact.

.. meta::
    :content class=swiftype name=title data-type=string:
        Recommended Actions

.. _recommended-actions:

==================================================
Recommended Actions
==================================================

.. recommended-actions-overview-start

**Recommended Actions** turns your unified customer data into a prioritized list of marketing plays. Instead of presenting a dashboard for you to interpret, Amperity surfaces specific recommendations that are ready for you to act on. These recommendations synthesize what's happening with your customers, what to do about it, and why it's worth doing.

Each recommendation includes the opportunity it addresses, the customer segment it targets, and the expected business impact, so you can move more quickly from insight to activation.

**Recommended Actions** is powered by :doc:`AmpAI <ampai>`, which drafts the analysis, explains each recommendation, and helps you turn a recommendation into a journey.

.. recommended-actions-overview-end


.. _recommended-actions-howitworks:

How Recommended Actions works
==================================================

.. recommended-actions-how-it-fits-start

**Recommended Actions** analyzes your unified customer data and presents the results as actions you can launch:

#. Review each recommendation, including its target customer segment, expected impact, and supporting insight.
#. Choose which recommendations to act on.
#. Activate a recommendation by sending its target segment into a journey or a campaign.
#. Monitor the performance of the activated segment through journey and campaign reporting.

**Recommended Actions** builds on the same unified customer data used across the platform as well as established customer analytics frameworks and Amperity's use case library, so each recommendation maps to a proven play rather than an ad-hoc idea. **Recommended Actions** uses :doc:`AmpAI <ampai>` to generate and explain recommendations, targets the value-tier :doc:`segments <segments>` as described below, and activates through :doc:`journeys <journeys>` and :doc:`campaigns <campaigns>`. For open-ended exploration of your data, use the :doc:`Customer Data Assistant <customer_data_assistant>`.

.. recommended-actions-how-it-fits-end


.. _recommended-actions-access:

Access Recommended Actions
==================================================

.. recommended-actions-access-start

Open the **Recommended Actions** page by clicking **Recommendations** on the left nav in the Amperity app.

The **Recommended Actions** page includes:

* A row of value-tier cards, one for each of the :ref:`six tiers of value <recommended-actions-segmentation>`, showing the value of each tier and how it is trending.
* A **Customers / Revenue** toggle that switches the cards and views between customer counts and revenue.
* A freshness indicator that shows whether the recommendations are up to date, along with the date they were last generated.
* A **View charts** link that opens the :ref:`Value Tier Matrix <recommended-actions-value-tier-matrix>`.
* The :ref:`Playbook <recommended-actions-playbook>` and :ref:`Analysis <recommended-actions-analysis>` tabs.

.. recommended-actions-access-end

.. recommended-actions-access-note-start

.. note:: **Recommended Actions** is configured by a **DataGrid Operator**. If **Recommended Actions** is not available for your tenant, contact your **DataGrid Operator** to request access.

.. recommended-actions-access-note-end


.. _recommended-actions-requirements:

Requirements
==================================================

.. recommended-actions-requirements-start

**Recommended Actions** requires the following:

* A Customer 360 database that includes Unified Transactions.
* AmpAI enabled for your tenant.
* A Customer Value Migration source table.

.. note:: Amperity creates the ``Customer_Value_Migration`` source table for you. When a **DataGrid Operator** configures **Recommended Actions**, Amperity generates the table from your unified transactions if it does not already exist. See :ref:`recommended-actions-configuration`.

.. recommended-actions-requirements-end


.. _recommended-actions-segmentation:

Value-tier segmentation model
==================================================

.. recommended-actions-segmentation-model-start

**Recommended Actions** groups your customers into value tiers along two axes: how often a customer purchases (purchase frequency) and how much a customer spends per order (average order value). Each axis is divided into tiers, and the combination of the two places every customer into one of six value tiers:

* **Champions** — the highest purchase frequency and the highest average order value.
* **Loyalists** — a high purchase frequency at a lower average order value.
* **Potential Champions** — a moderate purchase frequency at a high average order value.
* **Potential Loyalists** — a moderate purchase frequency at a lower average order value.
* **Needs Attention** — a low purchase frequency at a high average order value.
* **Lower Value** — a low purchase frequency at a lower average order value.

The tier boundaries are configured for your account. To see the exact ranges that apply to your data, open the :ref:`Value Tier Matrix <recommended-actions-value-tier-matrix>`. Each value tier can be activated as a :doc:`segment <segments>`.

.. recommended-actions-segmentation-model-end


.. _recommended-actions-value-tier-matrix:

Value Tier Matrix
--------------------------------------------------

.. recommended-actions-value-tier-matrix-start

Click **View charts** to open the **Value Tier Matrix**. The matrix has two views:

* **Value Matrix** — a grid of average order value tiers (rows) and purchase frequency tiers (columns). Each cell shows the number of customers in that combination and the value tier the combination maps to. Use the **Period** menu to change the time period the matrix summarizes.
* **Trends Over Time** — a chart that shows how each value tier changes across a series of time windows. Use the **View by** and **Metric** menus to change how the trend is summarized.

.. recommended-actions-value-tier-matrix-end


.. _recommended-actions-anatomy:

Anatomy of a recommendation
==================================================

.. recommended-actions-anatomy-start

Each recommendation describes a single action to take and the reasoning behind it. A recommendation includes:

* **The opportunity or risk it addresses** — the customer behavior the action responds to.
* **The target customer segment** — the value tier or group of customers the action applies to.
* **The expected impact** — an estimate of the business result if you act on the recommendation, together with the reasoning behind the estimate.
* **A supporting insight** — a finding from your data that explains why the recommendation matters.
* **A suggested activation** — a suggestion of how to act on the recommendation, such as a journey or a campaign.

Each recommendation belongs to a category, such as Engagement, Retention, or Growth, that describes the kind of action it represents.

.. recommended-actions-anatomy-end


.. _recommended-actions-playbook:

The Playbook
==================================================

.. recommended-actions-playbook-start

The **Playbook** tab lists the recommended actions for your account, ordered by priority. Use the filter buttons to narrow the list:

* **All** shows every recommendation.
* **Top picks** shows the highest-priority recommendations.
* A category button, such as **Engagement**, **Retention**, or **Growth**, shows the recommendations in that category.

Each recommendation appears as a card. A collapsed card shows the category, the title, and an **Impact** badge. Expand a card to see:

* A description of the recommended action.
* An **Impact** panel with the expected impact and the reasoning behind the estimate.
* An **Insights** panel with a supporting finding.
* Two AmpAI actions: **Dive deeper**, which opens an AmpAI session to explore the recommendation, and **Explore as a journey**, which opens an AmpAI session that drafts a :doc:`journey <journeys>` from the recommendation.

.. note:: Content generated by AmpAI should be verified before you act on it.

.. recommended-actions-playbook-end


.. _recommended-actions-analysis:

The Analysis view
==================================================

.. recommended-actions-analysis-start

The **Analysis** tab presents a narrative summary of your customer base, organized into sections and supporting points. A **Themes** panel groups the analysis into themed findings, each with a short description. From the **Analysis** tab you can select **Dive deeper with AmpAI** to explore the analysis in an AmpAI session, or **View playbook** to return to the recommendations.

.. recommended-actions-analysis-end


.. _recommended-actions-configuration:

Configure Recommended Actions
==================================================

.. recommended-actions-configure-start

A **DataGrid Operator** configures **Recommended Actions** by selecting one or more Customer Value Migration source tables. If a Customer Value Migration source table does not yet exist, Amperity creates one from your unified transactions. Each entry identifies the database and source table to analyze and gives the entry a name. Entries can be paused, resumed, and removed.

.. recommended-actions-configure-end


.. _recommended-actions-refresh:

Refresh cadence and freshness
--------------------------------------------------

.. recommended-actions-refresh-cadence-start

Each configured source refreshes on a cadence: **Monthly** or **Quarterly**. The **Recommended Actions** page shows the freshness of the recommendations, including whether they are up to date, being generated, or waiting on a database rebuild, along with the date they were last generated.

.. recommended-actions-refresh-cadence-end


.. _recommended-actions-how-tos:

How-tos
==================================================

.. recommended-actions-how-tos-start

Tasks related to configuring and acting on recommendations in Amperity:

.. recommended-actions-how-tos-end

.. recommended-actions-how-tos-list-start

* :ref:`recommended-actions-howtos-configure`
* :ref:`recommended-actions-howtos-review`
* :ref:`recommended-actions-howtos-act`
* :ref:`recommended-actions-howtos-monitor`

.. recommended-actions-how-tos-list-end


.. _recommended-actions-howtos-configure:

Configure Recommended Actions
--------------------------------------------------

.. recommended-actions-howtos-configure-start

A **DataGrid Operator** configures the source tables that **Recommended Actions** analyzes.

**To configure Recommended Actions**

#. From the **Recommended Actions** page, click **Edit config**.
#. In the configuration dialog, click **Add entry**.
#. Select the database that contains your unified customer data.
#. Select a Customer Value Migration source table, or click **Create CVM table** to generate one from your unified transactions.
#. Enter a name for the entry.
#. Select a refresh cadence: **Monthly** or **Quarterly**.
#. Click **Save**.

The entry appears in the configuration dialog with its cadence and status. Amperity generates the first set of recommendations from the configured source table.

.. recommended-actions-howtos-configure-end


.. _recommended-actions-howtos-review:

Review recommendations
--------------------------------------------------

.. recommended-actions-howtos-review-start

Review the recommendations generated for your account on the **Recommended Actions** page.

**To review recommendations**

#. Open the **Recommended Actions** page.
#. On the **Playbook** tab, use the **All**, **Top picks**, and category filter buttons to narrow the list.
#. Click a recommendation card to expand it.
#. Review the **Impact** estimate and its supporting reasoning, along with the **Insights** for the recommendation.
#. To read a narrative summary of your customer base, select the **Analysis** tab.

.. recommended-actions-howtos-review-end


.. _recommended-actions-howtos-act:

Act on a recommendation
--------------------------------------------------

.. recommended-actions-howtos-act-start

Activate a recommendation by sending its target segment into a journey or a campaign.

**To act on a recommendation**

#. On the **Playbook** tab, expand the recommendation you want to act on.
#. Click **Explore as a journey**. Amperity opens an AmpAI session that drafts a :doc:`journey <journeys>` from the recommendation and its target segment.
#. Review and refine the journey, then launch it.

You can also activate the recommendation's target value tier as a :doc:`segment <segments>` in a :doc:`campaign <campaigns>`.

.. recommended-actions-howtos-act-end


.. _recommended-actions-howtos-monitor:

Monitor performance
--------------------------------------------------

.. recommended-actions-howtos-monitor-start

After you activate a recommendation, monitor the performance of the target segment through the journey or campaign that activates it.

**To monitor performance**

#. Launch the :doc:`journey <journeys>` or :doc:`campaign <campaigns>` that activates the recommendation's target segment.
#. Track the segment's performance through journey and campaign reporting.

.. recommended-actions-howtos-monitor-end


.. _recommended-actions-use-cases:

Use-case ideas
==================================================

.. recommended-actions-use-cases-start

Use **Recommended Actions** to turn value-tier analysis into targeted plays, such as:

* Re-engage a **Needs Attention** segment, whose customers spend well but purchase infrequently, with a win-back journey.
* Move **Potential Champions** toward **Champions** with targeted upsell and cross-sell campaigns.
* Recognize and retain **Champions** with loyalty and early-access programs.
* Reactivate lapsing **Loyalists** before they churn.

.. recommended-actions-use-cases-end
