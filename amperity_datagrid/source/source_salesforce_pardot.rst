.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |source-name| replace:: Salesforce Pardot
.. |plugin-name| replace:: Salesforce Pardot
.. |feed-name| replace:: OnlinePromotions
.. |example-filename| replace:: tablename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |source-interface| replace:: the |ext_salesforce_pardot|
.. |what-pull| replace:: prospect, opportunity, and visitor data


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Salesforce Pardot.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Salesforce Pardot.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Pardot

==================================================
Pull from Pardot
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-salesforce-pardot-start
   :end-before: .. term-salesforce-pardot-end

.. source-salesforce-pardot-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-salesforce-pardot-get-details>`
#. :ref:`Add courier <source-salesforce-pardot-add-courier>`
#. :ref:`Get sample tables <source-salesforce-pardot-get-sample-tables>`
#. :ref:`Add feeds <source-salesforce-pardot-add-feeds>`
#. :ref:`Add load operations <source-salesforce-pardot-add-load-operations>`
#. :ref:`Run courier <source-salesforce-pardot-run-courier>`
#. :ref:`Add to courier group <source-salesforce-pardot-add-to-courier-group>`

.. source-salesforce-pardot-steps-to-pull-end


.. _source-salesforce-pardot-get-details:

Get details
==================================================

.. source-salesforce-pardot-get-details-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-overview-start
   :end-before: .. sources-get-details-fivetran-overview-end

#. .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-request-to-enable-start
      :end-before: .. sources-get-details-fivetran-request-to-enable-end

#. Access to an active Pardot account.

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-connect-start
      :end-before: .. sources-get-details-fivetran-connect-end

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-does-not-store-data-start
      :end-before: .. sources-get-details-fivetran-does-not-store-data-end

#. A Pardot account ID with an Administrator role.
#. A Pardot Business Unit ID.
#. A Salesforce access token.
#. The Pardot API version and time zone.

   .. tip:: This is available from the **My Profile** page in Pardot.

#. A new security token for using SSO with Salesforce.

   .. tip:: Reset your security token to be sent an email that contains the new security token.

#. The daily API call limit. (Default is 150,000.)

#. .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-access-to-snowflake-start
      :end-before: .. sources-get-details-fivetran-access-to-snowflake-start

.. source-salesforce-pardot-get-details-end


.. _source-salesforce-pardot-add-courier:

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

.. source-salesforce-pardot-add-courier-example-table-list-start

For example:

::

   [
     "AMPERITY_A1BO987C.PARDOT_ACME.PROSPECT",
     "AMPERITY_A1BO987C.PARDOT_ACME.VISITOR",
     "AMPERITY_A1BO987C.PARDOT_ACME.EMAIL",
     "AMPERITY_A1BO987C.PARDOT_ACME.OPPORTUNITY",
   ]

.. source-salesforce-pardot-add-courier-example-table-list-end

**Example stage name**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. source-salesforce-pardot-add-courier-example-stage-name-start

For example:

::

   AMPERITY_A1BO987C.PARDOT_ACME.ACME_STAGE

.. source-salesforce-pardot-add-courier-example-stage-name-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. source-salesforce-pardot-add-courier-example-load-operation-start

For example:

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.PROSPECT"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.VISITOR"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.EMAIL"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.OPPORTUNITY"
       }
     ]
   }

.. source-salesforce-pardot-add-courier-example-load-operation-end

**To add a courier for Snowflake table objects**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-start
   :end-before: .. sources-add-courier-fivetran-end


.. _source-salesforce-pardot-get-sample-tables:

Get sample tables
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-fivetran-start
   :end-before: .. sources-get-sample-files-fivetran-end


.. _source-salesforce-pardot-add-feeds:

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


.. _source-salesforce-pardot-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-fivetran-start
   :end-before: .. sources-add-load-operation-example-intro-fivetran-end

.. source-salesforce-pardot-add-load-operations-example-start

For example:

::

   {
     "df-A1B2C3": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.PROSPECT"
       }
     ],
     "df-D4E5F6": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.VISITOR"
       }
     ],
     "df-G7H8I9": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.EMAIL"
       }
     ],
     "df-J0K1L2": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.PARDOT_ACME.OPPORTUNITY"
       }
     ]
   }

.. source-salesforce-pardot-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-salesforce-pardot-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-salesforce-pardot-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
