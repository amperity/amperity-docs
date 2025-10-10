.. https://docs.amperity.com/user/


.. |destination-name| replace:: Pinterest
.. |destination-api| replace:: Pinterest API
.. |plugin-name| replace:: SFTP
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours
.. |attributes-sent| replace:: |destination-name| requires email addresses. Amperity applies SHA-256 hashing to email addresses automatically.


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Pinterest Ads.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Pinterest Ads.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Pinterest Ads

==================================================
Send query results to Pinterest Ads
==================================================

.. destination-pinterest-start

Use a query to build an audience that meets the criteria for how your brand wants to advertise on |destination-name|. Send the list of email addresses associated with that audience to |destination-name| using an orchestration, after which that list of email addresses will be available in Pinterest Ads as a customer list.

.. destination-pinterest-end

.. include:: ../../amperity_operator/source/destination_pinterest.rst
   :start-after: .. destination-pinterest-shared-start
   :end-before: .. destination-pinterest-shared-end

.. include:: ../../amperity_operator/source/destination_pinterest.rst
   :start-after: .. destination-pinterest-api-note-start
   :end-before: .. destination-pinterest-api-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-pinterest-build-query:

Build query
==================================================

.. sendto-pinterest-build-query-start

Build a query that returns a list of email addresses. Use additional filters in a **WHERE** clause to scope your audience for your use cases and goals for marketing to your customers within |destination-name|.

.. sendto-pinterest-build-query-end

.. destination-pinterest-build-segment-tip-start

.. tip:: Be sure to exclude the following from query results:

   #. Users who have opted out of targeted advertising on |destination-name|
   #. User activity from an app or website
   #. Additional profile information, such as names, phone numbers, or physical addresses

.. destination-pinterest-build-segment-tip-end

**Example**

.. sendto-pinterest-build-query-example-start

The following query returns a list of hashed email addresses for customers who are engaged with your brand, have opted in to receiving email communication, have made at least 4 purchases within the previous year, and have spent at least $400.

.. code-block:: sql
   :linenos:

   SELECT
     TO_HEX(
       SHA256(
         TO_UTF8(
           UPPER(
             TRIM(email)
           )
         )
       )
     ) AS email
     FROM Merged_Customers mc
     INNER JOIN Customer_Attributes ca
     ON mc.amperity_id = ca.amperity_id
     INNER JOIN Transaction_Attributes_Extended tae
     ON mc.amperity_id = tae.amperity_id
     WHERE (
       LOWER(mc.email) IS NOT NULL
       AND pin.contactable_pinterest = TRUE
       AND tae.L12M_order_frequency >= 4
       AND tae.L12M_order_revenue >= 400
     )

.. sendto-pinterest-build-query-example-end


.. _sendto-pinterest-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-pinterest-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end


.. _destination-pinterest-product-catalogs:

Product catalogs
==================================================

.. include:: ../../amperity_user/source/destination_pinterest.rst
   :start-after: .. destination-pinterest-product-catalogs-start
   :end-before: .. destination-pinterest-product-catalogs-end
