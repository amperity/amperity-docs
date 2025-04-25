.. https://docs.amperity.com/legacy/


.. |destination-name| replace:: Sailthru
.. |destination-api| replace:: Sailthru API
.. |plugin-name| replace:: Sailthru
.. |what-send| replace:: email address lists
.. |email-plus-send| replace:: additional attributes
.. |filter-the-list| replace:: "sai"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |credential-type| replace:: sailthru
.. |credential-details| replace:: the Sailthru API key and API secret
.. |sendto-link| replace:: |sendto_sailthru|
.. |channel-link| replace:: |campaign_sailthru|


==================================================
Send data to Sailthru
==================================================

.. note:: This topic contains information about configuring a destination to send audiences to |destination-name| using campaigns *and* for configuring a destination that sends query results using orchestrations, but have not yet been upgraded to the new user experience. To configure a destination that sends query results to |destination-name| using orchestrations see `this topic <https://docs.amperity.com/operator/destination_sailthru.html>`__ |ext_link|.

.. include:: ../../shared/terms.rst
   :start-after: .. term-sailthru-start
   :end-before: .. term-sailthru-end

.. destination-sailthru-start

Use Amperity to manage audience lists in |destination-name|. Build a query using the **email** field, and then send the results of that query to |destination-name| or build a segment that matches specific criteria, and then send the email addresses for customers who belong to that audience. You may extend the audience using custom attributes.

.. destination-sailthru-end

.. destination-sailthru-api-note-start

.. note:: This destination uses the `Sailthru API <https://getstarted.sailthru.com/developers/api-basics/introduction/>`__ |ext_link|.

.. destination-sailthru-api-note-end

.. destination-sailthru-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Get details <destination-sailthru-get-details>`
#. :ref:`Add destination <destination-sailthru-add-destination>`
#. :ref:`Add data template <destination-sailthru-add-data-template>`

.. destination-sailthru-steps-to-send-end


.. _destination-sailthru-get-details:

Get details
==================================================

.. destination-sailthru-get-details-start

|destination-name| requires the following configuration details:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - An API key and API secret.

       .. tip:: You can find the API key and secret after you log in to |destination-name|. The `API key and API secret <https://getstarted.sailthru.com/account/management/settings/>`__ |ext_link| are available after you authenticate to the |destination-name| API. (See the first item under "Setup – API & Postbacks" on that page.)

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - The list name to which the |destination-name| connector will write. This can be the name of an existing list or a new list.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Detail one.
          :align: left
          :class: no-scaled-link
     - A query that outputs the fields that must be mapped to the |destination-name| audience.

.. destination-sailthru-get-details-end


.. _destination-sailthru-extended-profile-attributes:

Extended profile attributes
==================================================

.. destination-sailthru-extended-profile-attributes-start

You can extend audiences that are sent to |destination-name| by including extended profile attributes.

The following SQL query shows how to return results that map to |destination-name| field naming requirements:

.. code-block::

   SELECT
     address AS postal_address
     ,address2 AS postal_address2
     ,birthdate AS birth_date
     ,city AS postal_city
     ,country
     ,full_name AS name
     ,gender
     ,given_name AS first_name
     ,phone
     ,postal AS postal_code
     ,surname AS last_name
     ,state AS postal_state
   FROM Customer360

.. note:: |destination-name| field names are case sensitive and cannot start with a number. Review the list of `extended profile attributes <https://getstarted.sailthru.com/audience/managing-users/set-variables-on-users/>`__ |ext_link| that are supported by |destination-name|.

.. destination-sailthru-extended-profile-attributes-end


.. _destination-sailthru-add-destination:

Add destination
==================================================

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-add-destinations-intro-all-start
   :end-before: .. destinations-add-destinations-intro-all-end

**To add a destination**

.. destination-sailthru-add-destination-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-destination-start
          :end-before: .. destinations-add-destination-end

       .. image:: ../../images/mockup-destinations-tab-add-01-select.png
          :width: 500 px
          :alt: Name, description, choose plugin.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-name-and-description-start
          :end-before: .. destinations-add-name-and-description-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-credentials-start
          :end-before: .. destinations-add-credentials-end

       .. image:: ../../images/mockup-destinations-tab-add-02-credentials.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-add-new-or-select-existing-start
          :end-before: .. destinations-add-new-or-select-existing-end

       .. image:: ../../images/mockup-destinations-tab-credentials-01-select.png
          :width: 500 px
          :alt: Choose an existing credential or add credential.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-intro-for-additional-settings-start
          :end-before: .. destinations-intro-for-additional-settings-end

       |destination-name| has the following settings:

       * API key
       * API secret

       .. tip:: You can find the API key and secret after you log in to |destination-name|. The `API key and API secret <https://getstarted.sailthru.com/account/management/settings/>`__ |ext_link| are available after you authenticate to the |destination-name| API. (See the first item under "Setup – API & Postbacks" on that page.)

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-settings-start
          :end-before: .. destinations-save-settings-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-destination-settings-start
          :end-before: .. destinations-destination-settings-end

       .. image:: ../../images/mockup-destinations-tab-add-03-settings.png
          :width: 500 px
          :alt: Settings for Sailthru.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-start
          :end-before: .. destinations-business-users-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-business-users-admonition-start
          :end-before: .. destinations-business-users-admonition-end


   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-save-start
          :end-before: .. destinations-save-end

.. destination-sailthru-add-destination-steps-end


.. _destination-sailthru-add-data-template:

Add data template
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-data-template-start
   :end-before: .. term-data-template-end

**To add a data template**

.. destination-sailthru-add-data-template-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-start
          :end-before: .. destinations-data-template-open-template-end

       .. image:: ../../images/mockup-data-template-tab-add-01-details.png
          :width: 500 px
          :alt: Step 1
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-open-template-name-start
          :end-before: .. destinations-data-template-open-template-name-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-start
          :end-before: .. destinations-data-template-business-users-end

       .. image:: ../../images/mockup-data-template-tab-add-02-allow-access.png
          :width: 500 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-access-not-configured-start
          :end-before: .. destinations-data-template-business-users-access-not-configured-end

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-business-users-allow-campaigns-start
          :end-before: .. destinations-data-template-business-users-allow-campaigns-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-verify-config-settings-start
          :end-before: .. destinations-data-template-verify-config-settings-end


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-start
          :end-before: .. destinations-data-template-save-end

       .. image:: ../../images/mockup-destinations-tab-add-05-save.png
          :width: 500 px
          :alt: Save the data template.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/destinations.rst
          :start-after: .. destinations-data-template-save-after-start
          :end-before: .. destinations-data-template-save-after-end

.. destination-sailthru-add-data-template-steps-end
