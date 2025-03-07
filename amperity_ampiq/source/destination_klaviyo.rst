.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: Klaviyo
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email** and customer profile attributes
.. |attributes-sent| replace:: |destination-name| requires only email addresses. You may configure campaigns to send additional customer profile attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Klaviyo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Klaviyo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Klaviyo

==================================================
Send audiences to Klaviyo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-klaviyo-start
   :end-before: .. term-klaviyo-end

.. include:: ../../amperity_datagrid/source/destination_klaviyo.rst
   :start-after: .. destination-klaviyo-api-note-start
   :end-before: .. destination-klaviyo-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end


.. _channel-klaviyo-build-segment:

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


.. _channel-klaviyo-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Klaviyo to a campaign**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end

       .. image:: ../../images/mockup-campaigns-destination-klaviyo.png
          :width: 500 px
          :alt: Add a destination for Klaviyo.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-note-start
          :end-before: .. channels-build-campaign-steps-destinations-note-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. image:: ../../images/mockup-campaigns-attributes-klaviyo.png
          :width: 500 px
          :alt: Edit the attributes for Klaviyo.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-klaviyo-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-klaviyo-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

   * - Customer profile attributes
     - :ref:`Review the list of customer profile parameters <destination-klaviyo-customer-profile-parameters>` your brand can send to |destination-name|. These may be configured as default attributes in Amperity.

.. channel-klaviyo-configure-default-attributes-end


.. _destination-klaviyo-customer-profile-parameters:

Customer profile parameters
==================================================

.. include:: ../../amperity_datagrid/source/destination_klaviyo.rst
   :start-after: .. destination-klaviyo-customer-profile-parameters-start
   :end-before: .. destination-klaviyo-customer-profile-parameters-end
