def bin2dez(bin):
    bin = str(bin)
    if not all(c in "01" for c in bin): return "err"
    dez = 0
    for i in range(len(bin)):
        dez += int(bin[len(bin) - 1 - i]) * (2 ** i)
    return str(dez)

print(bin2dez(1000)) # => 8
print(bin2dez(1010)) # => 10
print(bin2dez(1111)) # => 15
print(bin2dez(10201)) # => err