.. https://docs.amperity.com/user/


.. |destination-name| replace:: Listrak SMS
.. |what-send| replace:: SMS profiles
.. |what-enable| replace:: **phone**
.. |attributes-sent| replace:: |destination-name| requires phone numbers. You may include system and custom profile attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Listrak SMS.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Listrak SMS.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Listrak SMS

==================================================
Send audiences to Listrak SMS
==================================================

.. include:: ../../amperity_operator/source/destination_listrak_sms.rst
   :start-after: .. destination-listrak-sms-about-start
   :end-before: .. destination-listrak-sms-about-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-listrak-sms-optin-start
   :end-before: .. setting-listrak-sms-optin-end

.. include:: ../../amperity_operator/source/destination_listrak_sms.rst
   :start-after: .. destination-listrak-sms-context-start
   :end-before: .. destination-listrak-sms-context-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-listrak-sms-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. _attributes:

.. channel-listrak-sms-configure-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Amperity attribute**
     - **Listrak profile field**

   * - phone
     - Phone

       Required. The primary identifier for each SMS profile

   * - email
     - Email Address

       A contact attribute.

   * - given_name
     - First Name

       Use for personalization.

   * - surname
     - Last Name

       Use for personalization.

   * - postal
     - Postal Code

       Use for location targeting.

   * - birthdate
     - Birthday

       Use for date-based segmentation.

   * - Custom attributes
     - Custom profile fields

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. setting-listrak-sms-enable-segmentation-caveat-start
          :end-before: .. setting-listrak-sms-enable-segmentation-caveat-end

.. channel-listrak-sms-configure-attributes-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-listrak-sms-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Listrak to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-listrak.png
          :width: 500 px
          :alt: Add a destination for Listrak.
          :align: left
          :class: no-scaled-link

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

       .. image:: ../../images/mockup-campaigns-attributes-listrak.png
          :width: 500 px
          :alt: Edit the attributes for Listrak.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end
