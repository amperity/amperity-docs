.. https://docs.amperity.com/operator/


.. |source-name| replace:: Optimizely
.. |plugin-name| replace:: Amazon S3
.. |feed-name| replace:: Decisions
.. |example-filename| replace:: filename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: interactions records
.. |credential-type| replace:: **iam-credential**
.. |filter-the-list| replace:: "ama"


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Optimizely.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Optimizely.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Optimizely

==================================================
Pull from Optimizely
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-optimizely-start
   :end-before: .. term-optimizely-end

.. source-optimizely-about-start

Optimizely can send `enriched exports events <https://docs.developers.optimizely.com/web/docs/enriched-events-export>`__ |ext_link| data to Amperity via Amazon S3. Enriched events include details such as event timestamps, event IDs, event tags, event names, visitor IDs, session IDs, experiment IDs, and variation IDs.

.. source-optimizely-about-end

.. source-optimizely-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-optimizely-get-details>`
#. :ref:`Review Amazon S3 requirements for Optimizely <source-optimizely-filedrop-requirements>`
#. :ref:`Add data source and feed <source-optimizely-add-data-source>`

.. source-optimizely-steps-to-pull-end


.. _source-optimizely-get-details:

Get details
==================================================

.. source-optimizely-get-details-start

Amperity can be configured to pull data from Optimizely using Amazon S3. This requires the following configuration details:

#. Access to an `Optimizely data service <https://docs.developers.optimizely.com/web/docs/access-optimizely-export-data-via-amazon-s3>`__ |ext_link| hosted in Amazon S3.
#. The Amazon Resource Name (ARN) for a role with cross-account access.
#. The name of the Amazon S3 bucket.
#. A list of objects by filename and file type in the Amazon S3 bucket to be pulled to Amperity.
#. A sample for each file to simplify feed creation.

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-amazon-s3-cross-account-start
   :end-before: .. sources-add-courier-amazon-s3-cross-account-end

.. source-optimizely-get-details-end


.. _source-optimizely-filedrop-requirements:

Amazon S3 requirements
==================================================

.. source-optimizely-filedrop-requirements-start

Amazon S3 requires the following:

* Credentials that |format_common_allow_access| from the Amazon S3 bucket used by Optimizely.
* Files provided in |format_parquet| format and using the YYYY-MM-DD date format.
* Files sent from Optimizely are :ref:`located in partitions <source-optimizely-filedrop-apache-parquet-optimizely-partitions>`, one for decisions and one for events.
* Optimizely uses AWS Key Management Service for encryption.

.. source-optimizely-filedrop-requirements-end


.. _source-optimizely-filedrop-credentials:

Amazon S3 credentials
--------------------------------------------------

.. source-optimizely-filedrop-credentials-start

Amperity requires the ability to connect to, and then read data from the Amazon S3 bucket used by Optimizely. The credentials that allow that connection and the permissions to read data are entered into the Amperity user interface while configuring a courier. These credentials are created and managed by the owner of the Amazon S3 bucket. Use SnapPass to share credentials with your Amperity representative, if necessary.

.. source-optimizely-filedrop-credentials-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-snappass-start
   :end-before: .. term-snappass-end


.. _source-optimizely-filedrop-apache-parquet-optimizely-partitions:

Optimizely S3 partitions
--------------------------------------------------

.. source-optimizely-s3-partitions-start

Enriched events exports are exported to a bucket named **optimizely-events-data** that contains two partitions: decisions and conversions.

The paths to these partitions are similar to:

::

   s3://optimizely-events-data/v1/account_id=<account_id>/
   type=decisions/date={YYYY-MM-DD}/experiment=<experiment_id>

or

:: 

   s3://optimizely-events-data/v1/account_id=<account_id>/
   type=events/date={YYYY-MM-DD}/event=<event_name>

where:

* **optimizely-events-data** is the name of the Amazon S3 bucket
* **account_id** is your unique account identifier
* **date** is the creation date for the data
* **experiment_id** is the unique experiment identifier used for the **decisions** partition
* **event_name** is the event or entity identifier used for the events partition

The daily partition files are ready when **_SUCCESS** is appended to the partition path.

.. note:: Optimizely uses AWS Key Management Service for encryption. Amperity must be able to decrypt these files to pull them to the Amazon S3 or Azure Blob Storage location used by your tenant.

.. source-optimizely-s3-partitions-end


.. _source-optimizely-add-data-source:

Add data source and feed
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-steps-00-intro-start
   :end-before: .. sources-steps-00-intro-end

**To add a data source for Optimizely**

.. source-optimizely-add-data-source-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-01-open-dialog-start
          :end-before: .. sources-steps-01-open-dialog-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-01-select-source-start
          :end-before: .. sources-steps-01-select-source-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials.rst
          :start-after: .. credentials-sources-configure-already-configured-start
          :end-before: .. credentials-sources-configure-already-configured-end

       .. tip::

          .. include:: ../../shared/credentials.rst
             :start-after: .. credentials-sources-configure-already-configured-tip-intro-start
             :end-before: .. credentials-sources-configure-already-configured-tip-intro-end

          .. image:: ../../images/mockup-credentials-add-02-credential-status-s3.png
             :width: 380 px
             :alt: Add 
             :align: left
             :class: no-scaled-link


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-select-file-start
          :end-before: .. sources-steps-03-select-file-end

       .. image:: ../../images/mockup-sources-add-03-file-settings.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-browse-start
          :end-before: .. sources-steps-03-browse-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-browse-note-start
          :end-before: .. sources-steps-03-browse-note-end

       .. image:: ../../images/mockup-sources-add-03-file-browser-sftp.png
          :width: 500 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-03-pgp-start
          :end-before: .. sources-steps-03-pgp-end

       .. image:: ../../images/mockup-sources-add-03-pgp-credential.png
          :width: 500 px
          :alt: Add 
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-start
          :end-before: .. sources-steps-04-review-end

       .. image:: ../../images/mockup-sources-add-03-file-formatting.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-contents-start
          :end-before: .. sources-steps-04-review-contents-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-pgp-start
          :end-before: .. sources-steps-04-review-pgp-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-04-review-formatting-details-start
          :end-before: .. sources-steps-04-review-formatting-details-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-options-start
          :end-before: .. sources-steps-05-feed-options-end


       **New feed**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-new-start
          :end-before: .. sources-steps-05-feed-new-end


       **Existing feed**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-feed-existing-start
          :end-before: .. sources-steps-05-feed-existing-end


       **Pull data**

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-types-start
          :end-before: .. sources-steps-05-load-types-end

       .. image:: ../../images/mockup-sources-add-04-feed-load-type.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-type-upsert-start
          :end-before: .. sources-steps-05-load-type-upsert-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-type-truncate-start
          :end-before: .. sources-steps-05-load-type-truncate-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-05-load-types-note-start
          :end-before: .. sources-steps-05-load-types-note-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-06-feed-editor-start
          :end-before: .. sources-steps-06-feed-editor-end


   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-courier-start
          :end-before: .. sources-steps-07-courier-end

       .. image:: ../../images/mockup-courier-add-07-menu-run.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-calendar-start
          :end-before: .. sources-steps-07-calendar-end

       .. image:: ../../images/mockup-courier-add-07-menu-load-data.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-steps-07-run-start
          :end-before: .. sources-steps-07-run-end

.. source-optimizely-add-data-source-steps-end
