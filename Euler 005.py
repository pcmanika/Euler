
for i in range(2,2432902008176640000):
    for a in range(2,21):
        if i % a != 0:
            break
        if a == 20:
            print(i)
