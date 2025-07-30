.. https://docs.amperity.com/user/

:orphan:

.. meta::
    :description lang=en:
        Analyze campaign data, including campaign results and recipient lists.

.. meta::
    :content class=swiftype name=body data-type=text:
        Analyze campaign data, including campaign results and recipient lists.

.. meta::
    :content class=swiftype name=title data-type=string:
        Analyze campaign data

==================================================
Analyze campaign data
==================================================

.. analyze-campaign-about-start

You can analyze data for campaigns by downloading campaign results or recipient lists or by analyzing campaign results from the **Queries** page.

.. analyze-campaign-about-end


.. _download-campaign-recipients:

Download recipients
==================================================

.. download-campaign-recipients-start

You can download a file that contains a list of campaign recipients (Amperity IDs) who belonged to a treatment group for a delivered campaign.

.. important:: For recurring campaigns, each date on which that campaign was sent must be selected, and then downloaded individually.

.. download-campaign-recipients-end

**To download campaign recipients**

.. download-campaign-recipients-steps-start

#. From the **Campaigns** page, choose a campaign, and then from the |fa-kebab| menu, choose **Download recipients**. This opens the **Download recipients** dialog.
#. Select the delivery date for the campaign.
#. Click **Download**. This downloads a CSV file to your local computer with two columns: one for the Amperity ID and the other for the treatment group ID.

.. download-campaign-recipients-steps-end


.. _download-campaign-results:

Download results
==================================================

.. download-campaign-results-start

You can download a file that contains a list of campaign results.

For example, a daily campaign has a launch date of March 7. From the **Download results** dialog, select "March 7" and 4 days. The downloaded file will show one row of data for each treatment group for every email address (as identified by the Amperity ID) that received the campaign on March 7-10.

.. download-campaign-results-end

**To download campaign results**

.. download-campaign-results-steps-start

#. From the **Campaigns** page, choose a campaign, and then from the |fa-kebab| menu, choose **Download results**. This opens the **Download results** dialog.
#. Select the list delivery date.
#. Select the date range for which you want to pull data. The first is the date from which data should begin, and the second is an integer that represents the number of days for which results should be downloaded.
#. Click **Download**.

.. download-campaign-results-steps-end

Campaign results columns
--------------------------------------------------

.. include:: ../../amperity_reference/source/campaigns.rst
   :start-after: .. campaigns-results-columns-start
   :end-before: .. campaigns-results-columns-end

.. include:: ../../amperity_reference/source/campaigns.rst
   :start-after: .. campaigns-results-column-descriptions-start
   :end-before: .. campaigns-results-column-descriptions-end
