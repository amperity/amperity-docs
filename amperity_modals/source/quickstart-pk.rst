.. /downloads/markdown/


What makes a good primary key?
==================================================

Stable and unique primary keys are crucial for keeping Amperity IDs stable and linking source rows to unified customer profiles.


Linking source rows to profiles
==================================================

After all of your source data is stitched together to form a single, unified customer profile, it is important to know exactly which source rows each profile came from.


Amperity ID stability
==================================================

Stitch depends on primary keys being defined for each source table in order to keep track of which source rows are linked to each unified customer profile after ID resolution.

When a source row changes, such as when a user adds a secondary phone number or changes their account preferences, Stitch wants to assign the same Amperity ID to that customer instead of creating a new one.

To keep a customer's Amperity ID stable, primary keys are used to recognize that a given source row changed and was not deleted.


What makes a good primary key?
==================================================

The two factors that make a good primary key are uniqueness and stability:

* **first_name** is an example of a bad primary key field because it is unlikely to be *unique* among all rows in a table
* **updated_at** is another example of a bad primary key field because even though it is unique, its value for a given row can *change*, making it unstable
* **customer_id** is an example of a good primary key field because it is likely to identify a single customer and is a reliable value over time