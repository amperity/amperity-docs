.. https://docs.amperity.com/user/


.. |destination-name| replace:: Google Analytics 4
.. |what-send| replace:: purchase events
.. |what-enablex| replace:: **email**
.. |attributes-sent| replace:: |destination-name| purchase events for transactions for offline attribution.


.. meta::
    :description lang=en:
        Send purchase events to Google Analytics 4.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send purchase events to Google Analytics 4.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send purchase events to Google Analytics 4

=================================================
Send purchase events to Google Analytics 4
=================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-google-analytics-start
   :end-before: .. term-google-analytics-end

.. include:: ../../amperity_operator/source/events_google_analytics.rst
   :start-after: .. events-google-analytics-overview-start
   :end-before: .. events-google-analytics-overview-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _events-google-analytics-build-query:

Build a query
==================================================

.. include:: ../../amperity_operator/source/events_google_analytics.rst
   :start-after: .. events-google-analytics-build-query-start
   :end-before: .. events-google-analytics-build-query-end

.. events-google-analytics-build-query-start

Extend the SQL to include :ref:`any of the additional fields <events-google-analytics-map-parameters>` that are accepted by |destination-name|.

.. events-google-analytics-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _events-google-analytics-event-parameters:

GA4 events parameters
==================================================

.. include:: ../../amperity_operator/source/events_google_analytics.rst
   :start-after: .. events-google-analytics-event-parameters-start
   :end-before: .. events-google-analytics-event-parameters-end

.. include:: ../../amperity_operator/source/events_google_analytics.rst
   :start-after: .. events-google-analytics-event-parameters-table-start
   :end-before: .. events-google-analytics-event-parameters-table-end


.. _events-google-analytics-map-parameters:

Map Amperity attributes to GA4 events parameters
==================================================

.. include:: ../../amperity_operator/source/events_google_analytics.rst
   :start-after: .. events-google-analytics-event-map-parameters-start
   :end-before: .. events-google-analytics-event-map-parameters-end

.. include:: ../../amperity_operator/source/events_google_analytics.rst
   :start-after: .. events-google-analytics-event-map-parameters-table-start
   :end-before: .. events-google-analytics-event-map-parameters-table-end
