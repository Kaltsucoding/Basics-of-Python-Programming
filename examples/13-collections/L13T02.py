# Tehtävä A
# Kysytään käyttäjältä arvosanoja 0-5 kunnes käyttäjä antaa tyhjän syötteen. Näytetään syötetyt arvosanat, niiden määrä ja keskiarvo

lista = [ ] 
while True:
    Arvosana = input("Syötä arvosanoja, arvosana-asteikko on 0-5: ")
    if not Arvosana:
        break
    else:
        lista.append(int(Arvosana))

print("Syöttämäsi arvosanat ovat: ", lista)
print("Arvosanoja on", len(lista), "kappaletta")

Keskiarvo = sum(lista) / len(lista)
print("Arvosanojen keskiarvosi on:", Keskiarvo) 