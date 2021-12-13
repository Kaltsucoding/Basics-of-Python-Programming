# Ohjelma jossa yritetään muuttaa arvoa jota ei ole olemassa. Alustetaan lista ja korjataan ohjelma niin ettei se kaadu.

Lista = [ 1, 3, 6, 9 ]
print("Lista on: ", Lista)

try:
    print("Koetetaan listan viimeiseksi numeroksi: ", Lista[4])
except IndexError:
    print("Odotettu virheilmoitus on IndexError tälle indexille.")

Lista2 = [ 1, 2, 3, 4 ]
print("Uusi listaus numeroista: ", Lista2)
print("Korjataan uudestaan uudella indexillä")
print("Viimeinen numero on siis: ", Lista2[3])