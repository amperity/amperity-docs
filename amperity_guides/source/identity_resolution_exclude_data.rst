.. https://docs.amperity.com/guides/


.. meta::
    :description lang=en:
        Some values in source data tables should be excluded from unified customer profiles in Amperity.

.. meta::
    :content class=swiftype name=body data-type=text:
        Some values in source data tables should be excluded from unified customer profiles in Amperity.

.. meta::
    :content class=swiftype name=title data-type=string:
        Exclude data

==================================================
Exclude data
==================================================

.. identity-resolution-05-exclude-data-start

Some values in source data tables should be excluded from unified customer profiles in Amperity. Amperity automatically converts excluded data into **NULL** values.

Open the **Identity resolution** page in **Quick start**. On the **Data exclusions** card, do one of the following:

#. Click **AmpAI select** to have the **AmpAI Assistant** determine which types of values are converted to a **NULL** value and are excluded from customer profiles.
#. Click **Manually select** to define the exclusions yourself.

   .. image:: ../../images/mockup-guided-idres-exclude-data.png
      :width: 280 px
      :alt: Identify tables with PII.
      :align: left
      :class: no-scaled-link

   .. note:: All fields to which semantic tags are applied are automatically trimmed to remove leading and trailing spaces.

      Use the **NULL date values** section to exclude specific date values. All excluded date values must be in "YYYY-MM-DD" format.

      Use the **Row exclusions** tab to exclude entire rows that match the exclusion criteria.

   .. tip:: You can add custom data exclusions. Type the exclusion and then press **ENTER** or **RETURN** on your keyboard. For example: "test" or "ampersand ('&')". Values are not case-sensitive. Specific values, such as an ampersand must be included within parentheses *and* single quotes.

.. identity-resolution-05-exclude-data-end
