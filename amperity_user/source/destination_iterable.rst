.. https://docs.amperity.com/user/


.. |destination-name| replace:: Iterable
.. |what-send| replace:: email lists


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Iterable.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Iterable.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Iterable

==================================================
Send query results to Iterable
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-iterable-start
   :end-before: .. term-iterable-end

.. include:: ../../amperity_operator/source/destination_iterable.rst
   :start-after: .. destination-iterable-api-note-start
   :end-before: .. destination-iterable-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-iterable-build-query>`
#. :ref:`Add orchestration <sendto-iterable-add-orchestration>`
#. :ref:`Run orchestration <sendto-iterable-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-iterable-build-query:

Build query
==================================================

.. sendto-iterable-build-query-start

To send query results to |destination-name| you must return an **email** column or a **userId** column, depending on how your |destination-name| project is configured. Choose one of the following:

* :ref:`Email address only <sendto-iterable-build-query-email-only>`
* :ref:`Email address and profile attributes <sendto-iterable-build-query-email-plus-profile>`

.. sendto-iterable-build-query-end

.. important::

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. destinations-steps-validate-audience-start
      :end-before: .. destinations-steps-validate-audience-end


.. _sendto-iterable-build-query-email-only:

Email address only
--------------------------------------------------

.. sendto-iterable-build-query-email-only-start

Return only the **email** field for the simplest audience send to |destination-name|:

.. code-block:: sql
   :linenos:

   SELECT
     email
   FROM Customer360
   WHERE email IS NOT NULL

.. sendto-iterable-build-query-email-only-end


.. _sendto-iterable-build-query-email-plus-profile:

Email address and profile attributes
--------------------------------------------------

.. sendto-iterable-build-query-email-plus-profile-start

You can send customer profile attributes alongside the email address. |destination-name| accepts standard profile fields such as first name, last name, and phone number, along with any custom data fields.

For example:

.. code-block:: sql
   :linenos:

   SELECT
     email
     ,given_name AS firstName
     ,surname AS lastName
     ,phone
     ,city
     ,state
     ,postal AS zipCode
     ,birthdate
   FROM Customer360
   WHERE email IS NOT NULL

Any column not recognized as a standard |destination-name| profile field is stored as a custom data field in the ``dataFields`` object and can be used for personalization and segmentation within |destination-name|.

.. sendto-iterable-build-query-email-plus-profile-end


.. _sendto-iterable-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-iterable-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
