#Tehtävä L10T01

def show_info():
    print("I'm Utils.Info")

#Tehtävä L10T02 

def sub(numero1, numero2):
    return numero1 - numero2

#Tehtävä L10T03

def average(keskiarvo1, keskiarvo2, keskiarvo3, lkm):
    average = (keskiarvo1 + keskiarvo2 + keskiarvo3) / lkm
    return average

#Tehtävä L10T04

def calc_consumption(Kulutus, Matka, Hinta):
    Matka = Matka + 0
    Kulutus = (Kulutus * 100) / Matka
    Hinta = Matka * (Kulutus / 100) * Hinta
    return Kulutus, Matka, Hinta