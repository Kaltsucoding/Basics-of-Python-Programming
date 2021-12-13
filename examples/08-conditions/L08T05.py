# Kysytään viisi lukua ja lasketaan yhteen nollaa suuremmat luvut

Numero1 = int(input("Anna ensimmäinen numero "))
if Numero1 <= 0:
    Numero1 = 0
Numero2 = int(input("Anna toinen numero "))
if Numero2 <= 0:
    Numero2 = 0
Numero3 = int(input("Anna kolmas numero "))
if Numero3 <= 0:
    Numero3 = 0
Numero4 = int(input("Anna neljäs numero "))
if Numero4 <= 0:
    Numero4 = 0
Numero5 = int(input("Anna viides numero "))
if Numero5 <= 0:
    Numero5 = 0
Yhteenlasku1 = Numero1 + Numero2 + Numero3 + Numero4 + Numero5 
print("Yhteenlaskun tulos ilman nollia tai negatiivista arvoa on", Yhteenlasku1)

# 1+2+3+4+5 = 15
# -2,0,2,4,6 = 12