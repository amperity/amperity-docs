.. https://docs.amperity.com/legions/

:orphan:


==================================================
Semantics: Keys
==================================================

.. _semantics-keys:

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-keys-start
   :end-before: .. semantics-keys-end

* :ref:`semantics-key-blocking`
* :ref:`semantics-key-customer`
* :ref:`semantics-key-foreign`
* :ref:`semantics-key-primary`
* :ref:`semantics-key-separation`


.. _semantics-key-blocking:

Blocking keys (bk)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-bk-start
   :end-before: .. term-bk-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-blocking-start
   :end-before: .. semantics-key-blocking-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-blocking-caution-start
   :end-before: .. semantics-key-blocking-caution-end


.. _semantics-key-customer:

Customer keys (ck)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-ck-start
   :end-before: .. term-ck-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-customer-tip-start
   :end-before: .. semantics-key-customer-tip-end


.. _semantics-key-foreign:

Foreign keys (fk)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-foreign-key-start
   :end-before: .. term-foreign-key-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-fk-start
   :end-before: .. term-fk-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-foreign-start
   :end-before: .. semantics-key-foreign-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-foreign-default-start
   :end-before: .. semantics-key-foreign-default-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-foreign-common-start
   :end-before: .. semantics-key-foreign-common-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-foreign-tip-start
   :end-before: .. semantics-key-foreign-tip-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-foreign-trivial-duplicates-start
   :end-before: .. semantics-key-foreign-trivial-duplicates-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-foreign-important-start
   :end-before: .. semantics-key-foreign-important-end

.. tip:: In an unusual case where a foreign key is associated with a field to which :ref:`a profile (PII) semantic tag is applied <semantics-profile>` be sure to configure the column created by the foreign key in customer 360 database tables to hide values from users without permission to view PII.


.. _semantics-key-primary:

Primary keys (pk)
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-primary-key-start
   :end-before: .. term-primary-key-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-primary-caution-start
   :end-before: .. semantics-key-primary-caution--end

.. include:: ../../shared/terms.rst
   :start-after: .. term-pk-start
   :end-before: .. term-pk-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-primary-tip-start
   :end-before: .. semantics-key-primary-tip-end


.. _semantics-key-separation:

Separation keys (sk)
==================================================

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-separation-non-default-start
   :end-before: .. semantics-key-separation-non-default-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-separation-warning-start
   :end-before: .. semantics-key-separation-warning-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-separation-start
   :end-before: .. semantics-key-separation-end

.. include:: ../../shared/terms.rst
   :start-after: .. term-sk-start
   :end-before: .. term-sk-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-separation-assign-pairs-start
   :end-before: .. semantics-key-separation-assign-pairs-end

.. include:: ../../amperity_reference/source/semantics.rst
   :start-after: .. semantics-key-separation-important-start
   :end-before: .. semantics-key-separation-important-end
