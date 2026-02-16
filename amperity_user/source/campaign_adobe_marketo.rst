.. https://docs.amperity.com/user/


.. |destination-name| replace:: Adobe Marketo
.. |what-send| replace:: static audience lists
.. |what-enable| replace:: email (required), along with any combination of first name, last name, phone, and company
.. |attributes-sent| replace:: |destination-name| requires email addresses. You may also select any combination of phone number, first name, last name, and company attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Adobe Marketo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Adobe Marketo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Adobe Marketo

==================================================
Send audiences to Adobe Marketo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-marketo-start
   :end-before: .. term-adobe-marketo-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. note::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-adobe-marketo-list-name-membership-start
      :end-before: .. setting-adobe-marketo-list-name-membership-end

.. channel-adobe-marketo-build-campaign-what-columns-start

.. important:: An email address must be sent to |destination-name|. You may also send first names, last names, company names, and phone numbers.

.. channel-adobe-marketo-build-campaign-what-columns-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-adobe-marketo-build-segment:

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

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-adobe-marketo-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Adobe Marketo to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-adobe-marketo.png
          :width: 500 px
          :alt: Add a destination for Adobe Marketo.
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

       .. image:: ../../images/mockup-campaigns-attributes-adobe-marketo.png
          :width: 500 px
          :alt: Edit the attributes for Adobe Marketo.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-adobe-marketo-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-adobe-marketo-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

   * - given_name
     - firstname

   * - surname
     - lastname

   * - phone
     - phone

   * - company
     - company

.. channel-adobe-marketo-configure-default-attributes-end
