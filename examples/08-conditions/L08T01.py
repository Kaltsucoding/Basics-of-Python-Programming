# Ohjelma jossa kysytään ikää eri ehdoilla

Ikä = int(input("Ikäsi: "))
if Ikä < 13:
    print("Child")
elif Ikä > 12 and Ikä < 19:
    print("Teen")
elif Ikä >= 19 and Ikä <= 65:
    print("Adult")
else:
    print("Senior")