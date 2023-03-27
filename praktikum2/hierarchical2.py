class Rakyat:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

class Pedagang(Rakyat):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def get_department(self):
        return self.department

class Penyanyi(Rakyat):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language

    def get_language(self):
        return self.language

# Hierarchical Inheritance
class SeniorPenyanyi(Penyanyi):
    def __init__(self, name, age, salary, language, level):
        super().__init__(name, age, salary, language)
        self.level = level

    def get_level(self):
        return self.level