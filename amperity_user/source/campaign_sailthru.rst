.. https://docs.amperity.com/user/


.. |destination-name| replace:: Sailthru by Marigold
.. |what-send| replace:: email address lists
.. |what-enable| replace:: **email**
.. |attributes-sent| replace:: |destination-name| requires only email addresses. There are no optional fields.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Sailthru by Marigold.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Sailthru by Marigold.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Sailthru by Marigold

==================================================
Send audiences to Sailthru by Marigold
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sailthru-start
   :end-before: .. term-sailthru-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-sailthru-build-segment:

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


.. _destination-sailthru-extended-profile-attributes:

Extended profile attributes
--------------------------------------------------

.. destination-sailthru-extended-profile-attributes-start

You can extend audiences that are sent to |destination-name| by including extended profile attributes. The following table shows the field name mapping that is required by |destination-name|. Rename fields within campaigns to the name that is required by |destination-name|.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Amperity name
     - Sailthru name

   * - **address**
     - **postal_address**

   * - **address2**
     - **postal_address2**

   * - **birthdate**
     - **birth_date**

   * - **city**
     - **postal_city**

   * - **country**
     - **country**

   * - **full_name**
     - **name**

   * - **gender**
     - **gender**

   * - **given_name**
     - **first_name**

   * - **phone**
     - **phone**

   * - **postal**
     - **postal_code**

   * - **surname**
     - **last_name**

   * - **state**
     - **postal_state**

.. note:: |destination-name| field names are case sensitive and cannot start with a number. Review the list of `extended profile attributes <https://getstarted.sailthru.com/audience/managing-users/set-variables-on-users/>`__ |ext_link| that are supported by |destination-name|.

.. destination-sailthru-additional-attributes-end


.. _channel-sailthru-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

**To add Sailthru to a campaign**

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

       .. image:: ../../images/mockup-campaigns-destination-sailthru.png
          :width: 500 px
          :alt: Add a destination for Sailthru.
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

       .. image:: ../../images/mockup-campaigns-attributes-sailthru.png
          :width: 500 px
          :alt: Edit the attributes for Sailthru.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end





.. _channel-sailthru-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-sailthru-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

.. channel-sailthru-configure-default-attributes-end
