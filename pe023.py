def adundant_number(limit):
    all_factor = [1]
    for i in range(2, int(limit ** 0.5) + 1):
        if limit % i == 0:
            all_factor.append(i)
            all_factor.append(limit // i)
    if sum(list(set(all_factor))) > limit:
        return limit
    else:
        return 0


full_list = []
check = [False] * 28124
for i in range(12, 28124):
    z = adundant_number(i)
    if z > 0:
        full_list.append(z)

print(len(full_list))

for i in range(len(full_list)):
    for j in range(i, len(full_list)):
        s = full_list[i] + full_list[j]
        if s > 28123:
            break
        check[s] = True

print(sum(i for i, x in enumerate(check) if not x))
