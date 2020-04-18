def count_factor(number):
    count = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            count = count + 2
    return count


last_number = 0
i = 1
a = True
while a:
    if count_factor(last_number)>500:
        a = False
        print(last_number)
    last_number += i
    i += 1
