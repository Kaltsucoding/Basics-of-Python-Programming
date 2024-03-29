
# declare a Vehicle class to hold information about vehicle data
class Vehicle:
    # override conversion from Vehicle to string with __str__
    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.engine_cc) + "cc, " + str(self.power_kw) + "kw"

    make = ""
    model = ""
    engine_cc = 0
    power_kw = 0


# declare a Vehicle class to hold information about vehicle data (toinen olio)
class Vehicle:
    def __init__(self, make="", model="", engine_cc=0, power_kw=0):
        self.make = make
        self.model = model
        self.engine_cc = engine_cc
        self.power_kw = power_kw

    # override conversion from Vehicle to string with __str__
    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.engine_cc) + "cc, " + str(self.power_kw) + "kw" 
        
    make = ""
    model = ""
    engine_cc = 0
    power_kw = 0

# Metodi eli erillinen funktio luokalle vechicle, palauttaa hevosvoimat
    def horsepower(self):
        return self.power_kw * 1.341