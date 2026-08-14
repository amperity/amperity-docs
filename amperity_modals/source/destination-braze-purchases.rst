.. /downloads/markdown/


.. |destination-name| replace:: Braze
.. |what-send| replace:: purchase events
.. |where-send| replace:: |destination-name|


Braze Purchases
==================================================

Send purchase events to |destination-name| using the Braze REST API. Each row returned by your query is sent as a single Braze purchase object and is matched to a Braze user profile by the identifier you choose.

.. caution:: Braze records and bills for every purchase you send as a data point. Amperity sends each row in the query result on every run and does not de-duplicate purchases against previous runs. Bound your query to recent purchases and avoid re-sending rows you have already sent, or Braze counts the revenue more than once.

.. admonition:: Beta

   The Braze Purchases connector is currently in beta. Contact your Amperity representative to learn more.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**REST API key**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-braze-purchases-api-key-start
   :end-before: .. credential-braze-purchases-api-key-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-braze-purchases-api-find-key-start
   :end-before: .. credential-braze-purchases-api-find-key-end


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

**Instance**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-braze-purchases-instance-start
   :end-before: .. setting-braze-purchases-instance-end

**User identifier**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-braze-user-identifier-start
   :end-before: .. setting-braze-user-identifier-end

**Update existing profiles only?**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-braze-purchases-update-existing-only-start
   :end-before: .. setting-braze-purchases-update-existing-only-end
