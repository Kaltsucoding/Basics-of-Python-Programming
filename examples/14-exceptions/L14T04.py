# Tehdään kokoelma, jossa viisi (5) merkkijonoa ja kysytään käyttäjältä mihin kohtaan (kokoelmaa) haluaa laittaa uuden tekstin
#Tulostetaan taulokun sisältö alussa ja korjataa ohjelma jos käyttäjä antaakin indexin kokoelman ulkopuolelta

# Tässä tapauksessa kokoelma sisältää erilaisia tervehdyksiä

Kokoelma = {
    1: "Hei",
    2: "Moi",
    3: "Terve",
    4: "Päivää",
    5: "Tervehdys"
}

def kokoelmamuutos(Kokoelma):
    muutos = int(input("Anna arvo 1 muuttaaksesi kokoelman sisältöä "))
    if muutos == 1:
        Kokoelma[int(input("Anna jokin kokoelman lukuarvo, johon haluat muuttaa tekstin: "))] = input("Muutettava teksti: ")
    else:
        print("Hups nyt meni pieleen, yritä uudestaan antamalla arvo 1")

kokoelmamuutos(Kokoelma)
print("Kokoelmasi näyttää seuraavalta: ",Kokoelma)