.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Determine the likelihood that a customer will perform a revenue-generating event within the next 30 days.

.. meta::
    :content class=swiftype name=body data-type=text:
        Determine the likelihood that a customer will perform a revenue-generating event within the next 30 days.

.. meta::
    :content class=swiftype name=title data-type=string:
        Event propensity

==================================================
Event propensity
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-event-propensity-start
   :end-before: .. term-event-propensity-end


.. _model-event-propensity-use-cases:

Use cases
==================================================

.. model-event-propensity-use-cases-start

The event propensity model enables support for marketing campaigns that benefit from knowing a customer's likelihood to perform a revenue-generating event, including:

#. :ref:`Recommended audience sizes <model-event-propensity-use-cases-recommended-audiences>`
#. :ref:`Ranking customers by propensity <model-event-propensity-use-cases-customer-ranking>`

.. model-event-propensity-use-cases-end


.. _model-event-propensity-use-cases-recommended-audiences:

Recommended audience sizes
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-recommended-audience-size-start
   :end-before: .. term-recommended-audience-size-end

.. model-event-propensity-use-cases-recommended-audiences-about-start

Recommended audience sizes are calculated for 30-day window. An event curve is generated, along with corresponding audience sizes that show what size audience is required to capture 50%, 70%, and 90% of purchases for a given revenue-generating event during the previous 30 days.

Audience sizes are inclusive of all smaller audience sizes.

* A medium audience size (70%) includes all of your customers who are in the small audience size (50%).
* A large audience size (90%) includes all of your customers who are in the small and medium audiences.

.. model-event-propensity-use-cases-recommended-audiences-about-end

.. image:: ../../images/use-cases-recommended-audience-size-all-events.png
   :width: 600 px
   :alt: The event curve.
   :align: left
   :class: no-scaled-link

.. model-event-propensity-recommended-audiences-usecase-start

Recommended audience sizes for event propensity modeling identify customers who are most likely to perform a revenue-generating event. Use recommended audience sizes to find customers who are likely to:

* Join your brand's loyalty program
* Sign up for your brand's credit card
* Make a repeat booking for a car rental, airline ticket, or hotel stay

.. model-event-propensity-recommended-audiences-usecase-end

.. model-event-propensity-use-cases-recommended-audiences-attributes-start

Attributes for recommended audience sizes are available from the **Event Propensity** table:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Attribute Name
     - Description
   * - **Audience Size Small**
     - A small audience is predicted to incude ~50% of customers who are likely to perform a revenue-generating event.
   * - **Audience Size Medium**
     - A medium audience is predicted to include ~70%of customers who are likely to perform a revenue-generating event
   * - **Audience Size Large**
     - A large audience is predicted to include ~90%of customers who are likely to perform a revenue-generating event

Combine these attributes with the **Target Event** attribute to build audiences for a specific revenue-generating event. You can access these attributes directly from the segment editor.

.. model-event-propensity-use-cases-recommended-audiences-attributes-end


.. _model-event-propensity-use-cases-customer-ranking:

Customer ranking
--------------------------------------------------

.. model-event-propensity-use-cases-customer-ranking-start

Use customer ranking to define an audience using the top N customers. Use customer ranking as an alternate to recommended audience sizes when an audience is too large (or small) or if a recommended audience size is unavailable for a specific event.

.. model-event-propensity-use-cases-customer-ranking-end

.. model-event-propensity-use-cases-customer-ranking-attribute-start

The **Ranking** attribute in the **Event Propensity** table ranks customer scores by event. A rank that is less than or equal to X will provide the top N customers with a propensity for this event. Combine this attribute with the **Target Event** attribute to build customer rankings for a specific revenue-generating event. You can access this attribute directly from the segment editor.

.. model-event-propensity-use-cases-customer-ranking-attribute-end
