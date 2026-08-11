.. https://docs.amperity.com/user/


.. |destination-name| replace:: SevenRooms
.. |what-send| replace:: email addresses and profile attributes
.. |what-enable| replace:: guest tagging and segmentation
.. |attributes-sent| replace:: email address


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to SevenRooms.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to SevenRooms.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to SevenRooms

==================================================
Send audiences to SevenRooms
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sevenrooms-start
   :end-before: .. term-sevenrooms-end

.. include:: ../../amperity_operator/source/destination_sevenrooms.rst
   :start-after: .. destination-sevenrooms-api-note-start
   :end-before: .. destination-sevenrooms-api-note-end

.. channel-sevenrooms-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. channel-sevenrooms-beta-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-sevenrooms-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. admonition:: How do I send |attributes-sent| to |destination-name|?

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-sevenrooms-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-sevenrooms-build-campaign-steps-start

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

.. channel-sevenrooms-build-campaign-steps-end


.. _channel-sevenrooms-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-sevenrooms-configure-default-attributes-start

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Source attribute
     - Destination attribute
   * - **email**
     - **email**

       *Required*

       The email address used to match the guest profile in |destination-name|.
   * - **phone_number**
     - **phone_number**

       The phone number written to the matching guest profile.
   * - **first_name**
     - **first_name**

       The first name written to the matching guest profile.
   * - **last_name**
     - **last_name**

       The last name written to the matching guest profile.

.. channel-sevenrooms-configure-default-attributes-end
