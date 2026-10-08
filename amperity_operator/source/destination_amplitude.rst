.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Amplitude
.. |plugin-name| replace:: "Amplitude"
.. |credential-type| replace:: "amplitude"
.. |required-credentials| replace:: "API Key" and "Secret Key"
.. |what-send| replace:: user properties, events, group properties, audiences, and deletion requests
.. |where-send| replace:: an |destination-name| project
.. |filter-the-list| replace:: "ampl"


.. meta::
    :description lang=en:
        Configure Amperity to send user properties, events, group properties, audiences, and deletion requests to an Amplitude project.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send user properties, events, group properties, audiences, and deletion requests to an Amplitude project.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Amplitude

====================================================
Configure destinations for Amplitude
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amplitude-start
   :end-before: .. term-amplitude-end

.. destination-amplitude-start

The |destination-name| connector sends |what-send| from Amperity into |where-send|. What each row becomes is set by the **Write mode** setting on the orchestration that sends to this destination, and an orchestration performs a single write mode for the entire run.

Each row is addressed by a single identity. The query results must include a column named ``identity_value`` that carries that identity: the |destination-name| ``user_id`` in user-properties and events modes, the group's value in group-properties mode, the cohort member in cohort-push mode, or the identity to delete in user-deletion mode.

user-properties, group-properties, and cohort-push modes sync incrementally. Amperity sends only what changed since the last successful run and reports unchanged rows as sent from cache. events and user-deletion modes have no incremental tracking — they process every row in the query results on each run, so scope those queries to the rows you intend to send.

.. destination-amplitude-end

.. important:: The connector reads each row's identity from a column named ``identity_value``. If your query produces the identity under another name, alias it — for example ``SELECT user_id AS identity_value``. A send whose query results have no ``identity_value`` column fails before any data is sent, with a message naming the missing column.

.. destination-amplitude-data-shape-start

The query results must include a column named ``identity_value``. What else the query needs depends on the destination's write mode:

* **user-properties** and **group-properties** send every other column in the results as a property, so return only the columns you want written.
* **events** also needs the two columns named by the **Event name column** and **Timestamp column** settings. Every other column becomes an event property.
* **cohort-push** and **user-deletion** send nothing but ``identity_value``. Other columns in the results are ignored.

.. destination-amplitude-data-shape-end

.. destination-amplitude-api-note-start

.. note:: This destination uses several of |destination-name|'s `REST APIs <https://amplitude.com/docs/apis>`__ |ext_link|: the `HTTP V2 <https://amplitude.com/docs/apis/analytics/http-v2>`__ |ext_link| and `Batch Event Upload <https://amplitude.com/docs/apis/analytics/batch-event-upload>`__ |ext_link| APIs for events, the `Identify <https://amplitude.com/docs/apis/analytics/identify>`__ |ext_link| and `Group Identify <https://amplitude.com/docs/apis/analytics/group-identify>`__ |ext_link| APIs for user and group properties, the `Behavioral Cohorts API <https://amplitude.com/docs/apis/analytics/behavioral-cohorts>`__ |ext_link| for audiences, and the `User Privacy API <https://amplitude.com/docs/apis/analytics/user-privacy>`__ |ext_link| for deletion requests.

.. destination-amplitude-api-note-end

.. destination-amplitude-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-amplitude-beta-end

.. destination-amplitude-prereq-start

.. important:: Set **Attribute updates only** on every orchestration whose write mode is *not* cohort-push. This setting has no reliable default — an orchestration that never has it set explicitly fails before any data is sent, with the message "Plugin configuration: missing audience name". Leave it cleared only for cohort-push.

.. note:: A successful connection test confirms that both credential fields are valid and correctly paired against |destination-name|. It does not exercise the ingest endpoints that user-properties, events, and group-properties modes write through, so it does not confirm that those modes will land data. After your first run, confirm the records appear in |destination-name|.

.. note:: Configure one orchestration per write mode, each sending its own query. To send more than one write mode against the same |destination-name| project, configure a separate orchestration, with its own query, for each.

.. destination-amplitude-prereq-end

.. destination-amplitude-region-note-start

.. note:: The **Amplitude region** setting must match the region your |destination-name| project is hosted in. Amperity sends to different |destination-name| hosts for **us** and **eu**, and a mismatch sends every request to the wrong host, so the run fails.

.. destination-amplitude-region-note-end


.. _destination-amplitude-write-modes:

Write modes
====================================================

.. destination-amplitude-write-modes-start

The **Write mode** setting selects what each row does. You choose the write mode, and its mode-specific settings, when you configure the orchestration that sends to this destination.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Write mode
     - What it sends
   * - **user-properties**
     - The default. Writes each row as properties on an |destination-name| user, addressed by ``identity_value`` as the ``user_id``. Every column other than ``identity_value`` becomes a user property, written with ``$set`` (overwrite on every run) or, for columns named in the **Set-once properties** setting, ``$setOnce`` (written once, never overwritten). Syncs incrementally.
   * - **events**
     - Sends each row as a named |destination-name| event. Requires the **Event name column** and **Timestamp column** settings, which name the columns that supply the event name and event time; every column other than those two and ``identity_value`` becomes an event property. The **Sync cadence** setting selects the ingest endpoint. Processes every row on each run.
   * - **group-properties**
     - Writes each row as properties on an |destination-name| group, addressed by ``identity_value`` as the group's value. Requires the **Group type** setting. Every column other than ``identity_value`` becomes a group property, with the same ``$set`` and ``$setOnce`` behavior as user-properties mode. Syncs incrementally.
   * - **cohort-push**
     - Sends one Amperity audience to |destination-name| as one behavioral cohort. Only ``identity_value`` is sent; other columns are ignored, because cohort membership carries no properties. Requires the **Cohort name**, **Cohort identifier type**, **Cohort owner email**, and **Amplitude app ID** settings. Syncs incrementally when **Cohort sync mode** is **append**.
   * - **user-deletion**
     - Submits a deletion request to |destination-name| for each row's identity, for honoring data-subject deletion requests. Only ``identity_value`` is sent; other columns are ignored. Requires the **Deletion identifier type** and **Deletion requester** settings. Processes every row on each run.

Property values are sent with the type your query returns them as — a number stays a number, a true or false value stays a boolean. |destination-name| fixes a property's type the first time it is written, so a column that arrives as text on its first run stays text in |destination-name| even if later runs send it as a number.

In user-properties and group-properties modes, a column whose value is null for a given row clears that property in |destination-name| rather than leaving the previous value in place. Because these modes only resend a row when something about it changes, a cleared value that was dropped instead would leave |destination-name|'s copy stale indefinitely. A column named in **Set-once properties** is an exception: a null value in one of those columns is skipped, because a write-once property has nothing to undo.

.. important:: Amperity does not send |destination-name| a deduplication key with an event, so an event that is sent twice is counted twice. Because events mode re-sends every row in the query results on each run, scope the query so that a run sends only events that have not been sent before.

.. caution:: user-deletion mode asks |destination-name| to delete each identity's data. |destination-name| schedules the request and processes it within 30 days; it can be revoked in |destination-name| until three days before its scheduled run date, after which it cannot be stopped and Amperity cannot restore the data. A successful run means |destination-name| accepted the request, not that the data is already gone — Amperity does not track the request to completion. Restrict these orchestrations to the identities you intend to delete, and see the **Delete from entire org** setting before enabling it.

.. destination-amplitude-write-modes-end


.. _destination-amplitude-cohorts:

Behavioral cohorts
====================================================

.. destination-amplitude-cohort-behavior-start

In cohort-push mode, one orchestration or campaign maintains one |destination-name| behavioral cohort, named by the **Cohort name** setting. Amperity creates the cohort on the first run and updates the same cohort on later runs of that name.

Every cohort's first run sends the full audience, in either **Cohort sync mode**, because |destination-name| assigns the cohort's identifier only on that first full send. From the second run onward, **replace** keeps re-sending the full audience and **append** sends only the members added and removed since the last run.

.. important:: |destination-name| only recognizes identities it has already seen. An identity that has never been sent through user-properties or events mode is not matched into a cohort — |destination-name| reports it as invalid, and Amperity reports those rows as failed. Send an audience's identities as user properties or events before, or alongside, pushing them into a cohort.

If the cohort is deleted in |destination-name| between runs, the next run creates a replacement cohort under the same name and continues from there. The replacement is a new cohort, so anything in |destination-name| that referenced the deleted one — a chart, a saved analysis — needs to be pointed at the new cohort.

An audience that is empty on a given run is not sent: |destination-name| rejects an empty membership, so the cohort keeps the membership it already had. This is reported as a warning in the run details rather than as a failure.

.. destination-amplitude-cohort-behavior-end


.. _destination-amplitude-volume:

Volume and rate limits
====================================================

.. destination-amplitude-limits-start

Amperity batches each write mode to |destination-name|'s own documented per-request limits and paces requests to stay inside its rate limits. Rate-limit and server-error responses are retried automatically with backoff.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Write mode
     - Limits that shape a run
   * - **user-properties**
     - |destination-name| documents no per-request limit for this endpoint. Amperity sends 100 users per request, an Amperity-side choice rather than an |destination-name| limit. |destination-name| separately throttles updates to any single user to 1,800 per hour.
   * - **events**
     - **steady-state** sends 10 events per request. **backfill** sends up to 2,000 events or 20 MB per request, |destination-name|'s documented cap for the Batch endpoint. |destination-name| throttles events for any single user to 30 per second.
   * - **group-properties**
     - |destination-name| caps a request at 1,024 groups, 1,024 group properties, and 1 MB, whichever is reached first. Amperity splits on all three.
   * - **cohort-push**
     - |destination-name| caps a request at 100,000 identifiers and a cohort at 2,000,000 members.
   * - **user-deletion**
     - |destination-name| caps a request at 100 identifiers and accepts 1 request per second, with up to 8 in flight at once.

An audience over the 2,000,000-member cohort limit is rejected before anything is sent, with a message naming the limit. This check applies when the full audience is sent — on a first run, or whenever **Cohort sync mode** is **replace**. It does not apply to **append** runs, which only ever see that run's own additions and removals and not the cohort's total size in |destination-name|.

.. note:: Limits are applied per run. Two orchestrations that send to the same |destination-name| project at the same time are not paced against each other, so overlapping schedules can reach |destination-name|'s project-wide limits sooner than either run would alone.

.. destination-amplitude-limits-end


.. _destination-amplitude-get-details:

Get details
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-amplitude-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       |checkmark-required| **Required**

       Both credential fields are required. No call can be made without them.

       **API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amplitude-api-key-start
             :end-before: .. credential-amplitude-api-key-end

       **Secret Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amplitude-secret-key-start
             :end-before: .. credential-amplitude-secret-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amplitude-find-keys-start
             :end-before: .. credential-amplitude-find-keys-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration setting**

       **Identity column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-identity-column-start
             :end-before: .. setting-amplitude-identity-column-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional destination settings**

       **Amplitude region**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-region-start
             :end-before: .. setting-amplitude-region-end

       **Set-once properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-set-once-properties-start
             :end-before: .. setting-amplitude-set-once-properties-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Orchestration settings**

       These are chosen for each orchestration that sends to this destination, not on the destination itself.

       **Write mode**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-write-mode-start
             :end-before: .. setting-amplitude-write-mode-end

       **Attribute updates only**

          |checkmark-required| **Required for every write mode except cohort-push**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-attribute-updates-only-start
             :end-before: .. setting-amplitude-attribute-updates-only-end

       **Event name column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-event-name-column-start
             :end-before: .. setting-amplitude-event-name-column-end

       **Timestamp column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-timestamp-column-start
             :end-before: .. setting-amplitude-timestamp-column-end

       **Sync cadence**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-sync-cadence-start
             :end-before: .. setting-amplitude-sync-cadence-end

       **Group type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-group-type-start
             :end-before: .. setting-amplitude-group-type-end

       **Cohort name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-cohort-name-start
             :end-before: .. setting-amplitude-cohort-name-end

       **Cohort sync mode**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-cohort-sync-mode-start
             :end-before: .. setting-amplitude-cohort-sync-mode-end

       **Cohort identifier type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-cohort-id-type-start
             :end-before: .. setting-amplitude-cohort-id-type-end

       **Cohort owner email**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-cohort-owner-email-start
             :end-before: .. setting-amplitude-cohort-owner-email-end

       **Cohort published**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-cohort-published-start
             :end-before: .. setting-amplitude-cohort-published-end

       **Amplitude app ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-app-id-start
             :end-before: .. setting-amplitude-app-id-end

       **Deletion identifier type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-deletion-id-type-start
             :end-before: .. setting-amplitude-deletion-id-type-end

       **Deletion requester**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-deletion-requester-start
             :end-before: .. setting-amplitude-deletion-requester-end

       **Delete from entire org**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-delete-from-org-start
             :end-before: .. setting-amplitude-delete-from-org-end


.. destination-amplitude-get-details-end


.. _destination-amplitude-credentials:

Configure credentials
====================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Amplitude**

.. destination-amplitude-credentials-steps-start

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

       |checkmark-required| **Required**

       Both credential fields are required.

       **API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amplitude-api-key-start
             :end-before: .. credential-amplitude-api-key-end

       **Secret Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amplitude-secret-key-start
             :end-before: .. credential-amplitude-secret-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-amplitude-find-keys-start
             :end-before: .. credential-amplitude-find-keys-end

.. destination-amplitude-credentials-steps-end


.. _destination-amplitude-add:

Add destination
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Amplitude**

.. destination-amplitude-add-steps-start

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

       **Identity column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-identity-column-start
             :end-before: .. setting-amplitude-identity-column-end

       **Amplitude region**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-region-start
             :end-before: .. setting-amplitude-region-end

       **Set-once properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-amplitude-set-once-properties-start
             :end-before: .. setting-amplitude-set-once-properties-end

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

.. destination-amplitude-add-steps-end


.. _destination-amplitude-validation:

Data validation
====================================================

.. destination-amplitude-validation-start

Amperity sends every row in the query results, except for rows it cannot build a valid request for. A row is skipped and reported as failed, and the run continues, when any of the following is true:

* The ``identity_value`` column is empty for that row, in any write mode.
* The write mode is **user-properties** or **events** and the row's ``identity_value`` is shorter than five characters. Five characters is |destination-name|'s documented minimum id length for event ingest; Amperity applies it to user properties as well. This minimum does not apply to the other three modes.
* The write mode is **events** and the **Event name column** is empty for that row.
* The write mode is **cohort-push** and |destination-name| does not recognize the identity, because it has not been sent through user-properties or events mode first.
* |destination-name| rejects the request that row belongs to.

Skipped rows are reported in the destination's run details. Identical messages are grouped with a count rather than repeated, and if a run produces more than 100 distinct messages, the rest are summarized as a count.

How much a rejection costs depends on the write mode, because |destination-name| reports failures differently per endpoint:

* In **user-properties** and **group-properties** modes, |destination-name| accepts or rejects a request as a whole and reports no per-row detail. One bad value fails every row in that request — up to 100 users, or up to 1,024 groups.
* In **events** mode, |destination-name| names the specific events it rejected. Amperity reports those as failed, then resends the rest of the batch once so that valid events are not lost alongside an invalid neighbor.
* In **cohort-push** mode, |destination-name| reports how many identifiers it matched, so only the unmatched ones are reported as failed. On an **append** run, an identifier that |destination-name| skips when removing a member is reported as a warning rather than a failure, because an identifier that is already not in the cohort is the intended end state.
* In **user-deletion** mode, every identifier in a request must already exist in |destination-name| or the whole request fails — up to 100 identities. Keep these orchestrations scoped to identities |destination-name| has already seen.

Some conditions stop the entire run instead of failing individual rows, and are caught before any data is sent:

* The query results have no ``identity_value`` column.
* **Set-once properties** names a column that is not in the query results, or names the identity column itself.
* The write mode is **events** and the **Event name column** or **Timestamp column** is missing from the query results.
* A required mode setting is not set — **Group type** in group-properties mode; **Event name column** or **Timestamp column** in events mode; **Cohort name**, **Cohort identifier type**, **Cohort owner email**, or **Amplitude app ID** in cohort-push mode; **Deletion identifier type** or **Deletion requester** in user-deletion mode.
* **Attribute updates only** is not set on a write mode that requires it, or is set on a cohort-push orchestration.
* The audience is over |destination-name|'s 2,000,000-member cohort limit, on a run that sends the full audience.

A run also stops when |destination-name| rejects the credentials, when it blocks the request, when the account's plan does not cover the endpoint being called, or when the configured **Amplitude region** does not match the project. These conditions would fail every remaining request the same way, so the run stops rather than reporting every row as failed. Rate-limit responses and transient |destination-name| server errors are retried automatically with backoff; if they persist after retries, the affected rows are reported as failed.

.. note:: If a single row carries more data than fits in one request — in group-properties mode, more than 1 MB or 1,024 properties for one group; in events mode on the **backfill** cadence, more than 20 MB for one event — the run stops with an error naming the columns involved. Unlike the conditions above, this is found while the query results are being sent, so on a large send some requests may already have reached |destination-name| before the run stops.

.. destination-amplitude-validation-end
