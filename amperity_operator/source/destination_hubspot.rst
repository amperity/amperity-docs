.. https://docs.amperity.com/operator/


.. |destination-name| replace:: HubSpot
.. |destination-api| replace:: HubSpot API
.. |plugin-name| replace:: "HubSpot"
.. |credential-type| replace:: "hubspot"
.. |required-credentials| replace:: "refresh token"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "hub"


.. meta::
    :description lang=en:
        Configure Amperity to send email lists to HubSpot.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send email lists to HubSpot.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure destination for HubSpot

==================================================
Configure destination for HubSpot
==================================================

.. note:: This topic contains information about configuring a destination that sends query results to |destination-name| using orchestrations. To configure a destination that sends audiences to |destination-name| using campaigns see `this topic <https://docs.amperity.com/legacy/destination_hubspot.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-hubspot-start
   :end-before: .. term-hubspot-end

.. destination-hubspot-start

Use Amperity to manage contact lists in |destination-name|. Build a query using the **email** field and send the results of that query to |destination-name|. Amperity will update contacts that already exist in |destination-name|; Amperity does not create contacts.

.. destination-hubspot-end

.. destination-hubspot-contain-only-numbers-letters-underscores-start

.. note:: Field names that are sent from Amperity to HubSpot should be lowercase and contain only letters (``a-z``), numbers (``0-9``), and underscores (``_``). Amperity automatically converts uppercase letters to lowercase and replaces non-underscore characters (such as ``#``, ``*``, or ``-``) with an underscore.

.. destination-hubspot-contain-only-numbers-letters-underscores-end

.. destination-hubspot-dates-and-datetimes-start

.. caution:: 

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-hubspot-dates-and-datetimes-start
      :end-before: .. setting-hubspot-dates-and-datetimes-end

.. destination-hubspot-dates-and-datetimes-end

.. destination-hubspot-build-query-start

.. important:: |destination-name| has `specific requirements for email address validation <https://developers.hubspot.com/docs/api/faq>`__ |ext_link|. All email addresses that are sent to |destination-name| must:

   #. Have a valid format, as defined by `RFC 2822 <https://tools.ietf.org/html/rfc2822>`__ |ext_link|.
   #. May not contain quotation marks in the local part of the address, which is the part to the left of the @ symbol.
   #. Must end in a valid top-level domain (TLD), as listed at `https://data.iana.org/TLD/tlds-alpha-by-domain.txt <https://data.iana.org/TLD/tlds-alpha-by-domain.txt>`__ |ext_link| and may contain Unicode characters within the TLD.

   If a list of email addresses that is sent to |destination-name| contains a single invalid email address the entire import will fail and return a 400 error.

   If you experience a 400 error (due to invalid email addresses), identify which email addresses are invalid, remove them from the list, and then resend a list of valid email addresses to |destination-name|.

   Amperity will update contacts that already exist in |destination-name|; Amperity does not create contacts.

.. destination-hubspot-build-query-end


.. _destination-hubspot-get-details:

Get details
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-get-details-start
   :end-before: .. setting-common-get-details-end

.. destination-hubspot-get-details-table-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail 1.
          :align: left
          :class: no-scaled-link
     - **Credential settings**

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end


.. destination-hubspot-get-details-end


.. _destination-hubspot-credentials:

Configure credentials
==================================================

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-configure-first-start
   :end-before: .. credential-configure-first-end

.. include:: ../../shared/credentials_settings.rst
   :start-after: .. credential-snappass-start
   :end-before: .. credential-snappass-end

**To configure credentials for HubSpot**

.. destination-hubspot-credentials-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-add-credential-start
          :end-before: .. credential-steps-add-credential-end

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-select-type-start
          :end-before: .. credential-steps-select-type-end

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/credentials_settings.rst
          :start-after: .. credential-steps-settings-intro-start
          :end-before: .. credential-steps-settings-intro-end

       **Refresh token**
          |checkmark-required| **Required**

          .. include:: ../../shared/credentials_settings.rst
             :start-after: .. credential-oauth-refresh-token-start
             :end-before: .. credential-oauth-refresh-token-end

.. destination-hubspot-credentials-steps-end


.. _destination-hubspot-reauthorize-amperity:

Reauthorize Amperity
--------------------------------------------------

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-reauthorize-start
   :end-before: .. destinations-oauth-reauthorize-end


.. _destination-hubspot-add:

Add destination
==================================================

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-common-sandbox-recommendation-start
   :end-before: .. setting-common-sandbox-recommendation-end

**To add a destination for HubSpot**

.. destination-hubspot-add-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
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
          :alt: Step 2.
          :align: left
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
          :alt: Step 3.
          :align: left
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
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-settings-start
          :end-before: .. destinations-steps-settings-end

       **Audience primary key**

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-common-audience-primary-key-start
             :end-before: .. setting-common-audience-primary-key-end

       **List name** (Required at orchestration)

          .. include:: ../../shared/destination_settings.rst
             :start-after: .. setting-hubspot-list-name-start
             :end-before: .. setting-hubspot-list-name-end

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destination_settings.rst
          :start-after: .. destinations-steps-business-users-start
          :end-before: .. destinations-steps-business-users-end

.. destination-hubspot-add-steps-end

.. TODO: Add workflow resolutions from existing topics HERE.
