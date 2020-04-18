def fact(number):
    result = 1
    while number > 1:
        result *= number
        number = number - 1
    return result


do = sum([int(i) for i in str(fact(100))])
print(do)
