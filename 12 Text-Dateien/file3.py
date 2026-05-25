mtknr = {}

data = open("dateien/studierende.txt", "r")

for line in data:
    line = line.strip()
    zeile = line.split(",")
    mtknr[zeile[0]] = zeile[1]

data.close()

print(mtknr["Julia Wolff"])

# ------

mtknr["Eli Müller"] = "12345678"
print(mtknr)

data = open("dateien/studierende_neu.txt", "w")
for name in mtknr:
    data.write(f"{name},{mtknr[name]}\n")

data.close()

# ------

data = open("dateien/studierende_neu.txt", "r")
for line in data:
    line = line.strip()
    print(line)
    
data.close()