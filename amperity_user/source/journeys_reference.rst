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

.. note:: These are hypothetical examples to give a sense of what is possible. Use them as inspiration or a starting point to structure a journey that fits your brand's particular circumstances. 

.. _journeys-use-case-welcome:

Welcome and onboarding journey
--------------------------------------------------

.. journeys-use-case-welcome-start

**Goal:** Turn a new customer into an engaged participant by providing helpful, sequenced information.

**Channels:** Email, SMS

**Example flow:**
  #. **Start:** Customer meets the "First-time buyer" segment criteria.
  #. **Activate (Email 1):** Send a personalized "Welcome" email with a thank you and brand story/mission.
  #. **Conditional split:** Check if the customer has made a purchase or viewed a product page within 7 days.
  #. **Path A (Engaged):**
       * **Activate (Email 2):** Send a "Tips and Tricks" email relevant to their purchased/viewed product.
  #. **Path B (Not Engaged):**
       * **Delay:** Wait 3 days.
       * **Activate (SMS):** Send a short, high-value message (e.g., "Use code WELCOME10 for 10% off your first order!").
  #. **Exit condition:** Customer completes a purchase.

**Why it works:** This sequence ensures the customer receives prompt, relevant communication, and non-engaged users get a message on an additional channel with an incentive to act quickly.

.. journeys-use-case-welcome-end

.. _journeys-use-case-abandoned-cart:

Abandoned cart journey
--------------------------------------------------

.. journeys-use-case-abandoned-cart-start

**Goal:** Convert users who started a purchase but abandoned their cart before completing the transaction.

**Channels:** Email, Retargeting ad audience

**Example flow:**
  #. **Start:** Customer meets the "Abandoned cart > $50" segment criteria.
  #. **Delay:** Wait 2 hours (to allow for organic purchase completion).
  #. **Conditional split:** Check if the customer has completed the purchase to meet the exit condition.
  #. **Path A (Purchased):** Customer exits the journey.
  #. **Path B (Did Not Purchase):**
       * **Activate (Email 1):** Send a simple "Did you forget something?" reminder email with product image.
       * **Delay:** Wait 24 hours.
       * **Conditional split:** Check if the cart value is > $150.
           * **High-Value Path:**
               * **Activate (Email 2):** Send an email with a 10% discount code.
           * **Standard Path:**
               * **Activate (Ad audience):** Add customer to a Facebook/Google Retargeting Ad Audience for the specific product.
  #. **Exit condition:** Customer completes a purchase.

**Why it works:** Reinforces the same intent across multiple touchpoints without redundancy. It uses immediate, low-incentive reminders first, reserving the higher-value incentive (the 10% discount) for the most valuable, high-AOV abandoned carts, thus protecting margins.

.. journeys-use-case-abandoned-cart-end

.. _journeys-use-case-birthday:

Birthday or loyalty milestone journey
--------------------------------------------------

.. journeys-use-case-birthday-start

**Goal:** Drive immediate, high-margin revenue through a personalized, time-sensitive offer. Deepen emotional connection and increase retention.

**Channels:** Email, SMS, Direct mail (optional)

**Example flow:**
  #. **Start:** Customer meets the "Birthday within 7 days" or "Loyalty tier anniversary" segment criteria.
  #. **Conditional split:** Split based on loyalty tier (e.g., VIP vs. Standard).
  #. **Path A (VIP):**
       * **Activate (Email):** Send an exclusive "Happy birthday, VIP!" email with a high-value offer (e.g., 20% off).
       * **Activate (Direct mail, optional):** Send a physical postcard announcing a double-points week.  
  #. **Path B (Standard):**
       * **Activate (Email):** Send a "Happy Birthday" email with a standard offer (e.g., 10% off).
  #. **Delay:** Wait 4 days.
  #. **Conditional split:** Check if the customer has redeemed the offer.
  #. **Path C (Did not redeem):**
       * **Activate (SMS):** Send a reminder that the offer expires soon.
  #. **Exit condition:** Offer redemption is detected via a purchase event.

**Why it works:** Identifies high-value, personalized attributes (birthdays, loyalty tiers) and tailors the channel and incentive value to protect margin while maximizing impact from the most valuable customers. 

.. journeys-use-case-birthday-end

.. _journeys-use-case-product-consideration:

Product consideration to purchase journey
--------------------------------------------------

.. journeys-use-case-product-consideration-start

**Goal:** Convert recent browsers/product page viewers into purchasers by nudging them with relevant product information and social proof.

**Channels:** Email, Social media, Point of sale

**Example flow:**
  #. **Start:** Customer meets the "Viewed Product Category X in last 48 hours, but did not purchase" segment criteria.
  #. **Delay:** Wait 2 hours.
  #. **Activate (Email):** Send an email featuring social proof (customer reviews, ratings) for the viewed products.
  #. **Delay:** Wait 24 hours.
  #. **Percent split (A/B Test):** Split 50%/50%.
  #. **Path A (Treatment):**
       * **Activate (Social audience):** Add the customer to a lookalike/retargeting audience to receive ads featuring a discount code.
  #. **Path B (Control):**
       * **Activate (Email 2):** Send a "Bestsellers in Category X" email without a discount.
  #. **Activate (CRM point of sale sync):** If customers visit a store, associate sees the same recommendations.
  #. **Exit condition:** Customer makes a purchase.

**Why it works:** It uses multi-channel engagement to keep the product top-of-mind, and the A/B test measures the incremental lift provided by the paid advertising/discount channel against organic email.

.. journeys-use-case-product-consideration-end

.. _journeys-use-case-cross-sell:

Cross-sell / complete-the-look journey
--------------------------------------------------

.. journeys-use-case-cross-sell-start

**Goal:** Increase average order value (AOV) by recommending complementary products immediately following a purchase.

**Channels:** Email, Push, Social ad audience 

**Example flow:**
  #. **Start:** Customer meets the "Purchased product Y in the last 24 hours" segment criteria.
  #. **Conditional split:** Check if the customer is already a VIP/loyalty member.
  #. **Path A (VIP):**
       * **Activate (Email 1):** Send a "Complete your look" email featuring high-margin, complementary products and offering double loyalty points on the next purchase.
  #. **Path B (Standard):**
       * **Activate (Email 1):** Send a "Complementary items" email with a focus on free shipping for the next order.
  #. **Delay:** Wait 48 hours.
  #. **Conditional split:** Check if a cross-sell purchase has been made.
  #. **Path C (No purchase):**
       * **Activate (Push notification):** Send a reminder focused on completing the look with the complementary product.
       * **Delay** Wait 24 hours.
       * **Activate (Social ad audience):** Run a carousel ad featuring coordinated items.
  #. **Exit condition:** Customer makes a second, qualifying cross-sell purchase.

**Why it works:** By referencing immediate purchase data, the journey is hyper-relevant. Splitting by loyalty status allows you to offer the most profitable incentive mix: points for VIPs and shipping for standard customers.

.. journeys-use-case-cross-sell-end

.. _journeys-use-case-seasonal:

Seasonal / holiday campaign journey
--------------------------------------------------

.. journeys-use-case-seasonal-start

**Goal:** Drive revenue and brand engagement during key shopping periods (e.g., Black Friday, Summer sale).

**Channels:** Email, SMS, Dynamic homepage, Direct mail, Social ad audience

**Example flow:**
  #. **Start:** Customer meets the "Has purchased in the last 12 months" segment criteria.
  #. **Conditional split:** Split by preferred product category based on past purchase history.
  #. **Path A (Category 1):**
       * **Activate (Email 1):** Send a pre-sale email with a sneak peek of Category 1 products.
       * **Delay:** Wait 24 hours.
       * **Activate (SMS):** Send a last-chance reminder about the exclusive early access to the sale.
       * **Activate (Dynamic homepage):** Products on homepage match promotion in targeted emails.
       * **Delay:** Wait 48 hours.
       * **Conditional split:** Check if the customer is a VIP/loyalty member.
           * **Path A1 (VIP):** 
               * **Activate (Direct mail):** Exclusive catalog with QR to curated collection.
           * **Path A2 (Non-VIP):**
               * **Activate (Social ad audience):** Social media ad carousel featuring relevant items. 
  #. **Path B (Category 2):**
       * **Activate (Email 2):** Send a pre-sale email with a sneak peek of Category 2 products.
       * **Delay:** Wait 24 hours.
       * **Activate (SMS):** Send a last-chance reminder about the exclusive early access to the sale.
       * **Activate (Dynamic homepage):** Products on homepage match promotion in targeted emails.
       * **Delay:** Wait 48 hours.
       * **Conditional split:** Check if the customer is a VIP/loyalty member.
           * **Path B1 (VIP):** 
               * **Activate (Direct mail):** Exclusive catalog with QR to curated collection.
           * **Path B2 (Non-VIP):** 
               * **Activate (Social ad audience):** Social media ad carousel featuring relevant items.
  #. **Exit condition:** Customer makes a purchase during the defined holiday/seasonal window.

**Why it works:** The journey uses highly personalized, category-specific messaging and time-sensitive incentives across multiple channels, mitigating message fatigue and ensuring campaign theme consistency. 

.. journeys-use-case-seasonal-end

.. _journeys-use-case-vip-upgrade:

VIP / loyalty tier upgrade journey
--------------------------------------------------

.. journeys-use-case-vip-upgrade-start

**Goal:** Reward and retain high value customers, securing future retention and spend.

**Channels:** Email, SMS, In-app, CRM for in-store

**Example flow:**
  #. **Start:** Customer meets the "Achieved loyalty gold tier" segment criteria.
  #. **Activate (Email):** Send an email welcoming them to the gold tier.
  #. **Activate (SMS):** Personalized thank you and link to website detailing new perks.
  #. **Delay:** Wait 24 hours.
  #. **Activate (In-app message):** Notification with access to bonus reward or exclusive collection.
  #. **Activate (CRM for in-store alert):** Store associate greets customer by name and mentions benefits.

**Why it works:** Recognition and exclusivity build emotional connection and brand loyalty.

.. journeys-use-case-vip-upgrade-end

.. _journeys-use-case-test-drive:

Test-drive / automotive service appointment journey
---------------------------------------------------

.. journeys-use-case-test-drive-start

**Goal:** Convert website interest (e.g., "Build and Price" activity) into an in-person appointment or service booking.

**Channels:** Website, Email, SMS, CRM

**Example flow:**
  #. **Start:** Customer meets the "Viewed Vehicle Details Page or Used 'Build & Price' tool in last 7 days" segment criteria.
  #. **Conditional split:** Check if the customer has already booked an appointment.
  #. **Path A (No appointment):**
       * **Activate (Email 1):** Send an email offering a local dealer consultation or link to book a test drive.
       * **Delay:** Wait 48 hours.
       * **Activate (SMS):** Send a follow up SMS with a link to book a test drive or service.
  #. **Path B (Appointment booked):**
       * **Activate (Email 2):** Send a "Pre-appointment checklist" email with confirmation details and required documentation.
  #. **Merge:** Bring both paths together.
  #. **Activate (SMS):** Send an SMS with reminder and details on the upcoming appointment.
  #. **Delay:** Wait 7 days.
  #. **Conditional split:** Check if test-drive customer has made a purchase.
  #. **Path A (Purchase made):**
       * **Exit condition** is satisfied.
  #. **Path B (No purchase made):** 
       * **Activate (CRM):** Sales rep is alerted to call customer.

**Why it works:** This journey creates a multi-touchpoint experience, bridging the gap between digital behavior and physical action by sending a lead to the sales CRM to trigger a response outside the marketing automation system. 

.. journeys-use-case-test-drive-end

.. _journeys-use-case-replenishment:

Skincare replenishment (or any subscription item) journey 
----------------------------------------------------------

.. journeys-use-case-replenishment-start

**Goal:** Drive repeat purchases based on predicted product consumption cycles.

**Channels:** Email, Ad audience, SMS

**Example flow:**
  #. **Start:** Customer meets the "Purchased 60-day size of Cleanser X, 50 days ago" segment criteria.
  #. **Activate (Email 1):** Send a "Time to reorder" email with a direct link to the product page.
  #. **Conditional split:** Check if the customer has clicked the reorder link within 3 days.
  #. **Path A (clicked Link):**
       * **Activate (Ad audience):** Add customer to an ad audience to show retargeting ads featuring the product and a small incentive (e.g., free sample with reorder).
  #. **Path B (Did not click):**
       * **Delay:** Wait 7 days.
       * **Activate (Email 2):** Send a "Did you run out yet?" SMS, focusing on the subscription option.
  #. **Exit condition:** Customer makes a purchase of the specific replenishment product.

**Why it works:** Segmenting customers not just by what they bought but by when they are predicted to need it again combines precise timing with a multi-channel nudge to maximize repeat sales.

.. journeys-use-case-replenishment-end

.. _journeys-use-case-financial-onboarding:

Financial services onboarding
--------------------------------------------------

.. journeys-use-case-financial-onboarding-start

**Goal:** Guide new account holders to full product adoption and usage.

**Channels:** Email, In-app notification, CRM

**Example flow:**
  #. **Start:** Customer meets the "New checking account opened in last 7 days" segment criteria.
  #. **Conditional split:** Split based on setup progress (e.g., Has direct deposit been set up? Yes/No).
  #. **Path A (Direct deposit set up):**
       * **Activate (Email 1):** Send "Congratulations!" email introducing advanced features (e.g., mobile check deposit).
  #. **Path B (Direct deposit not set up):**
       * **Delay:** Wait 48 hours.
       * **Activate (In-App Notification):** Trigger a personalized in-app notification with a step-by-step guide for setting up direct deposit.
       * **Delay:** Wait 7 days.
       * **Conditional split:** Has the user logged into the app in the last 7 days?
       * **High-Risk Path (No login):** Trigger a task in the call center queue for a proactive outreach call.
  #. **Exit condition:** Direct deposit is successfully activated and the account is funded.

**Why it works:** This journey uses data across channels to move customers from awareness to activation, building deeper engagement. 

.. journeys-use-case-financial-onboarding-end