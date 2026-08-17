.. https://docs.amperity.com/operator/


.. |source-name| replace:: SevenRooms
.. |plugin-name| replace:: SevenRooms
.. |credential-type| replace:: **sevenrooms**
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: guest profiles, reservations, venues, and charges
.. |credential-fields| replace:: the name of the credential, a description, and the |source-name| Client ID and Client Secret


.. meta::
    :description lang=en:
        Configure Amperity to pull data from SevenRooms.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from SevenRooms.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from SevenRooms

==================================================
Pull from SevenRooms
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sevenrooms-start
   :end-before: .. term-sevenrooms-end

.. source-sevenrooms-context-start

|source-name| can send |what-pull| to Amperity. Choose which data streams to pull: **clients** (guest profiles) and **venues** are pulled as full exports, while **reservations** and **charges** are pulled incrementally based on the courier's date range. Amperity creates a feed and domain table for each data stream you select.

.. source-sevenrooms-context-end

.. source-sevenrooms-beta-start

.. admonition:: Beta

   The |source-name| source connector is currently in beta. Contact your Amperity representative to learn more.

.. source-sevenrooms-beta-end

.. source-sevenrooms-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-sevenrooms-get-details>`
#. :ref:`Add courier <source-sevenrooms-add-courier>`
#. :ref:`Run courier <source-sevenrooms-run-courier>`
#. :ref:`Review feed and domain table <source-sevenrooms-review-data>`
#. :ref:`Add to courier group <source-sevenrooms-add-to-courier-group>`

.. source-sevenrooms-steps-to-pull-end


.. _source-sevenrooms-get-details:

Get details
==================================================

.. source-sevenrooms-get-details-start

|source-name| requires the following configuration details:

#. The **Client ID** and **Client Secret** for your |source-name| API credentials.

   .. include:: ../../shared/credentials_settings.rst
      :start-after: .. credential-sevenrooms-find-credentials-start
      :end-before: .. credential-sevenrooms-find-credentials-end

#. The **Base URL** for the |source-name| API, including the version path. For example: ``https://demo.sevenrooms.com/api-ext/2_2``. Your production base URL differs from the demo URL.

#. The **Venue Group ID** for your |source-name| account. This scopes the data that Amperity pulls.

#. The **Data types** to pull. Select any combination of **clients**, **reservations**, **venues**, and **charges**.

.. tip:: Use |ext_snappass| to securely share configuration details for |source-name| between your company and your Amperity representative.

.. source-sevenrooms-get-details-end


.. _source-sevenrooms-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

**To add a courier**

.. source-sevenrooms-add-courier-start

#. From the **Sources** page, click **Add Courier**. The **Add Courier** page opens.
#. Find, and then click the icon for |plugin-name|. The **Add Courier** page opens.
#. Enter the name of the courier. For example: "|source-name|".

   From the **Credential** field, select an existing credential or select **Create a new credential**.

   To add a credential, enter |credential-fields|. Click **Save**.

   When finished click **Continue**.

#. Enter the **Base URL** and **Venue Group ID** for your |source-name| account.
#. Under **Data types**, select the data streams to pull: **clients**, **reservations**, **venues**, and **charges**.
#. Click **Create**.

   Amperity creates a feed and domain table for each selected data type.

.. source-sevenrooms-add-courier-end


.. _source-sevenrooms-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-sevenrooms-review-data:

Review feed and domain table
==================================================

.. source-sevenrooms-review-data-start

After running the |source-name| courier, Amperity creates a feed and domain table for each data type you selected: **clients**, **reservations**, **venues**, and **charges**. You may apply semantic tags to the fields in these tables and you may make each domain table available to Stitch, depending on your use case.

.. source-sevenrooms-review-data-end


.. _source-sevenrooms-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
