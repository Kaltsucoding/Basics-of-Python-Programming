# String: count
# Tässä esimerkkilasku merkkijonon ällien "l" määrästä
string = "Kalle V"
input_string = "Kalle V"
string_count = input_string.count ("l")
print("Ällien määrä on", string_count)

# Perus yhteenlaskua kahdella muuttujalla
string1 = 60
string2 = string1 + 4
print("string2 on", string2)

# String: startswith
# Selvitetään alkaako lause sanalla "Kesä"
string3 = "Kesä on paras vuodenaika Suomessa!"
string4 = string3.startswith ("Kesä") 
print(string4)

# String: endswith
# Selvitetään päättykö lause kysymysmerkkiin
string5 = "Saunominen on suomalaisten juttu."
string6 = string5.endswith ("?")
print(string6)

# string: replace
# Tässä esimerkissä annettu teksti palautetaan muutettuna terminaaliin
string7 = "Testilause ennen muutoksen"
string8 = string7.replace ("ennen", "jälkeen")
print(string8)

# String: lower
# Otetaan selvää mitä lower tekee tekstille
string9 = "Halutaan pienentää TÄMÄ"
string10 = string9.lower()
print(string10)

# String: upper
# Otetaan selvää mitä upper tekee tekstille
string11 = "Halutaan suurentaa tämä"
string12 = string11.upper()
print(string12)

# String: split
# Otetaan selvää mitä split tekee
string13 = "Testailua splitillä kuinka se toimii"
string14 = string13.split()
print(string14)