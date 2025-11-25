.. https://docs.amperity.com/user/


.. |destination-name| replace:: LiveRamp
.. |what-send| replace:: email address, phone numbers, and other profile attributes
.. |what-enable| replace:: **email**, **phone**, and other profile attributes
.. |attributes-sent| replace:: You must select the set of attributes that are sent to |destination-name|. Review your downstream requirements, open the **Edits attributes** page, and then select the attributes you want to send to |destination-name| for this campaign.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to LiveRamp.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to LiveRamp.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to LiveRamp

==================================================
Send audiences to LiveRamp
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-liveramp-start
   :end-before: .. term-liveramp-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-liveramp-build-segment:

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


.. _channel-liveramp-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. include:: ../../amperity_user/source/destination_liveramp.rst
   :start-after: .. sendto-liveramp-start
   :end-before: .. sendto-liveramp-end

.. important:: `LiveRamp terms of service restrict PII data <https://docs.liveramp.com/connect/en/liveramp-data-restrictions.html>`__ |ext_link| -- government-issued identification numbers (like social security numbers), financial and customer account numbers, birthdates, gender, email addresses, names (first, last, and full), and similar data -- should be excluded from campaigns that are sent to |destination-name|.

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-important-filedrop-start
   :end-before: .. channels-build-campaign-important-filedrop-end

**To add LiveRamp to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-liveramp.png
          :width: 500 px
          :alt: Add a destination for LiveRamp.
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

       .. image:: ../../images/mockup-campaigns-attributes-files.png
          :width: 500 px
          :alt: Edit the attributes for campaigns that are sent to SFTP sites.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end


