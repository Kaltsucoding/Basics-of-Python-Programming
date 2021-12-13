# Tehtävä L1204
# Jatkoa tehtävään L12T03

# Tämä tehtävä oli mielestäni haastava toteuttaa rautalankamallina niin että satunnaisesti generoisi sekä auton että hinnan molemmat olioilla.
# Ensimmäinen osio on ohjelma, joka toteuttaa vain luokasta Car satunnaisesti hinnat.
# Alhaalla on ohjelma, joka ei ole olio-ohjelma, mutta se toimii generoiden satunnaisesti sekä autot että hinnan.
# Eli tässä on ikäänkuin kaksi eri toimivaa ohjelmaa samassa tiedostossa.

import random 

class Car:
    brand = ""
    model = ""
    price = 0
    
    def car_bmw(self):
        tiedot4 = "Neljännen auton merkki on" + self.brand + ",sen malli on" + self.model + "ja hinta " + str(self.price) + "€"
        return tiedot4

    def car_vw(self):
        tiedot5 = "Viidennen auton merkki on" + self.brand + ",sen malli on" + self.model + "ja hinta " + str(self.price) + "€"
        return tiedot5

    def car_ford(self):
        tiedot6 = "Kuudennen auton merkki on" + self.brand + ",sen malli on" + self.model + "ja hinta " + str(self.price) + "€"
        return tiedot6

    def car_opel(self):
        tiedot7 = "Seitsemännen auton merkki on" + self.brand + ",sen malli on" + self.model + "ja hinta " + str(self.price) + "€"
        return tiedot7

    def car_audi2(self):
        tiedot8 = "Kahdeksannen auton merkki on" + self.brand + " ,sen malli on" + self.model + "ja hinta " + str(self.price) + "€"
        return tiedot8


car_bmw = Car()
car_bmw.brand = " BMW "
car_bmw.model = " 5-sarja "
car_bmw.price = random.randint(1000, 10000)

car_vw = Car()
car_vw.brand = " VW "
car_vw.model = " Golf "
car_vw.price = random.randint(1000, 10000)

car_ford = Car()
car_ford.brand = " Ford "
car_ford.model = " Mondeo "
car_ford.price = random.randint(1000, 10000)

car_opel = Car()
car_opel.brand = " Opel "
car_opel.model = " Insignia "
car_opel.price = random.randint(1000, 10000)

car_audi2 = Car()
car_audi2.brand = " Audi"
car_audi2.model = " A6 "
car_audi2.price = random.randint(1000, 10000)

print(car_bmw.car_bmw())
print(car_vw.car_vw())
print(car_ford.car_ford())
print(car_opel.car_opel())
print(car_audi2.car_audi2())

# Tässä toteutettu for loopilla, jossa on 7 autoa ja niistä generoidaan satunnaisesti 5 sekä satunnaisesti hinta väliltä 1000-10 000

price = []
brand = ["BMW 5-Sarja", "VW Golf", "Ford Mondeo", "Opel Insingnia", "Audi A6", "Renault Laguna", "Toyota Avensis"]

for i in range(0,5):
    satunnaishinta = random.randint(1000,10000)
    price.append(satunnaishinta)
    autot = random.sample(brand,5)

print("Viisi satunnaista autoa seitsemästä ovat: ", autot)
print("Viiden satunnaisen auton hinnat ovat: ", price)
print("Autojen yhteishinta on euroina: ", sum(price))