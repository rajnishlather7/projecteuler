fact_list = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
total = 1000000
num = 0

while total != 0:
    for i in fact_list:
        a = total//i
        result.append(l.pop(a))
        num = num+1
        total = total - i*a
print(result)
