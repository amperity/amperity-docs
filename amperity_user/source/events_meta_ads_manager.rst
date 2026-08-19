.. https://docs.amperity.com/user/


.. |destination-name| replace:: Meta Ads Manager
.. |what-send| replace:: events
.. |what-enable| replace:: **EXTERN_ID**, **EMAIL**, **FN**, **LN**, **ST**, **CT**, **ZIP**, **COUNTRY**, **BIRTH**, **GEN**, **MADID**, and **PHONE**
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours
.. |attributes-sent| replace:: |destination-name| requires the **EXTERN_ID**, **EMAIL**, **FN**, **LN**, **ST**, **CT**, **ZIP**, **COUNTRY**, **BIRTH**, **GEN**, **MADID**, and **PHONE** attributes. The **MADID** (mobile advertising ID) attribute is optional.


.. meta::
    :description lang=en:
        Send events from Amperity to Meta Ads Manager.

.. meta::
    :content class=swiftype name=body data-type=text:
        Send events from Amperity to Meta Ads Manager.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send events to Meta Ads Manager

==================================================
Send events to Meta Ads Manager
==================================================

.. include:: ../../amperity_operator/source/events_meta_ads_manager.rst
   :start-after: .. events-meta-ads-manager-overview-start
   :end-before: .. events-meta-ads-manager-overview-end

.. include:: ../../amperity_operator/source/events_meta_ads_manager.rst
   :start-after: .. events-meta-ads-manager-overview-window-start
   :end-before: .. events-meta-ads-manager-overview-window-end

.. events-meta-ads-manager-allowfor-start

.. note:: Events are not immediately available in |destination-name|. Allow for up to 24 hours after the point at which Amperity has finished sending events for them to be available.

   Events that are sent to |destination-name| can be accessed from `Meta Events Manager <https://www.facebook.com/business/help/898185560232180?id=565900110447546>`__ |ext_link|.

.. events-meta-ads-manager-allowfor-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _events-meta-ads-manager-build-segment:

Build a query
==================================================

.. include:: ../../amperity_operator/source/events_meta_ads_manager.rst
   :start-after: .. events-meta-ads-manager-offline-events-build-query-start
   :end-before: .. events-meta-ads-manager-offline-events-build-query-end

**Multiple event types in the same query**

.. include:: ../../amperity_operator/source/events_meta_ads_manager.rst
   :start-after: .. events-meta-ads-manager-offline-events-build-query-variations-start
   :end-before: .. events-meta-ads-manager-offline-events-build-query-variations-end

.. events-meta-ads-manager-offline-events-parameters-start

Review the :ref:`Conversions API parameters <events-meta-ads-manager-conversions>` section for detailed information about the columns that should be returned by your query.

.. events-meta-ads-manager-offline-events-parameters-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end

.. _events-meta-ads-manager-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. admonition:: What is a dataset ID?

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-meta-ads-manager-dataset-id-start
      :end-before: .. setting-meta-ads-manager-dataset-id-end

   A dataset ID may need to be configured for the orchestration.

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _events-meta-ads-manager-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _events-meta-ads-manager-conversions:

Conversions API parameters
==================================================

.. include:: ../../amperity_operator/source/events_meta_ads_manager.rst
   :start-after: .. events-meta-ads-manager-conversion-api-parameters-start
   :end-before: .. events-meta-ads-manager-conversion-api-parameters-end
