# Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot. 
# Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda). 
# Keksi itse erilaisia rekisterinumeroita ja automerkkejä. Tallenna tiedot valitsemaasi kokoelmaan. 
# Tulosta sen jälkeen autojen tiedot ensin aakkosjärjestyksssä automerkin mukaan, ja sen jälkeen aakkosjärjestyksessä rekisterinumeron mukaan.

Autokokoelma = {
    12345670: "VW Golf",
    12345671: "Audi A4",
    12345672: "Skoda Octavia",
    12345673: "BMW 3-Sarja",
    12345674: "Volvo s60",
    12345675: "Mercedes-Benz C-Sarja",
    12345676: "Lada Niva",
    12345677: "Toyota Avensis",
    12345678: "Subaru Impreza",
    12345679: "Honda Accord"
}

Rekisterikokoelma = {
    123456789: "AEA-313",
    123456790: "JYY-567",
    123456791: "HUI-121",
    123456792: "GTJ-380",
    123456793: "BGJ-632",
    123456794: "MNM-960",
    123456795: "COF-651",
    123456796: "SAI-666",
    123456797: "FIO-279",
    123456798: "BOV-526"
}

# Tulostetaan autot ja rekisterinumerot aakkosjärjestyksessä

# Autot merkin mukaan aakkosjärjestyksessä
print("Autot aakkosjärjestyksessä ovat: ")
Aakkoslistaus = [sorted(Autokokoelma.values())]
print(Aakkoslistaus)

# Rekisterinumerot aakkosjärjestyksessä
print("Rekisterikilvet aakkosjärjestyksessä ovat: ")
Aakkoslistaus2 = [sorted(Rekisterikokoelma.values())]
print(Aakkoslistaus2)