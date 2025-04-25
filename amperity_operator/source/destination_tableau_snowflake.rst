.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Configure Amperity to send data to Snowflake, and then connect to that data from Tableau.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Snowflake, and then connect to that data from Tableau.

.. meta::
    :content class=swiftype name=title data-type=string:
        Connect Tableau to Snowflake

==================================================
Connect Tableau to Snowflake
==================================================

.. destination-tableau-snowflake-start

Some organizations choose to store their visualization source data in Snowflake, and then connect to Snowflake from Tableau.

You may send an Apache Parquet, Apache Avro, CSV, or JSON file from Amperity to Snowflake, and then connect to that data from Tableau.

.. destination-tableau-snowflake-end

.. destination-tableau-snowflake-admonition-start

.. admonition:: What is Snowflake?

   .. include:: ../../shared/terms.rst
      :start-after: .. term-snowflake-start
      :end-before: .. term-snowflake-end

.. destination-tableau-snowflake-admonition-end


.. _destination-tableau-snowflake-workflow-start:

Add workflow
==================================================

.. destination-tableau-snowflake-workflow-start

Amperity can be configured to send data directly to Snowflake. Tableau can be configured to connect to Snowflake, and use Amperity as a source for data visualizations.

.. destination-tableau-snowflake-workflow-end

.. image:: ../../images/destination-tableau-snowflake.png
   :width: 600 px
   :alt: Connect Tableau to Snowflake.
   :align: left
   :class: no-scaled-link

**To connect Tableau to Snowflake**

.. destination-tableau-snowflake-steps-start

The steps required to configure Amperity to send data that is accessible to Tableau from a Snowflake data warehouse requires completion of a series of short workflows, some of which must be done outside of Amperity.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Configure Snowflake to sync data using :doc:`Amperity Bridge <bridge_snowflake>`.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Connect Tableau to `Snowflake <https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm>`__ |ext_link|, and then access the data sent from Amperity.

       .. note:: The URL for the Snowflake data warehouse, the Snowflake username, the password, and the name of the Snowflake data warehouse are sent to the Tableau user within a SnapPass link. Request this information from your Amperity representative prior to attempting to connect Tableau to Snowflake.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Validate the workflow within Amperity and the data within Tableau.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - Configure Amperity to automate this workflow for a regular (daily) refresh of data.

.. destination-tableau-snowflake-steps-end
