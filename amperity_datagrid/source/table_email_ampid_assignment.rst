.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Configure and manage the Email AmpID Assignment table.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure and manage the Email AmpID Assignment table.

.. meta::
    :content class=swiftype name=title data-type=string:
        Email AmpID Assignment table

==================================================
Email AmpID Assignment table
==================================================

.. table-email-ampid-assignment-start

The **Email AmpID Assignment** table narrows the many-to-many relationships between Amperity IDs and email addresses down to one-to-one relationships, and then makes the one-to-one relationships available to the **Merged Customers** table to help your brand identify the best email address for each of your customers.

.. table-email-ampid-assignment-end

.. table-email-ampid-assignment-note-start

.. note:: The **Email AmpID Assignment** table does not prevent Amperity IDs from being associated with multiple email addresses *or* prevent email addresses from being associated with multiple Amperity IDs.

   This table enforces a one-to-one relationship for use in the **Merged Customers** table.

   Many-to-many relationships exist and are accessible from the **Unified Coalesced**, **All Opted-in Emails**, and **Email Opt Status** tables.

.. table-email-ampid-assignment-note-end


.. _table-email-ampid-assignment-howitworks:

How this table works
==================================================

.. table-email-ampid-assignment-howitworks-start

The **Email AmpID Assignment** table:

#. Returns a list of all email addresses.
#. Ranks email addresses by Amperity ID using a prioritized list of attributes that have been configured for this table.
#. Ranks email addresses using a prioritized list of email-specific attributes that have been configured for this table.
#. Ranks email addresses by Amperity ID, limiting the rankings to a configured threshold.
#. Ranks Amperity IDs by email addresses.
#. Compares both rankings, and then finds all email addresses and Amperity IDs where both rankings share the top ranking.

   All email addresses and Amperity IDs that share a top ranking are removed from further ranking.
#. Reranks all remaining email addresses and Amperity ID and identifies email addresses and Amperity IDs that share the top ranking.
#. Unions the two sets of matching email addresses and Amperity IDs into a single list.

   Some email addresses and Amperity IDs will not be matched. These non-matched email addresses and Amperity IDs are often not the best choice for a given email address or Amperity ID and should not be used to build campaigns that require the highest-ranked email address.

.. table-email-ampid-assignment-howitworks-end


.. _table-email-ampid-assignment-configure-table:

Configure table
==================================================

.. table-email-ampid-assignment-configure-table-start

Configuring the **Email AmpID Assignment** table requires the following steps:

#. :ref:`Define the list of Amperity ID attributes <table-email-ampid-assignment-configure-ampid-attributes>`
#. :ref:`Define the list of email address attributes <table-email-ampid-assignment-configure-email-attributes>`
#. :ref:`Define priority for email addresses <table-email-ampid-assignment-configure-email-priority>`
#. :ref:`Define priority for Amperity IDs <table-email-ampid-assignment-configure-ampid-priority>`
#. :ref:`Set thresholds for ranking Amperity IDs and email addresses <table-email-ampid-assignment-configure-thresholds>`

.. table-email-ampid-assignment-configure-table-end

.. table-email-ampid-assignment-configure-table-caution-start

.. caution:: You should only configure the list of Amperity ID and email address attributes, and then update the priority for ranking Amperity IDs and email addresses.

   For most tenants, the thresholds should not be updated. No other sections within the **Email AmpID Assignment** table require updates.

.. table-email-ampid-assignment-configure-table-caution-end


.. _table-email-ampid-assignment-configure-ampid-attributes:

Amperity ID attributes
--------------------------------------------------

.. table-email-ampid-assignment-configure-ampid-attributes-start

Transaction attributes, such as those that capture purchase history or those that predict future purchases, are useful when ranking Amperity IDs. Including these types of attributes will help build a robust ranking of Amperity IDs.

The following block shows the default list of attributes used for ranking Amperity IDs. These rankings may be extended to include additional attributes.

.. code-block:: sql

   ,attrs_by_amp AS (
     SELECT
       univ.amperity_id
       ,univ.email
       ,univ.update_dt
       ,MAX(tae.latest_order_datetime) AS latest_order_datetime
       ,MAX(tae.l12m_order_revenue) AS L12M_order_revenue
       ,MAX(pclv.predicted_clv_next_365d) AS predicted_clv_next_365d
     FROM email_universe univ
     LEFT JOIN Transaction_Attributes_Extended tae ON tae.amperity_id = univ.amperity_id
     LEFT JOIN Predicted_CLV_Attributes pclv ON pclv.amperity_id = univ.amperity_id
     GROUP BY univ.amperity_id, univ.email, univ.update_dt
   )

.. important:: The **amperity_id**, **email**, and **update_dt** columns *must* be specified. At least one additional attribute must be provided.

   The additional attributes in the previous block are a combination of transaction and predictive attributes. For your tenant, use attributes that best represent customer value as it relates to your brand.

**To configure the list of Amperity ID attributes**

#. Update the list to align to the transaction attributes your brand wants to use for determining priority of Amperity IDs.

   For example, the previous block includes the following transaction attributes in the priority ranking:

   .. code-block:: sql

      ,MAX(tae.latest_order_datetime) AS latest_order_datetime
      ,MAX(tae.l12m_order_revenue) AS L12M_order_revenue

   .. note:: If your tenant does not include transaction attributes, remove the following lines:

      .. code-block:: sql

         LEFT JOIN Transaction_Attributes_Extended tae
         ON tae.amperity_id = univ.amperity_id

#. The **Predicted CLV Attributes** *should* be included in Amperity ID ranking when it is availalbe, though it is not required. Remove the following lines when the **Predicted CLV Attributes** table is not present in your database:

   .. code-block:: sql

      ,MAX(pclv.predicted_clv_next_365d) AS predicted_clv_next_365d

   and:

   .. code-block:: sql

      LEFT JOIN Predicted_CLV_Attributes pclv
      ON pclv.amperity_id = univ.amperity_id

   .. note:: You may include other predicted modeling tables.

.. table-email-ampid-assignment-configure-ampid-attributes-end


.. _table-email-ampid-assignment-configure-email-attributes:

Email address attributes
--------------------------------------------------

.. table-email-ampid-assignment-configure-email-attributes-start

Email attributes, such as those that capture consent status and engagement with your brand's marketing activities, are useful when ranking email addresses. Including these types of attributes will help build a robust ranking of email addresses.

The following block shows the default list of attributes used for ranking email addresses. These rankings may be extended to include additional attributes.

.. code-block:: sql

   ,all_attrs AS (
     SELECT
       attrs_by_amp.*
       ,ee_summ.most_recent_email_click_datetime
       ,ee_summ.email_clicks_last_30_days
       ,email_opt.is_email_opted_in
     FROM attrs_by_amp
     LEFT JOIN Email_Engagement_Summary ee_summ
     ON LOWER(ee_summ.email) = attrs_by_amp.email
     LEFT JOIN Email_Opt_Status email_opt
     ON LOWER(email_opt.email) = attrs_by_amp.email
     AND email_opt.amperity_id = attrs_by_amp.amperity_id
   )

**To configure the list of email address attributes**

#. Update the list to align to the email engagement summary attributes your brand wants to use for determining priority of email addresses. For example, the previous block includes the following email engagement summary attributes in the priority ranking:

   .. code-block:: sql

      ,ee_summ.most_recent_email_click_datetime
      ,ee_summ.email_clicks_last_30_days

   .. note:: If your tenant does not include email engagement summary attributes, remove the following lines:

      .. code-block:: sql

         LEFT JOIN Email_Engagement_Summary ee_summ
         ON LOWER(ee_summ.email) = attrs_by_amp.email

#. Remove the following lines when the **Email Opt Status** table is not present in your database:

   .. code-block:: sql

      ,email_opt.is_email_opted_in

   and:

   .. code-block:: sql

      LEFT JOIN Email_Opt_Status email_opt
      ON LOWER(email_opt.email) = attrs_by_amp.email
      AND email_opt.amperity_id = attrs_by_amp.amperity_id

.. table-email-ampid-assignment-configure-email-attributes-end


.. _table-email-ampid-assignment-configure-email-priority:

Email address priority
--------------------------------------------------

.. table-email-ampid-assignment-configure-email-priority-start

All email addresses are ranked against :ref:`email address attributes <table-email-ampid-assignment-configure-email-attributes>` to determine email address priority.

The **ORDER BY** clause lists the attributes that determine priority. You may extend these rankings to include additional attributes and you may change the order.

.. note:: The following block shows the recommended priority for ranking email addresses. This block is commented out in the SQL template and must be uncommented and updated before this table can be activated.

.. code-block:: sql

   ,amp_email_ranking AS (
     SELECT *
     FROM (
       SELECT *
       ,ROW_NUMBER() OVER (
         PARTITION BY amperity_id
         ORDER BY
           is_email_opted_in DESC
           ,email_clicks_last_30_days DESC
           ,most_recent_email_click_datetime DESC
           ,update_dt DESC
           ,email
       ) AS email_rank
       FROM all_attrs
     )
     WHERE email_rank <= 10
   )

Email address priority is defined by the following list of attributes:

::

   is_email_opted_in DESC
   ,email_clicks_last_30_days DESC
   ,most_recent_email_click_datetime DESC
   ,update_dt DESC
   ,email

Adjust the position of these columns to align email address priority to how it should be defined for your tenant.

.. table-email-ampid-assignment-configure-email-priority-end


.. _table-email-ampid-assignment-configure-ampid-priority:

Amperity ID priority
--------------------------------------------------

.. table-email-ampid-assignment-configure-ampid-priority-start

All Amperity IDs are ranked against :ref:`Amperity ID attributes <table-email-ampid-assignment-configure-ampid-attributes>` to determine Amperity ID priority.

The **ORDER BY** clause lists the attributes that determine priority. You may extend these rankings to include additional attributes and you may change the order.

.. note:: The following block shows the recommended priority for ranking Amperity IDs. This block is commented out in the SQL template and must be uncommented and updated before this table can be activated.

.. code-block:: sql

   ,email_amp_ranking AS (
     SELECT *
     FROM (
       SELECT
         email
         ,amperity_id
         ,update_dt
         ,email_rank
         ,ROW_NUMBER() OVER (
           PARTITION BY email
           ORDER BY
             predicted_clv_next_365d DESC
             ,l12m_order_revenue DESC
             ,latest_order_datetime DESC
             ,amperity_id
         ) AS amp_rank
       FROM amp_email_ranking
     )
    WHERE amp_rank <= 10

Amperity ID priority is defined by the following list of attributes:

::

   predicted_clv_next_365d DESC
   ,l12m_order_revenue DESC
   ,latest_order_datetime DESC
   ,amperity_id

Adjust the position of these columns to align Amperity ID priority to how it should be defined for your tenant.

.. table-email-ampid-assignment-configure-ampid-priority-end


.. _table-email-ampid-assignment-configure-thresholds:

Thresholds
--------------------------------------------------

.. table-email-ampid-assignment-configure-thresholds-start

Both email address and Amperity ID priorities are limited to return only the top 10, by default. This limitation helps prevent superclusters of email addresses and Amperity IDs from being included.

It is recommended to keep the default thresholds, but they may be adjusted if necessary:

* For email address priority:

  .. code-block:: sql

     WHERE email_rank <= 10

* For Amperity ID priority:

  .. code-block:: sql

     WHERE amp_rank <= 10

.. table-email-ampid-assignment-configure-thresholds-end


.. _table-email-ampid-assignment-configure-blocklist-values:

Blocklist values
--------------------------------------------------

.. table-email-ampid-assignment-configure-blocklist-values-start

If your tenant is not using the bad-values blocklist, you must remove the following line from this SQL template:

.. code-block:: sql

   AND NOT COALESCE(blv_email, FALSE)

.. table-email-ampid-assignment-configure-blocklist-values-end
