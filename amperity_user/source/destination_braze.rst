.. https://docs.amperity.com/user/


.. |destination-name| replace:: Braze
.. |plugin-name| replace:: Braze
.. |what-send| replace:: custom attributes
.. |attributes-sent| replace:: |destination-name| requires "extern_id" or "braze_id", along with a list of custom attributes that are defined by your brand.


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to Braze.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to Braze.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to Braze

==================================================
Send query results to Braze
==================================================

.. destination-braze-context-start

You can send customer profile and custom attributes to |destination-name| using a query and orchestration. Build a SQL query that returns a list of active customers, and then associate that list of active customers with the custom attributes that you want to send to |destination-name| from Amperity. Send the results of a query for active customers as often as you need; send updates for all custom attributes on a less frequent basis.

.. destination-braze-context-end

.. sendto-braze-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`About custom attributes <sendto-braze-about-braze-attributes>`
#. :ref:`Build a query <sendto-braze-build-query>`
#. :ref:`Add orchestration <sendto-braze-add-orchestration>`
#. :ref:`Run orchestration <sendto-braze-run-orchestration>`

.. sendto-braze-steps-to-send-end

.. caution:: This destination is available for sending query results to |destination-name| after it is configured by a Datagrid Operator or your Amperity representative.

   If this destintion cannot be selected from the campaigns editor or activations canvas ask your Datagrid Operator or Amperity representative to configure a destination for sending sending query results to |destination-name|.


.. _sendto-braze-about-braze-attributes:

About Braze attributes
==================================================

.. destination-braze-ampiq-and-amp360-unshared-intro-start

Attributes in |destination-name| describe your customers.

* :ref:`Profile attributes <destination-braze-profile-attributes>` describe who your customers are. For example: names, birthdates, email addresses, and phone numbers.
* :ref:`Custom attributes <destination-braze-custom-attributes>` describe how your customers have interacted with your brand. For example: purchase histories, loyalty status, and value tiers.

.. destination-braze-ampiq-and-amp360-unshared-intro-start

.. include:: ../../shared/braze.rst
   :start-after: .. braze-attributes-about-start
   :end-before: .. braze-attributes-about-end


.. _destination-braze-profile-attributes:

Customer profiles
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-about-start
   :end-before: .. braze-customer-profiles-about-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-admonition-start
   :end-before: .. braze-customer-profiles-admonition-end

.. destination-braze-profile-attributes-start

An orchestration can send customer profile updates to |destination-name| as the results of a query. For example:

.. code-block:: sql
   :linenos:

   SELECT
     amperity_id AS external_id
     ,given_name AS first_name
     ,surname AS last_name
     ,email
     ,phone
     ,city AS home_city
     ,country
     ,birthdate AS dob
     ,gender
   FROM Customer_360

.. destination-braze-profile-attributes-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-common-attributes-start
   :end-before: .. braze-customer-profiles-common-attributes-end

.. include:: ../../shared/braze.rst
   :start-after: .. braze-customer-profiles-common-attributes-note-start
   :end-before: .. braze-customer-profiles-common-attributes-note-end


.. _destination-braze-custom-attributes:

Custom attributes
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-custom-attributes-start
   :end-before: .. braze-custom-attributes-end


.. _destination-braze-use-in-segments:

Use in Braze segments
--------------------------------------------------

.. destination-braze-use-in-segmentss-start

The list of custom attributes that is managed by Amperity is available from the **Data Settings** page in |destination-name|. Click **Data Settings** in the left-side navigation, and then choose **Custom Attributes**. This opens a page similar to:

.. image:: ../../images/destination-braze-custom-attributes.png
   :width: 500 px
   :alt: A list of custom attributes available from within Braze.
   :align: left
   :class: no-scaled-link

Custom attributes are listed alphabetically and are case-sensitive. For example, **One and Done**, **one and done**, and **One_and_Done** are unique custom attributes within |destination-name|.

Custom attributes are available from a filter when you build segments in |destination-name|. Add a filter, and then choose **Custom Attributes**:

.. image:: ../../images/destination-braze-custom-attributes-filter-choose.png
   :width: 380 px
   :alt: Custom attributes are available as a filter within the Braze segment editor.
   :align: left
   :class: no-scaled-link

and then select any of your Amperity-managed custom attributes for use in your |destination-name| segment:

.. image:: ../../images/destination-braze-custom-attributes-filter.png
   :width: 200 px
   :alt: Custom attributes are available as a filter within the Braze segment editor.
   :align: left
   :class: no-scaled-link

.. destination-braze-use-in-segments-end


.. _destination-braze-data-points:

About data points
--------------------------------------------------

.. include:: ../../shared/braze.rst
   :start-after: .. braze-data-points-start
   :end-before: .. braze-data-points-end

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-start

.. important:: Connected Content does not write data to user profiles, which means you can use Connected Content to dynamically populate values into messages without consuming data points.

.. profile-api-usecase-braze-connected-content-does-not-use-data-points-end


.. _sendto-braze-build-query:

Build query
==================================================

.. sendto-braze-build-query-start

Use the query editor to filter by the user identifier associated with your segment in |destination-name| -- "external_id" or "braze_id" -- and then return the list of custom attributes. Use an orchestration to send the results of this query to |destination-name|.

For example, ACME wants to manage custom attributes in |destination-name| by sending customer profile attributes, along with set of purchase history attributes. The following example uses the following standard output tables:

#. **Merged Customers** for customer profile attributes; the table uses the Amperity ID to ensure the |destination-name| table is unique by Amperity ID and also to provide to |destination-name| the Amperity ID as the "extern_id", which is a required attribute

   .. note:: The following query shows a field in **Merged Customers** that returns a customer's opt status. This field might be somewhere else in your tenant. It's important to filter your query to include *only* customers who are opted in to reduce the number of data points that are updated when you send custom attributes to |destination-name|.
#. **Transaction Attributes Extended** for purchase history attributes
#. **Customer Attributes** for historical purchaser lifecycle status

.. code-block:: sql
   :linenos:

   SELECT
     mc.amperity_id AS external_id
     ,mc.given_name AS first_name
     ,mc.surname AS last_name
     ,mc.email
     ,mc.phone
     ,mc.city AS home_city
     ,mc.country
     ,mc.birthdate AS dob
     ,mc.gender
     ,ta.L30D_purchase_channels
     ,ta.L30D_order_revenue
     ,ta.L30D_order_frequency
     ,ta.L3M_purchase_channels
     ,ta.L3M_order_revenue
     ,ta.L3M_order_frequency
     ,ta.L12M_rfm_score
     ,ta.L12M_recency
     ,ta.L12M_frequency
     ,ta.L12M_monetary
     ,ta.lifetime_order_revenue
     ,ta.one_and_done
     ,ta.multi_purchase_channel
     ,ta.first_to_second_order_days
     ,ta.days_since_latest_order
     ,ta.latest_order_datetime
     ,ca.historical_purchaser_lifecycle_status
     ,ta.early_repeat_purchaser
   FROM Merged_Customers mc
   LEFT JOIN Transaction_Attributes_Extended ta ON mc.amperity_id = ta.amperity_id
   LEFT JOIN Customer_Attributes ca ON mc.amperity_id = ca.amperity_id

The **external_id** does not need to be associated with the Amperity ID. For example, if your brand has an internal identifier that you have pulled into Amperity, you can associate that identifier with the **external_id**.

.. note:: You can make the query results available to campaigns if the query results are unique by Amperity ID. This allows users of campaigns to select |destination-name| attributes when configuring which attributes are sent to |destination-name| for sub-audiences within your campaigns.

.. sendto-braze-build-query-end

.. sendto-braze-build-segments-whatfor-start

.. admonition:: What can you use custom attributes with in Braze?

   You can use custom attributes directly within segments, and then use those segments to engage with your customers across a variety of channels, including:

   * `Content cards <https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards>`__ |ext_link|
   * `Email <https://www.braze.com/docs/user_guide/message_building_by_channel/email>`__ |ext_link|
   * `In-app messaging <https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages>`__ |ext_link|
   * `Push <https://www.braze.com/docs/user_guide/message_building_by_channel/push>`__ |ext_link|
   * `SMS and MMS <https://www.braze.com/docs/user_guide/message_building_by_channel/sms>`__ |ext_link|
   * `WhatsApp <https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp>`__ |ext_link|
   * `Custom webhooks <https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks>`__ |ext_link|

.. sendto-braze-build-segments-whatfor-end


.. _sendto-braze-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-braze-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
