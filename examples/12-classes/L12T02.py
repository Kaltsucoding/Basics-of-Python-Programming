# Tehdään luokka Cat ja annetaan sille kaksi ominaisuutta Name ja Color, lisäksi metodi miau

class Cat:
    name = ""
    color = "" 
    Ääni = ""

    def kissa1(self):
        Viesti = "Ensimmäisen kissan nimi on" + self.name +"," + "hänen värinsä on" + self.color + "ja hän naukuu kuten " + self.Ääni
        return Viesti

    def kissa2(self):
        Viesti2 = "Toisen kissan nimi on" + self.name +"," + "hänen värinsä on" + self.color + "ja toinen naukuu lailla " + self.Ääni
        return Viesti2

# Oliot ja ominaisuudet

Kissa1 = Cat()
Kissa1.name = " Olli "
Kissa1.color = " Musta "
Kissa1.Ääni = "Miuku"

Kissa2 = Cat()
Kissa2.name = " Mauno "
Kissa2.color = " Valkoinen "
Kissa2.Ääni = "Mauku"

print("Molemmat kissamme naukuu.")
print("Kissamme ovat seuraavan nimisiä ja värisiä:")
print(Kissa1.kissa1())
print(Kissa2.kissa2())

print("Tarinamme kissoista päättyy tähän.")