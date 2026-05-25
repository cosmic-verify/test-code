zahl = 0

while zahl < 10:
    zahl += 1
    if zahl == 5:
        print("5 übersprungen")
        continue
    if zahl == 8:
        print("8 Ende")
        break
    print(zahl)
