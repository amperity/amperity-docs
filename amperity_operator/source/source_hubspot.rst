.. https://docs.amperity.com/operator/


.. |source-name| replace:: HubSpot
.. |plugin-name| replace:: HubSpot
.. |feed-name| replace:: Customers
.. |example-filename| replace:: tablename_YYYY-MM-DD.csv
.. |domain-table-name| replace:: |source-name|:|feed-name|
.. |source-interface| replace:: the `HubSpot API <https://developers.hubspot.com/docs/api/overview>`__ |ext_link|
.. |what-pull| replace:: customer records and interaction records


.. meta::
    :description lang=en:
        Configure Amperity to pull data from HubSpot.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from HubSpot.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from HubSpot

==================================================
Pull from HubSpot
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-hubspot-start
   :end-before: .. term-hubspot-end

.. source-hubspot-context-start

HubSpot is a good source of marketing event data, including:

* Customer lists
* Customer profile data, such as names, email addresses, phone numbers, physical addresses
* Email opt-in and opt-out preferences
* Campaign details, such as clicks and opens
* Custom property fields defined in HubSpot

.. source-hubspot-context-end

.. source-hubspot-steps-to-pull-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-overview-list-intro-start
   :end-before: .. sources-overview-list-intro-end

#. :ref:`Get details <source-hubspot-get-details>`
#. :ref:`Add courier <source-hubspot-add-courier>`
#. :ref:`Get sample tables <source-hubspot-get-sample-tables>`
#. :ref:`Add feeds <source-hubspot-add-feeds>`
#. :ref:`Add load operations <source-hubspot-add-load-operations>`
#. :ref:`Run courier <source-hubspot-run-courier>`
#. :ref:`Add to courier group <source-hubspot-add-to-courier-group>`

.. source-hubspot-steps-to-pull-end


.. _source-hubspot-get-details:

Get details
==================================================

.. source-hubspot-get-details-start

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-details-fivetran-overview-start
   :end-before: .. sources-get-details-fivetran-overview-end

#. .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-request-to-enable-start
      :end-before: .. sources-get-details-fivetran-request-to-enable-end

#. Permission to sychronize Fivetran to HubSpot. This must be done by a user of HubSpot with `Super Admin level privileges <https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#super-admin>`__ |ext_link|. Log into HubSpot as a user with **Super Admin** privileges, select the account you want to synchronize, click **Grant Access**, and then click **Save & Test**.

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-connect-start
      :end-before: .. sources-get-details-fivetran-connect-end

   .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-does-not-store-data-start
      :end-before: .. sources-get-details-fivetran-does-not-store-data-end

#. .. include:: ../../shared/sources.rst
      :start-after: .. sources-get-details-fivetran-access-to-snowflake-start
      :end-before: .. sources-get-details-fivetran-access-to-snowflake-start

.. source-hubspot-get-details-end


.. _source-hubspot-add-courier:

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

.. source-hubspot-add-courier-example-table-list-start

For example:

::

   [
     "AMPERITY_A1BO987C.HUBSPOT_ACME.CONTACT",
     "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_EVENT",
     "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_SUBSCRIPTION",
     "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_SUBSCRIPTION_CHANGE",
   ]

.. source-hubspot-add-courier-example-table-list-end

**Example stage name**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-stage-name-start
   :end-before: .. sources-add-courier-fivetran-stage-name-end

.. source-hubspot-add-courier-example-stage-name-start

For example:

::

   AMPERITY_A1BO987C.HUBSPOT_ACME.ACME_STAGE

.. source-hubspot-add-courier-example-stage-name-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-load-operation-start
   :end-before: .. sources-add-courier-fivetran-load-operation-end

.. source-hubspot-add-courier-example-load-operation-start

For example:

::

   {
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.CONTACT"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_EVENT"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_SUBSCRIPTION"
       }
     ],
     "df-xxxxx": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_SUBSCRIPTION_CHANGE"
       }
     ]
   }

.. source-hubspot-add-courier-example-load-operation-end

**To add a courier for Snowflake table objects**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-courier-fivetran-start
   :end-before: .. sources-add-courier-fivetran-end


.. _source-hubspot-get-sample-tables:

Get sample tables
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-get-sample-files-fivetran-start
   :end-before: .. sources-get-sample-files-fivetran-end


.. _source-hubspot-add-feeds:

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


.. _source-hubspot-add-load-operations:

Add load operations
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-start
   :end-before: .. sources-add-load-operation-end

**Example load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-example-intro-fivetran-start
   :end-before: .. sources-add-load-operation-example-intro-fivetran-end

.. source-hubspot-add-load-operations-example-start

For example:

::

   {
     "df-A1B2C3": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.CONTACT"
       }
     ],
     "df-D4E5F6": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_EVENT"
       }
     ],
     "df-G7H8I9": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_SUBSCRIPTION"
       }
     ],
     "df-J0K1L2": [
       {
         "type": "load",
         "file": "AMPERITY_A1BO987C.HUBSPOT_ACME.EMAIL_SUBSCRIPTION_CHANGE"
       }
     ]
   }

.. source-hubspot-add-load-operations-example-end

**To add load operations**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-load-operation-steps-start
   :end-before: .. sources-add-load-operation-steps-end


.. _source-hubspot-run-courier:

Run courier manually
==================================================

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-start
   :end-before: .. sources-run-courier-end

**To run the courier manually**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-run-courier-steps-start
   :end-before: .. sources-run-courier-steps-end


.. _source-hubspot-add-to-courier-group:

Add to courier group
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-courier-group-start
   :end-before: .. term-courier-group-end

**To add the courier to a courier group**

.. include:: ../../shared/sources.rst
   :start-after: .. sources-add-to-courier-group-steps-start
   :end-before: .. sources-add-to-courier-group-steps-end
