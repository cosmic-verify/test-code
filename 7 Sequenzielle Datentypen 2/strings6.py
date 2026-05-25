code = "1AB2AC"

print(code.isalnum()) # True, da alle Zeichen alphanumerisch sind
print(code.isalpha()) # False, da es auch Ziffern enthält
print(code.isdigit()) # False, da es auch Buchstaben enthält
print(code.islower()) # False, da es auch Großbuchstaben enthält
print(code.isupper()) # False, da es auch Kleinbuchstaben enthält
print(code.startswith("1A")) # True, da der String mit "1A" beginnt
print(code.endswith("AC")) # True, da der String mit "AC" endet