.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Configure Amperity to pull data from Braze.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to pull data from Braze.

.. meta::
    :content class=swiftype name=title data-type=string:
        Pull from Braze

==================================================
Pull from Braze
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-braze-start
   :end-before: .. term-braze-end
   
.. source-braze-integration-start

Response data from campaigns can be integrated using |ext_braze_currents|, which synchronizes response data to Amazon S3 in |format_avro| format.

To integrate Braze response data into Amperity:

#. Configure a |ext_braze_currents_send_to_s3|.
#. Configure Amperity to :doc:`read Apache Avro files from that Amazon S3 bucket <source_amazon_s3>`.
#. Configure feeds and automate data loads using standard workflows.

.. source-braze-integration-end
