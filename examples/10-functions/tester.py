from utils import *
show_info()

from utils import sub

from utils import average

numero = sub(10, 5)
print("vähennyslaskusta palautetaan luku:", numero)

keskiarvo1 = int(input("Anna ensimmäinen kokonaisluku: "))
keskiarvo2 = int(input("Anna toinen kokonaisluku: "))
keskiarvo3 = int(input("Anna kolmas kokonaisluku: "))
lkm = int(input("Montako kokonaislukua annoit? "))
print("Keskiarvosi on:")
print(average(keskiarvo1, keskiarvo2, keskiarvo3, lkm))