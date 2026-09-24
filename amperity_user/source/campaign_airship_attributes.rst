.. https://docs.amperity.com/user/


.. |destination-name| replace:: Airship Attributes
.. |what-send| replace:: attributes
.. |attributes-sent| replace:: The attributes sent are the airship_identifier column and every additional column in the audience, which Airship applies as an attribute. Each additional column must match an existing attribute in your Airship project.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Airship Attributes.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Airship Attributes.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Airship Attributes

==================================================
Send audiences to Airship Attributes
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-airship-attributes-start
   :end-before: .. term-airship-attributes-end

.. include:: ../../amperity_operator/source/destination_airship_attributes.rst
   :start-after: .. destination-airship-attributes-api-note-start
   :end-before: .. destination-airship-attributes-api-note-end

.. include:: ../../amperity_operator/source/destination_airship_attributes.rst
   :start-after: .. destination-airship-attributes-beta-start
   :end-before: .. destination-airship-attributes-beta-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end

.. _channel-airship-attributes-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. admonition:: About segments that use the sub-audience editor

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _channel-airship-attributes-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-airship-attributes-build-campaign-steps-start

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

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end

.. channel-airship-attributes-build-campaign-steps-end


.. _channel-airship-attributes-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-airship-attributes-configure-default-attributes-start

|destination-name| requires the **airship_identifier** field. Every other field is sent as an Airship attribute and must exactly match the ID of an attribute that already exists in your Airship project.

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Source attribute
     - Required?
     - Destination attribute
   * - **airship_identifier**
     - Yes
     - The identifier Airship matches the row against. Its contents must match the **Identifier type** configured on the destination: a named user ID, a channel ID, or an email address. Rows with a blank value are dropped and counted as failed.
   * - Additional attributes
     - No
     - Each additional field is sent as an Airship attribute, matched to the attribute in your Airship project whose ID is exactly the field name. Values are sent as they appear in Amperity.

.. channel-airship-attributes-configure-default-attributes-end
