.. https://docs.amperity.com/operator/


.. |destination-name| replace:: OpenAI Audiences
.. |destination-api| replace:: OpenAI Advertiser API
.. |plugin-name| replace:: "OpenAI Audiences"
.. |credential-type| replace:: "openai-ads-audiences"
.. |required-credentials| replace:: "API key"
.. |what-send| replace:: audiences
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "openai"


.. meta::
    :description lang=en:
        Configure Amperity to send campaigns to OpenAI Audiences.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send campaigns to OpenAI Audiences.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure campaigns for OpenAI Audiences

==================================================
Configure campaigns for OpenAI Audiences
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-openai-ads-audiences-start
   :end-before: .. term-openai-ads-audiences-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-beta-start
   :end-before: .. destination-openai-ads-audiences-beta-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-start
   :end-before: .. destination-openai-ads-audiences-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-api-note-start
   :end-before: .. destination-openai-ads-audiences-api-note-end

.. include:: ../../amperity_operator/source/destination_openai_ads_audiences.rst
   :start-after: .. destination-openai-ads-audiences-behavior-start
   :end-before: .. destination-openai-ads-audiences-behavior-end


.. _campaign-openai-ads-audiences-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. campaign-openai-ads-audiences-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: center
          :class: no-scaled-link
     - **Credential settings**

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-openai-ads-audiences-api-key-start
             :end-before: .. credential-openai-ads-audiences-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-openai-ads-audiences-find-api-key-start
             :end-before: .. credential-openai-ads-audiences-find-api-key-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Match identifier**

          |checkmark-required| **Required**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-match-identifier-start
             :end-before: .. setting-openai-ads-audiences-match-identifier-end

       **List name**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-start
             :end-before: .. setting-openai-ads-audiences-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-archived-start
             :end-before: .. setting-openai-ads-audiences-list-name-archived-end

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 3.
          :align: center
          :class: no-scaled-link
     - A campaign that is configured to use the sub-audience editor or one-time campaign that is configured to use a query or segment.

.. campaign-openai-ads-audiences-get-details-table-end


.. _campaign-openai-ads-audiences-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for OpenAI Audiences**

.. campaign-openai-ads-audiences-credentials-steps-start

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

       **API key**

          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-openai-ads-audiences-api-key-start
             :end-before: .. credential-openai-ads-audiences-api-key-end

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-openai-ads-audiences-find-api-key-start
             :end-before: .. credential-openai-ads-audiences-find-api-key-end

.. campaign-openai-ads-audiences-credentials-steps-end


.. _campaign-openai-ads-audiences-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for OpenAI Audiences**

.. campaign-openai-ads-audiences-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-start
          :end-before: .. campaigns-steps-add-destinations-end

       .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-add-destinations-select-start
          :end-before: .. campaigns-steps-add-destinations-select-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-select-credential-start
          :end-before: .. campaigns-steps-select-credential-end

       .. tip::

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-test-connection-start
             :end-before: .. campaigns-steps-test-connection-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-name-and-description-start
          :end-before: .. campaigns-steps-name-and-description-end

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
          :start-after: .. campaigns-steps-settings-start
          :end-before: .. campaigns-steps-settings-end

       **Match identifier**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-match-identifier-start
             :end-before: .. setting-openai-ads-audiences-match-identifier-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-start
             :end-before: .. setting-openai-ads-audiences-list-name-end

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-openai-ads-audiences-list-name-archived-start
             :end-before: .. setting-openai-ads-audiences-list-name-archived-end

       **Campaign file settings**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. campaigns-steps-campaign-settings-start
             :end-before: .. campaigns-steps-campaign-settings-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. campaigns-steps-business-users-start
          :end-before: .. campaigns-steps-business-users-end

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-validate-audience-start
          :end-before: .. destinations-steps-validate-audience-end

.. campaign-openai-ads-audiences-add-steps-end
