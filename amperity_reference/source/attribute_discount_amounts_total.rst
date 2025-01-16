.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        The total discount amount should equal the order-level discount amount plus the sum of all item-level discount amounts for the same order ID.

.. meta::
    :content class=swiftype name=body data-type=text:
        The total discount amount should equal the order-level discount amount plus the sum of all item-level discount amounts for the same order ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        Total discount amount

==================================================
Total discount amount
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-total-discount-amount-start
   :end-before: .. term-total-discount-amount-end

.. attribute-discount-amounts-total-start

.. note:: Total discount amount is not a default attribute in Amperity, but you may configure your tenant to support it.

   You can extend your customer 360 database to include this attribute using SQL within a domain table (and then apply a custom semantic tag like **txn-total-discount-amount**) or within your customer 360 database.

.. attribute-discount-amounts-total-end
