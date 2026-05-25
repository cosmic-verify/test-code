liste = [1, 2, 4, 6, 8, 9, 10, 11, 12]

for x in liste:
    if x % 2 == 0:
        x_quadrat = x ** 2
        print(x, "ist gerade, sein Quadrat ist", x_quadrat)