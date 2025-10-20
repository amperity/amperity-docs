.. https://docs.amperity.com/user/

:orphan:


.. meta::
    :description lang=en:
        A journey is an automated sequence for connecting with customers across channels.

.. meta::
    :content class=swiftype name=body data-type=text:
        A journey is an automated sequence for connecting with customers across channels.

.. meta::
    :content class=swiftype name=title data-type=string:
        Design journeys

==================================================
Design journeys
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-start
   :end-before: .. term-journey-end

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howitworks-start
   :end-before: .. journeys-howitworks-end

.. journeys-howitworks-steps-start

The following sections describe the steps you will follow to set up and configure a journey.

.. journeys-howitworks-steps-end

.. journeys-howitworks-callouts-start

.. list-table::
   :widths: 10 90
   :header-rows: 0


   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - Open the **Journeys** canvas. This is available on the **Activations** page. Select the **Journeys** button on the top left and then click **Create journey**.

       Add a name for the journey.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Who enters?**

       .. include:: ../../amperity_reference/source/journeys.rst
          :start-after: .. journeys-setup-who-enters-start
          :end-before: .. journeys-setup-who-enters-end

       **Who is excluded?**

       .. include:: ../../amperity_reference/source/journeys.rst
          :start-after: .. journeys-setup-who-is-excluded-start
          :end-before: .. journeys-setup-who-is-excluded-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **Activate node**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-journey-node-activate-start
          :end-before: .. term-journey-node-activate-end

       On the **Journeys** canvas, under an existing node, click the plus symbol and then choose **Activate**.

       .. image:: ../../images/mockup-journeys-canvas-plus-activate.png
          :width: 280 px
          :alt: Activate node
          :align: left
          :class: no-scaled-link

       Name the activate node and then choose one or more destinations from the dropdown menu.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **Delay node**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-journey-node-delay-start
          :end-before: .. term-journey-node-delay-end

       On the **Journeys** canvas, under an existing node, click the plus symbol and then choose **Delay**.

       Name the delay node and then set the length of time.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - **Conditional split node**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-journey-node-conditional-split-start
          :end-before: .. term-journey-node-conditional-split-end

       On the **Journeys** canvas, under an existing node, click the plus symbol and then choose **Conditional split**.

       Name the delay node and then add paths. For each path, define the sub-audience using a segment or custom criteria.


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - **Percent split node**

       .. include:: ../../shared/terms.rst
          :start-after: .. term-journey-node-percent-split-start
          :end-before: .. term-journey-node-percent-split-end

       On the **Journeys** canvas, under an existing node, click the plus symbol and then choose **Percent split**.

       Name the delay node and then add paths. For each path, define the percentages.

       A control group is set to 10% by default. You may increase or decrease the size of the control group. Control groups use the concepts of `people-based measurement <https://docs.amperity.com/ampiq/people_based_measurement>`__ to assign customers to control and treatment groups, which gives marketers the ability to accurately measure the incremental effects of a campaign.


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step seven.
          :align: center
          :class: no-scaled-link
     - A journey may use any combination of nodes to define the paths that your brand wants your customers to take.

       For example:

       .. image:: ../../images/mockup-journeys-overview.png
          :width: 600 px
          :alt: Journey built out in the journeys canvas interface
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step eight.
          :align: center
          :class: no-scaled-link
     - When you are finished building the journey, click **Save**.

.. journeys-howitworks-callouts-end
