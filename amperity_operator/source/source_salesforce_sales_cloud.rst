.. https://docs.amperity.com/operator/


.. |source-name| replace:: Salesforce Sales Cloud
.. |plugin-name| replace:: Salesforce Sales Cloud
.. |feed-name| replace:: Accounts
.. |example-filename| replace:: accounts.ndjson
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |what-pull| replace:: customer records
.. |credential-type| replace:: **salesforce**
.. |filter-the-list| replace:: "sales"

.. meta::
    :description lang=en:
        Configure Amperity to pull data from Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Salesforce Sales Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Salesforce Sales Cloud

==================================================
Pull from Salesforce Sales Cloud
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-sales-cloud-start
   :end-before: .. term-salesforce-sales-cloud-end

.. source-salesforce-sales-cloud-rest-api-start

Salesforce Sales Cloud is a REST API that provides data for files and reports. Amperity can pull this data from Salesforce Sales Cloud for any or all of the resources that are defined for the Salesforce account.

* Salesforce Sales Cloud query results are always loaded into Amperity in full.
* Any date range supplied indirectly via a courier group is ignored.
* No input is needed when running a query manually.

.. source-salesforce-sales-cloud-rest-api-end

.. source-salesforce-sales-cloud-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-salesforce-sales-cloud-get-details>`
#. :ref:`Add data source and feed <source-salesforce-sales-cloud-add-data-source>`

.. source-salesforce-sales-cloud-steps-to-pull-end


.. _source-salesforce-sales-cloud-get-details:

Get details
==================================================

.. source-salesforce-sales-cloud-get-details-start

Salesforce Sales Cloud requires the following configuration details:

#. The username and password of a Salesforce account configured for API access.
#. The Salesforce Sales Cloud security token that belongs to username. (The security token is not required if IP range policies are configured from the Salesforce admin console.)
#. The scheme and host for a custom Salesforce Sales Cloud URL, if used by customer.
#. If Salesforce Sales Cloud will send data to Amperity from a sandbox instance.
#. A sample for each file to simplify feed creation.

.. tip:: Use SnapPass to securely share the credentials and setup information for |source-name| between your company and your Amperity representative.

.. source-salesforce-sales-cloud-get-details-end


.. _source-salesforce-sales-cloud-add-data-source:

Add data source and feed
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-steps-00-intro-start
   :end-before: .. sources-steps-00-intro-end

**To add a data source for any SFTP site**

.. source-salesforce-sales-cloud-add-data-source-steps-start

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

          .. image:: ../../images/mockup-credentials-add-02-credential-status-sftp.png
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

.. source-salesforce-sales-cloud-add-data-source-steps-end
