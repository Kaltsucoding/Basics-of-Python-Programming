# Ohjelma jossa kysytään käyttäjältä vuotta, tulostetaan konsoliin onko kysytty vuosi karkausvuosi vai ei.

input_year = int(input("Kysy onko vuosi karkausvuosi: "))
if (input_year%400 == 0):
 print("%d on karkausvuosi" %input_year)
elif (input_year%100 == 0):
 print("%d ei ole karkausvuosi" %input_year)
elif (input_year%4 == 0):
 print("%d on karkausvuosi" %input_year)
else:
 print("%d ei ole karkausvuosi" %input_year)