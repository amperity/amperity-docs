.. https://docs.amperity.com/operator/


.. |destination-name| replace:: MoEngage
.. |plugin-name| replace:: "MoEngage"
.. |credential-type| replace:: "iam-role-to-role"
.. |required-credentials| replace:: "iam-role-to-role"
.. |what-send| replace:: CSV file in UTF-8 format
.. |where-send| replace:: an Amazon S3 bucket
.. |filter-the-list| replace:: "moen"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to MoEngage.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to MoEngage.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for MoEngage

==================================================
Configure campaigns for MoEngage
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-moengage-start
   :end-before: .. term-moengage-end

You can configure Amperity to send CSV files to |destination-name| for the following import types:

* A list of users who registered on |destination-name|.
* A list of anonymous users not registered on |destination-name|.
* Standard events, such as campaign interactions, along with user-defined events.


.. _campaign-moengage-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-pinterest-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Configure an Amazon S3 bucket**

       |destination-name| can `pull files from a folder in an Amazon S3 bucket <https://help.moengage.com/hc/en-us/articles/10170540879380-S3-Imports>`__ |ext_link|.

       Configure the bucket to `grant access <https://help.moengage.com/hc/en-us/articles/10170540879380-S3-Imports#h_01GK4871W1NY2TYX3AY4P888SE>`__ |ext_link| to |destination-name|.


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Review file import requirements**

       Review `MoEngage requirements for file imports <https://help.moengage.com/hc/en-us/articles/12246167449236-Overview-Imports>`__ |ext_link| and review the requirements for all file imports and specific requirements for each import type.

       All files must be CSV files with a header row. Column names are case sensitive.

       **For registered users**

       The imported file must have a column that maps to the user identifier in |destination-name|.

       Configure a filename template for registered users like this:

       ::

          registered_user_data_{{now|format:'dd-MM-yyyy'}}.csv


       **For anonymous users**

       The imported file must have a column that maps to an anonymous identifier, such as an email address or mobile phone number.

       Configure a filename template for anonymous users like this:

       ::

          anonymous_user_data_{{now|format:'dd-MM-yyyy'}}.csv


       **For events**

       The imported file must have columns that map to the time at which the event occurred and the registered user identifier.

       The filename for events should contain the name of the event followed by a datetime value. For example:

       ::

          <event-filename>_{{now|format:'dd-MM-yyyy'}}.csv

       .. tip:: Use the same name for "<event-filename>" in the filename template as the name of the event type in |destination-name|.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Enable S3 imports in MoEngage**

       Use `Data Imports <https://help.moengage.com/hc/en-us/articles/10170540879380-S3-Imports#h_01HDQXTY70G3RVNNDM6R3SC15R>`__ |ext_link| to configure the Amazon S3 import process.

       Log in to |destination-name|, and then navigate to **Dashboard** > **Data** > **Data Imports**.

       Use the **+Import** option, select the Amazon S3 import type, and then follow the steps for importing registered, anonymous, or events file types.

       Add connection details for the Amazon S3 bucket, such as bucket name, access key, secret key, folder path, and encryption keys.

       Review the imported file, and then map columns in the imported file to |destination-name| attributes.

.. campaign-pinterest-get-details-table-start


.. _campaign-moengage-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Throtle**

.. campaign-moengage-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. image:: ../../images/mockup-destinations-add-01-select-destination-s3.png
          :width: 380 px
          :alt: Add 
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

       .. admonition:: Configure business user access

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-allow-start
             :end-before: .. setting-common-business-user-access-allow-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-business-user-access-restrict-pii-start
             :end-before: .. setting-common-business-user-access-restrict-pii-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end


       **File format**
          |checkmark-required| **Required**

          Set this value to CSV.


       **Header**
          |checkmark-required| **Required**

          Enable header rows.


       **Campaign file settings**
          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

.. campaign-moengage-add-steps-end
