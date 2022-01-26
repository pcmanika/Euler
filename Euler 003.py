for i in range(2,600851475143):
    prime = True
    for a in range(2,(i // 2) + 1): 
        if i % a == 0:
            prime = False
            break
    if prime == True:
        if 600851475143 % i == 0:
            print(i)
        
