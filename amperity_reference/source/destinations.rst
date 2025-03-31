.. https://docs.amperity.com/reference/

.. |destination-name| replace:: a destination
.. |plugin-name| replace:: the plugin for the destination
.. |filter-the-list| replace:: the first three characters of the destination

.. meta::
    :description lang=en:
        Destinations are connections between Amperity and downstream systems that enable users of Amperity to send data to those systems.

.. meta::
    :content class=swiftype name=body data-type=text:
        Destinations are connections between Amperity and downstream systems that enable users of Amperity to send data to those systems.

.. meta::
    :content class=swiftype name=title data-type=string:
        About destinations

==================================================
About destinations
==================================================

.. destinations-about-start

Destinations are connections between Amperity and downstream systems that enable users of Amperity to send data to those systems.

A destination is a connection between Amperity and a downstream system that enables users of Amperity to send data to that system.

After a destination is configured, users of Amperity can:

* Use orchestrations to send the results of any query to any configured destination.
* Use segments to define audiences, and then assign those segments to single-touch campaigns or to nodes in a journey. More than one destination can be configured for a campaign or for a node in a journey.

.. destinations-about-end


.. _destinations-add:

Add destinations
==================================================

.. destinations-add-start

To add destinations to your Amperity tenant, do the following:

#. :ref:`Get details <destinations-get-details>`
#. :ref:`Configure credentials <destinations-configure-credentials>`
#. :ref:`Add destination <destinations-add-destination>`

.. destinations-add-end


.. _destinations-get-details:

Get details
--------------------------------------------------

.. destinations-get-details-start

Each destination requires configuration, such as:

* Providing credentials that allow Amperity to access the downstream location
* Ensuring that certain fields are named in certain ways
* Configuring Amperity to send the correct file type for file-based destinations
* Configuring Amperity for audience identifiers, such as audience names, list IDs, or activation IDs

Configuration requirements are unique to each destination and use case. Review the "Get details" section for each destination that your brand wants to configure in Amperity. Review any links to external documentation to help ensure that your brand understands destination-specific requirements.

After a destination is configured, run a test using a small audience. Verify that the data has arrived correctly. Make adjustments, if necessary, before sending an audience that will be used with your brand's marketing activity.

.. destinations-get-details-end


.. _destinations-configure-credentials:

Configure credentials
--------------------------------------------------

.. destinations-configure-credentials-start

Use the **Credentials** page to view and manage credentials for data sources and destinations. After you have added a credential for a destination you can configure Amperity to send data to that destination.

.. destinations-configure-credentials-end


.. _destinations-add-destination:

Add destination
--------------------------------------------------

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. destinations-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

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
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       Settings are documented on the individual pages for each destination.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destinations-add-destination-steps-end

.. _destinations-premium-connectors:

Premium connectors
--------------------------------------------------

.. destinations-premium-connectors-start

The following set of connectors are designated as premium connectors. A monthly surcharge is incurred for any premium connectors used in that month.

* Amazon Ads
* Criteo Audience API
* Criteo Retail Audience API
* Facebook
* Google Ads
* Google Customer Match
* Google Enhanced Conversions
* LiveRamp
* Meta Ads Offline Events
* Microsoft Ads
* Microsoft Invest
* Neustar
* Pinterest
* Snapchat
* The Trade Desk
* The Trade Desk 3P Marketplace
* The Trade Desk Offline Events
* TikTok Ads
* TikTok Ads Offline Events
* Yahoo DSP

.. destinations-premium-connectors-end
