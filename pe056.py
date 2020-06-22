def sum_of_digits(number):
    number = [int(i) for i in list(str(number))]
    return sum(number)


ma = 0
for i in range(2, 100):
    for j in range(2, 100):
        z = sum_of_digits(i**j)
        if z > ma:
            ma = z
print(ma)
