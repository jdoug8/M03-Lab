
class Vehicle:
    def __init__(self, type):
        self.type = type



class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

user_year = Automobile(input("Please enter the year of your vehicle: "))
user_make = Automobile(input("Please enter the maker of your vehicle: "))
user_model = Automobile(input("Please enter the model of your vehicle: "))
user_doors = Automobile(input("Please enter the number of doors on your vehicle: "))
user_roof = Automobile(input("Please enter type of roof on your vehicle: "))

print("Vehicle type:", user_type.type)
print("Year:", user_year.model)
print("Make:", user_make.make)
print("Model:", user.model.model)
print("Number of doors:", user_doors.doors)
print("Type of roof:", user_roof.roof)