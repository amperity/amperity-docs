.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Build automated, multi-step marketing interactions across channels.

.. meta::
    :content class=swiftype name=body data-type=text:
        Build automated, multi-step marketing interactions across channels.

.. meta::
    :content class=swiftype name=title data-type=string:
        About journeys


==================================================
About journeys
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-start
   :end-before: .. term-journey-end

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-about-context-start
   :end-before: .. journeys-about-context-end


.. _journeys-howitworks:

How journeys work
==================================================

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howitworks-start
   :end-before: .. journeys-howitworks-end

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howitworks-context-start
   :end-before: .. journeys-howitworks-context-end


.. _journeys-setup:

Journey setup
==================================================

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-setup-start
   :end-before: .. journeys-setup-end


.. _journeys-setup-who-enters:

Who enters?
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-setup-who-enters-start
   :end-before: .. journeys-setup-who-enters-end


.. _journeys-setup-who-is-excluded:

Who is excluded?
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-setup-who-is-excluded-start
   :end-before: .. journeys-setup-who-is-excluded-end


.. _journeys-exit-conditions:

Exit conditions
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-exit-conditions-start
   :end-before: .. journeys-exit-conditions-end


.. _journeys-canvas:

Journeys canvas
==================================================

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-canvas-start
   :end-before: .. journeys-canvas-end

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-types-start
   :end-before: .. journeys-node-types-end


.. _journeys-node-start:

Journey start
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-journey-node-start-start
   :end-before: .. term-journey-node-start-end

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-start-start
   :end-before: .. journeys-node-start-end


.. _journeys-node-activate:

Activate
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-activate-start
   :end-before: .. journeys-node-activate-end


.. _journeys-node-delay:

Delay
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-delay-start
   :end-before: .. journeys-node-delay-end


.. _journeys-node-split-conditional:

Conditional split
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-split-conditional-start
   :end-before: .. journeys-node-split-conditional-end


.. _journeys-node-split-percent:

Percent split
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-split-percent-start
   :end-before: .. journeys-node-split-percent-end


.. _journeys-node-split-individual:

Individual split
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-split-individual-start
   :end-before: .. journeys-node-split-individual-end


.. _journeys-node-merge:

Merge
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-merge-start
   :end-before: .. journeys-node-merge-end


.. _journeys-add-node:

Add a node
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-node-add-start
   :end-before: .. journeys-node-add-end


.. _journeys-configure-destination-attributes:

Configure destination attributes
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howtos-edit-destination-attributes-start
   :end-before: .. journeys-howtos-edit-destination-attributes-end

**To configure destination attributes**

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howtos-edit-destination-attributes-steps-start
   :end-before: .. journeys-howtos-edit-destination-attributes-steps-end


.. _journeys-schedule-a-journey:

Schedule a journey
--------------------------------------------------

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howtos-schedule-a-journey-start
   :end-before: .. journeys-howtos-schedule-a-journey-end

**To schedule a journey**

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howtos-schedule-a-journey-steps-start
   :end-before: .. journeys-howtos-schedule-a-journey-steps-end

.. include:: ../../amperity_reference/source/journeys.rst
   :start-after: .. journeys-howtos-schedule-a-journey-important-admonition-start
   :end-before: .. journeys-howtos-schedule-a-journey-important-admonition-end


.. _journeys-sample-use-cases:

Journeys use case examples
==================================================

The following examples demonstrate how to structure a journey in the Journeys canvas to achieve specific business outcomes.

.. journeys-use-case-examples-note-start

.. note:: These are hypothetical examples to give a sense of what is possible. Use them as inspiration or a starting point to structure a journey that fits your brand's particular circumstances.

.. journeys-use-case-examples-note-end

.. _journeys-use-case-new-customer:

New customer
--------------------------------------------------

.. journeys-use-case-new-customer-start

The goal of a new customer journey is to turn a new customer into an engaged participant by providing helpful, sequenced information that guides customers to a second purchase.

.. admonition:: Why new customer journeys work

   A new customer journey ensures the customer receives prompt, relevant communication, and non-engaged users get an additional message on a separate channel with an incentive to act quickly.

**Example basic new customer journey**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "First-time buyer" segment criteria.
   * - **Activate** 
     - Send a personalized "Welcome" email with a thank you and brand story/mission.
   * - **Delay**
     - Wait 24 hours.
   * - **Activate**
     - Send a short, high value SMS (for example, "Use code WELCOME10 for 10% off your next order!"). 
   * - **Exit**
     - Customers exit a new customer journey when they complete a second purchase.


**Example new customer journey flow with split:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "First-time buyer" segment criteria.
   * - **Activate** 
     - Send a personalized "Welcome" email with a thank you and brand story/mission.
   * - **Conditional split** 
     - Check if the customer has viewed a product page within 7 days.
   * - **Path A (Engaged)**
     - **Activate:** Send a "Tips and Tricks" email relevant to their viewed product.
   * - **Path B (Not Engaged)**
     - For customers who have not made a second purchase or viewed any additional products, take the following steps: 
       
       #. **Delay:** Wait 3 days.
       #. **Activate:** Send a short, high value SMS (for example, "Use code WELCOME10 for 10% off your next order!").
   * - **Exit** 
     - Customers exit a new customer journey when they complete a second purchase.

.. journeys-use-case-welcome-end

.. _journeys-use-case-abandoned-cart:

Abandoned cart
--------------------------------------------------

.. journeys-use-case-abandoned-cart-start

The goal of an abandoned cart journey is to convert users who started a purchase but abandoned their cart before completing the transaction.

.. admonition:: Why abandoned cart journeys work

   An abandoned cart journey reinforces the same intent across multiple touchpoints without redundancy. It uses immediate, low-incentive reminders first, reserving the higher-value incentive (the 10% discount) for the most valuable, high-AOV abandoned carts, thus protecting margins.

.. note:: Abandoned cart journeys require real-time functionality to be enabled.

**Example abandoned cart journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Abandoned cart > $50" segment criteria..
   * - **Delay**
     - Wait 2 hours to allow for organic purchase completion.
   * - **Conditional split**
     - Check if the customer has completed the purchase to meet the exit condition.
   * - **Path A (Purchased)**
     - Customer exits journey 
   * - **Path B (Has not purchased)**
     - For customers who have not purchased, take the following steps:

       #. **Activate**: Send a simple "Did you forget something?" reminder email with product image.
       #. **Delay**: Wait 24 hours.
       #. **Activate**: Send SMS with a 10% discount code        
       #. **Delay**: Wait 24 hours.
       #. **Activate**: Add customer to a Facebook/Google Retargeting Ad Audience for the specific product.
   * - **Exit**
     - Customers exit an abandoned cart journey when they complete the purchase.

.. journeys-use-case-abandoned-cart-end

.. _journeys-use-case-birthday:

Birthday
--------------------------------------------------

.. journeys-use-case-birthday-start

The goal of a birthday journey is to drive immediate, high-margin revenue through a personalized, time-sensitive offer. At the same time, it aims to deepen emotional connection and increase retention.

It can also be used for other similar milestones, like the aniversary of reaching a new tier in the loyalty program.

.. admonition:: Why birthday journeys work

   A birthday journey uses a highly personal attribute and tailors the channel and incentive to protect margin while getting the most impact from the most valuable customers.

**Example birthday journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Birthday within 7 days" segment criteria.
   * - **Conditional split**
     - Split based on loyalty tier (for example, VIP vs. Standard).
   * - **Path A (VIP)**
     - **Activate:** Send an exclusive "Happy birthday, VIP!" email with a high-value offer (for example, 20% off, double points, etc). 
       
       **Activate:** (optional) Send a physical postcard with a high value offer.
   * - **Path B (Standard)** 
     - **Activate:** Send a "Happy Birthday" email with a standard offer (for example, 10% off).
   * - **Merge**
     - Merges paths back together.
   * - **Conditional split**
     - Check if the customer has redeemed the offer.
   * - **Path A (Did redeem)** 
     - Customer exits the journey.
   * - **Path B (Did not redeem)** 
     - **Activate:** Send an SMS reminder that the offer expires soon.
   * - **Exit**
     - Customers exit a birthday journey if they redeem the offer and make a purchase.

.. journeys-use-case-birthday-end

.. _journeys-use-case-product-consideration:

Product consideration
--------------------------------------------------

.. journeys-use-case-product-consideration-start

The goal of a product consideration journey is to convert recent browsers and product page viewers into purchasers by nudging them with relevant product information and social proof.

.. admonition:: Why product consideration journeys work

   Product consideration journeys use multi-channel engagement to keep the product top-of-mind, while the A/B test measures the incremental lift provided by the paid advertising or discount channel against organic email.

**Example product consideration journey flow**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Viewed Product Category X in last 48 hours, but did not purchase" segment criteria.
   * - **Activate**
     - Send an email featuring social proof (customer reviews, ratings) for the viewed products.
   * - **Delay**
     - Wait 24 hours.
   * - **Percent split**
     - A/B test with a 50/50 split.
   * - **Path A (Treatment)**
     - **Activate:** Add the customer to a lookalike/retargeting audience to receive ads featuring a discount code. 
   * - **Path B (Control)**
     - **Activate:** Send a "Bestsellers in Category X" email without a discount.
   * - **Merge**
     - Merges paths back together.
   * - **Activate**
     - CRM syncs with point of sale so that if customers visit a store, associate sees the same recommendations.
   * - **Exit**
     - Customers exit a product consideration journey when they make a purchase.

.. journeys-use-case-product-consideration-end

.. _journeys-use-case-cross-sell:

Cross-sell
--------------------------------------------------

.. journeys-use-case-cross-sell-start

The goal of a cross-sell journey is to increase order frequency by recommending complementary products immediately following a purchase. A cross-sell journey activates customers using email or SMS campaigns and through paid media advertising, depending on the type of customer and the immediate goal.

.. admonition:: Why cross-sell journeys work

   A cross-sell journey references immediate purchase data to stay relevant. Split this audience by loyalty status to offer the best incentives, such as double loyalty points for VIPs and free shipping for everyone else.

**Example cross-sell journey flow**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Purchased product Y in the last 24 hours" segment criteria.
   * - **Conditional split**
     - Check if the customer is already a VIP/loyalty member.
   * - **Path A**
     - **Activate**: Send a "Complete your look" email to VIPs featuring high-margin, complementary products and offering double loyalty points on the next purchase.
   * - **Path B**
     - **Activate**: Send a "Complementary items" email to everyone else with a focus on free shipping for the next order.
   * - **Delay**
     - Wait 48 hours.
   * - **Merge**
     - Bring the two paths back together.
   * - **Conditional split**
     - Check if a cross-sell purchase has been made.
   * - **Path A**
     - Customers who have made a qualifying second purchase exit the journey.
   * - **Path B**
     - For customers who have not made a qualifying second purchase within the last 48 hours, send a reminder focused on purchasing a complementary product.

       Path B takes the following steps:

       #. **Activate**: Use SMS advertising to send a reminder focused on purchasing a complementary product.
       #. **Delay**: Wait 24 hours.
       #. **Activate** Use a lookalike audience on a paid media platform to run a carousel ad that features complementary items.
   * - **Exit**
     - Customers exit a cross-sell journey after they make a second, qualifying purchase within the timeframe defined by the cross-sell journey.


.. journeys-use-case-cross-sell-end

.. _journeys-use-case-seasonal:

Seasonal campaign
--------------------------------------------------

.. journeys-use-case-seasonal-start

The goal of a seasonal campaign journey is to drive revenue and brand engagement during key shopping periods (for example, Black Friday, Summer sale).

.. admonition:: Why seasonal campaign journeys work

   The seasonal campaign journey uses highly personalized, category-specific messaging and time-sensitive incentives across multiple channels, mitigating message fatigue and ensuring campaign theme consistency.

**Example seasonal campaign journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Has purchased in the last 12 months" segment criteria.
   * - **Activate**
     - Send a pre-sale email with a sneak peek of new products.
   * - **Delay**
     - Wait 24 hours.
   * - **Activate**
     - Send a last-chance SMS reminder about exclusive early access to the sale.
   * - **Activate**
     - Use dynamic homepage to display products on site matching promotion in targeted emails & SMS.
   * - **Delay**
     - Wait 48 hours.
   * - **Conditional split**
     - Check if the customer is a VIP/loyalty member
   * - **Path A (VIP)**
     - **Activate:** Exclusive direct mailcatalog with QR to curated collection. 
   * - **Path B (Non-VIP)**
     - **Activate:** Social media ad carousel featuring relevant items.
   * - **Exit**
     - Customers exit a seasonal campaign journey by making a purchase during the defined seasonal window.

.. journeys-use-case-seasonal-end

.. _journeys-use-case-vip-upgrade:

Loyalty tier upgrade
--------------------------------------------------

.. journeys-use-case-vip-upgrade-start

The goal of a loyalty tier upgrade journey is to reward and retain high value customers when they hit a new level of the loyalty program, encouraging future engagement and spend.

.. admonition:: Why loyalty tier upgrade journeys work

   Loyalty tier upgrade journeys provide the recognition and exclusivity that build emotional connection and brand loyalty.

**Example loyalty tier upgrade journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Achieved loyalty gold tier" segment criteria.
   * - **Activate**
     - Send an SMS with a personalized thank you and link to a website detailing new perks.
   * - **Delay**
     - Wait 24 hours.
   * - **Activate**
     - In-app notification with access to bonus reward or exclusive collection.
   * - **Activate**
     - CRM syncs with point of sale so store associate greets customer by name and mentions benefits.
   * - **Exit**
     - Customers exit a loyalty tier upgrade journey 30 days after achieving the new status tier.

.. journeys-use-case-vip-upgrade-end

.. _journeys-use-case-test-drive:

Car test-drive
---------------------------------------------------

.. journeys-use-case-test-drive-start

The goal of a car test-drive journey is to convert website interest (for example, "Build and Price" activity) into an in-person appointment or service booking.

.. admonition:: Why car test-drive journeys work

   Car test-drive journeys create a multi-touchpoint experience, bridging the gap between digital behavior and physical action by sending a lead to the sales CRM to trigger a response outside the marketing automation system. 

**Example car test-drive journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Viewed Vehicle Details Page or Used 'Build & Price' tool in last 7 days" segment criteria.
   * - **Conditional split**
     - Check if the customer has already booked an appointment.
   * - **Path A (No appointment)**
     - For customers who have not yet booked an appointment, take the following steps:

       #. **Activate**: Send an email offering a local dealer consultation or link to book a test drive.
       #. **Delay**: Wait 48 hours.
       #. **Activate**: Send a follow up SMS with a link to book a test drive.
   * - **Path B (Appointment booked)**
     - **Activate:** Send a "Pre-appointment checklist" email with confirmation details and required documentation.
   * - **Merge**
     - Bring the two paths back together.
   * - **Activate**
     - Send an SMS with reminder and details on the upcoming appointment.
   * - **Delay**
     - Wait 7 days.
   * - **Conditional split**
     - Check if the test-drive customer has made a purchase.
   * - **Path A (Purchase made)**
     - Exit condition is satisfied.
   * - **Path B (No purchase made)** 
     - **Activate:** CRM alerts sales rep to call customer.
   * - **Exit**
     - A customer exits a car test-drive journey when they have completed a purchase.

.. journeys-use-case-test-drive-end

.. _journeys-use-case-replenishment:

Product replenishment
----------------------------------------------------------

.. journeys-use-case-replenishment-start

The goal of a product replenishment journey is to drive repeat purchases based on predicted product consumption cycles.

.. admonition:: Why product replenishment journeys work

   A product replenishment journey segments customers not just by what they bought but by when they are predicted to need it again, combining precise timing with a multi-channel nudge to maximize repeat sales.


**Example product replenishment journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "Purchased 60-day size of Product Y, 50 days ago" segment criteria.
   * - **Activate**
     - Send a "Time to reorder" email with a direct link to the product page.
   * - **Conditional split**
     - Check if the customer has clicked the reorder link within 3 days.
   * - **Path A (clicked link)**
     - **Activate:** Add customer to a retargeting audience to see display ads featuring the product and a small incentive (for example, free sample with reorder). 
   * - **Path B (did not click)**
     - For customers who did not click the reorder link, take the following steps:

       #. **Delay**: Wait 7 days.
       #. **Activate**: Send an SMS asking "Did you run out yet?" with a link to reorder, also highlighting the option to subscribe.
   * - **Exit**
     - Customers exit a product replenishment journey when they purchase the specific product or activate a subscription.

.. journeys-use-case-replenishment-end

.. _journeys-use-case-financial-onboarding:

Financial services welcome
--------------------------------------------------

.. journeys-use-case-financial-onboarding-start

The goal of a financial services welcome journey is to guide new account holders to full product adoption and usage.

.. admonition:: Why financial services welcome journeys work

   A financial services welcome journey uses data across channels to move customers from awareness to activation, building deeper engagement. 

**Example financial services welcome journey flow:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Step
     - Description
   * - **Start**
     - Customer meets the "New checking account opened in last 7 days" segment criteria.
   * - **Conditional split**
     - Split based on setup progress (for example, Has direct deposit been set up?).
   * - **Path A (Direct deposit set up)**
     - **Activate:** Send "Congratulations!" email introducing advanced features (for example, mobile check deposit). 
   * - **Path B (Direct deposit not set up)**
     - For customers who have not yet set up direct deopsit take the following steps:

       #. **Delay**: Wait 48 hours.
       #. **Activation**: Trigger a personalized in-app notification with a step-by-step guide for setting up direct deposit.
       #. **Delay**: Wait 7 days.
       #. **Activate**: CRM flags a task in the call center queue for a proactive outreach call.
   * - **Exit**
     - Customers exit a financial services welcome journey when direct deposit is set up.

.. journeys-use-case-financial-onboarding-end