.. https://docs.amperity.com/operator/


.. |destination-name| replace:: Iterable
.. |destination-api| replace:: Iterable API
.. |plugin-name| replace:: "Iterable"
.. |credential-type| replace:: "iterable"
.. |required-credentials| replace:: "API Key" and "Base URL"
.. |audience-primary-key| replace:: "email"
.. |what-send| replace:: email lists
.. |where-send| replace:: |destination-name|
.. |filter-the-list| replace:: "ite"
.. |allow-for-what| replace:: audiences
.. |allow-for-duration| replace:: up to 48 hours


.. meta::
    :description lang=en:
        Build campaigns in Amperity that send audiences to Iterable.

.. meta::
    :content class=swiftype name=body data-type=text:
        Build campaigns in Amperity that send audiences to Iterable.

.. meta::
    :content class=swiftype name=title data-type=string:
        Build campaigns that send data to Iterable

==================================================
Build campaigns that send data to Iterable
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-iterable-start
   :end-before: .. term-iterable-end

.. campaign-iterable-start

Use Amperity to build campaigns that send audiences to |destination-name|. Configure the campaign to manage list membership and sync user profile attributes to support personalized messaging across email, push notifications, SMS, and in-app channels.

.. campaign-iterable-end


.. _campaign-iterable-prerequisites:

Prerequisites
==================================================

.. campaign-iterable-prerequisites-start

Before you can build campaigns that send audiences to |destination-name|, you must:

#. :doc:`Configure a destination for Iterable <destination_iterable>`.
#. Build a segment or query that returns the audience you want to send to |destination-name|.
#. Verify that your query includes the **email** or **userId** field as required by your |destination-name| project type.

.. campaign-iterable-prerequisites-end

