

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance -= amount

    def pretty_print(self):
        # print(self.owner + " has EUR " + self.balance)
        # print("{} has EUR {}".format(self.owner, self.balance))
        print(f"{self.owner} has EUR {self.balance}")


account_paul = BankAccount("Paul")
account_joris = BankAccount("Joris")

account_paul.deposit(150)
account_paul.withdraw(50)
account_paul.pretty_print()

accounts = [account_paul, account_joris]
total_balance = account_paul.balance + account_joris.balance
total_balance_loop = 0
for acc in accounts:
    total_balance_loop += acc.balance


class Base:
    pass


class Derived(Base):
    pass


class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def drive(self):
        return "Driving"

    def brake(self):
        return "Braking"


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def brake(self):
        return "Breaking real hard"


car = Car("AB123DF")
print(car.drive())
print(car.brake())

truck = Truck("ZC134F")
print(truck.drive())
print(truck.brake())
