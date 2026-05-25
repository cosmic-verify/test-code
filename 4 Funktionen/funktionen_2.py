def fak(x):
    for i in range(x-1, 1, -1):
        x *= i
    return x

print(fak(5))
print(fak(6))
print(fak(7))
print(fak(8))

def fak_aber_besser(x):
    if x == 0:
        return 1
    else:
        return x * fak_aber_besser(x-1)
    
print(fak_aber_besser(5))
