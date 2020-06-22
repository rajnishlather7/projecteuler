"""Digit fifth powers"""


def sumof(number):
    number = str(number)
    total = 0
    for i in number:
        total += int(i)**5
    return total


result = 0
upper_limit = 6*(9**5)
for i in range(2, upper_limit):
    if i == sumof(i):
        result += i
print(result)
