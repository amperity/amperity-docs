.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Yahoo DSP
.. |plugin-name| replace:: "Yahoo DSP"
.. |credential-type| replace:: "yahoo-dsp"
.. |required-credentials| replace:: "seat MDM ID"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |audience-primary-key| replace:: "email" or "phone"
.. |filter-the-list| replace:: "yahoo"
.. |duration| replace:: (in days)
.. |duration-value| replace:: "0" - "90"
.. |allow-for-what| replace:: audience lists
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Configure Amperity to send audiences to Yahoo DSP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences to Yahoo DSP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Yahoo DSP

==================================================
Send audiences to Yahoo DSP
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_yahoo_dsp.html>`__ |ext_link|.

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


.. _destination-yahoo-dsp-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-yahoo-dsp-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Seat MDM ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-yahoo-dsp-mdm-id-start
             :end-before: .. credential-yahoo-dsp-mdm-id-end

          .. tip:: You can find your brand's **Site MDM ID** from the |destination-name| user interface. Log in to |destination-name|, then navigate to the **Advertisers** page. Open your brand's profile. The **Site MDM ID** is available from the **MDM ID** field.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: left
          :class: no-scaled-link
     - **Required configuration settings**

       None. The segment name will be applied automatically if not specified. Membership duration defaults to 30 days.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: left
          :class: no-scaled-link
     - **General Data Protection Regulation (GDPR) requirements**

       To ensure that audiences are compliant with General Data Protection Regulation (GDPR) requirements for "information storage and access" and "personalization" features within the `transparency consent framework <https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework/blob/master/Consent%20string%20and%20vendor%20list%20formats%20v1.1%20Final.md#what-are-the-purposes-and-features-being-supported->`__ |ext_link| you must include the following fields:

       * **storage-consent**
       * **personalization-consent**

       Both fields have a Boolean data type and may be set to "true" or "false".

       When these fields are present in an audience, any users for whom the fields are not set or are both set to "false" will be omitted from the upload to |destination-name|. Only users who have both fields set and at least one field set to "true" are uploaded.

       .. important:: If your brand knows your audience contains users who reside in the Europe and are protected by GDPR consent requirements you should include these fields in the audience to ensure that your brand meets GDPR consent requirements.


.. destination-yahoo-dsp-get-details-table-end


.. _destination-yahoo-dsp-add-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Yahoo DSP**

.. destination-yahoo-dsp-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Seat MDM ID**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-yahoo-dsp-mdm-id-start
             :end-before: .. credential-yahoo-dsp-mdm-id-end

.. destination-yahoo-dsp-credentials-steps-end


.. _destination-yahoo-dsp-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Yahoo DSP**

.. destination-yahoo-dsp-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-yahoo-dsp.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-select-credential-start
          :end-before: .. destinations-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. destinations-steps-test-connection-start
             :end-before: .. destinations-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-name-and-description-start
          :end-before: .. destinations-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Segment name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-yahoo-dsp-segment-name-start
             :end-before: .. setting-yahoo-dsp-segment-name-start

       **Membership duration**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-membership-duration-start
             :end-before: .. setting-common-membership-duration-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-yahoo-dsp-add-steps-end
