"""1000-digit Fibonacci number"""


def fib(number):
    list_l = [1, 1]
    result = 1
    if number == 0 or number == 1:
        return 1
    else:
        while number > 1:
            result = list_l[-1] + list_l[-2]
            list_l.append(result)
            number = number - 1
        return result


number = 200

while len(str(fib(number))) != 1000:
    number = number + 1
    if len(str(fib(number))) == 1000:
        print(number+1)
