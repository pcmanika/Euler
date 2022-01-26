s = 0
for i in range(2,1000000):
    prime = True
    for a in range(2,(i // 2) + 1): 
        if i % a == 0:
            prime = False
            break
    if prime == True:
        s = s + 1
        print(i,s)