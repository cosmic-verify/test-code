data = open("dateien/studierende.txt", "r")

for line in data:
    line = line.strip() # entfernt die Zeilenumbrüche
    print(line)

data.close()

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)