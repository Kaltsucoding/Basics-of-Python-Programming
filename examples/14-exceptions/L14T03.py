# Toteutaan funktio isthiszero(num). Funktiolla välitetään yksi parametri. 
# Funktio palauttaa true jos parametrin arvo on nolla. 
# Funktio palauttaa false, jos parametri on luku mutta ei nolla. 
# Funktio nostaa TypeError-poikkeuksen, jos parametri ei ole luku. 
# Kokeile kutsua ohjelmasta funktioita eri arvoilla. Toteuta kutsuvalla ohjelmalle try - except.

# Ohjelma toimii funktion määrittelemällä lukualueella, mutta kirjaimilla antaa TypeError tai NameError
# Lisäksi operaattorista >= herjaa 'str' and 'int' 

def isthiszero(num):
    if num == 0:
        return True
    elif num >= 1:
        return False
    else:
        if num is not int:
            raise TypeError("Annettu arvo ei ole nolla tai nollaa isompi")

try:
    isthiszero
except TypeError:
    print("Odotettu virheilmoitus on TypeError")

# Anna arvo sulkujen sisään ja aja ohjelma
print(isthiszero(1))