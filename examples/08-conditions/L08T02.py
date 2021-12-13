# Kysytään kolme kokonaislukua ja tulostetaan niistä suurimman

Numero1 = int(input("Anna ensimmäinen numero "))
Numero2 = int(input("Anna toinen numero "))
Numero3 = int(input("Anna kolmas numero "))
if (Numero1 >= Numero2) and (Numero1 >= Numero3):
 Suurin = Numero1
elif (Numero2 >= Numero1) and (Numero2 >= Numero3):
 Suurin = Numero2
else:
 Suurin = Numero3
 print("Suurin numero: ", Suurin)