class Person:
    current_year = 2025

    def __init__(self, name, years_old):
        self.name = name
        self.years_old = years_old

    def __init_subclass__(cls, name):
        return (name, 25)

    @classmethod
    def factory_25years_old(cls, name):
        return (name, 25)


p1 = Person("João", 25)
print(type(p1))
print(p1.__dict__)
p2 = Person.factory_25years_old("João")
print(type(p2))
print(p2)
p3 = Person.__init_subclass__("João")
print(type(p3))
print(p3)
