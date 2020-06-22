def check_prime(num):
    if num == 1:
        return False
    for i in range(2, int((num) ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def SieveOfEratosthenes(n):
    prime = [i for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == p):
            for i in range(p * p, n + 1, p):
                prime[i] = 0
        p += 1
    return [i for i in prime if i != 0]


l = SieveOfEratosthenes(1000000)


def trunc_number(num):
    z = str(num)
    s = ""
    l1 = [int(z)]
    for i in range(1, len(z)):
        l1.append(int(z[i:]))
    s2 = ""
    l2 = [int(z)]
    for i in range(1, len(z)):
        ind = -1 * i
        l2.append(int(z[:ind]))
    return l1, l2


all_tr = []
for i in l:
    #     if len(all_tr)>14:
    #         break
    l1, l2 = trunc_number(i)
    r = True
    for j in range(len(l1)):
        if not check_prime(l1[j]):
            r = False
            break
        if not check_prime(l2[j]):
            r = False
            break
    if r:
        all_tr.append(i)
        print(all_tr)
print(sum(all_tr[4:]))