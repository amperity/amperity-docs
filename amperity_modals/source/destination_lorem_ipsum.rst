.. 
.. /markdown
.. 


Lorem Ipsum
==================================================


.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-lorem-ipsum-alt-start
   :end-before: .. setting-lorem-ipsum-alt-end

.. include:: ../../shared/destination_settings.rst
   :start-after: .. setting-lorem-ipsum-long-start
   :end-before: .. setting-lorem-ipsum-long-end


Requirements
==================================================

This destination has the following requirements.

#. .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-short-start
      :end-before: .. setting-lorem-ipsum-short-end

#. .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-short-start
      :end-before: .. setting-lorem-ipsum-short-end

#. .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-short-start
      :end-before: .. setting-lorem-ipsum-short-end



Settings
==================================================

Configure the following settings.

**setting**

   **Required**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-short-start
      :end-before: .. setting-lorem-ipsum-short-end

**setting**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-short-start
      :end-before: .. setting-lorem-ipsum-short-end

**setting**

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-alt-start
      :end-before: .. setting-lorem-ipsum-alt-end

   Configure this setting: `in DESTINATION <https://docs.amperity.com>`__ then use that value here.


Setup destination
--------------------------------------------------

This is a series of steps:

#. Get details.
#. Create credentials.
#. Configure destination.

   .. include:: ../../shared/destination_settings.rst
      :start-after: .. setting-lorem-ipsum-short-start
      :end-before: .. setting-lorem-ipsum-short-end

#. Validate workflow.


More information
--------------------------------------------------

If we need more information we can add a section.

Formatting observations for Markdown files in app modals:

* No admonitions in the core file.
* Includes from /shared and other files is OK.
* No tables (because tables are hard).
* No images from docs site; app could put images into the modal.
* Docs comments and docs TODO are not passed through by Pandoc when converting .rst > .md.
* Links cannot be REF or DOC, only defined as external with paths (can be a relative path, should that be necessary).


Links
==================================================

* Link to `Amperity Docs <https://docs.amperity.com>`__.
* Link to `Active Campaign <https://docs.amperity.com/datagrid/destination_active_campaign.html>`__.
* Relative link example (probably 404s) `some link text here <../tutorials/start_here.html>`__
