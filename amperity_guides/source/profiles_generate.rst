.. https://docs.amperity.com/guides/


.. meta::
    :description lang=en:
        Customer profiles should be refreshed whenever source tables with personally identifiable information (PII) are updated.

.. meta::
    :content class=swiftype name=body data-type=text:
        Customer profiles should be refreshed whenever source tables with personally identifiable information (PII) are updated.

.. meta::
    :content class=swiftype name=title data-type=string:
        Generate customer profiles

==================================================
Generate customer profiles
==================================================

.. profiles-02-generate-start

Customer profiles should be refreshed whenever source tables with personally identifiable information (PII) are updated.

This should be done with a scheduled workflow, but may be done manually from the **Customer profiles** page in **Quick start**. On the **Generate tables** card click the **Generate profiles** button.

This will start a workflow that:

#. Updates domain table data.
#. Performs a data quality check to `validates source table data <../operator/validate_inputs.html>`__. For example, invalid phone numbers, missing item quantities, missing revenue, if order and store IDs are present in transactions data, or invalid email addresses.
#. Runs Stitch.
#. Refreshes customer profiles in the database.

.. profiles-02-generate-end
