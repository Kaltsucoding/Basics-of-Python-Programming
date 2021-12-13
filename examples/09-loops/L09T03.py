# Kysytään käyttäjältä luku 1-10 ja tulostetaan luvusta 1 syötettyyn lukuun lukujen neliöt

Kokonaisluku = int(input("Anna luku väliltä 1-10: "))
for Kokonaisluku in range(1, Kokonaisluku +1):
 Neliö = Kokonaisluku * Kokonaisluku
 print("Luvun", Kokonaisluku, "neliö on", Neliö)