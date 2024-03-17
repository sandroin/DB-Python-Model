# DB-Python-Model
This aim of this project is to simulate interaction of class Employee with an SQLite database table named employee. Below is a summary of its functionalities:

1) Class Method - get: Retrieves an Employee object from the database based on the provided primary key (pk).
2) Representation Method - __repr__: Returns a string representation of the Employee object, including its ID, full name, and age.
3) Method - update: Updates the database entry for the current Employee object with its current attributes.
4) Method - create: Creates a new entry in the database for the current Employee object.
5) Method - save: Saves changes made to the current Employee object. If it already exists in the database, it updates the entry; otherwise, it creates a new one.
6) Class Method - get_list: Retrieves a list of Employee objects from the database based on optional filtering criteria provided as keyword arguments.
7) Method - delete: Deletes the database entry corresponding to the current Employee object.
8) Comparison Methods - __gt__, __lt__: Implements comparison operations between Employee objects based on their ages.
9) Class Method - delete_group: Deletes multiple entries from the database based on optional filtering criteria provided as keyword arguments.
