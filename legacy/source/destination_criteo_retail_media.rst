.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Criteo Retail Media
.. |plugin-name| replace:: "Criteo Retail Media"
.. |credential-type| replace:: "criteo-retail-media"
.. |required-credentials| replace:: "API key" and "URL"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |audience-primary-key| replace:: "email"
.. |filter-the-list| replace:: "crit"
.. |sendto-link| replace:: send query results
.. |channel-link| replace:: send campaigns


====================================================
Configure campaigns for Criteo Retail Media
====================================================

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_criteo_retail_media.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-criteo-retail-media-start
   :end-before: .. term-criteo-retail-media-end


.. _destination-criteo-retail-media-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-criteo-retail-media-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Use OAuth to connect Amperity to Criteo Retail Media**

       A refresh token that is generated by the OAuth process that authorizes Amperity to send data to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       **Account ID**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-account-id-start
             :end-before: .. setting-criteo-account-id-end

       **Retailer ID**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-retailer-id-start
             :end-before: .. setting-criteo-retailer-id-end

       **Identifier type**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-identifier-type-start
             :end-before: .. setting-criteo-identifier-type-end

.. destination-criteo-retail-media-get-details-table-end


.. _destination-criteo-retail-media-credentials:

Use OAuth
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oauth-start
   :end-before: .. term-oauth-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-intro-start
   :end-before: .. destinations-oauth-intro-end

.. important:: OAuth for "Criteo Retail Media" *must* be completed within Criteo prior to configuring OAuth in Amperity.

**To configure OAuth**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-1-start
          :end-before: .. destinations-oauth-configure-step-1-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-2-start
          :end-before: .. destinations-oauth-configure-step-2-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-oauth-configure-step-3-start
          :end-before: .. destinations-oauth-configure-step-3-end


.. _destination-criteo-retail-media-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Criteo Retail Media**

.. destination-criteo-retail-media-add-steps-start

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

       .. image:: ../../images/mockup-destinations-add-01-select-destination-criteo-retail-media.png
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

          #. .. include:: ../../shared/destination_settings.rst
                :start-after: .. setting-common-business-user-access-allow-start
                :end-before: .. setting-common-business-user-access-allow-end

          #. .. include:: ../../shared/destination_settings.rst
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

       **Account ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-account-id-start
             :end-before: .. setting-criteo-account-id-end

       **Retailer ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-retailer-id-start
             :end-before: .. setting-criteo-retailer-id-end

       **Identifier type**
          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-criteo-identifier-type-start
             :end-before: .. setting-criteo-identifier-type-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-criteo-retail-media-add-steps-end
