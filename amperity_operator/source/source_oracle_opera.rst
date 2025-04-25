.. https://docs.amperity.com/operator/


.. |source-name| replace:: Oracle OPERA
.. |plugin-name| replace:: Oracle OPERA
.. |feed-name| replace:: Oracle OPERA
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |credential-type| replace:: **oracle-opera**
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: profile and events data
.. |credential-fields| replace:: the name of the credential, a description, the |source-name| API key
.. |box-names| replace:: Email Metrics


.. meta::
    :description lang=en:
        Configure Oracle OPERA to push data to Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Oracle OPERA to push data to Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Push data to Amperity from Oracle OPERA

==================================================
Push data to Amperity from Oracle OPERA
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-opera-start
   :end-before: .. term-oracle-opera-end

.. source-oracle-opera-context-start

Your brand can configure |source-name| to push profile and reservation events data to a websocket using the `OPERA Cloud Streaming API <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_streaming_api.htm>`__ |ext_link|, from which Amperity will pull events data.

.. note:: This connector requires configuration steps to be completed in |source-name| first, and then within Amperity. Enable the profiles and events stream in |source-name| *only after* the courier is configured in Amperity.

.. important:: Configure only one courier in Amperity for |source-name|. Each time the courier runs it pulls all of the data that is available *at that time* to Amperity. This courier should be configured to run at least one time per week to avoid data loss. Depending on the volume of data that is pushed to Amperity, this courier may need to be configured to run more frequently, such as daily, every six hours, or some other frequency that is required to support your brand's use cases and to prevent loss of streamed events data.

.. source-oracle-opera-context-end

.. source-oracle-opera-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-oracle-opera-get-details>`
#. :ref:`Configure Oracle OPERA to stream profile and reservation events <source-oracle-opera-configure>`
#. :ref:`Add courier <source-oracle-opera-add-courier>`
#. :ref:`Enable streaming from Oracle OPERA <source-oracle-opera-enable-streaming>`
#. :ref:`Run courier <source-oracle-opera-run-courier>`
#. :ref:`Add to courier group <source-oracle-opera-add-to-courier-group>`

.. source-oracle-opera-steps-to-pull-end


.. _source-oracle-opera-get-details:

Get details
==================================================

.. source-oracle-opera-get-details-start

|source-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - **Configure environment and application, get Oracle OPERA config settings**

       Do the following steps in |source-name| before configuring Amperity:

       #. `Create an environment in Oracle OPERA <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_adding_an_environment.htm>`__ |ext_link|. After the environment is created, get the enterprise ID and chain code for that environment.

          .. caution:: Do not enable streaming in the |source-name| environment until **after** the courier that will pull streamed data to Amperity has been configured.

       #. Get the `client ID, client secret, and gateway URL <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_viewing_environment_details_ssd.htm>`__ |ext_link| for |source-name|

       #. `Register an application <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_registering_an_application.htm>`__ |ext_link|. After the application is registered, `get the application key <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_view_application_key.htm>`__ |ext_link| for that application.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - **Configure Amperity**

       :ref:`Configure a courier <source-oracle-opera-add-courier>` for streaming events using the configuration settings from |source-name|.

       Use the **Client ID** and **Client secret** to configure credentials.

       Use the **Gateway URL**, **Application key**, **Enterprise ID**, and **Chain code** to configure the courier.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail three.
          :align: left
          :class: no-scaled-link
     - **Configure business events for streaming, enable stream**

       Configure the environment to stream individual datasets for the following business event types:

       #. Configure profile events.

          Review the list of `profile events <https://docs.oracle.com/en/industries/hospitality/opera-cloud/22.5/ocsuh/t_admin_interfaces_configuring_business_events.htm#BusinessEvents-Profile-D539AA2F>`__ |ext_link| that are available from |source-name|.

          .. tip:: Profile events contain the following datasets: delete history, delete profile, delete relationship, new history, new profile, new relationship, purge profile, subscribed profile, update history, update profile, and update relationship.

       #. Configure reservation events.

          Review the list of `reservation events <https://docs.oracle.com/en/industries/hospitality/opera-cloud/22.5/ocsuh/t_admin_interfaces_configuring_business_events.htm#BusinessEvents-Reservation-D5B52CB2>`__ |ext_link| that are available from |source-name|.

          .. tip:: Reservation events contain the following datasets: advance check-in, cancel, check-in, check-out, close guest folio, delete reservation, delete routing, delete guest message, delete trace, join guest, new reservation, new guest message, new routing, new trace, no-show, reactivate no-show, reactivate waitlist, reverse advance check-in, reverse check-in, reverse check-out, rollback cancel, separate guest from share, turnaway, update certificate, update reservation, update routing, update guest message, and update trace.

       #. `Enable streaming in the environment <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_customer_enabling_streaming.htm>`__ |ext_link| that was created in |source-name|.

          .. note:: Business events have three layers:

             #. Module
             #. Action type
             #. Elements

             For example, within |source-name| Profile events is the module, "new profile" is the dataset, and elements represents each field in the dataset.

       #. Run the Amperity courier manually, and then verify that streamed data is available in Amperity.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail four.
          :align: left
          :class: no-scaled-link
     - |source-name| makes streamed data available from the `Streaming API <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_streaming_api.htm>`__ |ext_link|.

       .. important:: Configure only one courier in Amperity for |source-name|. Each time the courier runs it pulls all of the data that is available *at that time* to Amperity. This courier should be configured to run at least one time per week to avoid data loss. Depending on the volume of data that is pushed to Amperity, this courier may need to be configured to run more frequently, such as daily, every six hours, or some other frequency that is required to support your brand's use cases and to prevent loss of streamed events data.


.. tip:: Use SnapPass to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-oracle-opera-get-details-end


.. _source-oracle-opera-configure:

Configure Oracle OPERA
==================================================

.. source-oracle-opera-configure-start

The following steps must be completed in |source-name| before you can configure Amperity:

#. `Create an environment in Oracle OPERA <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_adding_an_environment.htm>`__ |ext_link|. After the environment is created, get the enterprise ID and chain code for that environment.

   .. caution:: Do not enable streaming in the |source-name| environment until **after** the courier that will pull streamed data to Amperity has been configured.

#. Get the `client ID, client secret, and gateway URL <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_viewing_environment_details_ssd.htm>`__ |ext_link| for |source-name|

#. `Register an application <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_registering_an_application.htm>`__. After the application is registered, `get the application key <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/t_view_application_key.htm>`__ |ext_link| for that application.

.. source-oracle-opera-configure-end


.. _source-oracle-opera-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. source-oracle-opera-add-courier-important-start

.. important:: Configure only one courier in Amperity for |source-name|. Each time the courier runs it pulls all of the data that is available *at that time* to Amperity. This courier should be configured to run at least one time per week to avoid data loss. Depending on the volume of data that is pushed to Amperity, this courier may need to be configured to run more frequently, such as daily, every six hours, or some other frequency that is required to support your brand's use cases and to prevent loss of streamed events data.

.. source-oracle-opera-add-courier-important-end

**To add a courier**

.. source-oracle-opera-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Source** page opens.
#. Find, and then click the icon for |source-name|. The **Add Courier** page opens.

   This automatically selects |credential-type| as the **Credential Type**.

#. From the **Credential** dropdown, select **Create a new credential**. Configure the credential using the **Client ID** and **Client secret**.

#. Under **Oracle Opera Settings** configure the **Gateway URL**, **Application key**, **Enterprise ID**, and **Chain code**.

   .. note:: The combination of gateway URL, application key, and chain code uniquely identifies a stream.

#. Under **Oracle Opera Settings** configure the load operations to pull each of the business events datasets that were made available. For example:

   .. code-block:: none

      {
        "FEED-ID": [
          {
            "type": "load",
            "file": "join-guest-data"
          }
        ],
        "FEED-ID": [
          {
            "type": "load",
            "file": "update-history-data"
          }
        ],
        ...
        "FEED-ID": [
          {
            "type": "load",
            "file": "check-in-data"
          }
        ],
        "FEED-ID": [
          {
            "type": "load",
            "file": "delete-guest-message-data"
          }
        ]
      }

   .. important:: If the business events are changed in |source-name| you must configure a new courier. Feed configuration within Amperity can be edited, but if the list of business events that are made available from the |source-name| change a new courier must be configured.

#. Click **Save**.

.. source-oracle-opera-add-courier-end


.. _source-oracle-opera-enable-streaming:

Enable streaming from Oracle OPERA
==================================================

.. source-oracle-opera-enable-streaming-start

Configure the |source-name| environment to stream individual datasets for the following business event types:

**Profile events**
   Review the list of `profile events <https://docs.oracle.com/en/industries/hospitality/opera-cloud/22.5/ocsuh/t_admin_interfaces_configuring_business_events.htm#BusinessEvents-Profile-D539AA2F>`__ |ext_link| that are available from |source-name|.

   .. tip:: Profile events contain the following datasets: delete history, delete profile, delete relationship, new history, new profile, new relationship, purge profile, subscribed profile, update history, update profile, and update relationship.

**Reservation events**
   Review the list of `reservation events <https://docs.oracle.com/en/industries/hospitality/opera-cloud/22.5/ocsuh/t_admin_interfaces_configuring_business_events.htm#BusinessEvents-Reservation-D5B52CB2>`__ |ext_link| that are available from |source-name|.

   .. tip:: Reservation events contain the following datasets: advance check-in, cancel, check-in, check-out, close guest folio, delete reservation, delete routing, delete guest message, delete trace, join guest, new reservation, new guest message, new routing, new trace, no-show, reactivate no-show, reactivate waitlist, reverse advance check-in, reverse check-in, reverse check-out, rollback cancel, separate guest from share, turnaway, update certificate, update reservation, update routing, update guest message, and update trace.

When finished `enable streaming in the environment <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_customer_enabling_streaming.htm>`__ |ext_link| that was created in |source-name|, after which you can :ref:`run the Amperity courier manually <source-oracle-opera-run-courier>` and verify that streamed data is available in Amperity.

.. source-oracle-opera-enable-streaming-end


.. _source-oracle-opera-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-oracle-opera-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
