.. https://docs.amperity.com/guides/


.. meta::
    :description lang=en:
        Semantic tags must be defined for every data source that provides customer profile data to Stitch.

.. meta::
    :content class=swiftype name=body data-type=text:
        Semantic tags must be defined for every data source that provides customer profile data to Stitch.

.. meta::
    :content class=swiftype name=title data-type=string:
        Validate profile semantics

==================================================
Validate profile semantics
==================================================

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-howitworks-start
   :end-before: .. semantics-howitworks-end

.. identity-resolution-02-tables-with-pii-start

To validate semantic tags open the **Identity resolution** page in **Quick start**. On the **Identity tables** card, do one of the following:

#. Click **AmpAI select** to have the **AmpAI Assistant** determine which tables contain the best data for identity resolution, which fields in each data source are the optimal primary key, and which customer profile semantic tags to apply to fields in each data source.
#. Click **Manually select** on the **Identity your fields** card to apply semantic tags, including custom semantic tags, without using the **AmpAI Assistant**.

   .. image:: ../../images/mockup-guided-idres-semantic-tags.png
      :width: 500 px
      :alt: Identify tables with PII.
      :align: left
      :class: no-scaled-link

   .. tip:: A custom semantic tag is a string, such as "loyalty-id", that is typed directly into the **Semantic tags** column. Press the **ENTER** or **RETURN** key on your keyboard to save the custom semantic tag in the **Semantic tag editor**.

#. Click **Edit** on the **Identity your fields** card to review tables that are already selected.

.. identity-resolution-02-tables-with-pii-end
