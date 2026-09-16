.. 
.. xxxxx
..


.. vale off

**TEMPLATE SECTIONS FOR SENDTOS**

.. vale on

Used in /user/destination and /user/events topics.

.. sendtos-ask-to-configure-start

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destination cannot be selected for orchestrations ask your Datagrid Operator or Amperity representative to configure a destination for sending query results to |destination-name|.

.. sendtos-ask-to-configure-end


Used in /user/campaigns topics.

.. sendtos-ask-to-configure-campaigns-start

.. caution:: This destination is available for sending campaign audiences to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destination cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending campaign audiences to |destination-name|.

.. sendtos-ask-to-configure-campaigns-end



.. sendtos-ask-to-configure-webhook-start

.. note:: |destination-name| must be enabled as a webhook destination before you can configure an orchestration to send query results.

.. sendtos-ask-to-configure-webhook-end


.. vale off

**MARKETER CONFIG CALLOUT**

.. vale on

.. destination-ask-to-config-start

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destination cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending query results to |destination-name|.

.. destination-ask-to-config-emd


.. vale off

**BUILD QUERY**

.. vale on

.. For any destination that defaults to just email-only.


.. sendtos-build-query-email-only-start

The default audience list in |destination-name| requires only an email address. This requires a simple ``SELECT`` statement that returns only the Amperity ID and its associated email address:

.. code-block:: sql
   :linenos:

   SELECT
     email AS email
   FROM Customer360

.. sendtos-build-query-email-only-end


.. sendtos-build-query-webhook-lambda-note-start

.. note:: A Lambda function running in AWS Lambda will |lambda-validate| before sending data to |destination-name|.

.. sendtos-build-query-webhook-lambda-note-end


.. vale off

**ADD ORCHESTRATION**

.. vale on

.. sendtos-add-orchestration-generic-start

#. Open the **Activations** page, select the **Orchestrations** tab, and then click the **Add orchestration** button. This opens the **Add orchestration** dialog box.
#. From the **Object type** dropdown, select **Query**.
#. From the **Object** dropdown, select the query for which results is sent to |destination-name|.
#. From the **Destination** dropdown, select a destination that is configured for sending data to |destination-name|.
#. Verify all settings.
#. Set the workflow to **Manual**. You can change this to automatic later, after verifying the end-to-end workflow.
#. Click **Save**.

.. sendtos-add-orchestration-generic-end


.. sendtos-add-orchestration-snowflake-start

#. Open the **Activations** page, select the **Orchestrations** tab, and then click the **Add orchestration** button. This opens the **Add orchestration** dialog box.
#. From the **Object type** dropdown, select **Query**.
#. From the **Object** dropdown, select the object to be exported to Snowflake.

   .. note:: This name will also be the name of the orchestration.
#. From the **Destination** dropdown, select the name of the destination that is configured to send data to Snowflake.
#. From the **Data template** dropdown, select the data template that maps a database export or query to a table in Snowflake.
#. Verify the **Snowflake Location** has the correct namespace, including the appended Amperity table name. This should be a period-delimited list of the Snowflake database name, the Snowflake schema name, and the Snowflake table name:

   ::

      SNOWFLAKE_DATABASE_NAME.SNOWFLAKE_SCHEMA.TABLE_NAME

   .. note:: Be sure that the table name is appended.

   For example:

   ::

      AMPERITY.CUSTOMER_360.TABLE_NAME

#. Verify the option to use for managing the table in Snowflake.
#. Set the workflow to **Manual**. You can change this to automatic later, after verifying the end-to-end workflow.
#. Click **Save**.

.. sendtos-add-orchestration-snowflake-end



.. vale off

**RUN ORCHESTRATION**

.. vale on

.. sendtos-run-orchestration-start

Run the orchestration manually to validate that it works.

.. sendtos-run-orchestration-end

.. sendtos-run-orchestration-steps-start

#. Open the **Activations** page, select the **Orchestrations** tab, and then open the |fa-kebab| menu for the |destination-name| orchestration. Select **Run**.
#. The **Status** column for the orchestration updates to say "Waiting to start", after which the notifications pane updates to include a notification that shows the current status.
#. When the orchestration has run successfully, the status is updated to "Completed".

.. sendtos-run-orchestration-steps-end