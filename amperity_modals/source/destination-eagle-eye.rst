.. /downloads/markdown/


.. |destination-name| replace:: Eagle Eye
.. |what-send| replace:: loyalty identities
.. |where-send| replace:: loyalty wallets in the |destination-name| AIR platform


Eagle Eye
==================================================

Send |what-send| from Amperity into |where-send|, performing one wallet operation for each person on every run. The **Wallet operation** setting selects what each row does — create, update, state-change, suspend, activate, terminate, or delete — and a send performs a single operation for the entire run.

.. admonition:: Beta

   The Eagle Eye connector is currently in beta. Contact your Amperity representative to learn more.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

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


Settings
==================================================

**Name and description**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-name-and-description-start
   :end-before: .. setting-common-name-and-description-end

**Business user access**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-allow-start
   :end-before: .. setting-common-business-user-access-allow-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-business-user-access-restrict-pii-start
   :end-before: .. setting-common-business-user-access-restrict-pii-end

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

**Wallet operation**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-eagle-eye-operation-start
   :end-before: .. setting-eagle-eye-operation-end

**Wallet state (state change)**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-eagle-eye-wallet-state-start
   :end-before: .. setting-eagle-eye-wallet-state-end
