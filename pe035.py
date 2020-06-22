# slow implementation:


def SieveOfEratosthenes(n):
    all_prime = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            all_prime.append(p)
    return all_prime


def circularOfThatNumber(num):
    result = [num]
    num = str(num)
    z = len(num)
    while z > 1:
        num = num[1:] + num[0]
        result.append(int(num))
        z = z - 1
    return result


number = 1000000
all_prime = SieveOfEratosthenes(number)
result = []

for i in all_prime:
    if len(str(i)) < 2:
        result.append(i)
    elif i not in result:
        list_1 = circularOfThatNumber(i)
        check = all(elem in all_prime for elem in list_1)
        if check:
            for k in list_1:
                result.append(k)
print(len(result))
