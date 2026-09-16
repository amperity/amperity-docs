.. https://docs.amperity.com/user/


.. |destination-name| replace:: SAP Emarsys
.. |destination-api| replace:: SAP Emarsys REST API
.. |plugin-name| replace:: emarsys
.. |attributes-sent| replace:: **email** or **phone**, along with optional profile and custom attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to SAP Emarsys.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to SAP Emarsys.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to SAP Emarsys

==================================================
Send audiences to SAP Emarsys
==================================================

.. include:: ../../amperity_operator/source/destination_sap_emarsys.rst
   :start-after: .. destination-sap-emarsys-about-start
   :end-before: .. destination-sap-emarsys-about-end

.. include:: ../../amperity_operator/source/destination_sap_emarsys.rst
   :start-after: .. destination-sap-emarsys-configure-start
   :end-before: .. destination-sap-emarsys-configure-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-sap-emarsys-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end


.. _attributes:

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-sap-emarsys-attributes-and-fields-start
   :end-before: .. setting-sap-emarsys-attributes-and-fields-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-sap-emarsys-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add SAP Emarsys to a campaign**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-note-start
          :end-before: .. channels-build-campaign-steps-destinations-note-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. image:: ../../images/mockup-campaigns-attributes-email.png
          :width: 500 px
          :alt: Edit the attributes for SAP Emarsys.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end


.. _channel-sap-emarsys-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-sap-emarsys-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email
   * - phone
     - phone

.. channel-sap-emarsys-configure-default-attributes-end
