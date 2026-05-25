l = [1, 2, 3, "D", 5.0]

print("s" in l)        # Überprüfung auf Vorhandensein
print(l.count(5))    # Zählen der Vorkommen eines Elements
print(l.index("D"))  # Index eines Elements
l.append(6)          # Element anhängen
print(l)
l.remove(2)         # Erstes Vorkommen eines Elements entfernen
print(l)