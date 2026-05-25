a = 42              # a verweist auf 42 (Integer)
b = 42              # b verweist ebenfalls auf 42 (Integer)

print(a is b)       # Ist a und b dasselbe Objekt? => Ja

c = 42.0            # c verweist auf 42.0 (Float)

print(a is c)       # Ist a und c dasselbe Objekt? => Nein


print(a == c)       # Haben a und c den gleichen Wert? => Ja