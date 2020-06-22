def check_true(num):
    z = (((1+24*num)**0.5) + 1)/6
    return z==int(z)
i=1
f= True
while f:
    i+=1
    n = (i * ((3 * i)- 1)) / 2;
    for j in range(1,i):
        m = (j * ((3 * j) - 1)) / 2;
        if check_true(n-m) and check_true(n+m):
            print(n-m)
            f= False
            break