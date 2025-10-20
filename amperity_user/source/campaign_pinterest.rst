.. https://docs.amperity.com/user/


.. |destination-name| replace:: Pinterest
.. |destination-api| replace:: Pinterest API
.. |plugin-name| replace:: SFTP
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours
.. |attributes-sent| replace:: |destination-name| requires email addresses. Amperity applies SHA-256 hashing to email addresses automatically.


.. meta::
    :description lang=en:
        Use segments and campaigns to send audiences from Amperity to Pinterest.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use segments and campaigns to send audiences from Amperity to Pinterest.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send audiences to Pinterest

==================================================
Send audiences to Pinterest Ads
==================================================

.. destination-pinterest-start

Use a segment to build an audience that meets the criteria for how your brand wants to advertise on |destination-name|. Send the list of email addresses associated with that audience to |destination-name| using a campaign, after which that list of email addresses will be available in Pinterest Ads as a customer list.

.. destination-pinterest-end

.. include:: ../../amperity_operator/source/destination_pinterest.rst
   :start-after: .. destination-pinterest-shared-start
   :end-before: .. destination-pinterest-shared-end

.. include:: ../../amperity_operator/source/destination_pinterest.rst
   :start-after: .. destination-pinterest-api-note-start
   :end-before: .. destination-pinterest-api-note-end

.. include:: ../../shared/channels.rst
   :start-after: .. channels-overview-note-start
   :end-before: .. channels-overview-note-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-campaigns-start
   :end-before: .. sendtos-ask-to-configure-campaigns-end


.. _channel-pinterest-build-segment:

Build a segment
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-segment-start
   :end-before: .. channels-build-segment-end

.. destination-pinterest-build-segment-tip-start

.. tip:: Be sure to exclude the following from a segment:

   #. Users who have opted out of targeted advertising on |destination-name|
   #. User activity from an app or website
   #. Additional profile information, such as names, phone numbers, or physical addresses

.. destination-pinterest-build-segment-tip-end

.. _attributes:

.. admonition:: Which attributes should you use?

   You can use any attributes in your customer 360 database to define the audience your brand wants to send to |destination-name|.

   Amperity sends a list of SHA-256 hashed email addresses that matches the audience you have defined to |destination-name|, after which they will be available in Pinterest Ads as a customer list.


.. _channel-pinterest-build-campaign:

Add to a campaign
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-build-campaign-start
   :end-before: .. channels-build-campaign-end

.. include:: ../../amperity_user/source/destination_tiktok_ads.rst
   :start-after: .. sendto-tiktok-ads-build-query-options-start
   :end-before: .. sendto-tiktok-ads-build-query-options-end

**To add Pinterest to a campaign**

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-open-page-start
          :end-before: .. channels-build-campaign-steps-open-page-end


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-start
          :end-before: .. channels-build-campaign-steps-destinations-end

       .. image:: ../../images/mockup-campaigns-destination-pinterest.png
          :width: 500 px
          :alt: Add a destination for Pinterest.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-destinations-note-start
          :end-before: .. channels-build-campaign-steps-destinations-note-end


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: center
          :class: no-scaled-link
     - .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-end

       .. image:: ../../images/mockup-campaigns-attributes-email.png
          :width: 500 px
          :alt: Edit the attributes for Pinterest.
          :align: left
          :class: no-scaled-link

       .. include:: ../../shared/channels.rst
          :start-after: .. channels-build-campaign-steps-edit-attributes-note-start
          :end-before: .. channels-build-campaign-steps-edit-attributes-note-end


.. _channel-pinterest-configure-default-attributes:

Configure default attributes
==================================================

.. include:: ../../shared/channels.rst
   :start-after: .. channels-configure-default-attributes-start
   :end-before: .. channels-configure-default-attributes-end

.. channel-pinterest-configure-default-attributes-start

|destination-name| has the following requirements for attributes.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Source attribute**
     - **Destination attribute**

   * - email
     - email

.. channel-pinterest-configure-default-attributes-end


.. _campaign-pinterest-product-catalogs:

Product catalogs
==================================================

.. campaign-pinterest-product-catalogs-start

To make your `product catalog available as a data source <https://help.pinterest.com/en/business/article/data-source-ingestion>`__ |ext_link| to |destination-name|, for the purpose of enabling Pins, configure an SFTP server with the file that contains the product catalog in a location that is accessible as a URL by a user-agent.

Provide that URL to |destination-name|. |destination-name| will validate the file and create a product Pin for each item in your product catalog that passes validation, up to 20 million rows.

If your product catalog is already accessible from a URL you can configure |destination-name| to use that location. Alternately, you can output your product catalog from Amperity, and then :doc:`send it to an SFTP site <destination_sftp>` that is configured to allow access to |destination-name|.

|destination-name| updates your product catalog every 24 hours by reloading the file. Update the file that is in the location from which |destination-name| pulls your product catalog to refresh your product catalog on |destination-name|.

.. campaign-pinterest-product-catalogs-end
