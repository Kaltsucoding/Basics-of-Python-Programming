from utils import calc_consumption

Polttoaine = float(input("Monta litraa tankkasit? "))
Kilometrit = float(input("Monta kilometriä ajoit? "))
Polttoainehinta = float(input("Mikä oli polttoaineen litrahinta? "))

print("Keskikulutuksesi/100km, Ajoit kilometrejä, Maksoit polttoaineesta")
print(calc_consumption(Polttoaine, Kilometrit, Polttoainehinta))