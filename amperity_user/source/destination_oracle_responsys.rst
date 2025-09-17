.. https://docs.amperity.com/user/


.. |destination-name| replace:: Oracle Responsys
.. |what-send| replace:: CSV files
.. |sftp-type| replace:: **oracle-responsys**
.. |sftp-hostname| replace:: **files.responsys.net** or **files.dc2.responsys.net**
.. |file-format| replace:: CSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Oracle Responsys.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Oracle Responsys.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Oracle Responsys

==================================================
Send query results to Oracle Responsys
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-responsys-start
   :end-before: .. term-oracle-responsys-end

.. sendto-oracle-responsys-important-start

.. important:: After files are delivered to |destination-name| from Amperity you must configure an job--one time or recurring-- that imports this data into a :ref:`profile list or profile extension table <sendto-oracle-responsys-import>` using `Connect <https://docs.oracle.com/en/cloud/saas/marketing/responsys-user/Connect_WizardUpload.htm>`__ |ext_link|.

.. sendto-oracle-responsys-important-end

.. sendto-oracle-responsys-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-oracle-responsys-build-query>`
#. :ref:`Add orchestration <sendto-oracle-responsys-add-orchestration>`
#. :ref:`Run orchestration <sendto-oracle-responsys-run-orchestration>`
#. :ref:`Import results to Oracle Responsys <sendto-oracle-responsys-import>`

.. sendto-oracle-responsys-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-oracle-responsys-build-query:

Build query
==================================================

.. sendto-oracle-responsys-build-query-start

You need to build a query that shapes the data so that fields in the output can be mapped to the fields required by |destination-name|.

.. sendto-oracle-responsys-build-query-end


.. _sendto-oracle-responsys-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-oracle-responsys-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _sendto-oracle-responsys-import:

Import results to Reponsys
==================================================

.. sendto-oracle-responsys-import-start

After these files are delivered to |destination-name| you must import this data into a profile list or profile extension table using `Connect <https://docs.oracle.com/en/cloud/saas/marketing/responsys-user/Connect_WizardUpload.htm>`__ |ext_link|.

* A profile list stores information for all customers, and then maintains a profile.
* A profile extension table stores additional attributes that define behavioral, demographic, or profile preference characteristics for your customer profiles.

.. caution:: The following steps outline how you should expect to do this from the **Connect** interace within |destination-name|. You should review these steps to ensure that you have a full understanding of the end to end workflow. The following steps are focused on how to ensure those configuration details match what is sent from Amperity.

**To import results to Oracle Responsys**

.. tip:: See the `Oracle Responsys help center page <https://docs.oracle.com/en/cloud/saas/marketing/responsys-user/Connect_WizardUpload.htm>`__ |ext_link| for complete steps on importing results from Amperity.

#. From the **Data** side navigation bar, select **Connect** > **Create Job** > **Import Profile Data**. Add the required details to describe the job, and then click **Done**.
#. Connect to a server.

   If you sent data to a server that is hosted by |destination-name|, click **Responsys File Server**.

   If you sent data to a server that is not hosted by |destination-name|, click **External server by SFTP**.
#. Provide information about the file to be imported. Use the following table to understand how settings in Amperity relate to settings required by |destination-name|:

   .. list-table::
      :widths: 300 300
      :header-rows: 1

      * - Amperity setting
        - Oracle Responsys setting
      * - **Filename template**

          The full name and extension of the file. For example: "ACMEResponsysChurn_2021-11-13.csv".
        - **File to upload**

          This must match the name of the file that was exported from Amperity.
      * - (None)

          Amperity supports UTF-8 character sets automatically.
        - **Character set**

          Set this value to UTF-8.
      * - **File format**

          Configure Amperity for the CSV file format.
        - **Field delimiter**

          Set this value to "," (comma).
      * - **Amperity**

          Enable the **Header** option to use column names as column headers in your output.
        - **First line contains column names**

          Select this checkbox if **Include header row in output files** is selected in Amperity.
      * - **PGP public key**

          Use this setting to provide a public encryption key.
        - **File is encrypted with PGP/GPG key**

          Select this checkbox when Amperity provides a public encryption key to ensure that it can be decrypted by |destination-name| before uploading.

#. Set the target definition to be a profile list or a profile extension table.
#. Map the columns from the file sent from Amperity to the fields in the target definition.

   .. important:: These fields **must** match the fields sent from Amperity, regardless of if it is from a campaign or if it is from an orchestration.
#. Select any post processing action to take after the job is successful, such as launching a campaign from |destination-name|.
#. Configure email notifications for this job.
#. Schedule the job to run once or on a recurring schedule.

.. sendto-oracle-responsys-import-end
