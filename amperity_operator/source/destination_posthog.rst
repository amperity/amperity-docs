.. https://docs.amperity.com/operator/


.. |destination-name| replace:: PostHog
.. |plugin-name| replace:: "PostHog"
.. |credential-type| replace:: "posthog"
.. |required-credentials| replace:: "Project API Key" and "Personal API Key"
.. |what-send| replace:: person and group properties, events, and deletion requests
.. |where-send| replace:: a |destination-name| project
.. |filter-the-list| replace:: "pos"


.. meta::
    :description lang=en:
        Configure Amperity to send person and group properties, events, and deletion requests to a PostHog project.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send person and group properties, events, and deletion requests to a PostHog project.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for PostHog

====================================================
Configure destinations for PostHog
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-posthog-start
   :end-before: .. term-posthog-end

.. destination-posthog-start

The PostHog connector sends |what-send| from Amperity into |where-send|. What each row becomes — a person-property update, a group-property update, a captured event, or a person deletion — is set by the **Write mode** setting on the orchestration that sends to this destination.

Each row is addressed by a single identity. The query results must include a column named ``identity_value`` that carries that identity: the PostHog ``distinct_id`` in person-properties and events modes, the group key in group-properties mode, or the person to delete in person-deletion mode. What Amperity does with the other columns depends on the write mode — see :ref:`destination-posthog-write-modes`.

Person-properties and group-properties modes sync incrementally: Amperity sends only the rows whose attributes changed since the last successful run, and reports unchanged rows as sent from cache. Events and person-deletion modes have no incremental tracking — they process every row in the query results on each run, so scope those queries to the rows you intend to send.

.. destination-posthog-end

.. important:: The connector reads each row's identity from a column named ``identity_value``. If your query produces the identity under another name, alias it — for example ``SELECT distinct_id AS identity_value``. A send whose query results have no ``identity_value`` column fails before any data is sent, with a message naming the missing column.

.. destination-posthog-api-note-start

.. note:: This destination uses the `PostHog API <https://posthog.com/docs/api>`__ |ext_link| — the capture API for property, group, and event writes, and the Persons API for person deletion.

.. destination-posthog-api-note-end

.. destination-posthog-beta-start

.. admonition:: Beta

   The PostHog connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-posthog-beta-end

.. destination-posthog-prereq-start

.. important:: A successful connection test confirms that PostHog is reachable and that both keys are well-formed. It does **not** confirm that data is landing. PostHog's capture endpoint accepts any well-formed Project API Key without verifying that it belongs to your project, so a wrong key — including a ``phs_`` Project Secret API Key — passes the test and then silently drops every record. Use the classic Project API Key (it starts with ``phc_``), and after your first run confirm that records appear on PostHog's **Persons** page.

.. note:: Configure one orchestration per write mode, each sending its own query. To send more than one write mode against the same PostHog project, configure a separate orchestration, with its own query, for each.

.. destination-posthog-prereq-end


.. _destination-posthog-write-modes:

Write modes
====================================================

.. destination-posthog-write-modes-start

The **Write mode** setting selects what each row does, and an orchestration performs a single write mode for the entire run. You choose the write mode, and its mode-specific settings, when you configure the orchestration that sends to this destination.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Write mode
     - What it sends
   * - **person-properties**
     - The default. Writes each row as properties on a PostHog person, addressed by ``identity_value`` as the ``distinct_id``. Every column other than ``identity_value`` becomes a person property, written with ``$set`` (overwrite on every run) or, for columns named in the **Set-once properties** setting, ``$set_once`` (written once, never overwritten). Syncs incrementally.
   * - **group-properties**
     - Writes each row as properties on a PostHog group, addressed by ``identity_value`` as the group key. Requires the **Group type** setting. Every column other than ``identity_value`` becomes a group property. Syncs incrementally.
   * - **events**
     - Captures each row as a PostHog event. Requires the **Event name column** and **Timestamp column** settings, which name the columns that supply the event name and event time; every column other than those two and ``identity_value`` becomes an event property. Processes every row on each run.
   * - **person-deletion**
     - Permanently deletes each row's person from PostHog, addressed by ``identity_value``. Only ``identity_value`` is used; other columns are ignored. Optionally also deletes each person's events and session recordings — see the **Delete events** and **Delete recordings** settings. Processes every row on each run.

In person-properties and group-properties modes, you can SHA-256 hash specific columns before sending with the **Hashed properties** setting. PostHog stores properties as literal, queryable values, so hash a column only when your own policy requires it — a hashed value can no longer be searched or filtered in PostHog.

.. caution:: In group-properties mode, PostHog also creates a person record for each group's key. Syncing a large number of groups adds an equal number of synthetic person records to your PostHog project, alongside the people you actually track, which can inflate person counts and clutter the Persons list. This is a property of how PostHog ingests group updates, not a setting Amperity can change.

.. caution:: person-deletion mode permanently removes each person from PostHog and cannot be undone. Restrict these orchestrations to the people you intend to delete.

.. destination-posthog-write-modes-end


.. _destination-posthog-get-details:

Get details
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-posthog-get-details-table-start

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

       **Project API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-posthog-project-api-key-start
             :end-before: .. credential-posthog-project-api-key-end

       **Personal API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-posthog-personal-api-key-start
             :end-before: .. credential-posthog-personal-api-key-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration setting**

       **Identity column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-identity-column-start
             :end-before: .. setting-posthog-identity-column-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional destination settings**

       **PostHog host**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-host-start
             :end-before: .. setting-posthog-host-end

       **Self-hosted URL**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-self-hosted-url-start
             :end-before: .. setting-posthog-self-hosted-url-end

       **Set-once properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-set-once-properties-start
             :end-before: .. setting-posthog-set-once-properties-end

       **Hashed properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-hashed-properties-start
             :end-before: .. setting-posthog-hashed-properties-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Orchestration settings**

       These are chosen for each orchestration that sends to this destination, not on the destination itself.

       **Write mode**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-write-mode-start
             :end-before: .. setting-posthog-write-mode-end

       **Group type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-group-type-start
             :end-before: .. setting-posthog-group-type-end

       **Event name column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-event-name-column-start
             :end-before: .. setting-posthog-event-name-column-end

       **Timestamp column**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-timestamp-column-start
             :end-before: .. setting-posthog-timestamp-column-end

       **Delete events**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-delete-events-start
             :end-before: .. setting-posthog-delete-events-end

       **Delete recordings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-delete-recordings-start
             :end-before: .. setting-posthog-delete-recordings-end


.. destination-posthog-get-details-end


.. _destination-posthog-credentials:

Configure credentials
====================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for PostHog**

.. destination-posthog-credentials-steps-start

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

       **Project API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-posthog-project-api-key-start
             :end-before: .. credential-posthog-project-api-key-end

       **Personal API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-posthog-personal-api-key-start
             :end-before: .. credential-posthog-personal-api-key-end

.. destination-posthog-credentials-steps-end


.. _destination-posthog-add:

Add destination
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for PostHog**

.. destination-posthog-add-steps-start

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
             :start-after: .. setting-posthog-identity-column-start
             :end-before: .. setting-posthog-identity-column-end

       **PostHog host**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-host-start
             :end-before: .. setting-posthog-host-end

       **Self-hosted URL**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-self-hosted-url-start
             :end-before: .. setting-posthog-self-hosted-url-end

       **Set-once properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-set-once-properties-start
             :end-before: .. setting-posthog-set-once-properties-end

       **Hashed properties**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-posthog-hashed-properties-start
             :end-before: .. setting-posthog-hashed-properties-end

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

.. destination-posthog-add-steps-end


.. _destination-posthog-validation:

Data validation
====================================================

.. destination-posthog-validation-start

Amperity sends every row in the query results, except for rows it cannot build a valid request for. A row is skipped and reported as failed, and the run continues, when any of the following is true:

* The ``identity_value`` column is empty for that row, in any write mode.
* The write mode is **events** and the **Event name column** is empty for that row.
* PostHog rejects the batch that row belongs to as malformed. PostHog validates a batch as a whole, so one bad value — such as a blank identity — fails every row in that batch, not only the offending row.

Skipped rows are reported in the destination's run details. In events mode, a row with an empty **Timestamp column** value is not skipped: PostHog records that event at ingest time instead of its true event time. In person-deletion mode, an identity that PostHog does not recognize — already deleted, or never present — is reported as succeeded, because the deletion is already satisfied.

Some conditions stop the entire run instead of failing individual rows, and are caught before any data is sent:

* The query results have no ``identity_value`` column.
* **Set-once properties** or **Hashed properties** names a column that is not in the query results, or names the identity column itself.
* The write mode is **events** and the **Event name column** or **Timestamp column** is missing from the query results.
* A required mode setting is not set — **Group type** in group-properties mode, or **Event name column** or **Timestamp column** in events mode.
* **PostHog host** is **self-hosted** but no **Self-hosted URL** is set.
* A single row's data is too large to send in one request.

A run also stops when PostHog rejects the credentials — a missing, invalid, or insufficiently scoped key — or when the configured **PostHog host** or **Self-hosted URL** is not valid. Rate-limit responses and transient PostHog server errors are retried automatically with backoff; if they persist after retries, the affected rows are reported as failed.

.. destination-posthog-validation-end
