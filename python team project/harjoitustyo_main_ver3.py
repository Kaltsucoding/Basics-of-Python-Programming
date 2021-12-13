# Harjoitustyömme pohjautuu luovaan ja pelinhenkiseen tarinaan
# Siinä on eri polkuja ja loppu on pelaajan päätettävissä
# Halutessaan voi palata pelin alkuun, tai lopettaa peli
# Peli suoritetaan VS Coden terminaalissa tai Windowsin komentokehotteella
# Koodikieli on: Python 3.9.5 64-bit

# Tarina: Kalle, Joona
# Koodi: Valtteri, Beatrice
# Kaikki osallistumme kuitenkin tarinan kehitykseen ja koodiin kirjoittamiseen jollain tavoin.

# Lähdesivu GAME OVER! ascii:lle --> http://www.patorjk.com/software/taag/#p=testall&f=Graffiti&t=GAME%20OVER! Font name BIG, hieman itse modifioitu.

# Otsikko: Aarteen metsästys

# Intro chapter 1

from harjoitustyo_funktiot import *

print("""
Aarteen metsästys

Olet aloittamassa tarinahenkistä peliä.
Tämän pelin aikana valitset eri vaihtoehtoja ja kuljet valitsemaasi polkua pitkin.
Voit palata takaisin pelin alkuun tai lopettaa pelin.
Pelin loppuratkaisu on sinusta itsestäsi kiinni.

""")

# Intro

kysymys_intro = str(input("Haluatko aloittaa? Valitse 'K' tai 'E': "))

if kysymys_intro == "K":
    print("Hyvä, aloitetaan peli! ")
elif kysymys_intro == "E":

    kysymys_intro2 = str(input("Oletko aivan varma? 'K' tai 'E': "))
    if kysymys_intro2 == "E":
        print("Hyvä, aloitetaan peli uudelleen!")
    else:
        kysymys_intro2 == "K"
        print("Ei sitten. Peli päättyi ennen kuin se alkoikaan. ")
        exit()
else:
    print("Yritä uudelleen: vastaus isolla alkukirjaimella 'K' tai 'E'")
    kysymys_intro3 = str(input("Haluatko aloittaa? Valitse 'K' tai 'E': "))
    if kysymys_intro3 == "K":
        print("Ei sitten. Lopetetaan peli.")
    elif kysymys_intro3 == "E":
        print("Jatketaan!")
    else:
        print("Kirjoitit liian monta kertaa väärin ja ohjelma päättyy tähän.")
        print("""
   _____          __  __ ______    ______      ________ _____  _  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \| |
 | |  __   //\|  | \  / | |__    | |  | \ \  / /| |__  | |__) | |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /| |
 | |__| |/ /  \ \| |  | | |____  | |__| | \  /  | |____| | \ \|_|
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_(_)
                                                                  """)
        exit()

# Ympäristön valinta

print("Tässä on vaihtoehdot eri ympäristöistä:", ', '.join(ymparistot()))
ympariston_valinta = int(input("Valitse joku ympäristöistä: 1, 2 tai 3: "))

if ympariston_valinta == 1:
    print("Valitsit Viidakon, hyvä. Jatketaan... ")
    polun_valinta = int(input("Haluatko edetä kivi- vai metsäreitille? Vastaa numerolla 1 tai 2: "))
    if polun_valinta == 1:
        kivi_reitti()
    elif polun_valinta == 2:
        metsa_reitti()
        exit()
    else:
        print("Jotain meni vikaa.")
elif ympariston_valinta == 2:
    print("Valitsit Aavikon... ")
    polku2_aavikko()
    polku2_aavikko_korttipeli()
elif ympariston_valinta == 3:
    print("Valitsit Luolan. Jatketaan... ")
    polku3_luola()
    polku3_luola_reittivalinta()
else:
    print("Jotain meni vikaan." )

# Outro

kysymys_outro = int(input("Löysitkö aarteen vai et? Vastaa 1 tai 2: "))
if kysymys_outro == 1:
    aarteen_loyto()
elif kysymys_outro == 2:
    aarteen_loyto()
else:
    print("Jotain meni vikaan.")


print('''

    *
   **
  ****               *
 ******              **
********            ****
   ||                ||
''')

print('''
    ____________
  /             )
 /              |
/_______________|
|               |
|               |
|-------o-------|
|               |
|               |
|_______________|


''')

print("Voitit pelin, onneksi olkoon! ")