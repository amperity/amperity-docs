.. https://docs.amperity.com/user/


.. |destination-name| replace:: Walmart DSP
.. |what-send| replace:: email addresses or UID2 tokens
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses or UID2 tokens. There are no optional fields.
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Walmart DSP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Walmart DSP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Walmart DSP

==================================================
Send audiences to Walmart DSP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-walmart-connect-start
   :end-before: .. term-walmart-connect-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../amperity_operator/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-whatis-20-start
   :end-before: .. destination-the-trade-desk-whatis-20-end

.. include:: ../../amperity_operator/source/destination_the_trade_desk.rst
   :start-after: .. destination-the-trade-desk-api-note-start
   :end-before: .. destination-the-trade-desk-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. caution:: This destination is available for sending campaign audiences to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending campaign audiences to |destination-name|.


.. _channel-walmart-dsp-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. _attributes:

.. admonition:: Which attributes should you use?

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

   Your brand should only send custom audiences that contain customers who reside within the United States.


.. _channel-walmart-dsp-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Walmart DSP to a campaign**

.. channel-walmart-dsp-build-campaign-steps-start

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

       .. image:: ../../images/mockup-campaigns-destination-walmart-dsp.png
          :width: 500 px
          :alt: Add a destination for Walmart DSP.
          :align: left
          :class: no-scaled-link

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

       .. image:: ../../images/mockup-campaigns-attributes-tdd.png
          :width: 500 px
          :alt: Edit the attributes for Walmart DSP.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end

.. channel-walmart-dsp-build-campaign-steps-end


.. _channel-walmart-dsp-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-walmart-dsp-configure-default-attributes-start

|destination-name| has the following requirements:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

   * - uid2

       You may use **uid2** as a source attribute when Amperity is configured as a `UID2 Operator <https://docs.amperity.com/reference/uid2.html>`__ |ext_link| for your brand.

     - uid2


.. channel-walmart-dsp-configure-default-attributes-end
