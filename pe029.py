all_list = []
for i in range(2, 101):
    for j in range(2, 101):
        z = i**j
        if z not in all_list:
            all_list.append(z)
print(len(all_list))
