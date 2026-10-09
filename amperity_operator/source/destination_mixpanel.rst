.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Mixpanel
.. |plugin-name| replace:: "Mixpanel"
.. |credential-type| replace:: "mixpanel"
.. |required-credentials| replace:: "Service account username" and "Service account secret"
.. |what-send| replace:: user profile properties, group profile properties, events, and deletion requests
.. |where-send| replace:: a |destination-name| project
.. |filter-the-list| replace:: "mix"


.. meta::
    :description lang=en:
        Configure Amperity to send user profile properties, group profile properties, events, and deletion requests to a Mixpanel project.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send user profile properties, group profile properties, events, and deletion requests to a Mixpanel project.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Mixpanel

====================================================
Configure destinations for Mixpanel
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-mixpanel-start
   :end-before: .. term-mixpanel-end

.. destination-mixpanel-start

The |destination-name| connector sends |what-send| from Amperity into |where-send|. What a destination writes is set by the **Operation** setting, and a destination performs one operation. To send more than one, configure a separate destination for each operation, each with its own query, all pointing at the same |destination-name| project.

Amperity reads a small set of fixed column names from the query results and sends every other column to |destination-name| as a property of the same name. Which fixed columns a destination needs depends on its operation — see :ref:`destination-mixpanel-operations`.

Every run sends the whole query result, not only the rows that changed since the last run. Re-sending does not duplicate data in |destination-name| — profile properties are overwritten in place, and events carry a deduplication key — but every row counts toward your |destination-name| usage. Scope each query, and choose each schedule, with that in mind.

.. destination-mixpanel-end

.. destination-mixpanel-api-note-start

.. note:: This destination uses |destination-name|'s `Ingestion API <https://docs.mixpanel.com/reference/ingestion-api>`__ |ext_link| — `Import Events <https://docs.mixpanel.com/reference/import-events>`__ |ext_link| for events, `User Profiles <https://docs.mixpanel.com/reference/profile-set>`__ |ext_link| and `Group Profiles <https://docs.mixpanel.com/reference/group-set-property>`__ |ext_link| for profile properties — and its `GDPR and CCPA API <https://docs.mixpanel.com/reference/gdpr-api>`__ |ext_link| for deletion requests.

.. destination-mixpanel-api-note-end

.. destination-mixpanel-beta-start

.. admonition:: Beta

   The |destination-name| connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-mixpanel-beta-end

.. destination-mixpanel-prereq-start

.. important:: The ``distinct_id`` that Amperity sends must be the same identifier that your own apps and website already send to |destination-name|. That is rarely the Amperity ID, so choose the column that carries your |destination-name| identifier. An identifier |destination-name| has not seen before creates a new profile rather than updating an existing one.

.. note:: Testing the connection writes nothing to your |destination-name| project. It confirms that the service account can see the project with a role that can send data, that the project is in a supported data residency, that the **Project token** belongs to that project, and — when the credential carries one — that the GDPR OAuth token works. Test the connection after changing any of those values.

.. destination-mixpanel-prereq-end


.. _destination-mixpanel-operations:

Operations
====================================================

.. destination-mixpanel-operations-start

The **Operation** setting selects what a destination writes, along with the columns its query results must contain. Column names are matched without regard to letter case, so ``DISTINCT_ID`` and ``distinct_id`` are the same column.

.. important:: A query must produce these columns under exactly these names. When yours produces them under other names, alias them — for example ``SELECT customer_id AS distinct_id``. A run whose query results are missing a column its operation requires fails before any data is sent, with a message naming each missing column.

.. list-table::
   :widths: 20 25 15 40
   :header-rows: 1

   * - Operation
     - Required columns
     - Optional columns
     - What it sends
   * - **user-profiles**
     - ``distinct_id``
     -
     - Sets properties on a |destination-name| user profile, addressed by ``distinct_id``. Every other column becomes a user profile property. A profile that does not exist yet is created.
   * - **group-profiles**
     - ``group_id``
     -
     - Sets properties on a |destination-name| group profile, addressed by ``group_id`` under the configured **Group key**. Every other column becomes a group profile property. A profile that does not exist yet is created.
   * - **events**
     - ``distinct_id``, ``event``, ``time``
     - ``insert_id``
     - Sends each row as a |destination-name| event, so that history your own apps did not send can be analyzed alongside the events they did. Every column other than the four named here becomes an event property.
   * - **deletions**
     - ``distinct_id``
     -
     - Files a GDPR or CCPA deletion request for each user named by ``distinct_id``. |destination-name| deletes everything it holds about those users, including their events and profile data.

What each fixed column carries:

* ``distinct_id`` — the user's identifier in |destination-name|.
* ``group_id`` — the group's identifier, such as a company ID, under the configured **Group key**.
* ``event`` — the event's name, such as ``Purchase``.
* ``time`` — when the event happened. A date and time, a date on its own (read as midnight UTC), or a Unix timestamp in seconds or milliseconds.
* ``insert_id`` — an optional per-event identifier that |destination-name| uses to recognize duplicates. See :ref:`destination-mixpanel-values`.

.. caution:: The **deletions** operation cannot be undone. |destination-name| deletes every event and profile it holds for each identifier sent, and once it begins processing a request the deletion cannot be reversed. Restrict a deletions destination to the users you intend to delete, and review its query before every run.

.. note:: A deletions run files the requests and records the request IDs that |destination-name| returns; those IDs appear in the run's output and are your audit trail. |destination-name| can take up to 30 days to complete a deletion request, and Amperity does not track a request to completion — a successful run means the requests were accepted, not that the data is already gone. |destination-name| allows a request to be canceled until it begins processing, and those request IDs are what identify it there; Amperity cannot cancel a request it has filed.

.. destination-mixpanel-operations-end


.. _destination-mixpanel-residency:

Data residency
====================================================

.. destination-mixpanel-residency-start

|destination-name| hosts projects in the United States, the European Union, and India. Amperity asks |destination-name| which residency hosts your project at the start of every run and sends that run to the matching host. There is no region setting to configure.

This is deliberate. Data sent to the wrong |destination-name| region is answered with a success response and then discarded, with no error to notice, so a region setting that disagreed with the project would lose data silently. A project hosted in a residency Amperity has no host for stops the run with an error naming the domain |destination-name| reported.

.. destination-mixpanel-residency-end


.. _destination-mixpanel-values:

How values are sent
====================================================

.. destination-mixpanel-values-start

Every column that is not one of the fixed columns for the destination's operation is sent to |destination-name| as a property with the same name. Return only the columns you want written — a column that is in the query results is a property in |destination-name|.

**Values keep the type the query returns.** A decimal column is sent as a number rather than as text, so that |destination-name| can use it in calculations. A value that does not parse as the type its column declares is sent as it came, rather than failing the row.

**Date and time values are sent in UTC**, in the format |destination-name| documents for date properties. Amperity reformats a column it holds as a date-time value into that format; a column it holds as a date already matches it. A text column is sent exactly as it reads — |destination-name| decides whether a value is a date from the value's own format rather than from the column it came from, so a date kept as text arrives as a date only when the text already matches that format. Give a column a date or date-time type in Amperity when you want it to arrive as one reliably.

**Empty cells are left out.** A column with no value for a row, or one holding only whitespace, is omitted from that row's update rather than sent as an empty value. Sending an empty value would overwrite whatever |destination-name| already holds for that property, and an empty cell in Amperity is not a request to clear a value. To clear a property in |destination-name|, change it there.

**Dates are displayed in the project's own timezone.** |destination-name| shows a value sent as 10:00 UTC as 03:00 in a project set to US Pacific. The stored value is correct.

**Identifiers are sent as text.** A numeric ``distinct_id`` or ``group_id`` is converted to its string form, because |destination-name| rejects a numeric identifier on the events endpoint.

**Events are deduplicated.** |destination-name| recognizes a repeated event by its ``$insert_id``. When the query results include an ``insert_id`` column, Amperity sends that value; when they do not, Amperity derives one from the event's own contents, so re-sending the same row does not count the event twice. An ``insert_id`` that |destination-name| would not accept intact — longer than 36 bytes, or containing anything other than letters, digits, and hyphens — is replaced by a stable value derived from it, so that two similar identifiers are not silently treated as the same event.

.. note:: |destination-name| shortens any text value longer than 255 characters.

.. destination-mixpanel-values-end


.. _destination-mixpanel-volume:

Volume and rate limits
====================================================

.. destination-mixpanel-limits-start

Amperity batches each operation to |destination-name|'s own documented per-request limits and paces requests to stay inside its rate limits. Rate-limit responses and transient |destination-name| server errors are retried automatically with backoff.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Operation
     - Limits that shape a run
   * - **user-profiles** and **group-profiles**
     - |destination-name| accepts up to 2,000 profile updates per request and caps a single update at 1 MB.
   * - **events**
     - |destination-name| accepts up to 2,000 events per request and caps a request at 10 MB and a single event at 1 MB. It also rejects an event carrying more than 255 properties, so a very wide query can fail on events where it would succeed on profiles.
   * - **deletions**
     - |destination-name| accepts up to 1,999 identifiers per deletion request and one deletion request per second, which places a ceiling of roughly seven million users an hour on a deletions run.

|destination-name| applies a per-project ingestion rate limit that your own apps and website share, and a large run draws on that same limit. Amperity paces its requests and backs off when |destination-name| reports a rate limit, but schedule large sends outside the hours when your own traffic peaks.

.. note:: An event must fall inside the project's data retention window, and |destination-name| rejects an event dated more than an hour in the future. Rows outside those bounds are reported as failed.

.. note:: Limits apply per run. Two destinations sending to the same |destination-name| project at the same time are not paced against each other, so overlapping schedules can reach the project's limits sooner than either run would alone.

.. destination-mixpanel-limits-end


.. _destination-mixpanel-get-details:

Get details
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-mixpanel-get-details-table-start

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

       The service account username and secret are required. The **GDPR OAuth token** is required only when **Operation** is **deletions**.

       **Service account username**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-mixpanel-service-account-username-start
             :end-before: .. credential-mixpanel-service-account-username-end

       **Service account secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-mixpanel-service-account-secret-start
             :end-before: .. credential-mixpanel-service-account-secret-end

       **GDPR OAuth token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-mixpanel-gdpr-oauth-token-start
             :end-before: .. credential-mixpanel-gdpr-oauth-token-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required destination settings**

       **Project ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-project-id-start
             :end-before: .. setting-mixpanel-project-id-end

       **Project token**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-project-token-start
             :end-before: .. setting-mixpanel-project-token-end

       **Operation**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-operation-start
             :end-before: .. setting-mixpanel-operation-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Operation-specific destination settings**

       **Group key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-group-key-start
             :end-before: .. setting-mixpanel-group-key-end

       **Compliance type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-compliance-type-start
             :end-before: .. setting-mixpanel-compliance-type-end


.. destination-mixpanel-get-details-end


.. _destination-mixpanel-credentials:

Configure credentials
====================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Mixpanel**

.. destination-mixpanel-credentials-steps-start

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

       The service account username and secret are required. The **GDPR OAuth token** is required only for a destination whose **Operation** is **deletions**.

       **Service account username**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-mixpanel-service-account-username-start
             :end-before: .. credential-mixpanel-service-account-username-end

       **Service account secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-mixpanel-service-account-secret-start
             :end-before: .. credential-mixpanel-service-account-secret-end

       **GDPR OAuth token**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-mixpanel-gdpr-oauth-token-start
             :end-before: .. credential-mixpanel-gdpr-oauth-token-end

.. destination-mixpanel-credentials-steps-end


.. _destination-mixpanel-add:

Add destination
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Mixpanel**

.. destination-mixpanel-add-steps-start

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

       **Project ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-project-id-start
             :end-before: .. setting-mixpanel-project-id-end

       **Project token**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-project-token-start
             :end-before: .. setting-mixpanel-project-token-end

       **Operation**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-operation-start
             :end-before: .. setting-mixpanel-operation-end

       **Group key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-group-key-start
             :end-before: .. setting-mixpanel-group-key-end

       **Compliance type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-mixpanel-compliance-type-start
             :end-before: .. setting-mixpanel-compliance-type-end

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

.. destination-mixpanel-add-steps-end


.. _destination-mixpanel-validation:

Data validation
====================================================

.. destination-mixpanel-validation-start

Amperity sends every row in the query results, except for rows it cannot build a valid request for. A row is skipped and reported as failed, and the run continues, when any of the following is true:

* The row's identifier — ``distinct_id``, or ``group_id`` for the **group-profiles** operation — is empty.
* The row's identifier is a placeholder rather than a real identifier. Amperity drops values such as ``null``, ``undefined``, ``unknown``, ``anonymous``, ``none``, ``n/a``, ``0``, ``-1``, ``true``, ``false``, and an all-zero UUID, matched without regard to letter case. |destination-name| rejects most of these on its events endpoint, but its profile endpoints accept them and gather every such row onto a single profile named after the placeholder — so Amperity drops them for every operation.
* The operation is **events** and the row has no event name, or its ``time`` value cannot be read as a date and time, a date, or a Unix timestamp in seconds or milliseconds.
* The row is larger than |destination-name|'s 1 MB limit for a single record.
* |destination-name| rejects that individual row — for example an event outside the project's retention window, or one carrying more than 255 properties.

Skipped rows are reported in the destination's run details. Identical messages are grouped with a count rather than repeated, and a run that produces more than 100 distinct messages summarizes the rest as a count.

One rejected row does not fail the rows alongside it. |destination-name| validates each record in a request on its own and stores the valid ones even when it reports the request as failed, and Amperity reads each response record by record — counting the rows |destination-name| accepted as sent and reporting only the rows it rejected. A request that |destination-name| refuses outright, such as one that is malformed, fails every row in that request instead.

Some conditions stop the entire run, and are caught before any data is sent:

* A column the operation requires is missing from the query results. The error names each missing column.
* The operation is **group-profiles** and the **Group key** setting is not set.
* The operation is **deletions** and the connected credential has no GDPR OAuth token.
* The service account cannot see the project named by **Project ID**, because the ID is wrong or the service account has not been added to that project.
* The service account's role on the project cannot send data. The error names the role it found.
* The project is hosted in a data residency this connector does not support.

A run also stops when |destination-name| rejects the service account, or refuses a request because the service account no longer holds the Owner or Admin role. These conditions would fail every remaining request the same way, so the run stops rather than reporting every row as failed. The rows already reported as failed keep their reasons in the run details.

.. destination-mixpanel-validation-end
