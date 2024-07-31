.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Amperity may be configured to act as a Unified ID 2.0 Operator for your brand.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity may be configured to act as a Unified ID 2.0 Operator for your brand.

.. meta::
    :content class=swiftype name=title data-type=string:
        About Unified ID 2.0 (UID2)

==================================================
About Unified ID 2.0
==================================================

.. uid2-overview-start

Unified ID 2.0 (UID2) is an |ext_uid2_about| that enables deterministic identity for advertising opportunities across the open internet for participants with access to the advertising ecosystem. UID2 is a standalone solution with a unique namespace and privacy controls that help participants meet local market requirements.

.. uid2-overview-end


.. _uid2-howitworks:

How UID2 works
==================================================

.. uid2-howitworks-start

Amperity may be configured as a UID2 Operator. A |ext_uid2_operator| is a participant in Unified ID 2.0 that is allowed to run the Operator Service. Operators may receive and store encryption keys and salts from the UID2 Core Service, salt and hash personal data to return raw UID2s, encrypt raw UID2s to generate UID2 tokens, and distribute UID2 token decryption keys.

.. uid2-howitworks-end

.. image:: ../../images/uid2.png
   :width: 600 px
   :alt: Unified ID 2.0 workflow with Amperity.
   :align: left
   :class: no-scaled-link

.. uid2-howitworks-table-start

The following sections describe at a high level the series of steps that are required to configure Amperity to act as a UID2 Operator for your brand.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Image panel 1.
          :align: left
          :class: no-scaled-link
     - Before you can configure Amperity to act as a UID2 Operator for your brand you must do the following:

       #. :ref:`Request access to UID2 <uid2-prerequisite-get-access>`.
       #. :ref:`Agree to the UID2 participation policy <uid2-prerequisite-participate>`.
       #. :ref:`Get an API key <uid2-prerequisite-get-credentials>` for the **Mapper** participant type. Use the credentials for this API key to allow Amperity to access endpoints in the UID2 API and act as a UID2 operator for your brand.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Image panel 2.
          :align: left
          :class: no-scaled-link
     - After your brand has adopted UID2 as part of your identity strategy you can configure Amperity to act as a UID2 operator for your brand.

       #. :ref:`Add your brand's credentials for UID2 to Amperity <uid2-configure-amperity-add-credentials>`.
       #. :ref:`Enable UID2 <uid2-configure-amperity-enable-uid2>`.
       #. :ref:`Add the UID2 table <uid2-configure-amperity-add-uid2-table>` to your brand's database.

       Use custom database tables, queries, and/or segments to configure Amperity to support your brand's use cases for UID2.


       .. admonition:: How does Amperity maintain UID2 tokens?

          Amperity uses the following UID2 endpoints when Amperity is configured to act as a UID2 Operator for your brand:

          #. Amperity sends an API request to Unified ID 2.0 using the |ext_uid2_endpoint_post_identity_buckets| endpoint to identify salt buckets that have expired. All UID2 tokens associated with an expired salt bucket are refreshed.

          #. Amperity sends an API request to Unified ID 2.0 using the |ext_uid2_endpoint_post_identity_map| endpoint. This request contains a list of normalized email addresses. Amperity gets this list of normalized email addresses from the **Unified Coalesced** table.

             The **POST /identity/map** endpoint responds with three values: a hashed email address, an advertising ID (the UID2 token), and a salt bucket ID.

          #. Amperity adds the normalized email address, hashed email address, advertising ID, and salt bucket ID to the **UID2** table.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Image panel 3.
          :align: left
          :class: no-scaled-link
     - Build workflows against the **UID2** table to support your brand's :ref:`UID2 workflows <uid2-workflows>`.

       Use custom database tables, queries, and segments in Amperity to build audiences of UID2 tokens that support your brand's advertising strategies. Send these audiences to demand-side platforms (DSPs) that participate in Unified ID 2.0, such as The Trade Desk.

       DSPs can receive UID2s from advertisers as first- and/or third-party data. Advertisers buy impressions across a range of publisher sites. DSPs help advertisers decide which ad impressions to purchase and how much to bid on them.

.. uid2-howitworks-table-end


.. _uid2-prerequisites:

Prerequisites
==================================================

.. uid2-prerequisites-start

Before your brand can configure Amperity to generate UID2 tokens you must do the following:

#. :ref:`Get access to UID2 <uid2-prerequisite-get-access>`.
#. Agree to :ref:`a UID2 participation policy <uid2-prerequisite-participate>`, which is a legal requirement for UID2 sharing.
#. :ref:`Get an API key <uid2-prerequisite-get-credentials>`. Use the credentials for this API key to allow Amperity to access endpoints in the UID2 API and act as a UID2 operator for your brand.

.. uid2-prerequisites-end


.. _uid2-prerequisite-get-access:

Get access to UID2
--------------------------------------------------

.. uid2-prerequisite-get-access-start

To get access to the UID2 framework, you may sign up directly from the |ext_uid2_request_access| website or connect directly with your The Trade Desk representative (or UID2 administrator).

.. uid2-prerequisite-get-access-end


.. _uid2-prerequisite-participate:

Participate in UID2
--------------------------------------------------

.. uid2-prerequisite-participate-start

You must agree to a UID2 participation policy, which is a |ext_uid2_participant_requirements|.

.. important:: Talk with your The Trade Desk representative if you are unsure of which |ext_uid2_participation_policy| is required to support your brand's UID2 use cases.

.. uid2-prerequisite-participate-end


.. _uid2-prerequisite-get-credentials:

Get Mapper credentials
--------------------------------------------------

.. uid2-prerequisite-get-credentials-start

Each participant in UID2 has its own set of unique |ext_uid2_mapper_credentials|, which allow access to specific areas within the UID2 ecosystem.

To configure Amperity to act as a UID2 Operator for your brand you must be a **Mapper** participant in Unified ID 2.0.

A mapper participant is a broad category that includes |ext_uid2_advertisers|, |ext_uid2_data_providers|, data on-boarders, measurement providers, identity graph providers, third-party data providers, and any other organization that sends data to other participants *and* organizations that collect user data and push it to other UID2 participants.

.. important:: Use your brand's **Mapper** participant credentials to configure Amperity to act as a UID2 Operator.

.. uid2-prerequisite-get-credentials-end


.. _uid2-configure-amperity:

Configure Amperity
==================================================

.. uid2-configure-amperity-start

After your brand has adopted UID2 as part of your identity strategy you can configure Amperity to act as a UID2 operator for your brand.

#. :ref:`Add your brand's Mapper credentials for UID2 to Amperity <uid2-configure-amperity-add-credentials>`.
#. :ref:`Enable UID2 <uid2-configure-amperity-enable-uid2>`.
#. :ref:`Add the UID2 table <uid2-configure-amperity-add-uid2-table>` to your brand's database.

.. uid2-configure-amperity-end


.. _uid2-configure-amperity-add-credentials:

Add Mapper credentials
--------------------------------------------------

.. uid2-configure-amperity-add-credentials-start

Add credential to **Credentials** tab in **Settings**.

Add your brand's Mapper credentials for UID2 to Amperity. Open the **Settings** page, select the **Credentials** tab, and then click **Add credential**.

.. image:: ../../images/mockup-credential-uid2.png
   :width: 440 px
   :alt: Add Mapper credentials for Unified ID 2.0.
   :align: left
   :class: no-scaled-link

Choose the **UID2** plugin. Provide a name and description for the credential that ensures users within your tenant know it's related to UID2. Add the API key and the client secret for your brand's **Mapper** participant credentials.

.. uid2-configure-amperity-add-credentials-end


.. _uid2-configure-amperity-enable-uid2:

Enable UID2 token generation
--------------------------------------------------

.. uid2-configure-amperity-enable-uid2-start

UID2 token generation is enabled from the **Customer 360** page. Click the **UID2** link to open the **UID2 Generation** dialog box. Select the **Enable UID2 generation** checkbox, and then choose your brand's **Mapper** credentials from the **Select credentials** drop-down.

.. image:: ../../images/mockup-databases-enable-uid2.png
   :width: 460 px
   :alt: Enable UID2 generation using your brand's Mapper credentials.
   :align: left
   :class: no-scaled-link

.. uid2-configure-amperity-enable-uid2-end


.. _uid2-configure-amperity-add-uid2-table:

Add UID2 table to database
--------------------------------------------------

.. uid2-configure-amperity-add-uid2-table-start

Add the **UID2** table to any database as a passthrough table. The **UID2** table is a core table.

.. uid2-configure-amperity-add-uid2-table-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-uid2-table-about-start
   :end-before: .. data-tables-uid2-table-about-end

.. include:: ../../amperity_reference/source/data_tables.rst
   :start-after: .. data-tables-uid2-table-start
   :end-before: .. data-tables-uid2-table-end


.. _uid2-workflows:

About UID2 workflows
==================================================

.. uid2-workflows-start

Use custom database tables, queries, and segments in Amperity to build audiences of UID2 tokens that support your brand's advertising strategies. Send these audiences to demand-side platforms (DSPs) that participate in Unified ID 2.0, such as The Trade Desk.

DSPs can receive UID2s from advertisers as first- and/or third-party data. Advertisers buy impressions across a range of publisher sites. DSPs help advertisers decide which ad impressions to purchase and how much to bid on them.

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Advertisers and UID2
          :align: left
          :class: no-scaled-link
     - Advertising with UID2 enables the use of use |ext_uid2_first_party| to build omnichannel campaigns across devices using a single identifier. Using UID2 as part of your advertising strategy will help your brand:

       * Manage advertising frequency
       * Suppress audiences across channels and devices
       * Simplify identity resolution for households *and* individuals
       * Create effective advertising in locations where cookies may not exist, such as connected TVs and mobile apps
       * Support better consumer privacy options, including opt-out
       * Improve campaign measurement

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Data providers and UID2
          :align: left
          :class: no-scaled-link
     - Data providers can use UID2 to enable the use of |ext_uid2_third_party|. This approach to advertising can reduce identity fragmentation and connect third-party data to a more durable, omnichannel, cross-device identifier.

.. uid2-workflows-end
