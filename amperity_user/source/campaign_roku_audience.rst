.. https://docs.amperity.com/user/


.. |destination-name| replace:: Roku Audience
.. |what-send| replace:: audiences
.. |attributes-sent| replace:: email addresses, phone numbers, mobile advertiser IDs, and IP addresses


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Roku Audience.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Roku Audience.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Roku Audience

==================================================
Send audiences to Roku Audience
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-roku-audience-start
   :end-before: .. term-roku-audience-end

.. include:: ../../amperity_operator/source/destination_roku_audience.rst
   :start-after: .. destination-roku-audience-api-note-start
   :end-before: .. destination-roku-audience-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-roku-audience-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. admonition:: About segments that use the sub-audience editor

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-roku-audience-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-roku-audience-build-campaign-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
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
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end

.. channel-roku-audience-build-campaign-steps-end


.. _channel-roku-audience-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-roku-audience-configure-default-attributes-start

|destination-name| requires the **email** field. You can optionally include **phone**, **maid** (mobile advertiser ID), and **ip** fields to improve match rates.

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Source attribute
     - Required?
     - Destination attribute
   * - **email**
     - Yes
     - The email address for the customer. This field is required and is used as the primary match key.

       Amperity automatically hashes email addresses using SHA-256 before sending to Roku.
   * - **phone**
     - No
     - The phone number for the customer. Use this field to improve match rates.
   * - **maid**
     - No
     - The mobile advertiser ID for the customer. Map the **mobile_advertiser_id** field from your customer profile to this attribute to improve match rates.
   * - **ip**
     - No
     - The IP address for the customer. Use this field to improve match rates.

.. channel-roku-audience-configure-default-attributes-end
