def fact(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result


all_fact = [fact(i) for i in range(0, 101)]
results = []

for i in range(23, 101):
    numb = i//2
    while True:
        if all_fact[i]/(all_fact[numb]*all_fact[i-numb]) > 1000000:
            results.append([i, numb])
            if [i, i - numb] not in results:
                results.append([i, i - numb])
            numb = numb - 1
        else:
            break
print(len(results))
