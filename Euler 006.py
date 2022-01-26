
s = 0
for i in range(1,101):
    a = i**2
    s = a + s
print(s)

b = 0
for i in range(1,1012):
    b = i + b
print(b**2)

print(b**2 - s)
