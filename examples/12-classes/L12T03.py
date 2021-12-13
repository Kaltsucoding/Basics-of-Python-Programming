# Tehdään luokka Car lisätään kolme ominaisuutta brand, model ja price. Tämän lisäksi määritellään kolme erilaista autoa (oliota)

class Car:
    brand = ""
    model = ""
    price = 0

    def car_skoda(self):
        tiedot = "Ensimmäisen auton merkki on" + self.brand +", sen malli on " + self.model + "ja hinta " + self.price
        return tiedot

    def car_audi(self):
        tiedot2 = "Toisen auton merkki on" + self.brand +", sen malli on " + self.model + "ja hinta " + self.price
        return tiedot2

    def car_volvo(self):
        tiedot3 = "Kolmannen auton merkki on" + self.brand +", sen malli on " + self.model + "ja hinta " + self.price
        return tiedot3

# Oliot eli tässä yhteydessä autot ja niiden ominaisuuksien määrittely

car_skoda = Car()
car_skoda.brand = " Skoda "
car_skoda.model = " Octavia "
car_skoda.price = " 3000 € "

car_audi = Car()
car_audi.brand = " Audi "
car_audi.model = " A4 "
car_audi.price = " 4000 € "

car_volvo = Car()
car_volvo.brand = " Volvo "
car_volvo.model = " V70 "
car_volvo.price = " 5000 € "

print(car_skoda.car_skoda())
print(car_audi.car_audi())
print(car_volvo.car_volvo())

# Muutetaan literalit inteiksi jotta saadaan kokonaishinta laskettua (Ihan vain muistin tueksi tämä välivaihe tehtävään)

Kolmetuhatta = "3000"
Muutos = int(Kolmetuhatta)
Neljätuhatta = "4000"
Muutos2 = int(Neljätuhatta)
Viisituhatta = "5000"
Muutos3 = int(Viisituhatta)

Yhteisarvo = (Muutos + Muutos2 + Muutos3)
print("Autojen kokonaishinta on yhteensä:", Yhteisarvo, "€")