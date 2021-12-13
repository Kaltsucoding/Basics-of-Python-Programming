# Kysy käyttäjältä muutetaanko fahrenheitit celciukseksi vai toisinpäin. Ja sen jälkeen kysytään vielä asteluku ja muutetaan se toiseen asteeseen.

# Teen tämän hyöydyntämällä funktioita ja if-else

Kysymys = float(input("Haluatko muuttaa 1. fahrenheitit celciukseksi vai 2. toisinpäin? Anna numero 1 tai 2 jatkaaksesi: "))

def fahrenheit_celcius(Kysymys):
    return (Kysymys - 32) * 5/9

def celcius_fahrenheit(Kysymys):
    return (Kysymys * 1.8) + 32

if Kysymys == 1:
    print("Haluat siis muuntaa fahrenheitit celciukseksi ")
    fahrenheit = float(input("Anna asteesi fahrenheittina: "))
    print(fahrenheit_celcius(fahrenheit), "celciusta")

if Kysymys == 2:
    print("Haluat siis muuntaa celciukset fahrenheitiksi ")
    celcius = float(input("Anna asteesi celciuksena: "))
    print(celcius_fahrenheit(celcius), "fahrenheittia")

else: 
    pass