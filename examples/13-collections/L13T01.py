# Kysytään käyttäjältä rekisterinumeroita kunnes annetaan tyhjä syöte. Tallennetaan rekisterinumerot listaan ja aakkosjärjestykseen

Lista = []
 
while True:
    Rekisteri = input("Syötä rekisterikilpiä, tyhjä kenttä lopettaa kysymyksen: ")
    if Rekisteri == '':
        break
    else:
        Lista.append(Rekisteri)
 
Lista.sort()
print(', '.join(Lista))
print("Rekisterikilvet ovat aakkosjärjestyksessä seuraavat: ",Lista)