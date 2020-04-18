def all_factors(number):
    result = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            result.append(i)
            result.append(number//i)
    return sum(result)


list_all_amicable = []
for i in range(5,10000):
    if i not in list_all_amicable:
        z = all_factors(i)
        if all_factors(z) == i and z != i:
            list_all_amicable.append(z)
            list_all_amicable.append(i)
print(sum(list_all_amicable))
