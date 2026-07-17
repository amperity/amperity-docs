.. https://docs.amperity.com/user/


.. |destination-name| replace:: Bloomreach Engagement
.. |what-send| replace:: customer profiles
.. |what-enable| replace:: customer profiles to be sent
.. |attributes-sent| replace:: **email**, **cookie**, **google_analytics**, or **external_id**


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Bloomreach Engagement.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Bloomreach

==================================================
Send audiences to Bloomreach
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bloomreach-start
   :end-before: .. term-bloomreach-end

.. include:: ../../amperity_operator/source/destination_bloomreach.rst
   :start-after: .. destination-bloomreach-api-note-start
   :end-before: .. destination-bloomreach-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-bloomreach-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/channels.rst
      :start-after: .. channels-build-segment-context-start
      :end-before: .. channels-build-segment-context-end

.. channel-bloomreach-build-segment-important-start

.. important:: The segment you build must include an attribute named to match the **Bloomreach identifier** selected for the destination, such as email, external ID, cookie, or Google Analytics ID. If no attribute matches, the campaign fails with an error before any data is sent. All other attributes in your segment are sent as customer properties to |destination-name|. Rows with blank values in the identity column are skipped.

.. channel-bloomreach-build-segment-important-end

.. include:: ../../amperity_operator/source/destination_bloomreach.rst
   :start-after: .. destination-bloomreach-attribute-limit-start
   :end-before: .. destination-bloomreach-attribute-limit-end


.. _channel-bloomreach-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add a campaign for Bloomreach**

.. channel-bloomreach-build-campaign-steps-start

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

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end

.. channel-bloomreach-build-campaign-steps-end

.. include:: ../../amperity_operator/source/destination_bloomreach.rst
   :start-after: .. destination-bloomreach-async-start
   :end-before: .. destination-bloomreach-async-end


.. _channel-bloomreach-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-bloomreach-configure-default-attributes-table-start

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Source attribute
     - Destination attribute
   * - **email**
     - **email**

       The email address for the customer. This is a Bloomreach hard identifier.

   * - **external_id**
     - **external_id**

       An external identifier for the customer, such as the Amperity ID. This is a Bloomreach hard identifier.

   * - **cookie**
     - **cookie**

       A cookie identifier for the customer. This is a Bloomreach hard identifier.

   * - **google_analytics**
     - **google_analytics**

       A Google Analytics identifier for the customer. This is a Bloomreach hard identifier.

   * - **given_name**
     - **given_name**

       The first name of the customer.

   * - **surname**
     - **surname**

       The last name of the customer.

   * - **birthdate**
     - **birthdate**

       The birthdate of the customer.

   * - **city**
     - **city**

       The city in which the customer lives.

   * - **state**
     - **state**

       The state in which the customer lives.

   * - **postal**
     - **postal**

       The ZIP code or postal code for the customer.

   * - **phone**
     - **phone**

       The phone number for the customer.

   * - **gender**
     - **gender**

       The gender of the customer.

.. channel-bloomreach-configure-default-attributes-table-end
