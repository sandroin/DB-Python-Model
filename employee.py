from db import c


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    def __repr__(self):
        return "<Employee {}, Full Name: {} {}, Age: {}>".format(self.id, self.name, self.surname, self.age)

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    @classmethod
    def get_list(cls, **kwargs):
        params_for_filtering = []
        values = []
        for k, v in kwargs.items():
            params_for_filtering.append("{} = ?".format(k))
            values.append(v)
        if len(params_for_filtering) == 0:
            rows = c.execute("SELECT * FROM employee")
        else:
            rows = c.execute("SELECT * FROM employee WHERE " + " AND ".join(params_for_filtering), values)
        employees = []
        for row in rows.fetchall():
            employee = Employee(row["name"], row["surname"], row["age"], row["id"])
            employees.append(employee)
        return employees

    def delete(self):
        c.execute("DELETE FROM employee WHERE id = ?", (self.id,))

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    @classmethod
    def delete_group(cls, **kwargs):
        params_for_filtering = []
        values = []
        for k, v in kwargs.items():
            params_for_filtering.append("{} = ?".format(k))
            values.append(v)
        if len(params_for_filtering) == 0:
            c.execute("DELETE FROM employee")
        else:
            c.execute("DELETE FROM employee WHERE " + " AND ".join(params_for_filtering), values)
            
