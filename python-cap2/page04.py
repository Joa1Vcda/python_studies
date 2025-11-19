"""atributes for class"""

class Person:
    current_year = 2025

    def __init__(self, name, years_old):
        self.name = name
        self.years_old = years_old

    def get_date_of_birth(self):
        return Person.current_year - self.years_old


p1 = Person("João", 19)
p2 = Person("Ludimila", 19)
p3 = Person("Mario", 65)

print(p3.get_date_of_birth())
print(p1.get_date_of_birth())
print(p2.get_date_of_birth())
