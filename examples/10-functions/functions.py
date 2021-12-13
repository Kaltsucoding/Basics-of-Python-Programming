#Esimerkki 1, perusfunktio eli def

def print_info():
    print("Info")

#Esimerkki2, Funktion kutsuminen koodissa, funktion nimi (suluissa parametrit)

print_info()

#Esimerkki3, Funktion palauttama arvo return-sanalla ja sijoitus on (=) merkillä.

def print_and_return_number():
    print("Info - returning 123")
    return 123

number = print_and_return_number()
print("print_and_return_number returned ", number)

#Esimerkki4, Funktio jossa parametrejä sulkujen sisällä, yhteenlasku

def sum(number1, number2):
    return number1 + number2

number = sum(5, 11)
print("sum returned ", number)


# define a function that takes text as a parameter and modifies it before printing

def modify_text(text):
    text += ", this text is added by function"
    print(text)

#Lisätään "about to call modify_text" ylempään funktioon
text = "About to call modify_text"
modify_text(text)
print(text)