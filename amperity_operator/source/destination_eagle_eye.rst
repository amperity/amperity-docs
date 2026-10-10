.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Eagle Eye
.. |plugin-name| replace:: "Eagle Eye"
.. |credential-type| replace:: "eagle-eye"
.. |required-credentials| replace:: "Client ID", "Client secret", and "API URL"
.. |what-send| replace:: loyalty identities
.. |where-send| replace:: loyalty wallets in the |destination-name| AIR platform
.. |filter-the-list| replace:: "eag"


.. meta::
    :description lang=en:
        Configure Amperity to send loyalty identities to wallets in the Eagle Eye AIR platform.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send loyalty identities to wallets in the Eagle Eye AIR platform.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Eagle Eye

====================================================
Configure destinations for Eagle Eye
====================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-eagle-eye-start
   :end-before: .. term-eagle-eye-end

.. destination-eagle-eye-start

The Eagle Eye connector sends |what-send| from Amperity into |where-send|, performing one wallet operation for each person on every run.

Each row in the query results is one wallet operation, addressed by the person's loyalty identity. There is no audience or list concept: Amperity does not keep a list in sync on the Eagle Eye side, it performs the configured operation for each person each time it runs. Amperity sends every row in the query results on each run; there is no incremental sync.

Two columns are sent, and the query that feeds the orchestration must produce them by name. The **identity_value** column (required) carries the person's loyalty identity in Eagle Eye — a loyalty card number, email, or whatever identity type your company unit is configured for — and is the value every operation is addressed by. The **friendly_name** column (optional) is a human-readable label for the wallet: the create operation applies it to a new wallet when it is present, and the update operation exists to change it and requires it. Column names are matched without regard to capitalization.

The **create** operation can also attach other identities to each wallet and enroll each person in loyalty schemes, using more columns named after the **Additional identity types** and **Loyalty scheme IDs** settings. See :ref:`destination-eagle-eye-identities-schemes`.

Every value is sent to Eagle Eye as text. An integer column, such as a card number stored as a number, is sent as its digits. Floating-point columns are not supported for identity values, because large numbers are written in scientific notation (for example ``1.0E10``) rather than as the card number. Cast such columns to a string or an integer in the query.

.. important:: The connector reads the loyalty identity from a column named ``identity_value`` — not from the **Identity type** setting. These are two different things and are easy to confuse:

   * The **Identity type** setting names the Eagle Eye identity *type* your company unit uses (for example ``CUSTOMER_ID``). You set it once on the destination.
   * The ``identity_value`` column carries the identity *values*, one per row. The query results must include a column with this exact name (capitalization does not matter).

   If your query outputs the values under a different column name, alias it to ``identity_value`` — for example ``SELECT loyalty_card_number AS identity_value``. A send whose query results have no ``identity_value`` column fails before any wallet is sent, with a message naming the missing column.

.. destination-eagle-eye-end

.. destination-eagle-eye-api-note-start

.. note:: This destination uses the `Eagle Eye AIR Wallet API <https://developer.eagleeye.com/docs/wallets-1>`__ |ext_link|.

.. destination-eagle-eye-api-note-end

.. destination-eagle-eye-beta-start

.. admonition:: Beta

   The Eagle Eye connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-eagle-eye-beta-end

.. destination-eagle-eye-prereq-start

.. important:: Eagle Eye provisions your API credentials and configures each company unit. Before you configure the destination, get the Client ID, Client secret, and regional API URL from your Eagle Eye account manager, and confirm the **Identity type** name your unit uses and the behavioral **state** values your unit accepts for wallets and for identities — these are separate value sets that need not overlap. A state value your unit does not recognize is rejected. If you attach more identity types or enroll people in loyalty schemes, also confirm those identity type names, your unit's loyalty scheme IDs, and the state values it accepts for scheme accounts, which are a third, separate value set.

.. note:: Wallet state and identity state were previously a single setting. If you set a state value on this destination before they were separated, that value now applies to **New wallet state** only. If it is an identity-namespace value — and your create sends were failing as a result — move it to **New identity state**.

.. note:: The Eagle Eye Wallet API has no bulk endpoint, so Amperity sends one request per person. Amperity paces requests at about five requests per second — an Amperity-side default, not a limit published by Eagle Eye — so a large send can take a long time (for example, a send of 100,000 people runs for several hours).

.. destination-eagle-eye-prereq-end


.. _destination-eagle-eye-operations:

Wallet operations
====================================================

.. destination-eagle-eye-operations-start

The **Wallet operation** setting selects what each row does, and a send performs a single operation for the entire run. You choose the operation, and the state used by state-change, when you configure the orchestration that sends to this destination.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Operation
     - What it does
   * - **create**
     - Provisions a wallet for each person and attaches their loyalty identity. This is the default. If the ``friendly_name`` column is present, its value is set as the new wallet's label. When **Additional identity types** or **Loyalty scheme IDs** is set, it also attaches the person's other identities and enrolls them in their loyalty schemes. A person who already has a wallet is recovered rather than duplicated, so re-sending the same query results is safe, and a re-send attaches anything the wallet is still missing.
   * - **update**
     - Changes a wallet's friendly name. Requires the ``friendly_name`` column.
   * - **state-change**
     - Changes a wallet's behavioral state. Requires the **Wallet state** setting.
   * - **suspend**
     - Temporarily halts a wallet's activity. Reversible with **activate**.
   * - **activate**
     - Returns a suspended or inactive wallet to service.
   * - **terminate**
     - Permanently closes a wallet. It cannot be undone, and Eagle Eye rejects any later change to a terminated wallet. It is the recommended operation for a consent-driven hard opt-out.
   * - **delete**
     - A soft delete on Eagle Eye's side: removes the wallet from active use but does not erase it. Intended for cleaning up test data, not for consent or data-subject requests — use **terminate** for those.

Every operation other than **create** first looks up the person's existing wallet by their identity value. A person with no wallet yet is reported as a failed row and the run continues.

.. destination-eagle-eye-operations-end


.. _destination-eagle-eye-identities-schemes:

Additional identities and loyalty schemes
====================================================

.. destination-eagle-eye-identities-schemes-start

The **create** operation can attach more than one identity to each wallet, such as a customer ID, a loyalty card, and an email address, and can enroll each person in one or more loyalty schemes. Two optional destination settings list what to attach, and the query results carry one column for each listed item:

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Column
     - Required
     - What it holds
   * - ``identity_value_<type>``
     - Yes, for **create**, one for each type in **Additional identity types**
     - The person's identity value of that type, for example ``identity_value_card`` for ``CARD``. A blank value means the person has no identity of that type.
   * - ``identity_state_<type>``
     - No
     - The state for that identity, from your unit's identity-state values. A blank value lets Eagle Eye apply that identity type's default state.
   * - ``scheme_state_<id>``
     - Yes, for **create**, one for each ID in **Loyalty scheme IDs**
     - The person's account state in that loyalty scheme, for example ``scheme_state_1234567``, from your unit's scheme-account state values. A state enrolls the person in the scheme in that state. A blank value means the person is not enrolled in that scheme.

The identity type or scheme ID is written in lower case in the column name, and column names are matched without regard to capitalization. The columns must be present in the query results for the **create** operation, but individual values may be blank. Every other operation ignores them.

For example, with **Identity type** set to ``CUSTOMER_ID``, **Additional identity types** set to ``CARD,EMAIL``, and **Loyalty scheme IDs** set to ``1234567``, where ``points_scheme_state`` holds each person's scheme-account state:

.. code-block:: sql
   :linenos:

   SELECT
     customer_id AS identity_value
     ,loyalty_card_number AS identity_value_card
     ,email AS identity_value_email
     ,points_scheme_state AS scheme_state_1234567
   FROM Customer_360

**How each send behaves**

* **New people.** Amperity creates the wallet with all of the person's identities and scheme accounts in a single request.
* **People who already have a wallet.** Amperity attaches the identities and scheme accounts the wallet is missing, and leaves the ones it already has. To add identities or schemes to existing wallets, add the columns and send with the **create** operation again.
* **Changed states.** When a person already has a scheme account or an identity, and the query results give it a different state, Amperity changes the state in Eagle Eye. A blank value never changes anything, so a blank scheme column never removes a person from a scheme. The state of the main identity comes from the **New identity state** setting and applies to new wallets only.
* **Identity values.** Eagle Eye compares identity values without regard to capitalization, and so does Amperity. A value repeated across a person's identity columns is sent once.

**When Eagle Eye rejects part of a person's wallet**

If Eagle Eye saves the wallet but will not attach one of the person's identities (for example, because the value already belongs to another wallet, or the identity type is not configured for your unit), will not enroll them in a scheme (for example, because the scheme ID is unknown or the state is not accepted), or will not change a state, the row still counts as succeeded. The reason is listed in the error log for the run, naming the identity type or scheme ID, and never the identity value. Correct the setting or the values, and then send again with the **create** operation to attach what is still missing.

.. note:: Eagle Eye keeps the identity values of a deleted wallet reserved, so a person whose wallet was deleted cannot receive a new wallet with the same identity value. When Amperity confirms this, the row fails with a message saying that the identity belongs to a deleted wallet and cannot be reused.

.. note:: Sending to people who already have a wallet takes a few more requests per person than creating new wallets, because Amperity checks what each wallet already has before attaching anything.

.. destination-eagle-eye-identities-schemes-end


.. _destination-eagle-eye-get-details:

Get details
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-eagle-eye-get-details-table-start

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

       All three credential fields are required. No call can be made without them.

       **Client ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-eagle-eye-client-id-start
             :end-before: .. credential-eagle-eye-client-id-end

       **Client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-eagle-eye-client-secret-start
             :end-before: .. credential-eagle-eye-client-secret-end

       **API URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-eagle-eye-api-url-start
             :end-before: .. credential-eagle-eye-api-url-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration setting**

       **Identity type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-identity-type-start
             :end-before: .. setting-eagle-eye-identity-type-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - **Optional destination settings**

       **Wallet type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-wallet-type-start
             :end-before: .. setting-eagle-eye-default-wallet-type-end

       **New wallet state**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-wallet-state-start
             :end-before: .. setting-eagle-eye-default-wallet-state-end

       **New identity state**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-identity-state-start
             :end-before: .. setting-eagle-eye-default-identity-state-end

       **Additional identity types**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-additional-identity-types-start
             :end-before: .. setting-eagle-eye-additional-identity-types-end

       **Loyalty scheme IDs**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-scheme-ids-start
             :end-before: .. setting-eagle-eye-scheme-ids-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 4.
          :align: center
          :class: no-scaled-link
     - **Orchestration settings**

       These are chosen for each orchestration that sends to this destination, not on the destination itself.

       **Wallet operation**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-operation-start
             :end-before: .. setting-eagle-eye-operation-end

       **Wallet state**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-wallet-state-start
             :end-before: .. setting-eagle-eye-wallet-state-end


.. destination-eagle-eye-get-details-end


.. _destination-eagle-eye-credentials:

Configure credentials
====================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Eagle Eye**

.. destination-eagle-eye-credentials-steps-start

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

       All three credential fields are required.

       **Client ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-eagle-eye-client-id-start
             :end-before: .. credential-eagle-eye-client-id-end

       **Client secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-eagle-eye-client-secret-start
             :end-before: .. credential-eagle-eye-client-secret-end

       **API URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-eagle-eye-api-url-start
             :end-before: .. credential-eagle-eye-api-url-end

.. destination-eagle-eye-credentials-steps-end


.. _destination-eagle-eye-add:

Add destination
====================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Eagle Eye**

.. destination-eagle-eye-add-steps-start

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

       **Identity type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-identity-type-start
             :end-before: .. setting-eagle-eye-identity-type-end

       **Wallet type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-wallet-type-start
             :end-before: .. setting-eagle-eye-default-wallet-type-end

       **New wallet state**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-wallet-state-start
             :end-before: .. setting-eagle-eye-default-wallet-state-end

       **New identity state**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-identity-state-start
             :end-before: .. setting-eagle-eye-default-identity-state-end

       **Additional identity types**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-additional-identity-types-start
             :end-before: .. setting-eagle-eye-additional-identity-types-end

       **Loyalty scheme IDs**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-scheme-ids-start
             :end-before: .. setting-eagle-eye-scheme-ids-end

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

.. destination-eagle-eye-add-steps-end


.. _destination-eagle-eye-validation:

Data validation
====================================================

.. destination-eagle-eye-validation-start

Amperity performs the configured operation for every row in the query results, except for rows it cannot process. A row is reported as failed, and the run continues, when any of the following is true:

* The ``identity_value`` column is empty for that row.
* The operation is **update** and the ``friendly_name`` column is empty for that row.
* The operation is anything other than **create** and Eagle Eye has no wallet for that row's identity value.
* Eagle Eye rejects that row's wallet payload, or the row targets a wallet that has already been terminated.
* Eagle Eye reports a conflict, or a locked wallet, for that row's operation.
* The operation is **create** and the person's wallet was deleted, so their identity value cannot be reused.

Failed rows are reported in the destination's run details. A row whose wallet is saved but whose additional identity, scheme account, or state change Eagle Eye rejects counts as succeeded, and the reason is listed in the error log for the run. See :ref:`destination-eagle-eye-identities-schemes`.

Some conditions stop the entire run instead of failing individual rows: query results with no ``identity_value`` column (or no ``friendly_name`` column when the operation is **update**), query results missing an ``identity_value_<type>`` or ``scheme_state_<id>`` column for a type or scheme listed in the settings when the operation is **create**, an **Additional identity types** setting that repeats the **Identity type**, an unknown wallet operation, or a **state-change** send with no **Wallet state** set (all caught before any data is sent), and a rejected credential or Eagle Eye being unavailable. Campaigns report a missing column, or an **Additional identity types** setting that repeats the **Identity type**, while you edit the campaign.

.. destination-eagle-eye-validation-end
