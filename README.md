# DB-Python-Model
This aim of this project is to simulate interaction of class Employee with an SQLite database table named employee. Below is a summary of its functionalities:

Class Method - get: Retrieves an Employee object from the database based on the provided primary key (pk).
Representation Method - __repr__: Returns a string representation of the Employee object, including its ID, full name, and age.
Method - update: Updates the database entry for the current Employee object with its current attributes.
Method - create: Creates a new entry in the database for the current Employee object.
Method - save: Saves changes made to the current Employee object. If it already exists in the database, it updates the entry; otherwise, it creates a new one.
Class Method - get_list: Retrieves a list of Employee objects from the database based on optional filtering criteria provided as keyword arguments.
Method - delete: Deletes the database entry corresponding to the current Employee object.
Comparison Methods - __gt__, __lt__: Implements comparison operations between Employee objects based on their ages.
Class Method - delete_group: Deletes multiple entries from the database based on optional filtering criteria provided as keyword arguments.
