.. https://docs.amperity.com/ampiq/


.. |destination-name| replace:: Amazon S3
.. |what-send| replace:: email address, phone numbers, and other profile attributes
.. |what-enable| replace:: **email**, **phone**, and other profile attributes
.. |attributes-sent| replace:: You must select the set of attributes that are sent to |destination-name|. Review your downstream requirements, open the **Edits attributes** page, and then select the attributes you want to send to |destination-name| for this campaign.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to any Amazon S3 bucket.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to any Amazon S3 bucket.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Amazon S3

==================================================
Send audiences to Amazon S3
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-s3-start
   :end-before: .. term-amazon-s3-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end


.. _channel-amazon-s3-build-segment:

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


.. _channel-amazon-s3-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Amazon S3 to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-amazon-s3.png
          :width: 500 px
          :alt: Add a destination for Amazon S3.
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

       .. image:: ../../images/mockup-campaigns-attributes-files.png
          :width: 500 px
          :alt: Edit the attributes for campaigns that are sent to Amazon S3.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-amazon-s3-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-amazon-s3-configure-default-attributes-start

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

.. channel-amazon-s3-configure-default-attributes-end
