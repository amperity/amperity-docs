.. /downloads/markdown/


.. |destination-name| replace:: Attentive
.. |file-format| replace:: CSV
.. |sftp-hostname| replace:: "ftp5.attentivemobile.com"
.. |remote-folder| replace:: "/uploads"
.. |what-send| replace:: CSV files
.. |where-send| replace:: |destination-name|


Attentive
==================================================

|destination-name| is an automation platform for email and SMS marketing. Use the `subscriber segment upload <https://docs.attentivemobile.com/pages/developer-guides/sftp-solution/subscriber-segment-upload/#subscriber-segment-upload>`__ |ext_link| process to manage lists of customers in |destination-name|.



Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Hostname**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-hostname-start
   :end-before: .. credential-sftp-hostname-end

**Username**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-username-start
   :end-before: .. credential-sftp-username-end

**Passphrase**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-sftp-passphrase-start
   :end-before: .. credential-sftp-passphrase-end


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

**Client domain**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-attentive-client-domain-start
   :end-before: .. setting-attentive-client-domain-end

**Segment name** (Required at orchestration)

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-attentive-segment-name-start
   :end-before: .. setting-attentive-segment-name-end

**Campaign file settings**

.. include:: ../../shared/destination_settings.rst
   :start-after: .. campaigns-steps-campaign-settings-start
   :end-before: .. campaigns-steps-campaign-settings-end
