#Kysytään käyttäjältä numeroita ja tulostetaan niiden lukumäärä sekä summa

#Muuttujat määritellään alkutilanteessa seuraavasti

Numero = 0
Yhteenlasku = 0

while True:
    Kokonaisluku = input("Anna kokonaisluku, tyhjä kenttä lopettaa kysymyksen: ")
    if not Kokonaisluku:
      break
    else:
        Kokonaisluku2 = int(Kokonaisluku)
        Numero = Numero + 1
        Yhteenlasku = (int(Yhteenlasku)) + Kokonaisluku2
print("Syötit lukuja", Numero, "kappaletta")
print("Kokonaislukujen summa:", Yhteenlasku)