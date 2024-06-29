.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |destination-name| replace:: LiveRamp
.. |plugin-name| replace:: LiveRamp
.. |what-send| replace:: CSV, TSV, or PSV files
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "liv"
.. |sftp-type| replace:: **liveramp**
.. |sftp-hostname| replace:: **files.liveramp.com** or **sftp.liveramp.com**
.. |file-format| replace:: CSV, TSV, or PSV
.. |encoding-method| replace:: "GZip".
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by the SFTP site were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_liveramp|
.. |channel-link| replace:: |campaign_liveramp|


.. meta::
    :description lang=en:
        Configure Amperity to send data to LiveRamp.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to LiveRamp.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to LiveRamp

==================================================
Send data to LiveRamp
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-liveramp-start
   :end-before: .. term-liveramp-end

.. destination-liveramp-start

You can associate records in Amperity to an audience in LiveRamp by sending a combination of identifier data and query data. LiveRamp uses:

* Identifier data to match records to other |ext_liveramp_data_identifiers| in the LiveRamp Identity Graph.
* Segment data to group records into |ext_liveramp_data_segments| based on certain attributes for downstream targeting, measurement, and personalization. 

LiveRamp requires an audience ID. This may be a client customer ID from another application, it may be the LiveRamp audience ID itself (from LiveRamp data that was imported to Amperity), or it may be the Amperity ID.

.. destination-liveramp-end

.. destination-liveramp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-liveramp-get-details>`
#. :ref:`Add destination <destination-liveramp-add-destination>`
#. :ref:`Add data template <destination-liveramp-add-data-template>`

.. destination-liveramp-steps-to-send-end


.. _destination-liveramp-get-details:

Get details
==================================================

.. destination-liveramp-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The username and passphrase.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The remote folder to which Amperity will send data.

       .. important:: A "/" (forward slash) must be used as the first character for this value. For example: ``/uploads/tenant-name``.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The |destination-name| public key to use for |ext_liveramp_gpg|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - |destination-name| requires a header row to be present in CSV, TSV, and PSV files.

.. destination-liveramp-get-details-end


.. _destination-liveramp-file-preferences:

File preferences
==================================================

.. destination-liveramp-file-preferences-start

Sending data to LiveRamp should follow recommendations for |ext_liveramp_upload_data|.

.. destination-liveramp-file-preferences-end


.. _destination-liveramp-file-limitations:

File limitations
--------------------------------------------------

.. destination-liveramp-file-limitations-start

Review LiveRamp |ext_liveramp_file_limitations|.

.. destination-liveramp-file-limitations-end


.. _destination-liveramp-file-format:

File formats
--------------------------------------------------

.. destination-liveramp-file-format-start

LiveRamp supports the following |ext_liveramp_file_formats|:

* CSV
* PSV
* TSV

.. important:: Be sure to enable the **Include header row in output files** option for the Amperity destination.

.. destination-liveramp-file-format-end


.. _destination-liveramp-file-encryption:

GPG encryption
--------------------------------------------------

.. destination-liveramp-file-encryption-start

LiveRamp prefers |ext_liveramp_gpg| and GZip compression.

.. destination-liveramp-file-encryption-end


.. _destination-liveramp-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-liveramp-add-destination-steps-start

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
          :start-after: .. destinations-add-credentials-sftp-start
          :end-before: .. destinations-add-credentials-sftp-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-sftp-start
          :end-before: .. destinations-intro-for-additional-settings-sftp-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials-sftp.png
          :width: 500 px
          :alt: Update the settings for the SFTP destination.
          :align: left
          :class: no-scaled-link

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

       .. image:: ../../images/mockup-destinations-tab-add-03-settings-sftp.png
          :width: 500 px
          :alt: Settings for SFTP destinations.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-sftp-start
          :end-before: .. destinations-destination-settings-sftp-end


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

.. destination-liveramp-add-destination-steps-end


.. _destination-liveramp-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

.. admonition:: About paid media campaigns

   .. include:: ../../shared/paid-media.rst
      :start-after: .. paid-media-admonition-about-start
      :end-before: .. paid-media-admonition-about-end

**To add a data template**

.. destination-liveramp-add-data-template-steps-start

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

       .. image:: ../../images/mockup-data-template-tab-add-03-settings.png
          :width: 500 px
          :alt: Verify settings for the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-note-start
          :end-before: .. destinations-data-template-verify-config-settings-note-end


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

.. destination-liveramp-add-data-template-steps-end
