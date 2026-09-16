.. https://docs.amperity.com/user/


.. |destination-name| replace:: ActiveCampaign
.. |what-send| replace:: audience lists
.. |allow-for-what| replace:: audience lists
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to ActiveCampaign.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to ActiveCampaign.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to ActiveCampaign

==================================================
Send query results to ActiveCampaign
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-active-campaign-start
   :end-before: .. term-active-campaign-end

.. sendto-active-campaign-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** field and send the results of that query to |destination-name|. If contacts exist in |destination-name| for the emails sent in the query, the contact list is updated to match the query.

.. sendto-active-campaign-end

.. include:: ../../amperity_operator/source/destination_active_campaign.rst
   :start-after: .. destination-active-campaign-api-note-start
   :end-before: .. destination-active-campaign-api-note-end

.. sendto-active-campaign-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-active-campaign-build-query>`
#. :ref:`Add orchestration <sendto-active-campaign-add-orchestration>`
#. :ref:`Run orchestration <sendto-active-campaign-run-orchestration>`

.. sendto-active-campaign-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-active-campaign-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-active-campaign-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-active-campaign-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
