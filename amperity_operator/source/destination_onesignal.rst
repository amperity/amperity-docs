.. https://docs.amperity.com/operator/


.. |destination-name| replace:: OneSignal
.. |plugin-name| replace:: "OneSignal"
.. |credential-type| replace:: "onesignal"
.. |required-credentials| replace:: "App API Key"
.. |what-send| replace:: customer attributes
.. |where-send| replace:: a |destination-name| app
.. |filter-the-list| replace:: "one"


.. meta::
    :description lang=en:
        Configure Amperity to send customer attributes to a OneSignal app as data tags.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send customer attributes to a OneSignal app as data tags.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for OneSignal

====================================================
Configure destinations for OneSignal
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-onesignal-start
   :end-before: .. term-onesignal-end

.. destination-onesignal-start

The OneSignal connector sends |what-send| from Amperity into |where-send|, where they are stored on each person as data tags. Your |destination-name| team then builds audiences and personalizes messages using those tags.

Each row in the query results is one person. The ``external_id`` column supplies that person's |destination-name| External ID, which is how Amperity and |destination-name| agree on who is who. Every other column except ``email`` and ``phone`` is sent as a data tag — see :ref:`destination-onesignal-data-tags`. An ``email`` or ``phone`` value creates a subscription on that person instead — see :ref:`destination-onesignal-subscriptions`.

Amperity syncs attributes incrementally. Only the rows whose attributes changed since the last successful run are sent, and unchanged rows are reported as sent from cache. Each row is upserted: a person is created when no |destination-name| user carries that External ID, and updated when one does.

.. destination-onesignal-end

.. important:: This connector does not create or manage a list or segment in |destination-name|. |destination-name| segments are defined by filter rules rather than by a membership list, so there is nothing for Amperity to add people to. Amperity writes the data tags, and you build the segments that filter on them. To act on an Amperity audience in |destination-name|, create a |destination-name| segment that filters on the tag Amperity sends.

.. destination-onesignal-api-note-start

.. note:: This destination uses the `OneSignal REST API <https://documentation.onesignal.com/reference/rest-api-overview>`__ |ext_link|, sending each person with `Create user <https://documentation.onesignal.com/reference/create-user>`__ |ext_link|.

.. destination-onesignal-api-note-end

.. destination-onesignal-beta-start

.. admonition:: Beta

   The OneSignal connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-onesignal-beta-end

.. destination-onesignal-prereq-start

.. important:: The connector reads each row's External ID from a column named ``external_id``. If your query produces the identifier under another name, alias it — for example ``SELECT amperity_id AS external_id``. A send whose query results have no ``external_id`` column fails before any data is sent, with a message naming the missing column.

.. important:: Column names are matched exactly, in lower case. ``external_id``, ``email``, and ``phone`` are recognized only when spelled that way, and a column spelled any other way is not recognized even though it passes validation. An identifier column under another spelling stops the send, and an ``email`` or ``phone`` column under another spelling is written as a data tag instead of creating a subscription. Alias these columns in your query when your source data spells them differently.

.. note:: A successful connection test confirms that the App API Key can reach the app named by the **App ID** setting, by requesting that app's configuration. Amperity runs the test when the destination is configured, so a key and App ID that do not belong to the same app surface then rather than during the first send.

.. caution:: Amperity writes data tags named after the columns in your query results. If your own app or website also writes tags with those names through a |destination-name| SDK, the last write wins and the values become unpredictable. Treat the tag names this destination manages as owned by Amperity, and do not write them from another source.

.. note:: |destination-name| has no bulk endpoint for users, so Amperity sends one request per changed person, several at a time. A large send takes proportionally longer than a destination that uploads all of its records in one operation.

.. destination-onesignal-prereq-end


.. _destination-onesignal-data-tags:

Data tags
====================================================

.. destination-onesignal-data-tags-start

Every column in the query results except ``external_id``, ``email``, and ``phone`` is sent to |destination-name| as a data tag. The column name becomes the tag name and the column value becomes the tag value.

* **Tag values are sent as strings.** Numbers, dates, and boolean values are converted to their string form. Build the exact string you want to see in |destination-name| in your query.
* **Tags are merged, not replaced.** |destination-name| keeps any tag that a request does not name, so sending a subset of a person's attributes never clears the rest.
* **An empty value removes the tag.** When a column is empty or null for a row, Amperity sends that tag with an empty value, which is how |destination-name| deletes it. This keeps an attribute that was cleared in Amperity from leaving a stale value behind in |destination-name|.
* **Some tag names are reserved.** |destination-name| uses ``message``, ``notification``, ``subscription``, ``user``, ``template``, ``app``, ``org``, ``dynamic_content``, ``data_feed``, ``journey``, and ``custom_data`` internally for message personalization. Do not return columns with those names.

.. caution:: |destination-name| limits how many distinct data tags a person can carry, and the limit depends on your |destination-name| plan. Exceeding the limit stops the run — |destination-name| rejects the write, nothing from the rejected request is applied, and every remaining row is likely to reach the same limit. Check your |destination-name| plan's data tag allowance before sending a wide set of attributes. Returning fewer columns prevents the next run from adding tags, but it does not bring a person who is already at the limit back under it: |destination-name| accepts no new tag for that person until tags are removed from them.

.. destination-onesignal-data-tags-end


.. _destination-onesignal-subscriptions:

Subscriptions
====================================================

.. destination-onesignal-subscriptions-start

Two columns are treated as subscriptions rather than as data tags.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Column
     - What it creates
   * - ``email``
     - An Email subscription on the person, using the column value as the email address.
   * - ``phone``
     - An SMS subscription on the person, using the column value as the phone number.

Both columns are optional. A row that has neither still updates that person's data tags, and a row whose ``email`` or ``phone`` is empty is sent without that subscription rather than with an empty one.

Sending the same address or number on every run is safe. |destination-name| identifies a subscription by its value, so repeated runs update the existing subscription instead of accumulating duplicates.

.. important:: ``phone`` must be in E.164 format: a leading plus sign, then the country code, then the national number, with no spaces, dashes, or parentheses. For example, ``+12065551234``. Amperity sends the value as your query produces it, apart from removing surrounding whitespace, so a national number (``2065551234``), a formatted number (``(206) 555-1234``), or a number with no country code is rejected by |destination-name|. ``email`` is sent the same way, with no normalization. A rejected value fails the whole row, which means that person's data tags are not written either, so normalize these columns in your query when your source data is not already in the required form.

.. note:: Amperity cannot create push subscriptions. A push token is issued to a device or browser by a |destination-name| SDK and cannot be created from a server, so a push audience is registered by your own app or website rather than by this destination. Amperity creates Email and SMS subscriptions only.

.. destination-onesignal-subscriptions-end


.. _destination-onesignal-get-details:

Get details
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-onesignal-get-details-table-start

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

       The credential field is required. No call can be made without it.

       **App API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-onesignal-api-key-start
             :end-before: .. credential-onesignal-api-key-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **App ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-onesignal-app-id-start
             :end-before: .. setting-onesignal-app-id-end

       **User identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-onesignal-user-identifier-start
             :end-before: .. setting-onesignal-user-identifier-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Query results**

       The query that sends to this destination must return a column named ``external_id``. Every other column except ``email`` and ``phone`` becomes a data tag named after that column, so the set of columns you return is the set of attributes that reach |destination-name|. These three names are matched exactly, in lower case.

       Check your |destination-name| plan's data tag allowance before you decide how many columns to return, avoid the tag names |destination-name| reserves, and make sure ``phone`` values are in E.164 format.


.. destination-onesignal-get-details-end


.. _destination-onesignal-credentials:

Configure credentials
====================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for OneSignal**

.. destination-onesignal-credentials-steps-start

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

       **App API Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-onesignal-api-key-start
             :end-before: .. credential-onesignal-api-key-end

.. destination-onesignal-credentials-steps-end


.. _destination-onesignal-add:

Add destination
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for OneSignal**

.. destination-onesignal-add-steps-start

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

       **App ID**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-onesignal-app-id-start
             :end-before: .. setting-onesignal-app-id-end

       **User identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-onesignal-user-identifier-start
             :end-before: .. setting-onesignal-user-identifier-end

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

.. destination-onesignal-add-steps-end


.. _destination-onesignal-validation:

Data validation
====================================================

.. destination-onesignal-validation-start

Amperity sends every changed row, except for rows it cannot build a valid request for. A row is reported as failed, and the run continues, when any of the following is true:

* The ``external_id`` column is empty for that row, so the person cannot be addressed in |destination-name|.
* The row's External ID already belongs to a different |destination-name| user. This usually means a duplicate value in the identifier column, or an External ID that was previously assigned to another user.
* |destination-name| rejects that row's request as malformed, most often because of an ``email`` or ``phone`` value it does not accept. The whole row fails, so that person's data tags are not written either.
* |destination-name| rejects that row as a conflict for any other reason. Only that row is affected, and the rest of the run continues.

Failed rows are reported in the destination's run details. A run shows at most 25 distinct error messages; the failed-row count still reflects every failure, so a problem affecting many rows does not bury the output in copies of one message.

Some conditions stop the entire run instead of failing individual rows:

* The query results have no ``external_id`` column. This is caught before any data is sent.
* |destination-name| rejects the App API Key. Confirm that the connected credential uses an App API Key from **Settings > Keys & IDs**.
* The App API Key is valid but does not grant access to the configured **App ID**. Confirm that the key and the App ID come from the same |destination-name| app.
* A person's data tags would exceed the allowance on your |destination-name| plan. Nothing from the rejected request is applied.

Each of these is a property of the credential, the settings, or the |destination-name| plan rather than of one row, so every remaining row would fail the same way. Amperity stops the run rather than working through the rest of the query results.

.. note:: A run that stops partway has already written the rows it sent before the failure. Amperity completes the requests that are in flight and then stops, so those people are updated in |destination-name| and the rest are not.

Rate-limit responses and transient |destination-name| server errors are retried automatically with backoff. Rows affected by errors that persist after the retries are reported as failed.

.. destination-onesignal-validation-end
