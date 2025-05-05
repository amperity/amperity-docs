.. https://docs.amperity.com/ampiq/


.. meta::
    :description lang=en:
        Configure the default attributes that your brand sends to destinations.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure the default attributes that your brand sends to destinations.

.. meta::
    :content class=swiftype name=title data-type=string:
        Configure default attributes for campaigns

==================================================
Default attributes
==================================================

.. campaigns-default-attributes-static-intro-start

Sending campaigns from Amperity to downstream marketing workflows is a combination of:

* A :doc:`segment <segments>` that defines the audience that you will use with your campaign.
* A :doc:`campaign <campaigns>` that breaks that audience down into sub-audiences that align to your marketing strategies and goals.
* A set of :doc:`destinations <destinations>` that specify the locations and channels to which you will send each sub-audience.

  Most destinations may be configured to send a list of attributes (this topic) that are specific to your brand's use cases.

.. campaigns-default-attributes-static-intro-end

.. campaigns-default-attributes-overview-start

Default attributes are configured from the **Campaigns** page. Each destination may be configured to send a list of attributes that your brand can use with a variety of downstream workflows, such as audience matching, customer activation, paid media workflows, or measuring campaign results using offline events.

.. important:: For many downstream marketing applications the names of attributes are not arbitrary. There are often specific requirements for names of attributes and the data that may be associated with each attribute.

   For example, the name of the field for an email address attribute may be case-sensitive, such as "email", "Email" or "EMAIL". Many downstream marketing applications require email addresses to be converted to a SHA-256 hashed value.

   Review the documentation for individual destinations to verify if additional non-default attributes may be configured, and then sent alongside the default attributes.

.. campaigns-default-attributes-overview-end

.. campaigns-default-attributes-steps-intro-start

The following sections describe the steps you'll follow to configure the default attributes for individual destinations.

.. campaigns-default-attributes-steps-intro-end

.. campaigns-default-attributes-steps-start

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link
     - Default attributes for each destination are configured from the **Campaigns** tab in the **Activations** page. Click **Settings** to open the **Configure attributes** dialog.

       .. image:: ../../images/mockup-campaigns-default-attributes.png
          :width: 650 px
          :alt: Configure default attributes for destinations.
          :align: left
          :class: no-scaled-link


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link
     - On the **Default attributes** tab, click **Add default attributes**. This opens the **Configure attributes** dialog.

       Under **Configure attributes** do the following:

       Select a destination from the **Destination** dropdown.

       Select a database from the **Databases** dropdown.

       Select a configured activation ID from the **Activation ID** dropdown.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link
     - Under **Default attributes** click **Add attribute**. Select a table, and then choose an attribute. For example, the list of attributes that may be sent to Meta Ads Manager:

       .. image:: ../../images/mockup-campaigns-default-attributes-meta-ads-manager.png
          :width: 650 px
          :alt: The list of default attributes for a destination.
          :align: left
          :class: no-scaled-link

       .. important:: A destination can have very specific requirements for the names of fields and the values each field may contain.

          For example, some destinations:

          * Only accept email addresses (or SHA-256 hashed email addresses).
          * Require email addresses, but also accept a larger set of optional attributes.
          * Require attributes to be mapped to specific naming patterns, such as "email", "Email" or "EMAIL" before they can be accepted.

          For destinations that use an API, Amperity pre-configures the list of attributes that are required and/or are optional. Review the Amperity documentation for each destination to understand which attributes may be configured.

          For destinations that accept files---SFTP, Amazon S3, Azure Blob Storage, and Google Cloud Storage---your brand should verify the requirements for the downstream system to which data will be sent before configuring default attributes.


   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link
     - When default attributes are ready, click the **Save** button in the lower right corner of the **Default attributes** page.

       .. tip:: Be sure to verify the names of the fields and the values that appear within each field in the downstream system. This will ensure that Amperity is sending the right data and can support your brand's use cases.

.. campaigns-default-attributes-steps-end
