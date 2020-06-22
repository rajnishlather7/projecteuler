c = 0
for i in range(1,100):
    for j in range(1,100):
        if len(str(i**j)) == j:
            c+=1
print(c)