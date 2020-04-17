"""10001st prime"""


def prime(number):
    for a in range(2, int(i**1/2) + 1):
        if i % a == 0:
            return False
    return True


i = 2
prime_list = list()
while len(prime_list) < 10001:
    if prime(i):
        prime_list.append(i)
    i += 1

print(prime_list[-1])
