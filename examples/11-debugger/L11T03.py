# Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen. 
# Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.

Lkm = 0
Yhteenlasku = " "

while True:
    Nimi = str(input("Anna Nimiä, tyhjä kenttä lopettaa kysymyksen: "))
    if not Nimi:
      break
    else:
        Nimi2 = str(Nimi)
        Lkm = Lkm + 1
        Yhteenlasku = (str(Yhteenlasku)) + Nimi2 + ","
print("Syötit nimiä", Lkm, "kappaletta")
print("Nimien määrä:",Yhteenlasku)