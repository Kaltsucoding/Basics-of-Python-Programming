# Ohjelma, jossa kysytään arvostelupisteet yhdelle mäkihypylle, tulostetaan yhteenlaskettu pistemäärä jättämällä suurin ja pienin pistemäärä pois

print("Mäkihyppääjä hyppäsi ja nyt on aika antaa viiden tuomarin pisteet ")

import random

tuomari1 = random.randint(1,10)
tuomari2 = random.randint(1,10)
tuomari3 = random.randint(1,10)
tuomari4 = random.randint(1,10)
tuomari5 = random.randint(1,10)

tuomarit_yht = [tuomari1, tuomari2, tuomari3, tuomari4, tuomari5]
print("Arvostelut yhteensä:")
print("Tuomarin nro 1 pisteet:", tuomari1) 
print("Tuomarin nro 2 pisteet:", tuomari2)
print("Tuomarin nro 3 pisteet:", tuomari3)
print("Tuomarin nro 4 pisteet:", tuomari4)
print("Tuomarin nro 5 pisteet:", tuomari5)
mylist = tuomarit_yht
mylist.remove(max(mylist))
mylist.remove(min(mylist))
tuomarit_yht = sum(mylist)

print("Lopulliset pisteet mäkihyppääjälle ovat: ", tuomarit_yht)