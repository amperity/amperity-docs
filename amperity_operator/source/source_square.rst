.. https://docs.amperity.com/operator/


.. |source-name| replace:: Square
.. |plugin-name| replace:: Square
.. |feed-name| replace:: Orders
.. |example-filename| replace:: tablename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |source-interface| replace:: |source-name|
.. |what-pull| replace:: customer records and interaction records


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Square.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Square.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Square

==================================================
Pull from Square
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-square-start
   :end-before: .. term-square-end

.. source-square-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-square-get-details>`
#. :ref:`Add courier <source-square-add-courier>`
#. :ref:`Get sample tables <source-square-get-sample-tables>`
#. :ref:`Add feeds <source-square-add-feeds>`
#. :ref:`Add load operations <source-square-add-load-operations>`
#. :ref:`Run courier <source-square-run-courier>`
#. :ref:`Add to courier group <source-square-add-to-courier-group>`

.. source-square-steps-to-pull-end


.. _source-square-get-details:

Get details
==================================================

.. source-square-get-details-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-overview-start
   :end-before: .. sources-get-details-fivetran-overview-end

#. .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-request-to-enable-start
      :end-before: .. sources-get-details-fivetran-request-to-enable-end

#. Access to an active |source-name| account using a private API key. Create an API key in |source-name| for use by Fivetran, and then provide the private API key to Amperity support. They need this to complete the configuration of Fivetran.

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-connect-start
      :end-before: .. sources-get-details-fivetran-connect-end

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-does-not-store-data-start
      :end-before: .. sources-get-details-fivetran-does-not-store-data-end

#. .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-access-to-snowflake-start
      :end-before: .. sources-get-details-fivetran-access-to-snowflake-start

.. source-square-get-details-end


.. _source-square-add-courier:

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

.. source-square-add-courier-example-table-list-start

For example:

::

   [
     "AMPERITY_C1AO712C.SQUARE_ACME.ORDER",
     "AMPERITY_C1AO712C.SQUARE_ACME.PAYMENT",
     "AMPERITY_C1AO712C.SQUARE_ACME.TRANSACTION",
   ]

.. source-square-add-courier-example-table-list-end

**Example stage name**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. source-square-add-courier-example-stage-name-start

For example:

::

   AMPERITY_C1AO712C.SQUARE_ACME.ACME_STAGE

.. source-square-add-courier-example-stage-name-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. source-square-add-courier-example-load-operation-start

For example:

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_C1AO712C.SQUARE_ACME.ORDER"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_C1AO712C.SQUARE_ACME.PAYMENT"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_C1AO712C.SQUARE_ACME.TRANSACTION"
       }
     ]
   }

.. source-square-add-courier-example-load-operation-end

**To add a courier for Snowflake table objects**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-start
   :end-before: .. sources-add-courier-fivetran-end


.. _source-square-get-sample-tables:

Get sample tables
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-fivetran-start
   :end-before: .. sources-get-sample-files-fivetran-end


.. _source-square-add-feeds:

Add feeds
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-feed-start
   :end-before: .. term-feed-end

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-note-fivetran-start
   :end-before: .. sources-add-feed-note-fivetran-end

**To add a feed**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-feed-steps-start
   :end-before: .. sources-add-feed-steps-end


.. _source-square-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-fivetran-start
   :end-before: .. sources-add-load-operation-example-intro-fivetran-end

.. source-square-add-load-operations-example-start

For example:

::

   {
     "df-A1B2C3": [
       {
         "type": "load",
         "file": "AMPERITY_C1AO712C.SQUARE_ACME.ORDER"
       }
     ],
     "df-D4E5F6": [
       {
         "type": "load",
         "file": "AMPERITY_C1AO712C.SQUARE_ACME.PAYMENT"
       }
     ],
     "df-G7H8I9": [
       {
         "type": "load",
         "file": "AMPERITY_C1AO712C.SQUARE_ACME.TRANSACTION"
       }
     ]
   }

.. source-square-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-square-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-square-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
