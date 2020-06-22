def get_digits(num):
    l = [int(i) for i in str(num)]
    return l
def sum_of_digits(num):
    l = len(str(num))
    t = 0
    for i in range(l):
        t+= num//(10**(l-i))
        num = num%(10**(l-i))
    return t+num
fact = [1,1,2,6,24,120,720,5040,40320,362880]
t = 0
for i in range(3,362880):
    l = get_digits(i)
    s = 0
    for j in l:
        s = s + fact[j]
    if s == i:
        t += i
        print(i)
print(t)