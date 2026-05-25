menge1 = set(("a", "b", "c"))
menge2 = set("abcd")
menge3 = frozenset(("a", "b", "c"))

print(menge1.isdisjoint(menge3))