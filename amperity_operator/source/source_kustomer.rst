.. https://docs.amperity.com/operator/


.. |source-name| replace:: Kustomer
.. |plugin-name| replace:: Kustomer
.. |feed-name| replace:: Customer
.. |example-filename| replace:: tablename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |source-interface| replace:: the `Kustomer API <https://developer.kustomer.com/kustomer-api-docs/reference/introduction>`__ |ext_link|
.. |what-pull| replace:: customer experience, service, and support data


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Kustomer.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Kustomer.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Kustomer

==================================================
Pull from Kustomer
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-kustomer-start
   :end-before: .. term-kustomer-end

.. source-kustomer-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-kustomer-get-details>`
#. :ref:`Add courier <source-kustomer-add-courier>`
#. :ref:`Get sample tables <source-kustomer-get-sample-tables>`
#. :ref:`Add feeds <source-kustomer-add-feeds>`
#. :ref:`Add load operations <source-kustomer-add-load-operations>`
#. :ref:`Run courier <source-kustomer-run-courier>`
#. :ref:`Add to courier group <source-kustomer-add-to-courier-group>`

.. source-kustomer-steps-to-pull-end


.. _source-kustomer-get-details:

Get details
==================================================

.. source-kustomer-get-details-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-overview-start
   :end-before: .. sources-get-details-fivetran-overview-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-request-to-enable-start
   :end-before: .. sources-get-details-fivetran-request-to-enable-end

The |source-name| data source requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: center
          :class: no-scaled-link
     - A `Kustomer API key <https://developer.kustomer.com/kustomer-api-docs/reference/authentication>`__ |ext_link|, along with the **org.user.read** role for that API key.

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-get-details-fivetran-connect-start
          :end-before: .. sources-get-details-fivetran-connect-end

       .. include:: ../../shared/sources.rst
          :start-after: .. sources-get-details-fivetran-does-not-store-data-start
          :end-before: .. sources-get-details-fivetran-does-not-store-data-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/sources.rst
          :start-after: .. sources-get-details-fivetran-access-to-snowflake-start
          :end-before: .. sources-get-details-fivetran-access-to-snowflake-start

.. source-kustomer-get-details-end


.. _source-kustomer-add-courier:

Add courier
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-start
   :end-before: .. term-courier-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-consolidate-start
   :end-before: .. sources-add-courier-fivetran-consolidate-end

**Example table list**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-table-list-start
   :end-before: .. sources-add-courier-fivetran-table-list-end

.. source-kustomer-add-courier-example-table-list-start

For example:

::

   [
     "AMPERITY_A1BO987C.KUSTOMER_ACME.CUSTOMER",
     "AMPERITY_A1BO987C.KUSTOMER_ACME.NOTE",
     "AMPERITY_A1BO987C.KUSTOMER_ACME.MESSAGE",
     "AMPERITY_A1BO987C.KUSTOMER_ACME.CONVERSATION",
   ]

.. source-kustomer-add-courier-example-table-list-end

**Example stage name**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. source-kustomer-add-courier-example-stage-name-start

For example:

::

   AMPERITY_A1BO987C.KUSTOMER_ACME.ACME_STAGE

.. source-kustomer-add-courier-example-stage-name-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. source-kustomer-add-courier-example-load-operation-start

For example:

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.CUSTOMER"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.NOTE"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.MESSAGE"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.CONVERSATION"
       }
     ]
   }

.. source-kustomer-add-courier-example-load-operation-end

**To add a courier for Snowflake table objects**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-start
   :end-before: .. sources-add-courier-fivetran-end


.. _source-kustomer-get-sample-tables:

Get sample tables
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-fivetran-start
   :end-before: .. sources-get-sample-files-fivetran-end


.. _source-kustomer-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-file-start
   :end-before: .. sources-add-feed-note-file-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-kustomer-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-fivetran-start
   :end-before: .. sources-add-load-operation-example-intro-fivetran-end

.. source-kustomer-add-load-operations-example-start

For example:

::

   {
     "df-A1B2C3": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.CUSTOMER"
       }
     ],
     "df-D4E5F6": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.NOTE"
       }
     ],
     "df-G7H8I9": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.MESSAGE"
       }
     ],
     "df-J0K1L2": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.KUSTOMER_ACME.CONVERSATION"
       }
     ]
   }

.. source-kustomer-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-kustomer-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-kustomer-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
