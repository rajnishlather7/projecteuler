def SieveOfEratosthenes(n):
    all_prime = []

    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            all_prime.append(p)
    return all_prime


z = SieveOfEratosthenes(2000000)
print(sum(z))
