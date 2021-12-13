#Kysytään jokaisen viikonpäivän sademäärää ja lasketaan kokonaissademäärä lopussa.

Sademäärä1 = int(input("Anna maanantain sademäärä: "))
Sademäärä2 = int(input("Anna tiistain sademäärä: "))
Sademäärä3 = int(input("Annan keskiviikon sademäärä: "))
Sademäärä4 = int(input("Anna torstain sademäärä: "))
Sademäärä5 = int(input("Anna perjantain sademäärä: "))
Sademäärä6 = int(input("Anna lauantain sademäärä: "))
Sademäärä7 = int(input("Anna sunnuntain sademäärä: "))
for Kokonaissademäärä in range(1, 8):
    print("Viikonpäivä",Kokonaissademäärä)
Kokonaissademäärä = Sademäärä1 + Sademäärä2 + Sademäärä3 + Sademäärä4 + Sademäärä5 + Sademäärä6 + Sademäärä7
print("Viikonpäivien 1-7 kokonaissademäärä:", Kokonaissademäärä, "millimetriä")