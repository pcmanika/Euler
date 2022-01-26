

from math import sqrt

s = 0
for i in range(2,2000001):
    prime = True
    for a in range(2,round(sqrt(i)) + 1): 
        if i % a == 0:
            prime = False
            break
    if prime == True:
        s = s + i
        print(i,s)

