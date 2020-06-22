def check_palindrome(number):
    if number == str(number)[::-1]:
        return True
result = []
number = 1000001
for i in range(0,number+1):
    if check_palindrome(str(i)) and check_palindrome(bin(i)[2:]):
        result.append(i)
print(sum(result))