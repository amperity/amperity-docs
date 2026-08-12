.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Oracle OPERA
.. |plugin-name| replace:: "Oracle Opera (Outbound)"
.. |credential-type| replace:: "oracle-opera-outbound"
.. |required-credentials| replace:: "Client ID", "Client Secret", "Application Key", "Gateway URL", "Enterprise ID", "Hotel ID", and "External System Code"
.. |what-send| replace:: guest profiles
.. |where-send| replace:: a property's |destination-name| profile database
.. |filter-the-list| replace:: "opera"


.. meta::
    :description lang=en:
        Configure Amperity to send guest profiles to Oracle OPERA Cloud.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send guest profiles to Oracle OPERA Cloud.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destinations for Oracle Opera (Outbound)

===================================================
Configure destinations for Oracle Opera (Outbound)
===================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-oracle-opera-start
   :end-before: .. term-oracle-opera-end

.. destination-oracle-opera-outbound-start

The Oracle Opera (Outbound) connector sends |what-send| from Amperity into |where-send|, so property staff see unified names and contact details for each guest.

Each guest is identified by their Amperity ID alone, which Amperity writes into |destination-name| as an external reference under the property's external system code. Guests are not matched on name, email, or phone. Because |destination-name| has no upsert operation, each guest is first looked up by their Amperity ID: a guest the property already holds is updated in place, and a guest it does not hold yet is created and stamped with the Amperity ID so that later runs find them again.

Amperity sends only the guests whose mapped fields changed since the last run.

The **Amperity ID** and **surname** fields are required; **given name**, **birth date**, **email**, and **phone** are optional. No other data is sent.

.. .. destination-oracle-opera-outbound-end

.. destination-oracle-opera-outbound-api-note-start

.. note:: This destination uses the `Oracle Hospitality Integration Platform (OHIP) CRM API <https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_oracle_hospitality_apis.htm>`__ |ext_link|.

.. destination-oracle-opera-outbound-api-note-end

.. destination-oracle-opera-outbound-beta-start

.. admonition:: Beta

   The Oracle Opera (Outbound) connector is currently in beta. Contact your Amperity representative to learn more.

.. destination-oracle-opera-outbound-beta-end

.. destination-oracle-opera-outbound-prereq-start

.. important:: Before Amperity can write any guest, the property must register Amperity as an external system and provide its code as the **External System Code** credential. In |destination-name| Cloud, create the entry under **Administration > Interfaces > Business Events > External Systems**, link it to the property under **Toolbox > System Setup > External Databases**, and confirm that it is active. Amperity verifies this once per run and stops before the first write when the code is missing or inactive. The external system code is the connector's only notion of guest identity.

.. note:: |destination-name| adds a changed email or phone number alongside the value it already holds rather than replacing it, so a previous value can remain on the profile. Clearing a field in Amperity does not remove it from |destination-name|. This ensures Amperity never overwrites contact details that property staff entered directly in |destination-name|.

.. destination-oracle-opera-outbound-prereq-end


.. _destination-oracle-opera-outbound-get-details:

Get details
===================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-oracle-opera-outbound-get-details-table-start

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

       All seven credential fields are required. No call can be made without the whole set.

       **Client ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-client-id-start
             :end-before: .. credential-oracle-opera-outbound-client-id-end

       **Client Secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-client-secret-start
             :end-before: .. credential-oracle-opera-outbound-client-secret-end

       **Application Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-app-key-start
             :end-before: .. credential-oracle-opera-outbound-app-key-end

       **Gateway URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-gateway-url-start
             :end-before: .. credential-oracle-opera-outbound-gateway-url-end

       **Enterprise ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-enterprise-id-start
             :end-before: .. credential-oracle-opera-outbound-enterprise-id-end

       **Hotel ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-hotel-id-start
             :end-before: .. credential-oracle-opera-outbound-hotel-id-end

       **External System Code**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-external-system-code-start
             :end-before: .. credential-oracle-opera-outbound-external-system-code-end


   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 2.
          :align: center
          :class: no-scaled-link
     - **Required configuration settings**

       **Profile type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-oracle-opera-outbound-profile-type-start
             :end-before: .. setting-oracle-opera-outbound-profile-type-end

       **Primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-oracle-opera-outbound-primary-key-start
             :end-before: .. setting-oracle-opera-outbound-primary-key-end


.. destination-oracle-opera-outbound-get-details-end


.. _destination-oracle-opera-outbound-credentials:

Configure credentials
===================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for Oracle Opera (Outbound)**

.. destination-oracle-opera-outbound-credentials-steps-start

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

       All seven credential fields are required.

       **Client ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-client-id-start
             :end-before: .. credential-oracle-opera-outbound-client-id-end

       **Client Secret**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-client-secret-start
             :end-before: .. credential-oracle-opera-outbound-client-secret-end

       **Application Key**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-app-key-start
             :end-before: .. credential-oracle-opera-outbound-app-key-end

       **Gateway URL**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-gateway-url-start
             :end-before: .. credential-oracle-opera-outbound-gateway-url-end

       **Enterprise ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-enterprise-id-start
             :end-before: .. credential-oracle-opera-outbound-enterprise-id-end

       **Hotel ID**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-hotel-id-start
             :end-before: .. credential-oracle-opera-outbound-hotel-id-end

       **External System Code**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oracle-opera-outbound-external-system-code-start
             :end-before: .. credential-oracle-opera-outbound-external-system-code-end

.. destination-oracle-opera-outbound-credentials-steps-end


.. _destination-oracle-opera-outbound-add:

Add destination
===================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for Oracle Opera (Outbound)**

.. destination-oracle-opera-outbound-add-steps-start

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

       **Profile type**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-oracle-opera-outbound-profile-type-start
             :end-before: .. setting-oracle-opera-outbound-profile-type-end

       **Primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-oracle-opera-outbound-primary-key-start
             :end-before: .. setting-oracle-opera-outbound-primary-key-end

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

.. destination-oracle-opera-outbound-add-steps-end
