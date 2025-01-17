.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: The Trade Desk
.. |what-send| replace:: email address lists
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to The Trade Desk.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to The Trade Desk.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to The Trade Desk

==================================================
Send query results to The Trade Desk
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-thetradedesk-start
   :end-before: .. term-thetradedesk-end

.. sendto-the-trade-desk-start

Use Amperity to manage email addresses in |destination-name|. Build a query using the **email** field and send the results of that query to |destination-name|. If contacts exist in |destination-name| for the emails sent in the query, the contact list will be updated to match the query.

.. sendto-the-trade-desk-end

.. destination-the-trade-desk-start

.. TODO: This must be manually kept in sync across /datagrid/destination_the_trade_desk.rst and /ampiq/destination_the_trade_desk.rst.

Amperity can manage audiences for |destination-name| demand-side platform, from which your brand can reach audiences throughout their entire digital journey and across every channel and device, including:

* Display advertising on ABC, ESPN, the Wall Street Journal, live sporting events (Major League Baseball), in-store advertising at WalMart, and more.
* Video advertising on over-the-top (OTT) and connected TV (CTV) apps and platforms, such as Disney+, Major League Baseball, Hulu, Fox, Vevo, Paramount+, and more.
* Audio advertising in-between songs and during podcasts across Spotify, Pandora, SoundCloud, iHeart, and more.

.. destination-the-trade-desk-start

.. include:: ../../amperity_datagrid/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-whatis-20-start
   :end-before: .. destination-the-trade-desk-whatis-20-end

.. include:: ../../amperity_datagrid/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-api-note-start
   :end-before: .. destination-the-trade-desk-api-note-end

.. sendto-the-trade-desk-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-the-trade-desk-build-query>`
#. :ref:`Add orchestration <sendto-the-trade-desk-add-orchestration>`
#. :ref:`Run orchestration <sendto-the-trade-desk-run-orchestration>`

.. sendto-the-trade-desk-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-the-trade-desk-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end

.. sendto-the-trade-desk-build-query-start

You may build a more refined list of email addresses, such as those associated with a high-value audience (historical or predicted), or those with affinities for certain products in your brand. You may use **uid2** as a source attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand.

.. sendto-the-trade-desk-build-query-end

.. sendto-the-trade-desk-build-query-admonition-start

.. admonition:: Which attributes should you use?

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

   Your brand should only send custom audiences that contain customers who reside within the United States and/or offline events that occurred within the United States to |destination-name|.

.. sendto-the-trade-desk-build-query-admonition-end


.. _sendto-the-trade-desk-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-the-trade-desk-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
