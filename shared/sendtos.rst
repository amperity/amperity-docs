.. 
.. xxxxx
..



**TEMPLATE SECTIONS FOR SENDTOS**


.. sendtos-ask-to-configure-start

.. note:: |destination-name| must be enabled before you can configure an orchestration to send query results.

.. sendtos-ask-to-configure-end


.. sendtos-ask-to-configure-webhook-start

.. note:: |destination-name| must be enabled as a webhook destination before you can configure an orchestration to send query results.

.. sendtos-ask-to-configure-webhook-end


**BUILD QUERY**

.. This section is for any destination that defaults to just email-only.


.. sendtos-build-query-email-only-start

The default audience list in |destination-name| requires only an email address. This requires a simple ``SELECT`` statement that returns only the Amperity ID and its associated email address:

.. code-block:: sql

   SELECT
     ,amperity_id AS "Amperity ID"
     ,email AS "Email"
   FROM Customer360

.. sendtos-build-query-email-only-end


.. sendtos-build-query-webhook-lambda-note-start

.. note:: A Lambda function running in AWS Lambda will |lambda-validate| before sending data to |destination-name|.

.. sendtos-build-query-webhook-lambda-note-end


**ADD ORCHESTRATION**

.. sendtos-add-orchestration-generic-start

#. From the **Destinations** tab, click **Add Orchestration**. This opens the **Add Orchestration** dialog box.
#. From the **Object Type** drop-down, select **Query**.
#. From the **Object** drop-down, select the query for which results will be sent to |destination-name|.
#. From the **Destination** drop-down, select a destination that is configured for sending data to |destination-name|.
#. From the **Data Template** drop-down, select a data template.
#. Verify all settings.
#. Set the workflow to **Manual**. (You can change this to automatic later, after verifying the end-to-end workflow.)
#. Click **Save**.

.. sendtos-add-orchestration-generic-end


.. sendtos-add-orchestration-snowflake-start

#. From the **Destinations** tab, click **Add Orchestration**. This opens the **Add Orchestration** dialog box.
#. From the **Object Type** drop-down, select **Database Export** or **Query**.
#. From the **Object** drop-down, select the object to be exported to Snowflake.

   .. note:: This name will also be the name of the orchestration.
#. From the **Destination** drop-down, select the name of the destination that is configured to send data to Snowflake.
#. From the **Data Template** drop-down, select the data template that maps a database export or query to a table in Snowflake.
#. Verify the **Snowflake Location** has the correct namespace, including the appended Amperity table name. This should be a period-delimited list of the Snowflake database name, the Snowflake schema name, and the Snowflake table name:

   ::

      SNOWFLAKE_DATABASE_NAME.SNOWFLAKE_SCHEMA.TABLE_NAME

   .. note:: Be sure that the table name is appended.

   For example:

   ::

      AMPERITY.CUSTOMER_360.TABLE_NAME

#. Verify the option to use for managing the table in Snowflake.
#. Set the workflow to **Manual**. (You can change this to automatic later, after verifying the end-to-end workflow.)
#. Click **Save**.

.. sendtos-add-orchestration-snowflake-end



**RUN ORCHESTRATION**

.. sendtos-run-orchestration-start

Run the orchestration manually to validate that it works.

.. sendtos-run-orchestration-end

.. sendtos-run-orchestration-steps-start

#. From the **Destinations** tab, under **Orchestrations**, open the |fa-kebab| menu for the |destination-name| orchestration, and then select **Run**.
#. The **Status** column for the orchestration will update to say "Waiting to start...", after which the notifications pane will update to include a notification that shows the current status.
#. When the orchestration has run successfully, the status is updated to "Completed".

.. sendtos-run-orchestration-steps-end