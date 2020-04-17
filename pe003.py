"""Largest prime factor"""


def check_prime(num):
    for c in range(2,int(num**(1/2))+1):
        if num%c == 0:
            return False
    return True


result = []
number = 600851475143
for i in range(1, int(number**(1/2)+1)):
    if number % i == 0 and check_prime(i):
        result.append(i)
print(max(result))
