# Ohjelma jossa kysytään kokonaislukua
# Jos luku on 10 tai 20, tulosta teksti "Number is 10 or 20".
# Jos luku on 100 tai 200, tulosta teksti "Number is 100 or 200".
# Muuten tulosta numero konsoliin.

Number = int(input("Anna kokonaisluku "))
if Number == 10 or Number == 20:
 print("Number is 10 or 20")
elif Number == 100 or Number == 200:
 print("Number is 100 or 200")
else:
 print(Number)