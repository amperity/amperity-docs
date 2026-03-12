.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Insider One


.. meta::
    :description lang=en:
        Configure Amperity to send user and events data to Insider One.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send user and events data to Insider One.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send user and events data to Insider One

==================================================
Send user and events data to Insider One
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-insider-one-start
   :end-before: .. term-insider-one-end

Send user and events data to |destination-name| using Amperity Bridge for Snowflake, and then import the tables from Snowflake to |destination-name|.

**To configure Amperity to send data tables to Insider One**

.. destination-insider-one-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **Create tables for user and events data**

       Configure user and events data tables in your customer 360 database. These tables can be built from standard output, such as the **Unified Itemized Transactions**, **Transaction Attributes Extended**, and **Customer 360** tables or from custom tables built using Spark SQL.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **Configure Amperity Bridge for Snowflake**

       Amperity Bridge for Snowflake is a first-class integration that uses `secure Data Sharing <https://docs.snowflake.com/en/user-guide/data-sharing-intro>`__ |ext_link| to enable bi-directional data access between Amperity and Snowflake without copying data or scheduling ETL workloads.

       :ref:`Configure Amperity Bridge for Snowflake <bridge-snowflake-sync-with-snowflake>` to share user and events tables in Amperity with Snowflake.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **Sync user and events data with Snowflake**

       You can configure Amperity to share any combination of schemas and tables that are available from the **Customer 360** page.

       Use the **Select tables** dialog box in the bridge configuration for Snowflake to :ref:`select any combination of user and events tables <bridge-snowflake-sync-with-snowflake-select-tables>`.

       .. image:: ../../images/bridge-select-databases-and-tables.png
          :width: 500 px
          :alt: Select schemas and tables to be shared.
          :align: left
          :class: no-scaled-link

       When finished, click **Save**.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - **Share user and events data from your Snowflake account**

       `Share user and events data from your Snowflake account <https://academy.insiderone.com/v1/docs/import-data-from-snowflake>`__ |ext_link| using the Snowflake integration in |destination-name|.

.. destination-insider-one-steps-end