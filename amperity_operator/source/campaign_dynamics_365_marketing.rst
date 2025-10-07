.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Dynamics 365 Marketing
.. |plugin-name| replace:: "Dynamics 365 Marketing"
.. |credential-type| replace:: "dynamics-365-marketing"
.. |required-credentials| replace:: "Azure tenant ID", "Azure client ID", and "Azure client secret"
.. |what-send| replace:: static segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "micro"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to Dynamics 365 Marketing.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to Dynamics 365 Marketing.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for Dynamics 365 Marketing

==================================================
Configure campaigns for Dynamics 365 Marketing
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dynamics-365-marketing-start
   :end-before: .. term-dynamics-365-marketing-end

.. campaign-dynamics-365-marketing-context-start

Send static segments to Dynamics 365 Marketing from Amperity, and then manage collections of contacts. Build customer journeys using any combination of contacts -- all contacts, by demographic, by behavior, by firmographic, or by other considerations -- to narrow your segments down to the right audience for your marketing campaign.

.. campaign-dynamics-365-marketing-context-end

.. campaign-dynamics-365-marketing-admonition-start

.. admonition:: What is a static segment in Dynamics 365 Marketing?

   A static segment represents a static list of customers who are selected on a per-contact basis rather than created logically based on field values.
   
   Static segments are added, and then submitted to the marketing-insights services each time they are loaded to |destination-name|, after which they are reevaluated by |destination-name|. Customers in a static segment are available from the **Members** tab in the |destination-name| user interface.

.. campaign-dynamics-365-marketing-admonition-end

.. campaign-dynamics-365-marketing-api-note-start

.. note:: This destination uses the `Microsoft Dynamics Segmentation API <https://learn.microsoft.com/en-us/dynamics365/marketing/developer/extend-segments>`__ |ext_link| to send static segments to |destination-name|. If the static segment does not exist, it will be created. If the static segment does exist, it is truncated, and then loaded.

.. campaign-dynamics-365-marketing-api-note-end


.. _campaign-microsoft-dynamics-365-marketing-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-microsoft-dynamics-365-marketing-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Azure tenant ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dynamics-365-marketing-azure-tenant-id-start
             :end-before: .. credential-microsoft-dynamics-365-marketing-azure-tenant-id-end

       **Azure client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-start
             :end-before: .. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Power Apps environment region**

          .. include:: ../../shared/destination_settings.rst
             :start-after: setting-microsoft-dynamics-365-environment-region-start
             :end-before: setting-microsoft-dynamics-365-environment-region-end

       **Power Apps environment name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: setting-microsoft-dynamics-365-environment-name-start
             :end-before: setting-microsoft-dynamics-365-environment-name-end

       **Marketing segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: setting-microsoft-dynamics-365-segment-name-start
             :end-before: setting-microsoft-dynamics-365-segment-name-end

.. campaign-microsoft-dynamics-365-marketing-get-details-end


.. _campaign-microsoft-dynamics-365-marketing-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Microsoft Dynamics 365 Marketing**

.. campaign-microsoft-dynamics-365-marketing-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Azure tenant ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dynamics-365-marketing-azure-tenant-id-start
             :end-before: .. credential-microsoft-dynamics-365-marketing-azure-tenant-id-end

       **Azure client ID and client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-start
             :end-before: .. credential-microsoft-dynamics-365-marketing-azure-client-id-and-secret-end

.. campaign-microsoft-dynamics-365-marketing-credentials-steps-end


.. _campaign-microsoft-dynamics-365-marketing-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Microsoft Dynamics 365 Marketing**

.. campaign-microsoft-dynamics-365-marketing-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Power Apps environment region**

          .. include:: ../../shared/destination_settings.rst
             :start-after: setting-microsoft-dynamics-365-environment-region-start
             :end-before: setting-microsoft-dynamics-365-environment-region-end

       **Power Apps environment name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: setting-microsoft-dynamics-365-environment-name-start
             :end-before: setting-microsoft-dynamics-365-environment-name-end

       **Marketing segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: setting-microsoft-dynamics-365-segment-name-start
             :end-before: setting-microsoft-dynamics-365-segment-name-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-orchestration-only-start
          :end-before: .. campaigns-steps-business-users-orchestration-only-end

.. campaign-microsoft-dynamics-365-marketing-add-steps-end


.. _campaign-dynamics-365-marketing-build-query:

Build query
==================================================

.. campaign-dynamics-365-marketing-build-query-start

You need to build a query that outputs fields that can be mapped to static segments in |destination-name|.

.. important:: Query results **must** include the **contactid** field, which is the same as the **contactid** field for Microsoft Dynamics 365 CRM Contact.

.. campaign-dynamics-365-marketing-build-query-end


.. TODO: Add workflow resolutions from existing topics HERE.
