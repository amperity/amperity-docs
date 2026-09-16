.. https://docs.amperity.com/user/


.. |destination-name| replace:: SendGrid
.. |what-send| replace:: email lists
.. |what-enable| replace:: email marketing campaigns
.. |attributes-sent| replace:: email address


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to SendGrid.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to SendGrid.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to SendGrid

==================================================
Send audiences to SendGrid
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sendgrid-start
   :end-before: .. term-sendgrid-end

.. include:: ../../amperity_operator/source/destination_sendgrid.rst
   :start-after: .. destination-sendgrid-api-note-start
   :end-before: .. destination-sendgrid-api-note-end

.. channel-sendgrid-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. channel-sendgrid-beta-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-sendgrid-build-segment:

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


.. _channel-sendgrid-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-sendgrid-build-campaign-steps-start

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

.. channel-sendgrid-build-campaign-steps-end


.. _channel-sendgrid-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-sendgrid-configure-default-attributes-start

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Source attribute
     - Destination attribute
   * - **email**
     - **email**

       *Required*

       The email address for the contact.

.. channel-sendgrid-configure-default-attributes-end
