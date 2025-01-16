.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: SFTP
.. |what-send| replace:: email address, phone numbers, and other profile attributes
.. |what-enable| replace:: **email**, **phone**, and other profile attributes
.. |attributes-sent| replace:: You must select the set of attributes that are sent to |destination-name|. Review your downstream requirements, open the **Edits attributes** page, and then select the attributes you want to send to |destination-name| for this campaign.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to any SFTP site.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to any SFTP site.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to any SFTP site

==================================================
Send audiences to any SFTP site
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sftp-start
   :end-before: .. term-sftp-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end


.. _channel-sftp-build-segment:

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


.. _channel-sftp-build-campaign:

Build a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-important-filedrop-start
   :end-before: .. channels-build-campaign-important-filedrop-end

**To build a campaign**

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

       .. image:: ../../images/mockup-campaigns-name-generic.png
          :width: 250 px
          :alt: Open the campaign builder and give your campaign a name.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-good-names-start
          :end-before: .. channels-build-campaign-steps-good-names-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-audience-start
          :end-before: .. channels-build-campaign-steps-audience-end

       .. image:: ../../images/mockup-campaigns-select-audience-from-segment-generic.png
          :width: 500 px
          :alt: Choose the audience to use with your campaign.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-audience-tip-start
          :end-before: .. channels-build-campaign-steps-audience-tip-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-exclusions-start
          :end-before: .. channels-build-campaign-steps-exclusions-end

       .. image:: ../../images/mockup-campaigns-select-exclusions-from-segment-generic.png
          :width: 500 px
          :alt: Exclude some customers from this campaign.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-subaudiences-start
          :end-before: .. channels-build-campaign-steps-subaudiences-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 4.
          :align: left
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


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-timing-start
          :end-before: .. channels-build-campaign-steps-timing-end


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step 8.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-launch-date-start
          :end-before: .. channels-build-campaign-steps-launch-date-end


   * - .. image:: ../../images/steps-09.png
          :width: 60 px
          :alt: Step 9.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-schedule-start
          :end-before: .. channels-build-campaign-steps-schedule-end


.. _channel-sftp-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-sftp-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - amperity_id
     - amperity_id

   * - email
     - email

   * - given_name
     - given_name

   * - surname
     - surname

   * - address
     - address

   * - address2
     - address2

   * - state
     - state

   * - city
     - city

   * - postal
     - postal

   * - country
     - country

.. channel-sftp-configure-default-attributes-end
