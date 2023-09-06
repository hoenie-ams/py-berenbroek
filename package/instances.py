"""
Difference between class and instance variables
"""


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate


class Person:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable
        Person.count += 1

    def say_hi(self):
        return f"{self.name} says hello"

    @classmethod  # decorators
    def population_count(cls):
        return f"The total population is {cls.count}"


paul = Person(name="Paul")

print(Person.count)
print(Person.population_count())


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, value):
        date_vars = value.split("-")
        year = date_vars[0]
        month = date_vars[1]
        day = date_vars[2]
        return cls(year, month, day)


d1 = Date(2023, 9, 6)
d2 = Date.from_string("2023-9-6")
d3 = Date.from_dict({"year": 2023, "month": 9, "day": 6})

print(d2.year)
print(d2.month)
print(d2.day)

import pandas as pd

df = pd.DataFrame()


class Car:
    def __init__(self, license_plate, options):
        self.license_plate = license_plate
        self.options = options

    def number_of_options(self):
        return len(self.options)


rows = [Car("ACB13", ["Alloy wheels", "Neon", "PDC"]),
        Car("DEB14", ["Alloy wheels", "Neon", "PDC"])]


class Mortgage:
    def __init__(self, amount, rate, redemption_type):
        ...


class Portfolio:
    def __init__(self, mortgages):
        ...

    def total_value(self):
        ...

    def yield_to_maturity(self):
        ...
