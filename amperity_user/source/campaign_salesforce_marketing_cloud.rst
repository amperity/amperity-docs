.. https://docs.amperity.com/user/


.. |destination-name| replace:: Salesforce Marketing Cloud
.. |what-send| replace:: contact data
.. |what-enable| replace:: **amperity_id**, **email**, **first_name**, and **last_name**
.. |attributes-sent| replace:: |destination-name| allows a long list of (optional) attributes.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Salesforce Marketing Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Salesforce Marketing Cloud

==================================================
Send audiences to Salesforce Marketing Cloud
==================================================

.. channel-salesforce-marketing-cloud-start

You can build queries that return |what-send|, and then use orchestrations to send those results to business units in |destination-name|. The |what-send| is uploaded to |destination-name| using SFTP, after which the Marketing Cloud SOAP API manages your data extensions and will move the |what-send| into the correct data extension automatically.

.. channel-salesforce-marketing-cloud-end

.. image:: ../../images/channel-salesforce-marketing-cloud.png
   :width: 600 px
   :alt: Send contact data from Amperity to Salesforce Marketing Cloud.
   :align: left
   :class: no-scaled-link

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. caution:: This destination is available for sending campaign audiences to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending campaign audiences to |destination-name|.


.. _channel-sfmc-build-segment:

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


.. _channel-sfmc-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Salesforce Marketing Cloud to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-sfmc.png
          :width: 500 px
          :alt: Add a destination for Salesforce Marketing Cloud.
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

       .. image:: ../../images/mockup-campaigns-attributes-sfmc.png
          :width: 500 px
          :alt: Edit the attributes for Salesforce Marketing Cloud.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end



