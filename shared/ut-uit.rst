.. 
.. xxxxx
..



**TEMPLATE SECTIONS FOR COMMON CONTENT RELATED TO ORDERS AND ITEMS**





.. TODO: term-item-discount-percent
.. TODO: term-order-discount-percent

.. between-zero-and-one-start

This value must be between 0 and 1.

.. between-zero-and-one-end



.. TODO: term-currency

.. currency-must-be-consistent-across-orders-start

Currency must be consistent across all orders from the same data source.

.. currency-must-be-consistent-across-orders-end




.. TODO: term-item-cost
.. TODO: term-item-discount-amount
.. TODO: term-item-list-price
.. TODO: term-item-profit
.. TODO: term-item-subtotal
.. TODO: term-order-discount-amount
.. TODO: term-order-list-price
.. TODO: term-unit-cost
.. TODO: term-unit-discount-amount
.. TODO: term-unit-list-price
.. TODO: term-unit-profit
.. TODO: term-unit-subtotal

.. greater-than-or-equal-to-zero-purchases-start

This value must be greater than or equal to 0 for purchases, but less than or equal to 0 for returns or cancellations.

.. greater-than-or-equal-to-zero-purchases-end




.. TODO: term-is-canceled
.. TODO: term-is-return
.. TODO: Do not apply to data_tables.rst

.. is-canceled-is-return-cannot-be-same-start

The **is-cancellation** and **is-return** semantic tags may not be applied to the same field.

.. is-canceled-is-return-cannot-be-same-end




.. TODO: term-order-returned-quantity

.. less-than-or-equal-to-zero-purchases-start

This value must be less than or equal to 0.

.. less-than-or-equal-to-zero-purchases-end




.. TODO: term-item-quantity
.. TODO: term-item-revenue
.. TODO: term-unit-revenue

.. less-than-or-equal-to-zero-semantic-is-return-canceled-start

This value must be less than or equal to 0 when **is-return** or **is-cancellation** are true.

.. less-than-or-equal-to-zero-semantic-is-return-canceled-end




.. TODO: term-order-canceled-quantity

.. less-than-or-equal-to-zero-is-canceled-start

This value must be less than or equal to 0 when **is_canceled** is ``TRUE``.

.. less-than-or-equal-to-zero-is-canceled-end




.. TODO: order-returned-quantity
.. TODO: order-returned-revenue

.. less-than-or-equal-to-zero-is-return-start

This value must be less than or equal to 0 when **is_return** is ``TRUE``.

.. less-than-or-equal-to-zero-is-return-end




.. TODO: term-order-id

.. order-id-should-never-change-start

The order ID should never change, even when an item in the order is returned or canceled.

.. order-id-should-never-change-end




.. TODO: term-order-id

.. recycled-order-ids-not-guaranteed-to-be-unique-start

If order IDs are recycled and/or are otherwise not guaranteed to be unique over time, the unique identifier for the order must be updated to be a combination of the order ID and the date on which the order occurred. This must be done using domain SQL similar to: ``CONCAT(order_id, order_date)``.

.. recycled-order-ids-not-guaranteed-to-be-unique-end





.. TODO: term-order-date

.. related-order-dates-should-be-added-to-upc-start

Other dates associated with an order that are not specific to a transactions, such as dates associated with hotel stays and reservations, should be added to the **Unified Product Catalog** table.

.. related-order-dates-should-be-added-to-upc-end





.. TODO: Use the following block as a template for adding these into tables:



       .. note::

          .. include:: ../../shared/ut-uit.rst
             :start-after: .. related-order-dates-should-be-added-to-upc-start
             :end-before: .. related-order-dates-should-be-added-to-upc-end