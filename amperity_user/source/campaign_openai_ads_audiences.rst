.. https://docs.amperity.com/user/


.. |destination-name| replace:: OpenAI Audiences
.. |what-send| replace:: audiences
.. |attributes-sent| replace:: a single hashed email or phone identifier


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to OpenAI Audiences.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to OpenAI Audiences.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to OpenAI Audiences

==================================================
Send audiences to OpenAI Audiences
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-openai-ads-audiences-start
   :end-before: .. term-openai-ads-audiences-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-beta-start
   :end-before: .. destination-openai-ads-audiences-beta-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-api-note-start
   :end-before: .. destination-openai-ads-audiences-api-note-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-behavior-start
   :end-before: .. destination-openai-ads-audiences-behavior-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-list-intro-start
   :end-before: .. channels-overview-list-intro-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end

.. _channel-openai-ads-audiences-build-segment:

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


.. _channel-openai-ads-audiences-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. channel-openai-ads-audiences-build-campaign-steps-start

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

.. channel-openai-ads-audiences-build-campaign-steps-end


.. _channel-openai-ads-audiences-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-openai-ads-audiences-configure-default-attributes-start

|destination-name| sends a single identifier per member — the one that matches the **Match identifier** configured on the destination. Map the default attribute for the campaign to the column that matches that setting.

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Source attribute
     - Required?
     - Destination attribute
   * - **email** / **phone** / **email_sha256** / **phone_number_sha256**
     - Yes
     - The one column that matches the configured **Match identifier**. Amperity hashes raw **email** and **phone** values with SHA-256 before sending; the **email_sha256** and **phone_number_sha256** columns are sent as supplied. Plaintext identifiers never leave Amperity.

.. channel-openai-ads-audiences-configure-default-attributes-end
