.. https://docs.amperity.com/datagrid/


.. |destination-name| replace:: Dynamics 365 Marketing
.. |plugin-name| replace:: Dynamics 365 Marketing
.. |what-send| replace:: segments
.. |filter-the-list| replace:: "dyn"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: environment region and environment name settings were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: send query results to |destination-name|
.. |channel-link| replace:: send campaign results


.. meta::
    :description lang=en:
        Configure Amperity to send data to Dynamics 365 Marketing.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Dynamics 365 Marketing.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send segments to Dynamics 365 Marketing

==================================================
Send segments to Dynamics 365 Marketing
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-dynamics-365-marketing-start
   :end-before: .. term-dynamics-365-marketing-end

.. destination-dynamics-365-marketing-context-start

Send static segments to Dynamics 365 Marketing from Amperity, and then manage collections of contacts. Build customer journeys using any combination of contacts -- all contacts, by demographic, by behavior, by firmographic, or by other considerations -- to narrow your segments down to the right audience for your marketing campaign.

.. destination-dynamics-365-marketing-context-end

.. destination-dynamics-365-marketing-admonition-start

.. admonition:: What is a static segment in Dynamics 365 Marketing?

   A static segment represents a static list of customers who are selected on a per-contact basis rather than created logically based on field values.
   
   Static segments are added, and then submitted to the marketing-insights services each time they are loaded to |destination-name|, after which they are reevaluated by |destination-name|. Customers in a static segment are available from the **Members** tab in the |destination-name| user interface.

.. destination-dynamics-365-marketing-admonition-end

.. destination-dynamics-365-marketing-api-note-start

.. note:: This destination uses the |ext_microsoft_dynamics_web_api_segments| to send static segments to |destination-name|. If the static segment does not exist, it will be created. If the static segment does exist, it will be truncated, and then loaded.

.. destination-dynamics-365-marketing-api-note-end

.. destination-dynamics-365-marketing-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-dynamics-365-marketing-get-details>`
#. :ref:`Build a query <destination-dynamics-365-marketing-build-query>`
#. :ref:`Add destination <destination-dynamics-365-marketing-add-destination>`
#. :ref:`Add data template <destination-dynamics-365-marketing-add-data-template>`

.. destination-dynamics-365-marketing-steps-to-send-end


.. _destination-dynamics-365-marketing-get-details:

Get details
==================================================

.. destination-dynamics-365-marketing-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Microsoft Azure must be configured for your Power Apps application, after which your |destination-name| application must be added to the Microsoft Power Platform.

       You will need to provide your Azure Active Directory tenant ID, Azure client ID, and your Azure client secret.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The environment region and environment name |destination-name|. For example: "crm" (region) and "acme" (name).

.. destination-dynamics-365-marketing-get-details-end


.. _destination-dynamics-365-marketing-build-query:

Build query
==================================================

.. destination-dynamics-365-marketing-build-query-start

You will need to build a query that outputs fields that can be mapped to static segments in |destination-name|.

.. important:: Query results **must** include the **contactid** field, which is the same as the **contactid** field for Microsoft Dynamics 365 CRM Contact.

.. destination-dynamics-365-marketing-build-query-end


.. _destination-dynamics-365-marketing-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-dynamics-365-marketing-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       |destination-name| has the following settings:

       * Azure Active Directory tenant ID
       * Azure client ID
       * Azure client secret

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Dynamics 365 Marketing.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Environment region**
            - The environment region for your instance of |destination-name|. For example: "crm".

          * - **Environment name**
            - The environment name for your instance of |destination-name|. For example: "acme".


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-allow-start
          :end-before: .. destinations-business-users-allow-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-dynamics-365-marketing-add-destination-steps-end


.. _destination-dynamics-365-marketing-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-dynamics-365-marketing-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       .. image:: ../../images/mockup-data-template-tab-add-03-settings.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-queries-only-start
          :end-before: .. destinations-data-template-save-after-queries-only-end

.. destination-dynamics-365-marketing-add-data-template-steps-end
