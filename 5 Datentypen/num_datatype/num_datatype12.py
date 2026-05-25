def dualtest(x):
    x = str(x)
    r = True
    for c in x:
        if c not in "01":
            r = False
            break
    return r

print(dualtest("1010101"))
print(dualtest("1020101"))
print(dualtest(1010101))