.. https://docs.amperity.com/user/


.. |destination-name| replace:: customer engagement platforms


.. meta::
    :description lang=en:
        A use case for building campaigns for an audience of customers who purchased yesterday.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building campaigns for an audience of customers who purchased yesterday.

.. meta::
    :content class=swiftype name=title data-type=string:
        Purchased yesterday

==================================================
Purchased yesterday
==================================================

.. usecase-purchased-yesterday-start

Build an audience of customers who purchased yesterday. Configure a recurring campaign to send this audience to |destination-name| on a daily basis. Use this audience in |destination-name| to build segments that help keep your customers engaged with your brand and to help drive their next purchase.

.. usecase-purchased-yesterday-end

.. usecase-purchased-yesterday-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that returns a list of customers who purchased yesterday.

.. usecase-purchased-yesterday-howitworks-end

**WHICH CUSTOMERS PURCHASED YESTERDAY?**

.. usecase-purchased-yesterday-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Open the Segment Editor.
          :align: center
          :class: no-scaled-link

     - Open the **Segment Editor**, look in the lower-right of the page and make sure your customer 360 database is selected.

       .. image:: ../../images/mockup-segments-tab-database-and-tables-small.png
          :width: 350 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find customers who purchased yesterday.
          :align: center
          :class: no-scaled-link

     - Identify customers who purchased yesterday using the **Has purchased** purchase behavior. Set the minimum number of purchases, select the "on" operator, and then define the range as "yesterday":

       .. image:: ../../images/attribute-has-purchased-yesterday.png
          :width: 540 px
          :alt: Find customers who purchased yesterday.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done building your audience! Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Purchased Yesterday"

       .. image:: ../../images/usecases-dialog-save-purchased-yesterday.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-purchased-yesterday-callouts-end
