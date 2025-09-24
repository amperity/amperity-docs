.. https://docs.amperity.com/user/


.. |destination-name| replace:: LinkedIn DMP
.. |what-send| replace:: audiences
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to LinkedIn DMP.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to LinkedIn DMP.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to LinkedIn DMP

==================================================
Send query results to LinkedIn DMP
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-linkedin-dmp-start
   :end-before: .. term-linkedin-dmp-end

.. include:: ../../amperity_operator/source/destination_linkedin_dmp.rst
   :start-after: .. destination-linkedin-dmp-about-start
   :end-before: .. destination-linkedin-dmp-about-end

.. destination-linkedin-dmp-api-note-start

.. note:: This destination uses the `LinkedIn Marketing API <https://learn.microsoft.com/en-us/linkedin/marketing/matched-audiences/create-and-manage-list-uploads?view=li-lms-2025-01&tabs=http>`__ |ext_link|.

   .. include:: ../../shared/destinations.rst
      :start-after: .. destinations-add-destinations-intro-allow-for-start
      :end-before: .. destinations-add-destinations-intro-allow-for-end

.. destination-linkedin-dmp-api-note-end

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-oauth-warning-about-reauthorize-start
   :end-before: .. destinations-oauth-warning-about-reauthorize-end

.. sendto-linkedin-dmp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-linkedin-dmp-build-query>`
#. :ref:`Add orchestration <sendto-linkedin-dmp-add-orchestration>`
#. :ref:`Run orchestration <sendto-linkedin-dmp-run-orchestration>`

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-linkedin-dmp-build-query:

Build query
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-build-query-email-only-start
   :end-before: .. sendtos-build-query-email-only-end

**Example**

.. sendto-linkedin-dmp-build-query-example-start

You may include additional audience details for title, country, and company.

.. code-block:: sql
   :linenos:

   SELECT 
     email AS email
     ,title AS title
     ,country AS employeecountry
     ,company AS company
   FROM Merged_Customers
   WHERE email IS NOT NULL

.. sendto-linkedin-dmp-build-query-example-end


.. _sendto-linkedin-dmp-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-linkedin-dmp-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
