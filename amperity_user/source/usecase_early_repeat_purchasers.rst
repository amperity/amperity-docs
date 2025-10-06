.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        A use case for building an audience of early repeat purchasers.

.. meta::
    :content class=swiftype name=body data-type=text:
        A use case for building an audience of early repeat purchasers.

.. meta::
    :content class=swiftype name=title data-type=string:
        Early repeat purchasers

==================================================
Early repeat purchasers
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-early-repeat-purchasers-start
   :end-before: .. term-early-repeat-purchasers-end

.. include:: ../../amperity_reference/source/attribute_early_repeat_purchaser.rst
   :start-after: .. attribute-early-repeat-purchaser-start
   :end-before: .. attribute-early-repeat-purchaser-end

.. usecase-early-repeat-purchasers-howitworks-start

The following sections describe using the **Segment Editor** to build a segment that returns a list of customers who are early repeat purchasers.

.. usecase-early-repeat-purchasers-howitworks-end

**FIND EARLY REPEAT PURCHASERS**

.. usecase-early-repeat-purchasers-howitworks-callouts-start

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
          :width: 340 px
          :alt: Use your customer 360 database to build segments.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Find early repeat purchasers.
          :align: center
          :class: no-scaled-link

     - To identify which customers have made an early repeat purchase, choose the **Early Repeat Purchaser** attribute from the **Transaction Attributes Extended** table, and then select the "is true" operator:

       .. image:: ../../images/attribute-early-repeat-purchaser-example.png
          :width: 540 px
          :alt: Find early repeat purchasers.
          :align: left
          :class: no-scaled-link

       Click the **Refresh** button located on the right side of the **Segment Editor** to see how many customers are in your segment, how much they spent in the past year, how many are active, and how many of them could belong to a future campaign.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Save your segment.
          :align: center
          :class: no-scaled-link
     - You're done. Click the **Save As** button in the top right corner of the **Segment Editor**. Give your segment a name that clearly describes the purpose and audience type for the segment. For example: "Early Repeat Purchasers".

       .. image:: ../../images/usecases-dialog-save-early-repeat-purchasers.png
          :width: 440 px
          :alt: Give your segment a name.
          :align: left
          :class: no-scaled-link

       .. tip:: Use the **Early Repeat Purchaser** attribute as a leading indicator for overall conversion rate of one-time purchasers to repeat customers, even when it does not capture the total number of one-time purchasers who have returned to purchase again.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Segment insights page
          :align: center
          :class: no-scaled-link
     - After your segment is saved the **Segment Overview** page opens and shows additional details, such as historical and predicted revenue, the percentage of customers that are reachable by email, by phone, on Facebook, and customer trends, such as purchases by channel, revenue by lifetime spend.

.. usecase-early-repeat-purchasers-callouts-end
