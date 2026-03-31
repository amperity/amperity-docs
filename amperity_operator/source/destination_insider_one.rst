.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Insider One
.. |destination-api| replace:: Insider One First-Party Segment API
.. |plugin-name| replace:: "Insider One"
.. |credential-type| replace:: "insiderone"
.. |required-credentials| replace:: "partner name" and "API token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: audience segments
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "ins"


.. meta::
    :description lang=en:
        Configure Amperity to send audiences and data to Insider One.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send audiences and data to Insider One.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Insider One

==================================================
Configure destinations for Insider One
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-insider-one-start
   :end-before: .. term-insider-one-end

.. destination-insider-one-about-start

Amperity supports two pathways for sending data to |destination-name|:

* Send first-party audience segments directly to |destination-name| using the :ref:`First-Party Segment API <destination-insider-one-api>`.
* Send user profile and events data to |destination-name| :ref:`using Amperity Bridge for Snowflake <destination-insider-one-snowflake>`, and then import the tables from Snowflake to |destination-name|.

.. destination-insider-one-about-end


.. _destination-insider-one-api:

Send audiences using the API
==================================================

.. destination-insider-one-api-about-start

Send first-party audience segments directly to |destination-name| using the `First-Party Segment API <https://developers.insiderone.com/#fe7e4b47-84e6-4574-910b-e847d9816282>`__ |ext_link|.

First-party audience segments group existing users into segments based on attribute values and are defined by a single user attribute. For example, a first name, an email address, a unique identifier, or the ID for the store a user most frequently shops at.

.. caution:: |destination-name| recommends that names of attributes be created in lowercase and without spaces. For example: **email**, **first_name**, or **store_id**. The name of the attribute sent from Amperity must match the `name of an attribute <https://academy.insiderone.com/docs/event-vs-attribute#attributes>`__ |ext_link| defined in |destination-name|.

   |destination-name| attributes also have data types so be sure to send attributes from Amperity that, in addition to being mapped to the correct attribute name in |destination-name|, also share a compatible data type.

After loading to |destination-name|, first-party audience segments are created on the **First-Party Segment** page under **Saved Segments**. All users in |destination-name| that match on that attribute belong to the first-party audience segment.

.. note:: Each unique first-party audience segment is a CSV file. Amperity updates first-party audience segments by downloading the CSV file from |destination-name| using the **First-Party Segment API**, updating the contents of the CSV file, and then uploading the CSV file to |destination-name|.

.. destination-insider-one-api-about-end


.. _destination-insider-one-api-howitworks:

How this destination works
--------------------------------------------------

.. destination-insider-one-api-howitworks-start

Amperity sends a single-column audience to |destination-name|, which processes the segment asynchronously, and then notifies Amperity when processing is complete.

.. destination-insider-one-api-howitworks-end

.. destination-insider-one-api-howitworks-table-start

A destination for |destination-name| works like this:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - **START WORKFLOW**

       After the workflow starts, Amperity:

       #. Gets the segment name and attribute name from the destination configuration.

       #. Builds the audience for the query or segment.

       #. Validates the audience. The audience must be a single column whose name matches the value of the **Attribute name** field configured for this destination.


       .. note:: Amperity writes the audience to a single-column CSV file without a header row. Each row in the CSV file contains a single value. The file is available to |destination-name| for up to 12 hours.

          Amperity generates a presigned download URL for the CSV file and submits the segment creation request to the |destination-api|.

          Amperity makes a `POST /fps/v1/upload <https://academy.insiderone.com/docs/first-party-segments-api>`__ |ext_link| request to submit the segment to |destination-name|.

          The request includes:

          * A segment name that matches the value of the **Segment name** field configured for this destination.
          * An attribute name that matches the value of the **Attribute name** field configured for this destination.
          * A presigned URL that |destination-name| uses to download the CSV file from Amperity.
          * A **Callback URL** that |destination-name| uses to notify Amperity when processing is complete.

          |destination-api| applies rate limits of up to 100 requests per second.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - **INSIDER ONE PROCESSES THE SEGMENT**

       |destination-name| downloads the audience file from Amperity using the presigned URL, processes each identifier value, and then reports counts of valid and invalid values sent to |destination-name| by Amperity.

       Processing can take up to 1 hour to complete.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - **END WORKFLOW**

       The workflow ends when |destination-name| reports counts of valid and invalid values.

.. destination-insider-one-api-howitworks-table-end


.. _destination-insider-one-api-get-details:

Get details
--------------------------------------------------

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-insider-one-api-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Partner name**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. setting-insider-one-partner-name-start
             :end-before: .. setting-insider-one-partner-name-end

       **API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. setting-insider-one-api-token-start
             :end-before: .. setting-insider-one-api-token-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Segment name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-insider-one-segment-name-start
             :end-before: .. setting-insider-one-segment-name-end

       **Attribute name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-insider-one-attribute-name-start
             :end-before: .. setting-insider-one-attribute-name-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A query or segment that outputs a single column whose name matches the value of the **Attribute name** field configured for this destination.

.. destination-insider-one-api-get-details-end


.. _destination-insider-one-api-credentials:

Configure credentials
--------------------------------------------------

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Insider One**

.. destination-insider-one-api-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Partner name**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. setting-insider-one-partner-name-start
             :end-before: .. setting-insider-one-partner-name-end

       **API token**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. setting-insider-one-api-token-start
             :end-before: .. setting-insider-one-api-token-end

.. destination-insider-one-api-credentials-steps-end


.. _destination-insider-one-add:

Add destination
--------------------------------------------------

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Insider One**

.. destination-insider-one-api-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-start
          :end-before: .. destinations-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-common.png
          :width: 380 px
          :alt: Add
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-add-destinations-select-start
          :end-before: .. destinations-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
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
          :alt: Step three.
          :align: center
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
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Segment name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-insider-one-segment-name-start
             :end-before: .. setting-insider-one-segment-name-end

       **Attribute name**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-insider-one-attribute-name-start
             :end-before: .. setting-insider-one-attribute-name-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end


   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. destination-insider-one-api-add-steps-end


.. _destination-insider-one-snowflake:

Send data tables using Snowflake
==================================================

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
