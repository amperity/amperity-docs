.. https://docs.amperity.com/amp360/


.. |destination-name| replace:: SFTP
.. |what-send| replace:: files
.. |sftp-type| replace:: **passphrase** or **private-key**
.. |sftp-hostname| replace:: **hostname**
.. |file-format| replace:: File format options include Apache Parquet (recommended when supported by the downstream workflow), CSV, TSV, and PSV
.. |encoding-method| replace:: Encoding method options include "Tar", "Tgz", "Zip", "GZip", and "None".


.. meta::
    :description lang=en:
        Use orchestrations to send query results from Amperity to any SFTP site.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use orchestrations to send query results from Amperity to any SFTP site.

.. meta::
    :content class=swiftype name=title data-type=string:
        Send query results to any SFTP Site

==================================================
Send query results to any SFTP Site
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-sftp-start
   :end-before: .. term-sftp-end

.. sendto-sftp-steps-to-send-start

.. include:: ../../shared/destinations.rst
   :start-after: .. destinations-overview-list-intro-start
   :end-before: .. destinations-overview-list-intro-end

#. :ref:`Build a query <sendto-sftp-build-query>`
#. :ref:`Add orchestration <sendto-sftp-add-orchestration>`
#. :ref:`Run orchestration <sendto-sftp-run-orchestration>`

.. sendto-sftp-steps-to-send-end

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-ask-to-configure-start
   :end-before: .. sendtos-ask-to-configure-end


.. _sendto-sftp-get-details-amperity:

Included SFTP site
==================================================

.. sendto-sftp-get-details-amperity-start

Every Amperity tenant includes an SFTP site with a hostname of ``<tenant>.sftp.amperity.com``. For example, if your company name is **ACME**, then your tenant's SFTP hostname is ``acme.sftp.amperity.com``. (The hostname is always all lowercase.)

.. note:: The SFTP site is provisioned by an Amperity administrator *after* the initial tenant creation. As such, the SFTP site is not immediately available, but this is not a long process. When the SFTP site is ready, Amperity will use SnapPass to send you the connection details. If you wish to use RSA key-based authentication, please provide the public key to your Amperity administrator when requesting SFTP access.

Once this site is provisioned, you may configure the SFTP site as an SFTP source or an SFTP destination to support any desired workflow. External customer processes can be configured to connect to the site using SFTP, after which they can add data to or pick up data from the site to support any external workflow.

.. caution:: The SFTP server has a 30-day limit on data and after 30 days, data may be moved automatically to an archive location. This location is still accessible to Amperity in case it becomes necessary to reuse it.

.. important:: The hostname for the SFTP site is always ``<tenant-name>.sftp.amperity.com``. Some older tenants may still be using the legacy address ``sftp.amperity.com``, if so, please contact your Amperity administrator about migrating.

.. sendto-sftp-get-details-amperity-end


.. _sendto-sftp-build-query:

Build query
==================================================

.. sendto-sftp-build-query-start

You will need to build a query, and then send the results to SFTP.

.. sendto-sftp-build-query-end


.. _sendto-sftp-add-orchestration:

Add orchestration
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-orchestration-start
   :end-before: .. term-orchestration-end

**To add an orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-add-orchestration-generic-start
   :end-before: .. sendtos-add-orchestration-generic-end


.. _sendto-sftp-run-orchestration:

Run orchestration
==================================================

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-start
   :end-before: .. sendtos-run-orchestration-end

**To run the orchestration**

.. include:: ../../shared/sendtos.rst
   :start-after: .. sendtos-run-orchestration-steps-start
   :end-before: .. sendtos-run-orchestration-steps-end
