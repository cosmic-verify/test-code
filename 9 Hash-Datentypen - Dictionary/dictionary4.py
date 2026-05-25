addrese = {
    "Vorname": "Max",
    "Nachname": "Mustermann",
    "Ort": "Musterstadt"
}

print(addrese.get("plz", "error: key not found"))
print(addrese.get("Ort", "error: key not found"))
print(addrese.items())
print(addrese.keys())
print(addrese.values())