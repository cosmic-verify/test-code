n = 10
i = 0

while n > 0:
    print(n)
    n -= 2
    i += 1
    if i >= 10:
        print("Vorzeitiger Stop")
        break