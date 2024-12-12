.. 
.. https://docs.amperity.com/amp360/
.. 

.. |destination-name| replace:: Mailchimp
.. |what-send| replace:: audience lists

.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Mailchimp.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Mailchimp.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Mailchimp

==================================================
Send query results to Mailchimp
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-mailchimp-start
   :end-before: .. term-mailchimp-end

.. sendto-mailchimp-api-note-start

.. note:: This destination uses the `Mailchimp REST API <https://mailchimp.com/developer/guides/an-introduction-to-rest/>`__ |ext_link|.

.. sendto-mailchimp-api-note-end

.. sendto-mailchimp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-mailchimp-build-query>`
#. :ref:`Add orchestration <sendto-mailchimp-add-orchestration>`
#. :ref:`Run orchestration <sendto-mailchimp-run-orchestration>`

.. sendto-mailchimp-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-mailchimp-build-query:

Build query
==================================================

.. sendto-mailchimp-build-query-start

You will need to build a query that outputs fields that can be mapped to audience fields tags in Mailchimp. For example, a Mailchimp audience may have the following fields and field tags:

.. list-table::
   :widths: 140 140 320
   :header-rows: 1

   * - Mailchimp Fields
     - Field Tags
     - Description
   * - **email_address**
     - email
     - Required.
   * - **first_name**
     - FNAME
     - Optional.
   * - **last_name**
     - LNAME
     - Optional.
   * - **address**
     - ADDRESS
     - Optional.
   * - **phone_number**
     - PHONE
     - Optional.
   * - **birthday**
     - BIRTHDAY
     - Optional.
   * - **status**
     - status_if_new
     - Required. Must have a value of "subscribed" or "unsubscribed" because data template mappings do not provide type conversions.

.. sendto-mailchimp-build-query-end

**Example**

.. sendto-mailchimp-build-query-example-start

The customer 360 database can provide email, first name, last name, and birthdate data. Use another table in the customer 360 database to keep a list of known email addresses with their subscription status available from a status column that can provide "subscribed" and "unsubscribed" values.

Build a query named "Mailchimp - Upcoming Birthdays" to collect email address, first name, last name, and birthdate data from the customer 360 database, but with a window for birthdays that spans "within the next 10 days from the current date", and then find only those individuals who are also subscribed to the mailing list:

.. code-block:: sql

   SELECT
     c360.email
     ,c360.given_name
     ,c360.surname
     ,c360.birthdate
     ,el.status
     ,DATE_FORMAT(birthdate, '%m-%d')
     ,current_date
   FROM Customer360 c360
   LEFT JOIN Email_List el ON c360.email = el.email
   WHERE DATE_FORMAT(birthdate, '%m-%d') = DATE_FORMAT((CURRENT_TIMESTAMP AT TIME ZONE 'America/Los_Angeles'+ interval '10' day), '%m-%d')
   AND status = 'subscribed'

which outputs results similar to:

.. code-block:: mysql

   ------------------------ ------------ ---------- ----------- ------------
    email                    given_name   surname    birthdate   status
   ------------------------ ------------ ---------- ----------- ------------
    triley@perezinc.com      Tyler        Riley      02-19       subscribed
    act_austin@rushllc.org   Austin       Williams   02-20       subscribed
    swelch@kellyllc.com      Sandra       Welch      02-20       subscribed
    justincurrie@mmail.com   Justin       Currie     02-21       subscribed
    ...
   ------------------------ ------------ ---------- ----------- ------------

.. sendto-mailchimp-build-query-example-end


.. _sendto-mailchimp-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-mailchimp-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
