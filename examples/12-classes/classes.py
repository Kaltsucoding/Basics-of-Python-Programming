# import the Vehicle class from another source file

from vehicle import Vehicle

# declare an object 'car' from 'Vehicle' class
car = Vehicle()

# declare an object 'car' from 'Vehicle' class
car = Vehicle()
car.make = "Datsun"
car.model = "100A"
car.engine_cc = 998
car.power_kw = 12

# print car info
print(car)


# declare an object 'car' from 'Vehicle' class (toiselle oliolle)
car = Vehicle("Datsun", "100A", 998, 12)

# declare an object 'car' from 'Vehicle' class (toinen olio)
car = Vehicle("Datsun", "100A", 998, 12)

# declare another vehicle
car2 = Vehicle("Toyota", "Celica", 1588, 43)

# print cars
print(car)
print(car2)


# use Vehicle.horsepower function to get power as hp (Kutsutaan hevosvoimia)
print("car power is: ", car.horsepower(), "hp")
print("car2 power is: ", car2.horsepower(), "hp")