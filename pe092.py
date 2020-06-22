# slow implementation


def sq_sum_digits(numb):
    numb = [int(i) * int(i) for i in list(str(numb))]
    return sum(numb)


count = 0
count_2 = 0
other_check = [1] * 568
for val in range(1, len(other_check)):
    z = val
    while True:
        if z == 1:
            other_check[val] = 1
            break
        elif z == 89:
            other_check[val] = 89
            break

        z = sq_sum_digits(z)

for i in range(568, 10000000):
    if other_check[sq_sum_digits(i)] == 89:
        count = count + 1

for i in other_check:
    if i == 89:
        count_2 = count_2 + 1

print(count + count_2)
