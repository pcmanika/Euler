
s = 0
for i  in range (100,999):
    for a in range (100,999):
        z = i * a
        zs = str(z)
        if zs == zs[::-1]:
            if z > s:
                s = z               
print(s)
            
