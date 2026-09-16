.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Use orchestrations to send query results to any destination.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results to any destination.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data with orchestrations

==================================================
Send data with orchestrations
==================================================

.. send-results-start

You can send results from Amperity using an orchestration that:

* :ref:`Sends query results <send-results-query>`
* :ref:`Sends a data export <send-results-data-exports>`

.. send-results-end


.. _send-results-query:

Send query results
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

.. include:: ../../amperity_reference/source/orchestrations.rst
   :start-after: .. orchestrations-about-start
   :end-before: .. orchestrations-about-end

.. include:: ../../amperity_reference/source/orchestrations.rst
   :start-after: .. orchestrations-add-start
   :end-before: .. orchestrations-add-end

**To add an orchestration**

.. include:: ../../amperity_reference/source/orchestrations.rst
   :start-after: .. orchestrations-add-steps-start
   :end-before: .. orchestrations-add-steps-end


.. _send-results-data-exports:

Send data exports
==================================================

.. data-exports-add-start

Database tables and databases can be sent from Amperity as a data export. A data export is configured from the **Customer 360** page, and then added to an orchestration from the **Destinations** page.

.. data-exports-add-end

**To assign a database export to an orchestration**

.. data-exports-add-to-orchestration-steps-start

#. From the **Destinations** page click **Add Orchestration**. This opens the **Add Orchestration** dialog box.
#. From the **Object Type** dropdown, select **Database Export**.
#. Select a destination and complete the rest of the orchestration settings.
#. Click **Save**.

.. data-exports-add-to-orchestration-steps-end
