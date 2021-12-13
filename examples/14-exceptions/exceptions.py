
#Tässä esimerkkinä perinteinen nollalla jako. Ohjelma pysähtyy ZeroDivisionError virheeseen eikä pysty enää jatkamaan suoritusta eteenpäin.
number1 = 100
number2 = 0
result = number1 / number2
print("Result is ", result)

#Tilanteen korjaus
try:
    number1 = 100
    number2 = 0
    result = number1 / number2
    print("Result is ", result)
except ZeroDivisionError:
    print("Can't divide by zero!")



#Toinen esimerkki. Kysytään käyttäjältä lukua ja hän syöttääkin merkkejä. Ohjelma pysähtyy ValueError virheeseen eikä pysty enää jatkamaan suoritusta eteenpäin.
number = int(input("Give a number: "))
print("you entered: ", number)

#Korjataan esimerkki jossa tekstin asettaminen numeromuuttujaan aiheutti virheen ohjelman toiminnassa. 
#Huomaa miten eri tyyppisiä poikkeuksia voidaan käsitellä peräkkäisissä except osioissa:

try:
    number = int(input("Give a number: "))
    print("you entered: ", number)
except ValueError:
    print("Unable to convert to number")
except:
    print("Something else went wrong :(")



#Viimeisenä melko tyypillinen ohjelmointivirhe. Taulukosta yritetään lukea tai kirjoittaa alkiota jota ei ole olemassa. Ohjelma pysähtyy IndexError virheeseen.
numbers = [ 1, 2, 3, 4, 5 ]
print("Last number is ", numbers[5])

#Korjataan esimerkki jossa taulukkoa yritettiin lukea alkiosta jota ei ollut olemassa.
try:
    numbers = [ 1, 2, 3, 4, 5 ]
    print("Last number is ", numbers[5])
except IndexError:
    print("Wrong index used in accessing list")


#Poikkeuksia voi myös heittää itse. 
#Tässä esimerkissä SafeDivision funktio tarkastaa jos jakaja on 0 ja aiheuttaa tarvittaessa virhetilanteen.
def safe_division(x, y):
    if y == 0:
        raise Exception("Exception from safe_division")
    return x / y

try:
    result = safe_division(100, 0)
except:
    print("safe_division raised an exception")


#Jos esittelet uuden funktion mutta jätät sen toistaiseksi toteuttamatta on hyvä merkitä se NotImplementedError poikkeuksella. 
#Jos funktio unohtuukin toteuttamatta, huomaat sen helposti koska saat kehitysvaiheessa poikkeuksen kun yrität kutsua metodia.
def someday_something_here():
    raise NotImplementedError("This function is not implemented currently")

someday_something_here()