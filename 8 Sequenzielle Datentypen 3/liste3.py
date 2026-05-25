m = ["Hallo", "Welt", "Python", "Programmierung"]
print(m)
re = list(reversed(m))
print(re)
re.reverse()
print(re)
m.sort(key=len, reverse=False)
print(m)