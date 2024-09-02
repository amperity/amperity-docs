.. 
.. https://docs.amperity.com/datagrid/
.. 

.. |destination-name| replace:: Amazon Redshift
.. |plugin-namex| replace:: Amazon Redshift
.. |what-send| replace:: table rows that match a table schema
.. |filter-the-list| replace:: "ama"
.. |data-template-name| replace:: |destination-name|
.. |data-template-description| replace:: Send |what-send| to |destination-name|.
.. |data-template-config-settings-list| replace:: settings required by |destination-name| were
.. |data-template-config-settings-list-them-vs-it| replace:: them
.. |sendto-link| replace:: |sendto_amazon_redshift|


.. meta::
    :description lang=en:
        Configure Amperity to send data to Amazon Redshift.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amperity to send data to Amazon Redshift.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send data to Amazon Redshift

==================================================
Send data to Amazon Redshift
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-amazon-redshift-start
   :end-before: .. term-amazon-redshift-end

.. destination-amazon-redshift-steps-to-send-start

**To send data to Amazon Redshift**

#. Configure Amperity to send data to :doc:`Amazon S3 <destination_amazon_s3>`, and then configure your instance of |destination-name| to pull data from that Amazon S3 bucket.

#. Within Amazon Web Services there are multiple options for moving data from an Amazon S3 bucket to |destination-name|, such as configuring `AWS Glue <https://aws.amazon.com/glue/>`__ |ext_link| or using an `Amazon S3 lambda function <https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html>`__ |ext_link|.

.. destination-amazon-redshift-steps-to-send-end
