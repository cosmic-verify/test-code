menge1 = set(("a", "b", "c"))
menge2 = set(("abcd"))
menge3 = frozenset(("a", "b", "c"))

for element in menge1:
    print(element)


for element in sorted(menge1, reverse=True):
    print(element)