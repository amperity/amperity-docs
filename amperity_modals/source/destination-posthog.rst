.. /downloads/markdown/


.. |destination-name| replace:: PostHog
.. |what-send| replace:: person and group properties, events, and deletion requests
.. |where-send| replace:: a |destination-name| project


PostHog
==================================================

Send |what-send| from Amperity into |where-send|. The **Write mode** setting selects what each row does — person-properties, group-properties, events, or person-deletion — and an orchestration performs a single write mode for the entire run.

.. admonition:: Beta

   The PostHog connector is currently in beta. Contact your Amperity representative to learn more.


Credentials
==================================================

**Name and description**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-common-name-and-description-start
   :end-before: .. credential-common-name-and-description-end

**Project API Key**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-posthog-project-api-key-start
   :end-before: .. credential-posthog-project-api-key-end

**Personal API Key**

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-posthog-personal-api-key-start
   :end-before: .. credential-posthog-personal-api-key-end


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
