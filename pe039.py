m_c =0 
num = 0
for i in range(1,1000):
    c = 0
    for j in range(1,i):
        for k in range(j+1,i-j):
            if j+k <i and k**2 + j**2 == (i-j-k)**2:
                c = c+1
    if c > m_c:
        m_c = c
        num = i
print(num)