# Ohjelma, jossa tallennetaan rahaa pankkitilille euroina ja sentteinä

Euromäärä = int(input("Euroa "))
Sentit = int(input("Senttiä "))
Tilinsaldo = Euromäärä + Sentit/100
print("Tilinsaldo: {:.2f} €".format(Tilinsaldo))