.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        Stream events to Amperity to compare anonymous profiles to known profiles. Checkout events, app login events, WiFi connections, and loyalty events can all be associated with a known profile. Anonymous-to-known profiles are immediately available for marketing activation using the Profile API v3 and single-profile activation journeys.

.. meta::
    :content class=swiftype name=body data-type=text:
        Stream events to Amperity to compare anonymous profiles to known profiles. Checkout events, app login events, WiFi connections, and loyalty events can all be associated with a known profile. Anonymous-to-known profiles are immediately available for marketing activation using the Profile API v3 and single-profile activation journeys.

.. meta::
    :content class=swiftype name=title data-type=string:
        Anonymous-to-known


==================================================
About anonymous-to-known
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-anonymous-profile-start
   :end-before: .. term-anonymous-profile-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-known-profile-start
   :end-before: .. term-known-profile-end


Use cases
==================================================

.. usecase-anonymous-to-known-about-start

Anonymous-to-known resolution makes these downstream outcomes possible.

.. usecase-anonymous-to-known-about-end


Better lookalike audiences
--------------------------------------------------

Lookalike audience seeds built from known profiles are cleaner and more complete than seeds built from a single export. Each resolved identity event adds matching keys and corrects fragmentary profile records--improving the completeness of the seed list and the quality of the lookalike model.


Cross-channel identity
--------------------------------------------------

When a customer logs in using a secondary email, phone number, or loyalty ID, Amperity's Stitch rules link the new identifier to the existing profile. Downstream systems that query the profile by any of the customer's known identifiers will find the same unified record.


Higher match rates
--------------------------------------------------

Paid media platforms match on hashed email addresses. A customer who has used two email addresses with your brand contributes two matching keys to your custom audience list. Amperity-known profiles that include all known email addresses for each customer produce higher audience match rates than single-system exports. The improvement is immediate when a new address is resolved.


List suppression
--------------------------------------------------

A customer who opted out using their work email and later logs in using their personal email is the same person. If the opt-out is stored against the work email in Amperity and the login event links the personal email to the same profile, the suppression flag is immediately visible on any lookup using either email.


Link offline to online
--------------------------------------------------

In-store transactions, venue check-ins, and point of sale (POS) interactions often carry phone numbers or loyalty IDs that do not appear in e-commerce or email data. Streaming these identification events to Amperity resolves the in-store identity against the online profile, creating a true omnichannel record.


Personalization accuracy
--------------------------------------------------

When a customer logs in to a new channel--an app they have never used, a venue WiFi network--the personalization lookup by their login email finds the full profile: loyalty tier, LTV decile, churn score. A partial profile or a missed lookup would produce a default experience. The known profile produces the right one.


.. _usecase-anonymous-to-known-how-it-works:

How it works
==================================================

.. note:: The strength of anonymous-to-known resolution depends on the linking keys configured in Amperity's Stitch rules and the keychain settings on each event type. An authentication event that carries only a session cookie--with no stable customer identity field--cannot be linked to a profile. Include at least one durable identifier in every authentication event payload: email, phone, customer ID, or loyalty ID. Configure that identifier as a keychain linking key on the Amperity event type.

.. usecase-anonymous-to-known-how-it-works-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - An anonymous customer clicks an ad on Google. This opens your brand's website with the page for the item shown. The customer is logged out of your website and remains anonymous. The customer puts the item into their cart. An event is sent.

       .. image:: ../../images/identity-recognition-unlinked1.png
          :width: 500 px
          :alt: A merge outcome for identity recognition of events in an event stream
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - The anonymous customer continues browsing, but puts no more items into their cart. The next day the same anonymous customer puts another item into their cart. The customer has still not logged into the website. Another event is sent that matches the anonymous identifier in the previous event.

       .. image:: ../../images/identity-recognition-unlinked2.png
          :width: 500 px
          :alt: A merge outcome for identity recognition of events in an event stream
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - The anonymous customer logs into the website. An event is sent that identifies the customer's loyalty account ID. The customer is no longer anonymous and the previously anonymous events now match to a known profile.

       .. image:: ../../images/identity-recognition-merge.png
          :width: 500 px
          :alt: A merge outcome for identity recognition of events in an event stream
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - The customer *almost* completes the transaction, stopping at the payment step. Maybe the customer forgot the password or card number for their payment option? The items remain in the cart.


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - Because the cart events are linked to a known profile a cart abandonment journey begins. In 3 hours an SMS message is sent to the customer reminding them of the items they put into the cart and an ask to complete the transaction.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - If the customer does not purchase within 24 hours an email reminder is sent to the customer's primary email account.

.. usecase-anonymous-to-known-how-it-works-end


Sources of events data
==================================================

The following integrations generate identification signals that support anonymous-to-known resolution. The linking keys each integration carries--email, phone, customer ID, loyalty ID--determine whether an event resolves to a known profile.


Checkouts
--------------------------------------------------

At checkout, a previously anonymous browser session becomes a known customer.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Integration
     - Description

   * - Shopify
     - Stream checkout events from Shopify to Amperity. Shopify's **checkouts/create** and **orders/create** webhooks carry the customer's email, phone, and Shopify customer ID. A checkout by a previously untracked email address resolves it against the existing Amperity profile for that customer.

   * - BigCommerce
     - Stream checkout and order events from BigCommerce. The order webhook carries email and customer ID for linking.

   * - WooCommerce
     - Stream order events from WooCommerce. WooCommerce order webhooks include the customer's billing email and customer ID.


Authentication platforms
--------------------------------------------------

These integrations stream identification events from login and authentication platforms.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Integration
     - Description

   * - Auth0
     - Stream login and registration events from Auth0 Log Streams to Amperity. Auth0's **user_name** field carries the email address; **user_id** carries the Auth0 internal identifier. Every login event is an anonymous-to-known signal: the customer has identified themselves at this moment, with this email, from this connection.

   * - Google
     - Anonymous-to-known resolution via Google sign-in has not yet been documented. Integration patterns for Google Identity Services are under research.

   * - Okta
     - Stream login and lifecycle events from Okta Event Hooks to Amperity. Okta's **alternateId** field on the event target carries the email. User creation events (**user.lifecycle.create**) are particularly valuable for initial profile creation at the moment of account registration.


Mobile apps
--------------------------------------------------

App login events link the mobile session identity to the customer profile.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Integration
     - Description

   * - Mobile app events
     - Stream login and profile-update events from your mobile app using the Amperity Events API directly from a backend service. Carry the customer's email, phone, and internal customer ID from the app's authenticated session.

   * - AppsFlyer
     - Stream AppsFlyer attribution events to Amperity. AppsFlyer's **customer_user_id** parameter carries your internal customer ID (set by the SDK on login), linking the mobile attribution event to the Amperity profile.

   * - Adjust
     - Stream Adjust attribution callbacks to Amperity. Adjust's **external_device_id** parameter carries your internal customer ID, linking mobile events to the Amperity profile at the moment of authentication.


Physical systems
--------------------------------------------------

Logins to physical systems, such as WiFi networks or point-of-sale terminals, are valuable opportunities for identity resolution.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Integration
     - Description

   * - WiFi captive portal
     - Resolve the Amperity profile at venue WiFi login using a SHA-256 hashed email. The raw email address is never forwarded to Amperity. The captive portal splash page can render personalized content (name, loyalty tier, points balance) from the known profile immediately after login.

   * - Points of sale
     - Query the Amperity profile at the point of sale (POS) terminal using the customer's email or loyalty ID at transaction time. Point of sale (POS) identification events that carry a new email or loyalty ID resolve against the customer's existing profile, linking in-store purchase history to the omnichannel record.


Event routing platforms
--------------------------------------------------

These platforms collect events from web, mobile, and server-side sources and route them to Amperity in real-time. Each carries an anonymous identifier on pre-login events and a customer identifier on authenticated events, making them a direct source of anonymous-to-known signals.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Integration
     - Description

   * - mParticle
     - Route events from web, iOS, and Android SDKs through mParticle's server-side pipeline. mParticle's anonymous device ID maps to the anonymous linking key; when IDSync fires at login with an email, the event links all prior anonymous activity to the known profile.

   * - RudderStack
     - Route events using the Segment-compatible spec. The **anonymousId** field is present on every event before login. When a customer authenticates, the **alias()** call carries both the prior anonymous ID and the new authenticated user ID, which Amperity uses as an explicit merge signal.

   * - Tealium
     - Forward behavioral events from Tealium EventStream to Amperity via the Webhook connector. When a customer identification event fires--a login, a registration, a loyalty scan--Tealium includes the customer's email or ID in the data layer and the connector forwards it directly.

   * - MetaRouter
     - Route events from websites, mobile apps, and server-side APIs using MetaRouter's native Amperity destination. MetaRouter's enrichment pipeline applies identity enrichment and consent filtering before forwarding identification events to Amperity.
