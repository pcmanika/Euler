x = 0
y = 1 
z = 0
s = 0
while True:
    z = x + y
    x = y
    y = z
    if z > 4000000:
        break
    print(z)
    if z % 2 == 0:
        s = s + z
print(s)