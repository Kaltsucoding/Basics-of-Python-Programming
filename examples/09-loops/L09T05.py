# Ohjelma joka arpoo 7 numeroa 1-40 hyödyntämällä random-modulia

# Tein tästä kaksi eri versiota: Tässä ensimmäinen jossa käyttäjä antaa numeronsa ja lopussa loton oikea rivi.
# Ohjelmat toimivat, mutta toinen niistä on laitettu hipsuilla tekstiksi ettei terminaalissa tule tulkintavirheitä!

import random

"""
Numero1 = int(input("Ensimmäinen numerosi: "))
Numero2 = int(input("Toinen numerosi: "))
Numero3 = int(input("Kolmas numerosi: "))
Numero4 = int(input("Neljäs numerosi: "))
Numero5 = int(input("Viides numerosi: "))
Numero6 = int(input("Kuudes numerosi: "))
Numero7 = int(input("Seitsemäs numerosi: "))
print("Syötit seuraavat numerot: ", Numero1, Numero2, Numero3, Numero4, Numero5, Numero6, Numero7)
print("Loton oikea rivi on: ")
print(random.randrange(1,40),random.randrange(1,40),random.randrange(1,40),random.randrange(1,40),random.randrange(1,40),random.randrange(1,40),random.randrange(1,40))

"""

# Toinen versio, jossa kone vain arpoo numerot

lottonumbers = []
 
for i in range (0,7):
 
    x = (random.randint(1,40))
    while x in lottonumbers:
        x = random.randint(1,40)
    lottonumbers.append(x)
    
print("Tämänkertainen loton oikea rivi on: ", lottonumbers)