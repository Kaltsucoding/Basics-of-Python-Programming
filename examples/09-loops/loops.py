#Perusesimerkki while-toistosta

number = 10
while number >= 0:
    print(number)
    number -= 1

#Esimerkki 2 operaattorilla and-or

number = 10
while number >= 0 and number < 100:
    print(number)
    number -= 1

#Esimerkki 3 i:n toistoa määritetyllä rangella

for i in range(10):
    print("Looping range(10):", i)

#Esimerkki 4 jossa rangea kasvatetaan kahdella (2)

for i in range(0, 10, 2):
    print("Looping range(0,10,2):", i)

#Esimerkki 5 merkkijonon merkit toistetaan konsolissa for:illa

for c in "Basics of programming with Python":
    print(c)

#Esimerkki 6 listausta for:illa

names = [ "John", "Cherry", "Jack" ]
for name in names:
    print(name)


# use of break and continue
print("Running a while loop with break and continue")
number = []
while True:
    number = int(input("Enter a number (0 to exit, 100 ignored) "))
    if number == 1:
        # use break to jump out of the loop without checking its condition
        # the rest of the code after 'break' is not executed
        break
    elif number == 100:
        print("Ignored")
        # use continue to jump back to to beginning of the loop without
        # executing the rest of the code in loop
        continue

    print("You entered: ", number)