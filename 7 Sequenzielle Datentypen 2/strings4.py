text = ("According to all known laws of aviation, there is no way a bee should be able to fly. "
        "Its wings are too small to get its fat little body off the ground. "
        "The bee, of course, flies anyway because bees don't care what humans think is impossible." )
        
print(text)
print(len(text))
print(text.find("bee"))
print(text.index("bee"))
# print(text.index("cat")) # ValueError: substring not found
print(text.count("bee"))
print(text.find("cat")) # -1, da nicht gefunden

print("-----------")

text.replace("bee", "cat")
print(text) # unverändert, da strings unveränderlich sind
print("-----------")
print(text.replace("bee", "cat")) # gibt neuen String zurück, der die Ersetzungen enthält