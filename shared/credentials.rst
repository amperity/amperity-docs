.. 
.. xxxxx
..


.. |sftp-type| replace:: ``xxxxx``
.. |sftp-hostname| replace:: ``xxxxx``


This topic contains credentials information that is shared across all credentials steps. The pathway into sources is different from destinations. Some credentials -- Amazon S3, for example -- will quickly have bespoke steps. Keep those either in the source/destination topics (if they are unique) OR use a shared file like /shared/amazon_s3 to ensure reusability.


**CREDENTIALS - INTRO, SOURCES & DESTINATIONS**

.. credentials-sources-intro-start

The following steps describe how to configure Amperity to connect to |source-name|.

.. important:: These steps may require administrator access to |source-name|. Configure this data source in a sandbox, verify the workflow, and then push these changes to your Amperity production tenant.

.. credentials-sources-intro-end


.. credentials-destinations-intro-start

The following steps describe how to configure Amperity to connect to |destination-name|.

.. important:: These steps may require administrator access to |destination-name|. Configure this destination in a sandbox, verify the workflow, and then push these changes to your Amperity production tenant.

.. credentials-destinations-intro-end




**CREDENTIALS - STEP ONE, A**

.. credentials-sources-configure-start

Open the **Sources** tab to configure credentials for |source-name|.

Click the **Add courier** button to open the **Add courier** dialog box.

.. credentials-sources-configure-end


.. credentials-destinations-configure-start

Open the **Destinations** tab to configure credentials for |destination-name|.

Click the **Add destination** button to open the **Add destination** dialog box.

.. credentials-destinations-configure-end


**CREDENTIALS - STEP ONE, B**

.. TODO: IMPORTANT. This is also used in step 2 of "Add data source and feed" because you end up doing the same exact thing.

.. credentials-sources-configure-options-start

Do one of the following to select |source-name|:

#. Click the row in which |source-name| is located.
#. Search for |source-name|. Start typing |filter-the-list|. The list will filter to show only matching sources.

.. credentials-sources-configure-options-end

.. credentials-destinations-configure-options-start

Select |destination-name| from the **Plugin** drop-down.

.. credentials-destinations-configure-options-end




**CREDENTIALS - STEP TWO, CREDENTIALS DO NOT EXIST**

.. credentials-sources-configure-credential-createx-start

Credentials allow Amperity to connect to |source-name|. Give the courier a name, and then select **Create a new credential** from the **Credential** drop-down.

.. credentials-sources-configure-credential-createx-end


.. credentials-destinations-configure-credential-createx-start

Credentials allow Amperity to connect to |destination-name|. Give the destination a name, and then select **Create a new credential** from the **Credential** drop-down.

.. credentials-destinations-configure-credential-createx-end





**CREDENTIALS - STEP TWO, CREDENTIALS EXIST**

.. credentials-sources-configure-already-configured-start

Credentials allow Amperity to connect to |source-name| and must exist before a courier can be configured to pull data from |source-name|. Select an existing credential from the **Credential** drop-down, and then click **Continue**.

.. credentials-sources-configure-already-configured-end


.. credentials-destinations-configure-already-configured-start

Credentials allow Amperity to connect to |destination-name| and must exist before Amperity can be configured to send data to |destination-name|. Select an existing credential from the **Credential** drop-down, and then click **Continue**.

.. credentials-destinations-configure-already-configured-end


**CREDENTIALS - SOURCES - STEP TWO, A**

.. credentials-sources-configure-already-configured-tip-intro-start

A courier that has credentials that are configured correctly will show a "Connection successful" status, similar to:

.. credentials-sources-configure-already-configured-tip-intro-end



**CREDENTIALS - SOURCES - STEP CONTINUE, A**

.. credentials-sources-configure-click-continue-start

When finished, click **Continue**.

.. credentials-sources-configure-click-continue-end


