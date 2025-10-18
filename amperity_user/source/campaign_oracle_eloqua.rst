.. https://docs.amperity.com/user/


.. |destination-name| replace:: Oracle Eloqua
.. |what-send| replace:: audiences
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires an email address. You may configure Amperity to send additional fields.
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 24 hours


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Oracle Eloqua.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Oracle Eloqua.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Oracle Eloqua

==================================================
Send audiences to Oracle Eloqua
==================================================

.. channel-oracle-eloqua-start

You can use segments and campaigns to manage shared lists in |destination-name|.

.. channel-oracle-eloqua-end

.. include:: ../../amperity_operator/source/destination_oracle_eloqua.rst
   :start-after: .. destination-oracle-eloqua-api-note-start
   :end-before: .. destination-oracle-eloqua-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-oracle-eloqua-build-segment:

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


.. _channel-oracle-eloqua-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Oracle Eloqua to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-oracle-eloqua.png
          :width: 500 px
          :alt: Add a destination for Oracle Eloqua.
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

       .. image:: ../../images/mockup-campaigns-attributes-oracle-eloqua.png
          :width: 500 px
          :alt: Edit the attributes for Oracle Eloqua.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-oracle-eloqua-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-oracle-eloqua-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - C_EmailAddress

.. channel-oracle-eloqua-configure-default-attributes-end
