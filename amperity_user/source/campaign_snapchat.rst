.. https://docs.amperity.com/user/


.. |destination-name| replace:: Snapchat
.. |what-send| replace:: email addresses, phone numbers, and mobile advertiser IDs
.. |what-enable| replace:: **email**, **phone**, or **mobile-id**
.. |attributes-sent| replace:: |destination-name| requires email addresses and phone numbers. You may also associate fields to mobile advertising IDs.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Snapchat.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Snapchat.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Snapchat

==================================================
Send audiences to Snapchat
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-snapchat-start
   :end-before: .. term-snapchat-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

.. channel-snapchat-build-segment-note-start

.. admonition:: Notes about sending data to Snapchat

   #. Snapchat allows the following fields: **email**, **mobile_id**, and **phone**.
   #. You may send only one of only one **email**, **mobile_id**, or **phone**. 
   #. Amperity ensure that fields are mapped correctly to the schema types required by Snapchat.
   #. Amperity applies SHA-256 hashing automatically.
   #. Audience targeting in Snapchat requires at least 1000 unique customers. Be sure your segment returns at least 1000 customers.

.. channel-snapchat-build-segment-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-snapchat-build-segment:

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


.. _channel-snapchat-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-snapchat-build-campaign-start

.. caution:: You must manually select the **mobile_id** field and the table in which it is located from the **Edit Attributes** pane. This field is not typically located in the **Merged Customers** table.

.. channel-snapchat-build-campaign-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add Snapchat to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-snapchat.png
          :width: 500 px
          :alt: Add a destination for Snapchat.
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

       .. image:: ../../images/mockup-campaigns-attributes-snapchat.png
          :width: 500 px
          :alt: Edit the attributes for Snapchat Ads.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end



.. _channel-snapchat-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-snapchat-configure-default-attributes-start

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

.. channel-snapchat-configure-default-attributes-end
