.. 
.. https://docs.amperity.com/datagrid/
.. 


.. meta::
    :description lang=en:
        Calculate the store that is nearest to an individual customer, as represented by their Amperity ID.

.. meta::
    :content class=swiftype name=body data-type=text:
        Calculate the store that is nearest to an individual customer, as represented by their Amperity ID.

.. meta::
    :content class=swiftype name=title data-type=string:
        Nearest store

==================================================
Nearest store
==================================================

.. calculate-nearest-store-start

Amperity can be configured to calculate the store that is nearest to an individual customer, as represented by their Amperity ID.

.. calculate-nearest-store-end

.. calculate-nearest-store-contact-support-start

.. important:: Nearest store calculations must be enabled for use in Amperity. This effort typically requires some customization and is not the same across tenants.

   Contact your Amperity support representative via the `Amperity Support Portal <../support/index.html>`__ (or send email to support@amperity.com) to discuss your options for adding nearest store capabilities to your tenant.

.. calculate-nearest-store-contact-support-start


.. _calculate-nearest-store-requirements:

Requirements
==================================================

.. calculate-nearest-store-requirements-start

Calculating nearest store requires data to be provided to Amperity that includes the latitude and longitude for each store location. Amperity then uses a publicly available dataset to convert home zip codes to latitude and longitude. Amperity then uses the geographic center of each zip code to calculate the straight-line distance for the store nearest to the individual.

.. calculate-nearest-store-requirements-end


.. _calculate-nearest-store-calculated-fields:

Calculated fields
==================================================

.. calculate-nearest-store-calculated-fields-start

For each record in the customer 360 database, the following fields are added:

* nearest_store_id
* nearest_store_name
* nearest_store_distance_miles

.. calculate-nearest-store-calculated-fields-end


.. _calculate-nearest-store-example:

Example
==================================================

.. calculate-nearest-store-example-start

A very simple example of calculating nearest stores starts with a common table expression that uses a |ext_haversine_formula| to calculate latitude and longitude. United States zip codes are joined to a table that contains data about the physical location of stores, after which stores are ranked by distance. The store with the highest rank is the closest store.

.. calculate-nearest-store-example-end

.. calculate-nearest-store-example-caution-start

.. caution:: This example is appropriate for use with small, static data sources, or for defining a proof of concept for early iteration that will require a more complex workflow.

.. calculate-nearest-store-example-caution-end

.. calculate-nearest-store-example-sql-start

.. code-block:: sql

   WITH
     distance_cte AS (
       SELECT
         2 * 3959 * asin(
           sqrt(
             power(
               sin((
                 radians(CAST(stores.Latitude AS decimal(15, 10))) -
                 radians(CAST(census.latitude AS decimal(15, 10))))
               / 2), 2)
             + cos(radians(CAST(stores.Latitude AS decimal(15, 10))))
             * cos(radians(CAST(census.latitude AS decimal(15, 10))))
             * power(
               sin((
                 radians(CAST(stores.Longitude AS decimal(15, 10))) -
                 radians(CAST(census.longitude AS decimal(15, 10))))
               / 2), 2)
             )
           ) distance
         ,census.zip_code
         ,stores.store_id
         ,stores.name
       FROM Stores_Table stores
       CROSS JOIN Census_Table census
       WHERE stores.Residence = true
     ),
     ranked_distance AS (
       SELECT 
         zip_code
         ,store_id
         ,distance
         ,`name`
       RANK() OVER (PARTITION BY zip_code ORDER BY distance asc, store_id) AS rank
       FROM distance_cte
       WHERE distance IS NOT NULL
     )

   SELECT
     *
   FROM ranked_distance
   WHERE rank = 1

.. calculate-nearest-store-example-sql-end
