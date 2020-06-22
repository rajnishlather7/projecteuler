a = [1]
for i in range(1,501):
    for j in range(4):
        a.append(a[-1]+(2*i))
print(sum(a))
    