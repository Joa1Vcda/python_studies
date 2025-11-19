"""___dict___ and vars for instance atributs"""


class Person:
    current_year = 2025

    def __init__(self, name, years_old):
        self.name = name
        self.years_old = years_old

    def get_date_of_birth(self):
        return Person.current_year - self.years_old


p1 = Person("João", 19)
p1.name = "Ludimila"
p1.__dict__["Adress"] = "R1 Number 333"
dict_class = p1.__dict__
print(dict_class)
# print(p1.__dict__)
# print(p1.Adress)
print(vars(p1))
