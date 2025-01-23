.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Yahoo DSP
.. |destination-api| replace:: Yahoo Ad Tech DataX API
.. |plugin-name| replace:: Yahoo DSP
.. |what-send| replace:: email addresses
.. |filter-the-list| replace:: "yah"
.. |credential-type| replace:: yahoo-dsp
.. |credential-details| replace:: the MDM ID
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |sendto-link| replace:: send query results
.. |channel-link| replace:: send campaigns
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "90"
.. |allow-for-what| replace:: audience lists
.. |allow-for-duration| replace:: up to 48 hours


==================================================
Send data to Yahoo DSP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-yahoo-dsp-start
   :end-before: .. term-yahoo-dsp-end

.. destination-yahoo-dsp-start

.. admonition:: What is DataX?

   DataX is a `component within the Yahoo Advertising infrastructure <https://help.yahooinc.com/datax/docs/introduction-scope>`__ |ext_link| that allows |destination-name| to exchange data with external partners in a secure, automated, and scalable manner. DataX uses a partner-facing RESTful API to enable external partners (like Amperity) to send audiences to specific locations within the `Yahoo DSP exchange's taxonomy <https://help.yahooinc.com/datax/docs/taxonomy-1>`__ |ext_link|.

   This destination enables your brand to manage audiences within the |destination-name| taxonomy from Amperity.

   Amperity uses the `PUT /TAXONOMY <https://help.yahooinc.com/datax/docs/put-append-taxonomy-node>`__ |ext_link| endpoint to determine the correct location within the |destination-name| taxonomy using your brand's MDM ID. This ID must be validated each time an audience is sent, which can take up to 30 minutes, after which the audience is sent to Yahoo DSP.

   Amperity uses the `POST /AUDIENCE <https://help.yahooinc.com/datax/docs/post-audience>`__ |ext_link| endpoint to manage the segment.

.. destination-yahoo-dsp-end

.. destination-active-campaign-api-note-start

.. note::

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-active-campaign-api-note-end

.. destination-yahoo-dsp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-yahoo-dsp-get-details>`
#. :ref:`Add destination <destination-yahoo-dsp-add-destination>`
#. :ref:`Add data template <destination-yahoo-dsp-add-data-template>`

.. destination-yahoo-dsp-steps-to-send-end


.. _destination-yahoo-dsp-get-details:

Get details
==================================================

.. destination-yahoo-dsp-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - Your brand's MDM ID.

       .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-yahoo-dsp-mdm-id-start
          :end-before: .. credential-yahoo-dsp-mdm-id-end

       .. tip:: You can find your brand's **Site MDM ID** from the |destination-name| user interface. Log in to |destination-name|, then navigate to the **Advertisers** page. Open your brand's profile. The **Site MDM ID** is available from the **MDM ID** field.

          .. image:: ../../images/destination-yahoo-site-mdm-id.png
             :width: 360 px
             :alt: Location of Yahoo DSP site MDM ID
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - The name of a segment in |destination-name|. This can be the name of an existing segment or be a new segment.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: left
          :class: no-scaled-link
     - To ensure that audiences are compliant with General Data Protection Regulation (GDPR) requirements for "information storage and access" and "personalization" features within the `transparency consent framework <https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework/blob/master/Consent%20string%20and%20vendor%20list%20formats%20v1.1%20Final.md#what-are-the-purposes-and-features-being-supported->`__ |ext_link| you must include the following fields:

       * **storage-consent**
       * **personalization-consent**

       Both fields have a Boolean data type and may be set to "true" or "false".

       When these fields are present in an audience, any users for whom the fields are not set or are both set to "false" will be omitted from the upload to |destination-name|. Only users who have both fields set and at least one field set to "true" are uploaded.

       .. important:: If your brand knows your audience contains users who reside in the Europe and are protected by GDPR consent requirements you should include these fields in the audience to ensure that your brand meets GDPR consent requirements.

.. destination-yahoo-dsp-get-details-end


.. _destination-yahoo-dsp-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-yahoo-dsp-add-destination-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       |destination-name| has the following settings:

       * **Seat MDM ID**

         .. include:: ../../shared/credentials_settings.rst
            :start-after: .. credential-yahoo-dsp-mdm-id-start
            :end-before: .. credential-yahoo-dsp-mdm-id-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Yahoo DSP.
          :align: left
          :class: no-scaled-link

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Segment name**
            - .. include:: ../../shared/destination_settings.rst
                 :start-after: .. setting-yahoo-dsp-segment-name-start
                 :end-before: .. setting-yahoo-dsp-segment-name-start
          * - **Membership duration**
            - .. include:: ../../shared/destination_settings.rst
                 :start-after: .. setting-common-membership-duration-start
                 :end-before: .. setting-common-membership-duration-end

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-enable-start
          :end-before: .. destinations-business-users-enable-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-allow-start
          :end-before: .. destinations-business-users-allow-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-yahoo-dsp-add-destination-end


.. _destination-yahoo-dsp-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-yahoo-dsp-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end

       The following settings are specific to |destination-name|:

       .. list-table::
          :widths: 180 320
          :header-rows: 1

          * - **Setting**
            - **Description**
          * - **Segment name**
            - .. include:: ../../shared/destination_settings.rst
                 :start-after: .. setting-yahoo-dsp-segment-name-start
                 :end-before: .. setting-yahoo-dsp-segment-name-start
          * - **Membership duration**
            - .. include:: ../../shared/destination_settings.rst
                 :start-after: .. setting-common-membership-duration-start
                 :end-before: .. setting-common-membership-duration-end

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-start
          :end-before: .. destinations-data-template-save-after-end

.. destination-yahoo-dsp-add-data-template-steps-end
