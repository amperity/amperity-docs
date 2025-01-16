.. /downloads/markdown/


What makes a good PK?
==================================================

Stable and unique PKs are crucial for keeping Amperity IDs stable and linking source rows to unified customer profiles.


Linking source rows to profiles
==================================================

After all of your source data is stitched together to form a single, unified customer profile, it’s often important to know exactly which source rows each profile came from.

For example, linking allows you to comply with a legal request to delete all source rows associated with a given customer.


Amperity ID stability
==================================================

Stitch depends on PKs being defined for each source table in order to keep track of which source rows are linked to each unified customer profile after ID resolution.

When a source row changes (e.g. a user adds a secondary phone number or changes their account preferences), Stitch wants to assign the same Amperity ID to that customer instead of creating a new one.

To keep a customer’s Amperity ID stable, PKs are used to recognize that a given source row changed and wasn't deleted.


What makes a good PK?
==================================================

The two factors that make a good PK are uniqueness and stability:

* **first_name** is an example of a bad PK field because it’s unlikely to be *unique* among all rows in a table
* **updated_at** is another example of a bad PK field because even though it’s unique, its value for a given row can *change*, making it unstable
* **customer_id** is an example of a good PK field because it’s likely to identify the same source row if the contents of the row changes, tomorrow