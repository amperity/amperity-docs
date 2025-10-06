.. https://docs.amperity.com/contributing/


==================================================
Terminology
==================================================

There are correct uses of terms within Amperity documentation. Refer to the Google Developer Documentation Style Guide: https://developers.google.com/style/ for words that are not specified here.


.. _term-s3:

**Amazon S3** vs. **S3**
   Amazon S3 is the correct trademarked name for the Simple Storage Service. It's often shortened to just S3, but we should use Amazon S3 in documentation as often as possible.


.. _term-amperity:

**Amperity** vs. **Amperity's**
   You should almost never write |company_name| (or any trademarked term) as a possessive, such as "Amperity's Stitch process is the best." Rewrite until |company_name| stands alone, such as "The best Stitch offerings are from |company_name|."

   .. note:: This is one of the reasons why the technical documentation uses a token for |company_name|: ``|company_name|``. Sure, you have to type more characters, but it also helps make sure that the company name is used correctly. (Plus, in the event of a merger or company rename--and we all know that will *never* happen--we can just change the token.)


.. _term-azure:

**Azure storage services**
   Azure, in the context of storage services like Azure Blob Storage and Azure Data Lake Storage should be used in the first instance. Microsoft does not use acronyms (ABS, ADLS), but does drop the Azure from second instances (Blob Storage, Data Lake Storage). In Amperity context, "Azure storage services" is probably fine also for generic references.


.. _term-blacklist:

**blacklist** / **whitelist**
   Do not use these terms. This remains true even when a third-party chooses to use those terms to describe their software. For background, see `Terminology, Power and Oppressive Language <https://tools.ietf.org/id/draft-knodel-terminology-00.html>`__ |ext_link|. See **blocklist** / **allowlist**.


.. _term-blocklist:

**blocklist** / **allowlist**
   Use the word-pair **blocklist** and **allowlist** to refer behaviors and processes that block or allow values to be processed by Amperity, such as a bad-values blocklist or a 360 values blocklist.


.. _term-datasource:

**datasource** vs. **data source**
   Use **data source** as two words to describe upstream sources from which Amperity is configured to pull data.


.. _term-datasheet:

**datasheet** vs. **data sheet**
   Use **datasheet** as a single word to describe a deliverable that contains technical information for customers about an |company_name| product or scenario.


.. _term-data-table:

**data table** vs. **datatable**
   Use **data table** as two words as a way to generically describe the things that exist in a database: "data tables".

   Use the correct name when it's available, such as "domain table" or "customer 360 table", but as a generic reference "data table" is fine.


.. _term-dummy:

**dummy**, **dumb**
   Avoid using **dummy** (and variations) as a synonym for "placeholder".


.. _term-e-commerce:

**e-commerce** vs. **ecommerce** or **eCommerce**
   It's **e-commerce**. Why? `Because Merriam-Webster says so <https://www.merriam-webster.com/dictionary/e-commerce>`__. It's arbitrary otherwise.


.. _term-excited:

**excited**
   Avoid using this term to prevent potential localization issues with the meaning of this word in certain parts of the world.


.. _term-filename:

**filename** vs. **FILENAME**
   Probably the latter. What we mean here is, for example, the file extension for a Microsoft Excel spreadsheet is literally ``.xls``. This should never be written literally, but instead abbreviated and in all caps, like ``XLS`` (as opposed to ``xls``), unless you need to say the full filename and extension together, in which case you'd use ``some-file.xls``.


.. _term-master:

**master** / **slave**
   Do not use these terms. This remains true even when a third-party chooses to use those terms to describe their software. For background, see `Terminology, Power and Oppressive Language <https://tools.ietf.org/id/draft-knodel-terminology-00.html>`__ |ext_link|. See **primary** / **replica**.


.. _term-multi-tenant:

**multitenant** vs **multi-tenant** or **multi tenant**
   It's **multitenant**. Why? Because.


.. _term-null:

**NULL** vs. **Null** vs. **null**
   **NULL** indicates something does not have a value. In Amperity documentation we use **NULL**. Why? Because the context of **NULL** in Amperity documentation is almost always a SQL context.


.. _term-on-premises:

**on-premises** vs. **on-premise**
   It's **on-premises**. Why? Because. The words premise and premises do not mean the same thing. The plural of premise is not premises.

   When referring to the installation of computer-related hardware, software, and whatnots within the customer's physical environment (and not, say, "the cloud") always (and without exception) use the term **on-premises**.

   .. note:: The use of a hyphen between on and premises in **on-premises** is debated in some circles, but not here at |company_name|. We use the hyphen. See **on-site**.


.. _term-on-site:

**on-site** vs. **onsite**
   A synonym of **on-premises** generally. Use **on-premises** when referring to hardware and software deployments that are not hosted in a Cloud environment, such as Amazon AWS. Use **on-site** for any non-on-premises situations, such as when individuals from |company_name| visit a customer: "An |company_name| representative visits with you on-site to discuss your on-premises deployment options."


.. _term-open-source:

**open source** vs. **open-source**
   |company_name| prefers **open source** (without the hyphen) though technically both are correct.


.. _term-primary-replica:

**primary** / **replica**
   Use the word-pair **primary** and **replica** to refer to machines in a cluster. For example, in a YARN/Spark/Hadoop cluster, a **primary** machine manages the cluster (the YARN Resource Manager), and then each **replica** node in the cluster is run when asked to by the primary (the YARN Node Manager).

   .. warning:: Use **primary** / **replica** even when the application to which you are referring uses another term, such as how YARN refers to **master** and **slave** nodes.


.. _term-replica:

**replica**
   See **primary** / **replica**.


.. _term-serial-comma:

**serial comma**
   See Oxford (or serial) comma.


.. _term-slave:

**slave**
   See **primary** / **replica**. Don't use this term.


.. _term-stitch:

**Stitch** vs. **stitch**, **stitched**, or **stitching**
   You can stitch data and data can be stitched, but only Stitch is a feature within Amperity.

   Use a capital "S" when referring to Stitch as a feature. Never use Stitched, or Stitch's. Just Stitch. Rewrite your sentences to make this happen.

   Any other use of stitch should have a lower-case "s" and may follow any other standard use cases.


.. _term-web-ui:

**web UI** vs. **web user interface** vs. **UI**
   Use **web UI** to describe a web user interface, generically, but use **UI** when referring to the web UI for a |company_name| application. For example, Amperity UI.


.. _term-white-paper:

**white paper** vs. **whitepaper**
   Use **white paper** (two words) to describe a technical article written by |company_name|.
