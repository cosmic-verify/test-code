mtknr = {}

data = open("dateien/studierende.txt", "r")

for line in data:
    line = line.strip()
    zeile = line.split(",")
    mtknr[zeile[0]] = zeile[1]

data.close()

print(mtknr["Julia Wolff"])