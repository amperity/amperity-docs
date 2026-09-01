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

Two columns are sent. The **identity_value** column (required) is the person's loyalty identity in Eagle Eye — a loyalty card number, email, or whatever identity type your company unit is configured for — and is the value every operation is addressed by. The **friendly_name** column (optional) is a human-readable label for the wallet: the create operation applies it to a new wallet when it is present, and the update operation exists to change it and requires it. Column names are matched without regard to capitalization, and values are sent to Eagle Eye as they appear in the query results.

.. destination-eagle-eye-end

.. destination-eagle-eye-api-note-start

.. note:: This destination uses the `Eagle Eye AIR Wallet API <https://developer.eagleeye.com/docs/wallets-1>`__ |ext_link|.

.. destination-eagle-eye-api-note-end

.. destination-eagle-eye-beta-start

.. admonition:: Beta

   The Eagle Eye connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-eagle-eye-beta-end

.. destination-eagle-eye-prereq-start

.. important:: Eagle Eye provisions your API credentials and configures each company unit. Before you configure the destination, get the Client ID, Client secret, and regional API URL from your Eagle Eye account manager, and confirm the **Identity type** name your unit uses and the behavioral **state** values your unit accepts. A state value your unit does not recognize is rejected.

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
     - Provisions a wallet for each person and attaches their loyalty identity. This is the default. If the ``friendly_name`` column is present, its value is set as the new wallet's label. A person who already has a wallet is recovered rather than duplicated, so re-sending the same query results is safe.
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

       **Wallet state (new wallets)**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-wallet-state-start
             :end-before: .. setting-eagle-eye-default-wallet-state-end


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

       **Wallet state (state change)**

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

       **Wallet state (new wallets)**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-eagle-eye-default-wallet-state-start
             :end-before: .. setting-eagle-eye-default-wallet-state-end

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

Failed rows are reported in the destination's run details. Some conditions stop the entire run instead of failing individual rows: an unknown wallet operation, or a **state-change** send with no **Wallet state** set (both caught before any data is sent), and a rejected credential or Eagle Eye being unavailable.

.. destination-eagle-eye-validation-end
