menge1 = set(("a", "b", "c"))
menge2 = set(("abcd"))
menge3 = frozenset(("a", "b", "c"))

print(len(menge1))
print(menge1 > menge2)
print(menge1 < menge2)
print(menge1 == menge3)
print(menge2 - menge1)