.. https://docs.amperity.com/operator/


.. meta::
    :description lang=en:
        Use gender prediction within your customer 360 database.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use gender prediction within your customer 360 database.

.. meta::
    :content class=swiftype name=title data-type=string:
        Gender prediction

==================================================
Gender prediction
==================================================

.. predict-gender-about-start

Gender prediction can be a helpful step when applying personalization to marketing campaigns, within email messages, and during visitor interactions on websites. When gender is known, it can be used as a signal for tailoring communications, recommendations, and product lists based on observed preferences that are common for that gender.

When used carefully, gender prediction can have low downside risk due to false positives. That said, gender prediction should not be used for 1:1 personalization or to predict pronouns (he, him, she, her, they, them) because the benefits of correctly predicting gender is, in most cases, outweighed by the high downside risks of being wrong.

It's important that your brand understands how gender prediction will be used prior to enabling it within your tenant. Work closely with partners to ensure this generated data is used responsibly.

.. predict-gender-about-end


.. _predict-gender-add-data-asset:

Add the data asset
==================================================

.. predict-gender-add-data-asset-start

Gender prediction must be enabled for your tenant. Amperity provides the **gender_name_ratios.csv** file as a data asset from an Amazon S3 bucket named "Amperity Data Assets".

Create a support ticket and request to enable this Amazon S3 bucket for your tenant, after which you may use a courier to pull the **gender_name_ratios.csv** file to your tenant using an Amazon S3 data source.

.. predict-gender-add-data-asset-end

**About gender_name_ratios.csv**

.. predict-gender-add-data-asset-csv-start

Gender prediction based on the **gender_name_ratios.csv** file (an Amperity data asset) should only be used for audiences that exist within the United States.

.. predict-gender-add-data-asset-csv-end

.. include:: ../../amperity_operator/source/add_data_assets.rst
   :start-after: .. data-asset-gender-name-ratios-start
   :end-before: .. data-asset-gender-name-ratios-end

**To add the gender_name_ratios.csv data asset**

.. include:: ../../amperity_operator/source/add_data_assets.rst
   :start-after: .. data-asset-gender-name-ratios-steps-start
   :end-before: .. data-asset-gender-name-ratios-steps-end


.. _predict-gender-accuracy-threshold:

Adjust accuracy threshold
==================================================

.. predict-gender-accuracy-threshold-start

The default accuracy threshold for gender prediction is ~95%. This means that for any given name it has a 20:1 likelihood of being associated with a specific gender. If greater accuracy is required for a use case, add a custom **gender_name_ratio** threshold to the query:

.. code-block:: sql

   WITH ratios AS (
     SELECT * 
     FROM Gender_Name_Ratios 
     WHERE gender_name_ratio >= 100
   )

   SELECT
     mc.amperity_id
     ,ratios.predicted_gender
   FROM Merged_Customers AS mc
   LEFT JOIN Gender_Name_Ratios AS ratios
   ON UPPER(
     COALESCE(mc.given_name, SPLIT(mc.full_name,' ')[0])
   ) = ratios.given_name

where "100" represents a 99% accuracy threshold for gender prediction.

.. predict-gender-accuracy-threshold-end
