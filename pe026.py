v = 0
m = 0
for i in range(1,1000):
    remainder_list = []
    num = 1
    while True:
        rem = num%i
        num = (num%i)*10
        if rem not in remainder_list:
            remainder_list.append(rem)
        else:
            break
    d =len(remainder_list)-remainder_list.index(rem)
    if d > m:
        m = d
        v = i
print(v,m )