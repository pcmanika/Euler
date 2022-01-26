
for c in range(0,1000):
    for b in range(0,1000):
        if c == b or b > c:
            break
        for a in range(0,1000):
            if a == b or a > b:
                break
            if c**2 == (a**2) + (b**2):
                if a + b + c == 1000:
                     print(a*b*c)
                     break
                break
