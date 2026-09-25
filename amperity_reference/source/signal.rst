.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Signal is the dashboarding surface in Amperity. Boards of charts are built on your transaction data, read over a period you choose, and compared against the same span one year earlier.

.. meta::
    :content class=swiftype name=body data-type=text:
        Signal is the dashboarding surface in Amperity. Boards of charts are built on your transaction data, read over a period you choose, and compared against the same span one year earlier.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Signal

==================================================
About Signal
==================================================

.. signal-overview-start

**Signal** is the dashboarding surface in Amperity. It shows your business as a set of charts built on the transaction data in your tenant, read over a period you choose, and compared against the same span one year earlier.

A **board** is one tab in **Signal**. A **card** is one chart on a board. A card names the database and table it queries, and declares the aggregate it measures, the dimension it breaks that total down by, and any rows it restricts itself to. Amperity builds the statement that runs it. Because a card carries a measure rather than a saved result, it re-measures every time you move the period, the granularity, or the filters.

Boards and cards are authored through :doc:`AmpAI <ampai>` rather than through a chart builder. **Signal** ships with no boards and no cards. A tenant's dashboard is whatever has been built in it, and a tenant that has built nothing opens **Signal** to an empty page that offers to build one.

A card reads a table in one of your Amperity databases. In practice that is an order-grain analytics table built from your unified transactions and named **UT_Analytics**: it is the table the filter bar reads its attributes from, and the table the cards **AmpAI** builds query. Because it carries the Amperity ID and an identified flag alongside order revenue, quantity, brand, and channel, a card can measure identified customers separately from anonymous orders.

.. signal-overview-end


.. _signal-boards-and-cards:

Boards and cards
==================================================

.. signal-boards-and-cards-start

A board is a tab: a title, an optional line of description beneath it, and its cards in render order. A tenant can have more than one. When it does, the board title at the top of the page becomes a switcher that lists every board, and **Signal** renders one board at a time. The **default board** is the one **Signal** opens when no board is named in the URL, or when the URL names a board this tenant does not have.

.. TODO: verify with the Signal PO -- the product overview says "currently just 1 customer health view", but Signal ships multiple boards today: a switcher, a tenant default, Duplicate board, and Delete board. This page documents multiple boards. Confirm that is the intended GA story before publication.

A board's layout follows from the order of its cards rather than from a grid you arrange:

* The **first metric card** is the hero: a headline value and its year-over-year change, above a trend chart.
* The **remaining metric cards** are stat tiles in a row beneath it, in order. Each shows its value, its year-over-year change, and a sparkline.
* **Stacked-bar cards** render at the bottom of the page, in order.

Selecting a stat tile promotes its metric into the hero for the rest of your session. The tile stays where it is and the board's own configuration is unchanged.

.. signal-boards-and-cards-end

.. signal-card-types-table-start

There are two kinds of card.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Card
     - What it shows
   * - Metric
     - One aggregate---revenue, orders, customers, average order value---as a single value with its change against the same span one year earlier. As the hero it also draws a trend chart across the period. As a stat tile it draws a sparkline.
   * - Stacked bar
     - One aggregate broken into bands by a dimension, such as revenue by brand or revenue by channel. Each band shows its share of the total and its year-over-year move. A card shows the ten largest bands in each window, ranked independently in each and paired by label, so a band present in one window and not the other shows with no comparison rather than a fall to zero.

.. signal-card-types-table-end

.. signal-period-and-grain-start

Period and granularity are viewer controls on the filter bar, not properties of a card. The period control offers **Last 7 days**, **Last 30 days**, **Last 90 days**, and **Last 12 months**; **Week to date**, **Month to date**, **Quarter to date**, and **Year to date**; and a custom start and end date. The granularity control offers **Daily**, **Weekly**, and **Monthly**. A board opens on **Last 12 months** at **Weekly** until you change them.

Every range is measured back from the date the board's tables are loaded through, not from today, so the dates the control shows are the dates the cards queried. A loading lag shifts the whole window back rather than emptying the shorter periods. When the load date is behind today, the page shows **Data freshness: through** and that date.

A board can name a fiscal calendar table, which is set through **AmpAI** rather than in the interface. On a board that names one and is read in fiscal view, the granularity control offers **Fiscal weekly**, **Fiscal monthly**, and **Fiscal quarterly** in place of the calendar granularities, and the to-date periods are measured on that calendar. A fiscal granularity is offered only where the calendar names the column that divides it.

.. signal-period-and-grain-end

.. signal-board-settings-start

**Board settings**, opened from the gear in the page header, sets the board's name and description, and two settings that are stored on the board rather than per viewer, so that everyone who opens it reads it the same way:

* **Chart scale**---**From zero** anchors every plot at zero, so two plots on one board can be compared by eye. **Series range** fits each plot to its own floor and peak.
* **Anchor dates to fiscal calendar**---appears only once the board names a fiscal calendar.

The board actions menu offers **Set as default board**, **Duplicate board**, and **Delete board**. Deleting a board deletes the cards on it.

.. signal-board-settings-end


.. _signal-card-definitions:

Card definitions
--------------------------------------------------

.. signal-card-definitions-start

Every card carries a definition control that shows how its number is calculated.

A card whose author wrote a description shows that description on hover, in plain language, with a **View SQL** link beneath it. A card with no description opens straight to the SQL instead. Opening the definition shows a dialog titled with the card name, containing whichever of these parts apply:

* **What this measures**---the card's description, in the language of your business.
* **Metric expressed as SQL**---the aggregate the card measures.
* **Filtered to**---the rows the card restricts itself to, where it sets its own restriction.
* **SQL**---the statement Amperity compiled and ran for the values on screen.

.. signal-card-definitions-end

.. signal-card-definitions-note-start

.. note:: A card's description is written when the card is authored. A card that has none shows its raw aggregate in place of a plain-language explanation. When you ask **AmpAI** to change what a card measures, ask it to rewrite the description in the same change.

.. signal-card-definitions-note-end


.. _signal-ask-ampai:

Ask AmpAI about a card
--------------------------------------------------

.. signal-ask-ampai-start

**Signal** has an **AmpAI** chat docked beside the dashboard. Depending on the width of your window it appears as a rail alongside the board, as a tab beside **Dashboard**, or as a pill that opens over the page. It can also be expanded to full screen.

Each card carries an **Ask AmpAI** control. Selecting it points the docked chat at that card rather than opening a second conversation: the chat keeps its history, and is re-grounded in the card's compiled SQL, the values currently on screen, the filters currently applied, and---if you have dragged across a run of buckets on the trend chart---the range you highlighted. It loads a question into the input box for you to edit or send. It does not send one for you.

With no card selected, the chat is grounded in the board as a whole: its title, and every card's kind, position, title, table, and measure.

**AmpAI** can also change the board. Ask it to add, remove, retitle, or reorder cards, or to change what a card measures, and it writes those changes to the board's configuration and the page reloads itself when the turn ends. It asks you to confirm before deleting anything, and configuration changes are recorded in your tenant's configuration history, where they can be reverted.

Before authoring or changing a card, **AmpAI** reads the custom prompt and the company context documents your tenant has set, so that card titles and metric definitions follow your own business rules and vocabulary. See :doc:`AmpAI <ampai>`.

.. signal-ask-ampai-end


.. _signal-access:

How to access
==================================================

.. signal-access-start

Click **Signal** in the left navigation. A board opens at its own address, so a link to a board can be shared with anyone in your tenant.

.. signal-access-end

.. signal-access-note-start

.. note:: If **Signal** is not available in your tenant, contact your **DataGrid Operator** to request access.

.. signal-access-note-end

.. signal-access-requirements-start

For **Signal** to show anything, three things must be in place:

* A :doc:`database <databases>` containing the table the cards query. Every card on a board must name the same database.
* Data loaded into that table. A table that reports no load date gives the board no window to measure, and every card on it reports that its window cannot be resolved.
* A board with at least one card on it. Until then, **Signal** shows an empty page offering to build one with **AmpAI**.

.. signal-access-requirements-end

.. signal-access-permissions-start

Access to **Signal** depends on the actions your :doc:`policy <policies>` allows.

.. list-table::
   :widths: 55 45
   :header-rows: 1

   * - To do this
     - You need this action
   * - View the boards and cards in your tenant
     - ``segments:read``
   * - Load a card's numbers
     - ``queries:execute``
   * - Create, change, or delete a board or a card
     - ``queries:write``

**Signal** configuration is tenant-wide rather than scoped to a resource group, but running a card is additionally authorized against the resource group of the database that card queries. A user who can open a board may still be unable to load a card that reads a database they do not have access to.

.. signal-access-permissions-end

.. TODO: verify with the Signal PO or the access model owner -- policies.rst documents permissions by policy name rather than by action, and has no Signal section. Confirm which named policies grant queries:write and queries:execute so this table can name them, and open a fast-follow to add a Signal section to policies.rst.


.. _signal-filters:

Filters and saved views
==================================================

.. signal-filters-start

The filter bar runs beneath the board header and carries two kinds of filter.

**The board's own filters** lead the strip. They are shown but cannot be edited, and Amperity applies them to every card on the board. They narrow a board's scope and cannot be widened from the dashboard---**Clear** empties your own filters and visibly leaves the board's alone. A board's filters are set through **AmpAI**.

**Your filters** are added from **+ Add filter**, which opens a picker: choose an attribute, then choose its values. Each filter can match with **is** or **is not**, can name several values, and several filters can be applied at once. Selecting a value narrows every card on the board at once.

The attributes the picker offers are discovered from the table the filter bar reads, so they reflect your own data rather than a fixed list. An attribute is offered when it is a text column with more than one and no more than 50 distinct values. Identifier columns are never offered, because they are unique or near-unique per row: the Amperity ID and any column whose name ends in ``_id`` are excluded. Numeric and date columns are not offered. Column names are shown as labels, so ``purchase_brand`` reads as **Purchase brand**.

.. signal-filters-end

.. signal-filters-persistence-start

The period, the granularity, your filters, the metric you promoted into the hero, and any range you highlighted on the trend chart are all held for your session only. None of them is written to the board, and none of them travels with a link---someone who opens a board you sent them sees the board, not your filters.

To keep a filtered view, use **Duplicate board**. It copies the board and its cards, and writes the filters currently on the bar into the copy as the copy's own board filters. The copy then opens permanently scoped to that filter, and its bar starts clean. Give the copy its own name, and share its address with anyone who should read it.

.. signal-filters-persistence-end


.. _signal-use-cases:

Use cases
==================================================

.. signal-use-cases-start

Use **Signal** to:

* **Track key business metrics on a cadence.** A board puts your headline metric and the metrics beneath it on one page, each against the same span a year earlier, at whichever period and granularity you are reviewing on.
* **Explore your customer data visually.** Break a total into bands by brand, channel, or customer type to see where it is moving, and drag across the trend chart to band the same stretch of time on every metric at once.
* **Ask follow-up questions of what you are looking at.** Point the **AmpAI** chat at a card and it starts from that card's definition, its current values, and the filters you have applied, rather than from an empty box.
* **Keep metric definitions in one place.** Every card says what it measures and shows the statement behind it, and the definitions **AmpAI** writes follow the custom prompt and company context set for your tenant.

.. signal-use-cases-end


.. _signal-limitations:

Limitations
==================================================

.. signal-limitations-start

**Signal** is a focused dashboard rather than a general reporting tool. Be aware of the following:

* **Two kinds of card.** A card is a metric or a stacked bar. There are no other chart types, and layout follows the order of the cards rather than a grid you arrange.
* **Signal reads data already in Amperity.** A card queries a table in one of your Amperity databases. Bringing outside data in is a separate exercise.
* **The comparison is fixed.** Every card compares the selected period against the same span one year earlier, or the same position one fiscal year earlier at a fiscal granularity. It cannot be changed to another baseline.
* **A stacked bar shows ten bands.** Only the ten largest bands in each window are returned, so a dimension with many values will not show them all.
* **Not every column can be filtered.** The filter bar offers text columns with no more than 50 distinct values, and excludes identifier columns. Numeric and date columns cannot be filtered.
* **One database per board, one date column per table.** Every card on a board must name the same database. Every card reading the same table must measure over the same date column. A board that breaks either rule cannot resolve its window, and every card on it stops loading, not just the card at fault.
* **No calendar quarter.** Granularity is daily, weekly, or monthly, plus the fiscal granularities a board's own calendar supports.
* **Session state is not saved.** Period, granularity, filters, and hero selection reset when you leave. Use **Duplicate board** to keep a filtered view.
* **The page does not refresh itself.** **AmpAI** reloads the board after a change it made, but a change made from anywhere else is not visible until you reload the page.
* **Windows follow your data, not the calendar.** Ranges are measured back from the date the board's tables are loaded through, so a board over stale data measures a stale window rather than an empty one.
* **Boards and cards are authored through AmpAI.** The interface can rename, duplicate, and delete a board and change how it is read, but adding a card, removing one, or changing what one measures is done by asking **AmpAI**.
* **The card catalog is retail order-grain.** The metrics **AmpAI** builds from are written for order data. On a tenant whose data describes tickets, stays, or other non-order events, **AmpAI** reports that gap rather than forcing the retail shape onto it.

.. signal-limitations-end

.. signal-limitations-feedback-start

.. tip:: When **Signal** cannot do something you need---a chart type, a granularity, or a control it does not offer---ask **AmpAI** in the **Signal** chat. It can file the request with Amperity's product team on your behalf, after you confirm.

.. signal-limitations-feedback-end
