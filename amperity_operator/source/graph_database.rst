.. https://docs.amperity.com/operator/

:orphan:

.. meta::
    :description lang=en:
        Use a graph database to store relationships between customer profiles, transactions, and the Amperity ID graph.

.. meta::
    :content class=swiftype name=body data-type=text:
        Use a graph database to store relationships between customer profiles, transactions, and the Amperity ID graph.

.. meta::
    :content class=swiftype name=title data-type=string:
        Graph database

==================================================
Graph database
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-graph-database-start
   :end-before: .. term-graph-database-end

.. graph-database-start

A graph database is a collection of vertices and edges:

* .. include:: ../../shared/terms.rst
     :start-after: .. term-vertex-start
     :end-before: .. term-vertex-end
* .. include:: ../../shared/terms.rst
     :start-after: .. term-edge-start
     :end-before: .. term-edge-end

.. graph-database-end

.. graph-database-important-start

.. important:: This topic describes a graph database that uses the Gremlin data format, which is a supported data format for Amazon Neptune.

   The graph database queries included with Amperity may be customized to support any graph database format and destination.

.. graph-database-important-end


.. _graph-database-workflow:

Graph database workflow
==================================================

.. graph-database-workflow-start

A graph database workflow has two main steps:

#. :ref:`Add query templates <graph-database-workflow-add-templates>`, and then  run queries in Amperity to return data in a format that can be loaded by a graph database.
#. :ref:`Send the data <graph-database-workflow-send-data>` to Amazon S3, Azure Blob Storage, Google Cloud Storage, or SFTP, and then load that data to a graph database.
#. Enabling downstream :ref:`use cases <graph-database-workflow-use-cases>`.

.. graph-database-workflow-end


.. _graph-database-workflow-add-templates:

Add query templates
--------------------------------------------------

.. graph-database-workflow-add-templates-start

The query templates for the graph database are added to, and then accessed from the **Queries** page.

.. graph-database-workflow-add-templates-end

**To add Graph Database queries**

.. graph-database-workflow-add-templates-steps-start

#. From the **Queries** page click **Create**, and then select **Add Folder**. This opens the **Create Folder** dialog box.
#. Name the folder "Graph Database".
#. From the **Template** dropdown, select **Graph Database**.
#. Click **Create**. This creates a folder, into which a collection of draft Graph Database queries are added.
#. Take a few minutes to review the queries that are added by the "Graph Database" query template.

.. graph-database-workflow-add-templates-steps-end


.. _graph-database-workflow-send-data:

Send to a graph database
--------------------------------------------------

.. graph-database-workflow-send-data-start

Send graph database query results to one of the following destinations:

* :doc:`Amazon S3 <destination_amazon_s3>`
* :doc:`Azure Blob Storage <destination_azure_blob_storage>`
* :doc:`Google Cloud Storage <destination_google_cloud_storage>`
* :doc:`SFTP <destination_sftp>`

and then load that data to your preferred query database. 

The following graph databases support using Gremlin and importing CSV files directly:

* `AWS Neptune <https://docs.aws.amazon.com/neptune/latest/userguide/intro.html>`__ |ext_link| (`load CSV file <https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html>`__ |ext_link|)
* `CosmoDB <https://docs.microsoft.com/en-us/azure/cosmos-db/>`__ |ext_link| (`load CSV file <https://docs.microsoft.com/en-us/azure/cosmos-db/import-data>`__ |ext_link|)
* `DataStax <https://www.datastax.com/>`__ |ext_link| (`load CSV file <https://docs.datastax.com/en/dse/5.1/dse-dev/datastax_enterprise/graph/dgl/dglCSV.html>`__ |ext_link|)
* `Neo4j <https://neo4j.com/>`__ |ext_link| (`load CSV file <https://neo4j.com/developer/guide-import-csv/>`__ |ext_link|)
* `OrientDB <https://orientdb.org/>`__ |ext_link| (`load CSV file <https://www.orientdb.com/docs/2.2.x/Import-from-CSV-to-a-Graph.html>`__ |ext_link|)

Other graph databases, such as `JanusGraph <https://janusgraph.org/>`__ |ext_link| require using APIs to convert, and then load the graph data.

.. graph-database-workflow-send-data-end


.. _graph-database-workflow-use-cases:

Use cases
--------------------------------------------------

.. graph-database-workflow-use-cases-start

A graph database enables downstream use cases, such as:

#. Supporting advanced data science teams who need to use internal tools and models to interact with Amperity data.
#. Establishing links between profiles and preferences, and then using those results to augment data that is provided to a recommendation engine.
#. Using graphs to support CCPA and GDPR compliance, such as by identifying one piece of data, and then traversing the identity graph.

.. graph-database-workflow-use-cases-end


.. _graph-database-gremlin:

About Gremlin
==================================================

.. graph-database-gremlin-start

Gremlin is a path-oriented query language that is used for complex traversals of graph databases. Gremlin is a component of Apache Tinkerpop and is supported by most graph databases.

Amperity graph database templates provide a template that outputs to a CSV file that is easily integrated into a graph database that supports the Gremin graph traversal language.

.. graph-database-gremlin-end


.. _graph-database-gremlin-vertices:

Vertices
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-vertex-start
   :end-before: .. term-vertex-end

.. graph-database-gremlin-vertices-start

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Field
     - Required?
     - Description
   * - **~id**
     - |policy|
     - The unique identifier for the vertice.
   * - **name:type**
     - 
     - The properties of the vertice. There is no limit to the number of properties that may be specified.

       The format for this field is is the name of the field in the Amperity data table and its data type, separated by a colon. For example: **given_name:String** or **birthdate:Date**.
   * - **~label**
     - |policy|
     - The type of vertice that matches the object type. For Amperity, this is a customer profile, a Customer 360 profile, or a transaction.

.. graph-database-gremlin-vertices-end


.. _graph-database-gremlin-edges:

Edges
--------------------------------------------------

.. include:: ../../shared/terms.rst
   :start-after: .. term-edge-start
   :end-before: .. term-edge-end

.. graph-database-gremlin-edges-start

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Field
     - Required?
     - Description
   * - **~id**
     - |policy|
     - The unique identifier for the edge.
   * - **~from**
     - |policy|
     - The primary key for the starting vertice. This must correspond to a vertice with a matching **~id**.
   * - **~to**
     - |policy|
     - The primary key for the ending vertice. This must correspond to a vertice with a matching **~id**.
   * - **~label**
     - |policy|
     - The type of vertice that matches the object type. For Amperity, this is a customer profile, a Customer 360 profile, or a transaction.
   * - **name:type**
     - 
     - The properties of the vertice. There is no limit to the number of properties that may be specified.

       The format for this field is is the name of the field in the Amperity data table and its data type, separated by a colon. For example: **given_name:String** or **birthdate:Date**.

.. graph-database-gremlin-edges-end


.. _graph-database-query-templates:

Amperity query templates
==================================================

Use the default query templates to return vertices and edges for customer profiles, transactions, and the Amperity ID graph. Extend the query database templates to match your tenant.

The following default query templates are available:

* :ref:`graph-database-query-template-edge-profile`
* :ref:`graph-database-query-template-vertice-profile`
* :ref:`graph-database-query-template-edge-c360`
* :ref:`graph-database-query-template-vertice-c360`
* :ref:`graph-database-query-template-edge-transaction`
* :ref:`graph-database-query-template-vertice-transaction`


.. _graph-database-query-template-vertice-profile:

Profile vertices
--------------------------------------------------

.. graph-database-query-template-vertice-profile-start

Profile vertices are derived from the **Unified Coalesced** table.

.. code-block:: sql

   SELECT
     CONCAT(uc.pk,uc.datasource) AS "~id"
     ,uc.amperity_id AS "amperity_id:String"
     ,uc.datasource AS "datasource:String"
     ,uc.given_name AS "givenname:String"
     ,uc.surname AS "surname:String"
     ,uc.email AS "email:String"
     ,uc.phone AS "phone:String"
     ,uc.gender AS "gender:String"
     ,uc.birthdate AS "birthdate:Date"
     ,uc.address AS "address:String"
     ,uc.address2 AS "address2:String"
     ,uc.city AS "city:String"
     ,uc.state AS "state:String"
     ,uc.postal AS "postal:String"
     ,'Original_Profile' AS "~label"
   FROM Unified_Coalesced AS uc

.. graph-database-query-template-vertice-profile-end


.. _graph-database-query-template-edge-profile:

Profile edges
--------------------------------------------------

.. graph-database-query-template-edge-profile-start

Profile edges link scores in the **Unified Scores** table to raw profiles

.. code-block:: sql

   SELECT
     CONCAT(us.amperity_id, us.pk1, us.pk2) AS "~id"
     ,CONCAT(us.pk1,source1) AS "~from"
     ,CONCAT(us.pk2,source2) AS "~to"
     ,'Amperity ID Link' AS "~label"
     ,us.score AS "score:Double"
   FROM Unified_Scores AS us

.. graph-database-query-template-edge-profile-end


.. _graph-database-query-template-vertice-c360:

Customer 360 vertices
--------------------------------------------------

.. graph-database-query-template-vertice-c360-start

Customer 360 vertices are derived from the **Customer 360** table. Vertices can be focused on the customer profile:

.. code-block:: sql

   SELECT
     cus.amperity_id AS "~id"
     ,cus.given_name AS "givenname:String"
     ,cus.surname AS "surname:String"
     ,cus.email AS "email:String"
     ,cus.phone AS "phone:String"
     ,cus.gender AS "gender:String"
     ,cus.birthdate AS "birthdate:Date"
     ,cus.address AS "address:String"
     ,cus.address2 AS "address2:String"
     ,cus.city AS "city:String"
     ,cus.state AS "state:String"
     ,cus.postal AS "postal:String"
     ,'Amperity Profile' AS "~label"
   FROM Customer_360 AS cus

Vertices can be focused on customer profile *and* transactions:

.. code-block:: sql

   SELECT
     cus.amperity_id AS "~id"
     ,cus.given_name AS "givenname:String"
     ,cus.surname AS "surname:String"
     ,cus.email AS "email:String"
     ,cus.phone AS "phone:String"
     ,cus.gender AS "gender:String"
     ,cus.birthdate AS "birthdate:Date"
     ,cus.address AS "address:String"
     ,cus.address2 AS "address2:String"
     ,cus.city AS "city:String"
     ,cus.state AS "state:String"
     ,cus.postal AS "postal:String"
     ,cus.multi_purchase_brand AS "multi_purchase_brand:Bool"
     ,cus.multi_purchase_channel AS "multi_purchase_channel:Bool"
     ,cus.one_and_done AS "one_and_done:Bool"
     ,cus.early_repeat_purchaser AS "early_repeat_purchaser:Bool"
     ,cus.lifetime_preferred_purchase_brand AS "lifetime_preferred_purchase_brand:String"
     ,cus.lifetime_preferred_purchase_channel AS "lifetime_preferred_purchase_channel:String"
     ,cus.lifetime_order_revenue AS "lifetime_order_revenue:Double"
     ,cus.lifetime_order_frequency AS "lifetime_order_frequency:Int"
     ,cus.lifetime_total_items AS "lifetime_total_items:Int"
     ,cus.lifetime_largest_order_value AS "lifetime_largest_order_value:Double"
     ,cus.lifetime_average_order_value AS "lifelifetime_average_order_value:Double"
     ,cus.lifetime_average_item_price AS "lifetime_average_item_price:Double"
     ,cus.lifetime_average_num_items AS "lifetime_average_num_items:Double"
     ,'Amperity Profile' AS "~label"
   FROM Customer_360 AS cus

.. graph-database-query-template-vertice-c360-end


.. _graph-database-query-template-edge-c360:

Customer 360 edges
--------------------------------------------------

.. graph-database-query-template-edge-c360-start

Customer 360 edges link raw profiles in the **Unified Coalesced** table to profiles in the **Customer 360** table.

.. code-block:: sql

   SELECT DISTINCT
     CONCAT(uc.pk, uc.amperity_id) AS "~id"
     ,CONCAT(uc.pk,uc.datasource) AS "~from"
     ,uc.amperity_id AS "~to"
     ,'Customer360' AS "~label"
   FROM Unified_Coalesced AS uc

.. graph-database-query-template-edge-c360-end


.. _graph-database-query-template-vertice-transaction:

Transaction vertices
--------------------------------------------------

.. graph-database-query-template-vertice-transaction-start

Transaction vertices are derived from the **Unified Transactions** table. Vertices should have a consistent primary key and should link to vertices derived from the **Customer 360** table using the Amperity ID.

.. code-block:: sql

   SELECT
     CONCAT(ut.pk, ut.amperity_id) AS "~id"
     ,ut.amperity_id AS "amperity_id:String"
     ,ut.datasource AS "datasource:String"
     ,ut.order_id AS "order_id:String"
     ,ut.store_id AS "store_id:String"
     ,ut.digital_channel AS "digital_channel:String"
     ,ut.purchase_channel AS "purchase_channel:String"
     ,ut.purchase_brand AS "purchase_brand:String"
     ,ut.order_datetime AS "order_datetime:Date"
     ,ut.order_revenue AS "order_revenue:Double"
     ,ut.order_quantity AS "order_quantity:Int"
     ,ut.order_returned_quantity AS "order_returned_quantity:Int"
     ,ut.order_canceled_quantity AS "order_canceled_quantity:Int"
     ,ut.order_returned_revenue AS "order_returned_revenue:Double"
     ,ut.order_canceled_revenue AS "order_canceled_revenue:Double"
     ,'Transaction' AS "~label"
   FROM Unified_Transactions AS ut
   WHERE ut.amperity_id IS NOT NULL AND ut.order_id IS NOT NULL

.. graph-database-query-template-vertice-transaction-end


.. _graph-database-query-template-edge-transaction:

Transaction edges
--------------------------------------------------

.. graph-database-query-template-edge-transaction-start

Transaction edges link vertices derived from the **Unified Transactions** table to vertices derived from the **Customer 360** table. Each link should have a unique primary key and the **~from** value should be a unique **~id** value from transactions data.

.. code-block:: sql

   SELECT DISTINCT
     CONCAT(ut.pk, ut.amperity_id) AS "~id"
     ,CONCAT(ut.pk, ut.amperity_id) AS "~from"
     ,ut.amperity_id AS "~to"
     ,'Transaction Link' AS "~label"
   FROM Unified_Transactions AS ut
   WHERE ut.amperity_id IS NOT NULL AND ut.order_id IS NOT NULL

.. graph-database-query-template-edge-transaction-end
