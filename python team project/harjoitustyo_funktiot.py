# Harjoitustyön aliohjelma, joka sisältää funktioita ja muita elementtejä

# Määritellään ympäristöt: Viidakko, Aavikko, Luola

# Muokkaa vielä ympäristöt ja polut numeroilla ja kirjaimilla...

def ymparistot():
    ymparisto1 = "Viidakko"
    ymparisto2 = "Aavikko"
    ymparisto3 = "Luola"
    return ymparisto1, ymparisto2, ymparisto3

# Määritellään Viidakko ja sen eri polut

def kivi_reitti():
    print("Olet saapunut viidakon uumeniin, aloita eteneminen. ")
    print("Reitin varrelle tuli vesieste, voi ei! Miten päästään siitä yli? ")
    este = int(input("Anna joku vaihtoehdoista 1, 2, 3 tai 4: naru, köysitikkaat, kajakki, kahlaus..?: "))
    if este == 1:
        print("Oletko aivan varma tästä? ")
        print("Noh, jatketaan. ")
    elif este == 2:
        print("Öö, oletko ihan varma tästä? ")
        print("Noh, jatketaan jokatapauksessa.")
    elif este == 3:
        print("Ajattelet fiksusti! Jatketaan. ")
    elif este == 4:
        print("Nerokasta! Jatketaan. ")
        print("Olet lähempänä aarteen löytämistä.")
    else:
        print("Jotain meni vikaan. ")

# Määritellään metsäpolku

def metsa_reitti():
    print("Olet saapunut metsään. Metsästä kuuluu ääniä ja puiden suhinaa. ")
    print("Eksyit. Ruokaa ei ole ja on kylmä. ")
    print("Sinun täytyy nyt pärjätä omillasi. ")
    pelin_lopetus1 = "Voimia."
    print("Valitettavasti tarina loppui tähän.",pelin_lopetus1)
    print('''

     *
    **
   ****               *
  ******              **
 ********            ****
    ||                ||
^^^^  ^^^^^^^^^^^^^^^^  ^^^^^

''')

# Määritellään Aavikko ja sen polut

def polku2_aavikko():
    print("Tapaat Gorillan.")
    print("Se on kookas ja täynnä intoa.")
    print("Se tykkää pelata korttia. Miten sinä arvelisit? Pelataan sen kanssa vähän korttia. ")

def polku2_aavikko_korttipeli():
    kysymys_kortti1 = str(input("Minkä värinen kortti laitetaan? Musta/Punainen?: "))
    if kysymys_kortti1 == "Musta":
        print("Valitsit viisaasti, hienoa! ")
        print("Olet lähempänä aarteen löytämistä. ")
    elif kysymys_kortti1 == "Punainen":
        print("Oivoi, valitsit huonosti, nyt gorilla vihastuu... ")
        print("Gorilla on todella vihainen.")
        print("Gorilla heittää kortit sivuun ja hyökkää sinun kimppuun.")
        print("Tarina loppuu tähän.")
        exit()
    else:
        print("Jotain meni vikaan. ")

# Määritellään Luola ja sen eri polut

def polku3_luola():
    print("Saavut luolalle joka vaikuttaa mielenkiintoiselta, astu sisään!")
    print("Luolassa on pimeää, siellä on jonkin verran kiviä ja sateen ropina kuuluu luolan suuaukon läheltä.")
    print("Luolasta löytyi eri reittejä...")

def polku3_luola_reittivalinta():
    valinta1 = int(input("Haluatko mennä oikealla vai vasemmalle? Vastaa '1' tai '2': "))
    if valinta1 == 1:
        print("Valitsit mennä oikealle, selvä...")
    elif valinta1 == 2:
        print("Valitsit mennä vasemmalle, okei...")
    else:
        print("Jotain meni vikaan.")
    valinta2 = int(input("Nyt sinun täytyisi valita kahdesta työkalusta: keihäs vai lasso? Vastaa nrolla 1, tai 2: "))
    if valinta2 == 1:
        print("Luolamies tulee vastaasi näköpiiriin.")
        print("Mitä ihmettä?")
        print("Luolamies vilkaisee sinuun ja mietit mitä kannattaisi tehdä..")
        valinta3 = int(input("Haluatko juosta karkuun, heitätkö keihään vai kiljutko? Vastaus nroilla: 1, 2, 3: "))
        if valinta3 == 1:
            print("Juoksit karkuun. Palasit luolan alkuun.")
            print("Mihin ihmeeseen jouduit?")
            print("Luolan sisäänkäynti on erilainen.")
            print("Olet joutunut eri ulottuvuuteen ja matkustit ajassa eteenpäin")
            print("Pian huomaat palatassesi takaisin, että ennen oli kaikki paremmin.")
            print("Olet yksinäinen ja mietit jatkoa.")
            print("Lopulta noh...")
            print("Tarina loppuu tähän.")
            exit()
        elif valinta3 == 2:
            print("Valitsit keihään, ohoh, heitit sen ohi!")
            print("Luolamies suuttuu...")
            print("Luolamies ottaa sinun keihään ja heittää sen sinua kohti.")
            print("Keihäs osuu sinua rintakehään ja alkaa vuotaa verta.")
            print("Valitettavasti olet vaurioitunut niin pahoin, ettet pysty jatkamaan.")
            print("Tarina päättyy tähän.")
            exit()
        elif valinta3 == 3:
            print("Rupesitko kiljumaan, mitä ihmettä??")
            print("Mitä se nyt tässä vaiheessa auttaa.")
            print("Luolamies hyökkää kimppuun.")
            print("Tarina ei valitettavasti jatku enää.")
            exit()
        else:
            print("Jotain meni vikaan.")
    elif valinta2 == 2:
        print("Valitsit lasson. Se on hyvä työkalu.")
        print("Selätit luolamiehen valitsemalla oikean työkalun, hyvä!")
        print("Nyt sinun on vain päästävä aarrearkun luokse...")
    else:
        print("Jotain meni vikaan. ")

# Määritellään aarteen löytyminen

def aarteen_loyto():
    print("Löysit aarteen")
    print("Se kimaltelee ja säihkyy.")
    print("Olet riemuissasi.")
    print("Mutta mitä teet aarteella, se jää sinun itsesi päätettäväksi.")
