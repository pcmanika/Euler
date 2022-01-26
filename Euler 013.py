
t = 0 
for i in range(1,1000000000000):
    t = t + i
    c = 0
    checkpoint = (t // 2 + 1) // 16
    for j in range(1, t // 2 + 1):
        if t % j== 0:
            c = c + 1
        if j == checkpoint and c < 500 // 16:
            print('Raus')
            break
    print(t,c,j)
    if c > 500:
        break
