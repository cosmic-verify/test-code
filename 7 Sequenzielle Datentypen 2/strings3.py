s1 = "Das ist ein ganz normaler String"
print(s1.split(" "))

s2 = "Das ist ein Text. \nauf mehreren Zeilen. \nUnd mit einem Tabulator \t hier."
print(s2.splitlines())
print(s2.splitlines(keepends=True))

s3 = "users/julia/desktop/hello.txt"
print(s3.split("/"))
print(s3.partition("/"))
print(s3.rpartition("/"))