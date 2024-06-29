.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Enable a privacy rights workflow to support CCPA and GDPR workflows.

.. meta::
    :content class=swiftype name=body data-type=text:
        Enable a privacy rights workflow to support CCPA and GDPR workflows.

.. meta::
    :content class=swiftype name=title data-type=string:
        Privacy rights

==================================================
Privacy rights
==================================================

.. privacy-rights-overview-start

A privacy rights workflow can help your organization stay in compliance with data protection and privacy regulations, such as those required by California Consumer Privacy Act (CCPA) or General Data Protection Regulation (GDPR).

* .. include:: ../../shared/terms.rst
     :start-after: .. term-ccpa-start
     :end-before: .. term-ccpa-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-gdpr-start
     :end-before: .. term-gdpr-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-australian-privacy-principles-start
     :end-before: .. term-australian-privacy-principles-end

This topic describes how to configure Amperity to support a self-service privacy rights workflow that deletes consumer profile data based on inbound delete requests and requested compliance actions.

.. privacy-rights-overview-end

.. privacy-rights-note-start

.. note:: General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA) compliance is the obligation of each customer, including interpreting and determining how to comply with each request made by a user. As such, each customer must define the process by which inbound requests for General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA) compliance are made available to Amperity.

   Each customer is encouraged to seek legal counsel regarding California Consumer Privacy Act (CCPA) compliance and should not rely solely on General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA) workflows within Amperity to ensure that compliance.

.. privacy-rights-note-end

.. privacy-rights-important-start

.. important:: This topic does not constitute legal advice to third parties regarding General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA) compliance, nor does it imply that steps taken by Amperity will satisfy these compliance requirements.

   Customers are encouraged to seek legal counsel regarding General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA) compliance and should not rely solely on Amperity for compliance.

.. privacy-rights-important-end


.. _privacy-rights-request-types:

Request types
==================================================

.. privacy-rights-request-types-start

You can configure Amperity to support the following compliance actions:

#. Respond to a data subject access request (DSAR)

    .. note::

      .. include:: ../../shared/terms.rst
          :start-after: .. term-dsar-start
          :end-before: .. term-dsar-end

#. Delete rows of records
#. Delete personally identifiable information (PII) from rows of records

.. privacy-rights-request-types-end

.. privacy-rights-request-types-tip-start

.. important:: Amperity deletes data when requested, but does not maintain a list of prior delete actions. Amperity is unaware when previously deleted customer records re-enter the system.

   Your brand should take steps to ensure that your upstream processes have completed their own delete actions before allowing those sources to provide updated data to Amperity.
  
.. privacy-rights-request-types-tip-end


.. _privacy-rights-request-strategies:

Request strategies
==================================================

.. privacy-rights-request-strategies-start

You can configure compliance actions to support the following request strategies:

#. Find all rows that exactly match the compliance request.
#. Find all rows that exactly match the compliance request *along with* any row in a stitched table that shares an Amperity ID with those records.

.. important:: You may wish to use Amperity to identify which records belong to a customer. If the strategy field is set to **connected_pii**, records are connected by the Amperity ID using probabilistic Stitch. The detailed report contains those records. Send these results to your downstream workflows to locate data that should be deleted from other systems.

.. privacy-rights-request-strategies-end


.. _privacy-rights-enable:

Enable privacy rights workflows
==================================================

.. privacy-rights-enable-start

A privacy rights workflow requires the following steps:

#. :ref:`Configure inbound requests table <privacy-rights-inbound-requests-table>`.
#. :ref:`Apply semantic tags to tables with desired deletes <privacy-rights-apply-semantic-tags>`.
#. :ref:`Create linkage tables if necessary <privacy-rights-build-linkage-tables>`.

.. privacy-rights-enable-end


.. _privacy-rights-inbound-requests-table:

Inbound requests table
----------------------------------------------------------

.. privacy-rights-inbound-requests-table-start

An inbound request table contains information about compliance requests. It must contain at least one field that is used to identify matching records: this is most commonly email address, but phone number, address, and custom fields such as a customer key or loyalty ID can also be used.

.. note:: If multiple identification fields exist, they are treated as though they are separate requests, identifying source domain records that can be matched to ANY of the identification fields.

.. note:: An address group is a single entity. A compliance action must match all fields within the address group: address, address2, city, state, postal, and country. It is important for addresses in incoming data to be standardized before they can be used for matching in compliance requests.

It also contains information about the request type and request strategy.

.. tip:: You may use a custom domain table to transform an inbound request table into the needed format. If you intend to use only a single **request_type** or **request_strategy**, those can be hard-coded in the custom domain table, rather than be included as part of the inbound request.

.. privacy-rights-inbound-requests-table-end

**Inbound request table columns**

.. privacy-rights-inbound-requests-table-columns-start

An inbound requests table may have the following columns. **compliance/request-** semantics are used to identify the fields.

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-compliance-request-table-start
   :end-before: .. semantics-compliance-request-table-end

.. privacy-rights-inbound-requests-table-columns-end


.. _privacy-rights-apply-semantic-tags:

Apply semantic tags source tables
-------------------------------------------------------------------

.. privacy-rights-apply-semantic-tags-start

Semantic tags are used to identify records and fields eligible for compliance actions.

.. privacy-rights-apply-semantic-tags-end

.. _privacy-rights-semantic-tag-find-records:

Identify records eligible for compliance actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. privacy-rights-semantic-tag-find-records-start

Inbound requests must include at least one field that can be used to identify records belonging to a person, such as email. If this field is tagged with the **compliance/request-email** semantic, it will be checked against any source table that has a field tagged with the **email** semantic.

In addition to email, phone number and physical address can be used to identify records belonging to a person.

.. note:: An address group contains multiple fields, but is a single entity for a compliance action. In order to match to records in source tables, ALL values must match. Address standardization should be applied upstream of Amperity so that address can be reliably used to identify source records.

Custom fields can also be used to identify records. If the inbound request table is tagged with the **compliance/request-custom-key** semantic, the values in there will be checked against any source table that has a field tagged with the **compliance/custom-field** semantic.

.. privacy-rights-semantic-tag-find-records-end

.. _privacy-rights-semantic-tag-find-fields:

Identify fields to delete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: This section only applies if the **delete_pii** request type is used.
  
The **delete** request type acts on entire rows of source tables, but it is possible to only delete PII from a record, while leaving the rest of the data intact.

Any field that is tagged with the **compliance/pii** semantic will be replaced with **NULL** if its record is eligible for compliance actions and an inbound request with the **delete_pii** request type is ingested.

.. _privacy-rights-build-linkage-tables:

Create linkage tables
----------------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-linkage-table-start
   :end-before: .. term-linkage-table-end

If a compliance request cannot be directly linked to a source table, but can be linked to a custom domain table, create a linkage table to identify the source table records and ensure compliance actions are applied to them.

.. include:: ../../amperity_reference/source/domain_tables.rst
   :start-after: .. domain-tables-add-linkage-steps-start
   :end-before: .. domain-tables-add-linkage-steps-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-compliance-table-pii-note-start
   :end-before: .. semantics-compliance-table-pii-note-end

.. _privacy-rights-reports-tables:

Reports tables
==================================================

.. privacy-rights-reports-tables-start

Amperity generates the following reports tables as part of a Stitch run. Each table contain the results of the most recent privacy rights workflow. These tables may be empty when no requests were made.

.. privacy-rights-reports-tables-end


.. _privacy-rights-reports-tables-unified-compliance-overview:

Unified Compliance Overview
----------------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-compliance-overview-table-start
   :end-before: .. term-unified-compliance-overview-table-end

The **Unified Compliance Overview** table contains the following columns:

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-compliance-overview-table-start
   :end-before: .. data-tables-unified-compliance-overview-table-end


.. _privacy-rights-reports-tables-unified-compliance:

Unified Compliance
----------------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-unified-compliance-table-start
   :end-before: .. term-unified-compliance-table-end

The **Unified Compliance** table contains the following columns:

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-unified-compliance-table-start
   :end-before: .. data-tables-unified-compliance-table-end

..
  need to add in info about suppression
