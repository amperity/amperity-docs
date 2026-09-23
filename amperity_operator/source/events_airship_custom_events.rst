.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Airship
.. |plugin-name| replace:: "Airship Custom Events"
.. |credential-type| replace:: "airship-custom-events"
.. |required-credentials| replace:: Client ID, Client Secret, App Key, and Data Center
.. |what-send| replace:: custom events
.. |where-send| replace:: |destination-name|

.. meta::
    :description lang=en:
        Configure Amperity to send custom events to Airship.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send custom events to Airship.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure custom events for Airship

==================================================
Configure custom events for Airship
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-airship-custom-events-start
   :end-before: .. term-airship-custom-events-end

.. events-airship-custom-events-overview-start

Send |what-send| to |destination-name| so that customer behavior in Amperity can trigger an |destination-name| automation — such as a push notification, in-app message, SMS, or email — and personalize the message it sends. Each row returned by your query is sent as a single |destination-name| custom event, carrying an event name, a customer identifier, an optional timestamp, and any additional columns as event properties.

An event is different from a profile attribute: an |destination-name| automation listens for an event by name and acts when it arrives, whereas attributes only enrich a profile for segmentation and personalization. This connector sends events; the Airship Attributes connector sends attributes. It also replaces the file-based "Audience Uploader" process, in which Amperity dropped a file over SFTP for Airship to turn into events, by sending events to |destination-name| directly.

Amperity sends customer identifiers to |destination-name| exactly as your query returns them. Unlike some event connectors, this connector does not hash or normalize identifiers, so provide values in the form |destination-name| expects.

.. events-airship-custom-events-overview-end

.. events-airship-custom-events-connectors-note-start

.. note:: Amperity provides three separate |destination-name| connectors, each with its own credentials: **Airship Custom Events** (this connector) sends behavioral events; **Airship Attributes** sends profile attributes; and **Airship** sends files to an |destination-name| SFTP location. Set up each connector you use separately.

.. events-airship-custom-events-connectors-note-end

.. events-airship-custom-events-beta-start

.. admonition:: Beta

   The Airship Custom Events connector is currently in beta. Contact your Amperity representative to learn more.

.. events-airship-custom-events-beta-end


.. _events-airship-custom-events-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. events-airship-custom-events-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **Client ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-client-id-start
             :end-before: .. credential-airship-custom-events-client-id-end

       **Client Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-client-secret-start
             :end-before: .. credential-airship-custom-events-client-secret-end

       **App Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-app-key-start
             :end-before: .. credential-airship-custom-events-app-key-end

       **Data Center**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-data-center-start
             :end-before: .. credential-airship-custom-events-data-center-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Airship settings**

       **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-custom-events-identifier-type-start
             :end-before: .. setting-airship-custom-events-identifier-type-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Request properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-custom-events-query-must-return-start
             :end-before: .. setting-airship-custom-events-query-must-return-end

          See :ref:`events-airship-custom-events-fields` for the full list of columns, and :ref:`events-airship-custom-events-identifier-types` for the allowed **Identifier type** values.

.. events-airship-custom-events-get-details-table-end


.. _events-airship-custom-events-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

.. events-airship-custom-events-credentials-airship-setup-start

Before you configure credentials in Amperity, create a set of OAuth client credentials in your |destination-name| project:

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-airship-custom-events-find-start
   :end-before: .. credential-airship-custom-events-find-end

.. note:: This connector requests the **Events** permission, where the Airship Attributes connector requests **Lists**. A set of credentials created for the Attributes connector alone cannot send events. There is no Amperity-managed |destination-name| application: you create these credentials in your own |destination-name| project, and they are scoped to that one project and region.

.. events-airship-custom-events-credentials-airship-setup-end

**To configure credentials for Airship Custom Events**

.. events-airship-custom-events-credentials-steps-start

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
     - In the **Credentials settings** dialog box, do the following:

       From the **Plugin** dropdown, select **Airship Custom Events**.

       .. note:: Amperity provides three |destination-name| connectors. Select **Airship Custom Events** to send behavioral events. **Airship Attributes** sends profile attributes and **Airship** sends files over SFTP; both are separate connectors.

       Assign the credential a name and description that ensures other users of Amperity can recognize when to use this destination.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Client ID**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-client-id-start
             :end-before: .. credential-airship-custom-events-client-id-end

       **Client Secret**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-client-secret-start
             :end-before: .. credential-airship-custom-events-client-secret-end

       **App Key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-app-key-start
             :end-before: .. credential-airship-custom-events-app-key-end

       **Data Center**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-airship-custom-events-data-center-start
             :end-before: .. credential-airship-custom-events-data-center-end

.. events-airship-custom-events-credentials-steps-end


.. _events-airship-custom-events-add-destination:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination**

.. events-airship-custom-events-add-destination-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       Enter the name of the destination and a description. For example: "|destination-name| custom events" and "Send custom events to |destination-name|.".

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

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

       **Identifier type**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-airship-custom-events-identifier-type-start
             :end-before: .. setting-airship-custom-events-identifier-type-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-orchestration-only-start
          :end-before: .. destinations-steps-business-users-orchestration-only-end

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. events-airship-custom-events-add-destination-end


.. _events-airship-custom-events-build-query:

Build a query
==================================================

.. events-airship-custom-events-build-query-start

Use a query to build a combination of data that returns one row per event to send to |destination-name|. Each row must include a customer identifier and an event name; you can also include a timestamp and any additional columns, which are sent as event properties that an |destination-name| automation can read to personalize its message.

.. events-airship-custom-events-build-query-end

.. events-airship-custom-events-build-query-required-start

Review the :ref:`events-airship-custom-events-fields` section for the columns your query must and may return, and the :ref:`events-airship-custom-events-identifier-types` section for the allowed **Identifier type** values.

.. events-airship-custom-events-build-query-required-end

Bound the query to recent events so each orchestration sends new events instead of re-sending history; choose a window that matches how often the orchestration runs. |destination-name| rejects any event older than three months, so keep the window well inside that bound. A query that returns a collection of recent purchase events for use in |destination-name| is similar to:

.. code-block:: sql
   :linenos:

   SELECT
     c360.loyalty_id AS airship_identifier  -- the ID your Airship named users are keyed on
     ,'purchase' AS event_name              -- lower-cased before sending
     ,ut.order_datetime AS occurred         -- uit.order_datetime
     ,ut.order_id AS order_id               -- uit.order_id (sent as a property)
     ,ut.order_revenue AS order_total       -- uit.order_revenue (sent as a property)
     ,ut.currency AS currency               -- uit.currency (sent as a property)
   FROM Unified_Transactions ut
   LEFT JOIN Customer_360 c360 ON ut.amperity_id = c360.amperity_id
   WHERE ut.order_datetime > (CURRENT_DATE - interval '30' day)
   AND c360.loyalty_id IS NOT NULL

.. note:: The **airship_identifier** column must hold a value that matches the **Identifier type** you configure on the destination. For **named_user_id**, use the identifier your |destination-name| named users are registered under; for a channel type, use a channel UUID. See :ref:`events-airship-custom-events-identifier-types`.


.. _events-airship-custom-events-identifier-types:

Identifier types
==================================================

.. events-airship-custom-events-identifier-types-start

The **Identifier type** setting names which kind of |destination-name| identifier the **airship_identifier** column holds. |destination-name| requires exactly one identifier per event, so this single choice applies to the whole orchestration. The supported values are:

* **named_user_id** — an |destination-name| named user ID. Limited to 128 characters.
* **channel** — a generic |destination-name| channel.
* **ios_channel**, **android_channel**, **amazon_channel**, **web_channel** — a channel for a specific platform.

Every value other than **named_user_id** must be a valid |destination-name| channel UUID. **sms_channel**, **email_channel**, and **open_channel** are not supported for events even though |destination-name| accepts them for some static list uploads, so an event cannot be keyed on an email address or phone number.

.. events-airship-custom-events-identifier-types-end


.. _events-airship-custom-events-data-validation:

Data validation
==================================================

.. events-airship-custom-events-data-validation-start

|destination-name| validates a batch of events all or nothing: one event it rejects causes the entire batch to be rejected, and no event in that batch is applied. To prevent one bad row from discarding the rest, Amperity validates each row before sending and holds back rows that |destination-name| would reject. Held-back rows are reported as failed with the reason, and the remaining rows are sent. A row is held back when:

* **airship_identifier** is missing.
* **Identifier type** is **named_user_id** and the identifier is longer than 128 characters.
* **Identifier type** is a channel type and the identifier is not a valid UUID.
* **event_name** is missing, or is longer than 255 characters.
* **occurred** is present but cannot be read as a timestamp, is more than three months old, or is more than one hour in the future.
* **interaction_id** or **interaction_type** is longer than 255 characters.
* The event's properties serialize to more than 65,536 bytes (64 KB).

.. events-airship-custom-events-data-validation-end


.. _events-airship-custom-events-fields:

Event fields
==================================================

.. events-airship-custom-events-fields-start

The following table describes each column Amperity sends to |destination-name|. A query must return columns with the same name as listed in the "Amperity name" column.

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-airship-custom-events-query-must-return-start
      :end-before: .. setting-airship-custom-events-query-must-return-end

.. list-table::
   :widths: 22 20 58
   :header-rows: 1

   * - Amperity name
     - Airship field
     - Description

   * - **airship_identifier**
     - **user**
     - **Required**

       The customer identifier the event is attached to. The **Identifier type** setting determines which kind of |destination-name| identifier this is. A named user ID is limited to 128 characters; every channel type must be a valid channel UUID. Sent as returned by your query — not hashed or normalized.

   * - **event_name**
     - **body.name**
     - **Required**

       The name of the event, which is what an |destination-name| automation listens for. Amperity lower-cases the value before sending, because |destination-name| rejects any name containing an uppercase character; spaces, dots, hyphens, leading digits, and non-English characters are all accepted. Limited to 255 characters.

       .. note:: |destination-name| accepts an event name that no automation listens for and silently does nothing with it. Confirm the exact event names your |destination-name| automations expect, and remember that the automation name must be lower case to match.

   * - **occurred**
     - **occurred**
     - **Optional**

       When the event occurred. Send a full |ext_iso_8601| timestamp that includes a time — for example, ``2026-07-10T12:00:00Z`` or ``2026-07-10T12:00:00``. A value with a UTC offset such as ``2026-07-10T12:00:00+02:00`` is converted to UTC. A date-only value (``2026-07-10``), a space-separated timestamp (``2026-07-10 12:00:00``), or a numeric epoch value is not accepted, and the row is held back. If the column is absent or blank, the time of the send is used. A value that is present but cannot be read as a timestamp causes the row to be held back rather than defaulted, because sending an event with the wrong date is worse than not sending it. |destination-name| rejects events more than three months old or more than one hour in the future.

       .. TODO: verify with connector team — how a date/time-typed query column (for example ut.order_datetime) serializes into the row value, and whether that string form is accepted by Instant/parse. If typed columns do not render as ISO 8601 with a "T" separator, the build-query example must cast occurred to an ISO 8601 string.

   * - **interaction_id**
     - **body.interaction_id**
     - **Optional**

       An interaction identifier carried on the event body. Limited to 255 characters.

       .. important:: Send **interaction_id** and **interaction_type** under exactly these column names. A property with any other name — including a spelling |destination-name| does not recognize — is accepted and stored as an ordinary property, where |destination-name| reporting cannot find it. The mismatch is invisible at send time and shows up later as missing values in reporting.

   * - **interaction_type**
     - **body.interaction_type**
     - **Optional**

       An interaction type carried on the event body. Limited to 255 characters.

   * - Any other column
     - **body.properties.<column>**
     - **Optional**

       Every column that is not one of the fields above is sent as an event property, keyed by the column name. Properties are what |destination-name| message templating reads, so use them to personalize the message an event triggers. Columns with a blank value are dropped rather than sent as empty properties, and all properties together must serialize to no more than 65,536 bytes (64 KB).

       .. note:: |destination-name| treats **value**, **transaction**, and **session_id** specially in its own API, but this connector does not: a column with one of those names is sent as an ordinary property, not on the event body.

.. events-airship-custom-events-fields-end


.. _events-airship-custom-events-workflow-actions:

Workflow actions
==================================================

.. include:: ../../shared/workflow-actions.rst
   :start-after: .. workflow-actions-common-table-intro-start
   :end-before: .. workflow-actions-common-table-intro-end

.. events-airship-custom-events-workflow-actions-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-a-start
          :end-before: .. workflow-actions-common-table-section-one-a-end

       .. image:: ../../images/mockup-destinations-tab-workflow-error.png
          :width: 500 px
          :alt: Review a notifications error.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-one-b-start
          :end-before: .. workflow-actions-common-table-section-one-b-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-two-start
          :end-before: .. workflow-actions-common-table-section-two-end

       .. image:: ../../images/mockups-workflow-failed.png
          :width: 500 px
          :alt: The workflow tab, showing a workflow with errors.
          :align: left
          :class: no-scaled-link

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-a-start
          :end-before: .. workflow-actions-common-table-section-three-a-end

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-three-b-start
          :end-before: .. workflow-actions-common-table-section-three-b-end

       Amperity provides a series of workflow actions that can help resolve specific issues that may arise with |destination-name|, including:

       * :ref:`events-airship-custom-events-workflow-actions-invalid-credentials`
       * :ref:`events-airship-custom-events-workflow-actions-invalid-settings`

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-a-start
          :end-before: .. workflow-actions-common-table-section-four-a-end

       .. include:: ../../shared/workflow-actions.rst
          :start-after: .. workflow-actions-common-table-section-four-b-start
          :end-before: .. workflow-actions-common-table-section-four-b-end

.. events-airship-custom-events-workflow-actions-end

.. note:: If |destination-name| rejects an entire batch of events, the workflow reports the error with |destination-name|'s message, which names only the first event |destination-name| objected to — review the event field values returned by your query. If sends are rate limited, Amperity retries automatically; reduce the volume of events sent per orchestration if the limit persists.

.. note:: A successful send confirms that |destination-name| accepted the events, not that they were delivered. |destination-name| accepts an event whose name matches no automation, and an identifier that matches no |destination-name| user, without reporting an error. Events cannot be deleted, corrected, or deduplicated after they are sent, so a retried send double-counts.


.. _events-airship-custom-events-workflow-actions-invalid-credentials:

Invalid credentials
--------------------------------------------------

.. events-airship-custom-events-workflow-actions-invalid-credentials-start

Amperity was unable to authenticate with |destination-name|. Verify the credential's **Client ID**, **Client Secret**, and **App Key** against your |destination-name| project's client credentials, and confirm the credentials grant the **Events** permission. Because credentials are regional, also confirm the **Data Center** matches the region hosting your |destination-name| project. |destination-name| client credentials can also be given an expiration date or be revoked, so confirm they are still active.

.. events-airship-custom-events-workflow-actions-invalid-credentials-end

.. events-airship-custom-events-workflow-actions-invalid-credentials-steps-start

To resolve this error, verify the credentials configured for this workflow in Amperity.

#. Open the **Destinations** page and review the credential connected to the |destination-name| destination associated with this workflow. Verify the **Client ID**, **Client Secret**, **App Key**, and **Data Center**, and confirm the credentials grant the **Events** permission and are still active.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. events-airship-custom-events-workflow-actions-invalid-credentials-steps-end


.. _events-airship-custom-events-workflow-actions-invalid-settings:

Invalid settings
--------------------------------------------------

.. events-airship-custom-events-workflow-actions-invalid-settings-start

Amperity was unable to reach |destination-name|. This most often means the credential's **Data Center** does not match the region hosting your |destination-name| project — verify that the **Data Center** is set to the region (US or EU) where your project is hosted.

.. events-airship-custom-events-workflow-actions-invalid-settings-end

.. events-airship-custom-events-workflow-actions-invalid-settings-steps-start

To resolve this error, verify the settings configured for this workflow in Amperity.

#. Open the **Destinations** page and review the credential connected to the |destination-name| destination associated with this workflow. Verify the **Data Center** matches the region hosting your |destination-name| project.
#. Return to the workflow action, and then click **Resolve** to retry this workflow.

.. events-airship-custom-events-workflow-actions-invalid-settings-steps-end
