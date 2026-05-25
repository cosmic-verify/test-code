l = [1, "a", 3.14, [1, 2, 3], "Test oder so", {"key": "value"}, {1, 2, 3}, None]
print(l)

l[2] = 3.141592
print(l)

l[1:3] = [1, 2, 3]
print(l)

del l[3]
print(l)