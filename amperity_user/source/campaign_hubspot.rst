.. https://docs.amperity.com/user/


.. |destination-name| replace:: HubSpot
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses. There are no optional fields.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to HubSpot.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to HubSpot.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to HubSpot

==================================================
Send audiences to HubSpot
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-hubspot-start
   :end-before: .. term-hubspot-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../amperity_operator/source/destination_hubspot.rst
   :start-after: .. destination-hubspot-contain-only-numbers-letters-underscores-start
   :end-before: .. destination-hubspot-contain-only-numbers-letters-underscores-end

.. include:: ../../amperity_operator/source/destination_hubspot.rst
   :start-after: .. destination-hubspot-build-query-start
   :end-before: .. destination-hubspot-build-query-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-hubspot-build-segment:

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


.. _channel-hubspot-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add HubSpot to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-hubspot.png
          :width: 500 px
          :alt: Add a destination for HubSpot.
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

       .. image:: ../../images/mockup-campaigns-attributes-hubspot.png
          :width: 500 px
          :alt: Edit the attributes for HubSpot.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-hubspot-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-hubspot-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

.. channel-hubspot-configure-default-attributes-end
