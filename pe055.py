def check_palindrome(number):
    if number == int(str(number)[::-1]):
        return True


def rev_number(number):
    number = str(number)
    return int(number[::-1])


count = 0
for i in range(1, 10001):
    till = 1
    while till < 51:
        i = i + rev_number(i)
        if check_palindrome(i):
            count = count + 1
            break
        till = till + 1
print(10000-count)
