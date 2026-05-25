vorname = "Maximiliane"
nachname = "Mustermann"
geschlecht = "w"

if geschlecht == "w":
    anrede = "Frau"
elif geschlecht == "m":
    anrede = "Herr"
else:
    anrede = ""

print("Guten Morgen,", anrede, vorname, nachname)