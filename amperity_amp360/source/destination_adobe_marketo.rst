.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Adobe Marketo
.. |what-send| replace:: static audience lists

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Adobe Marketo.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Adobe Marketo.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Adobe Marketo

==================================================
Send query results to Adobe Marketo
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-adobe-marketo-start
   :end-before: .. term-adobe-marketo-end

.. note::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-adobe-marketo-list-name-membership-start
      :end-before: .. setting-adobe-marketo-list-name-membership-end

.. sendto-adobe-marketo-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-adobe-marketo-build-query>`
#. :ref:`Add orchestration <sendto-adobe-marketo-add-orchestration>`
#. :ref:`Run orchestration <sendto-adobe-marketo-run-orchestration>`

.. sendto-adobe-marketo-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-adobe-marketo-build-query:

Build query
==================================================

.. sendto-adobe-marketo-build-query-start

You will need to build a query that outputs fields that can be mapped to audience fields in |destination-name|. For example, a |destination-name| audience may have the following fields:

.. list-table::
   :widths: 140 140 320
   :header-rows: 1

   * - Amperity column
     - Marketo field
     - Description
   * - **email**
     - email
     - Required.
   * - **given_name**
     - firstname
     - Optional.
   * - **surname**
     - lastname
     - Optional.
   * - **phone**
     - phone
     - Optional.
   * - **company**
     - company
     - Optional.

.. sendto-adobe-marketo-build-query-end

**Example**

.. sendto-adobe-marketo-build-query-example-start

Build a query named "Marketo - Audience List and Attributes" builds an audience list that includes email address, first name, last name, phone, and company:

.. code-block:: sql

   SELECT
     email AS email
     ,given_name AS firstname
     ,surname AS lastname
     ,phone AS phone
     ,company AS company
   FROM Merged_Customers

.. sendto-adobe-marketo-build-query-example-end


.. _sendto-adobe-marketo-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. sendto-adobe-marketo-add-orchestration-important-start

.. important:: Specify the list and folder names as they are defined in |destination-name|. This is the list, and then folder names, to which Amperity will send audience list updates.

.. sendto-adobe-marketo-add-orchestration-important-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-adobe-marketo-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
