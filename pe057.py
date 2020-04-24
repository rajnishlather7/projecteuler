
a = 1
b = 1
count = 0
for i in range(1000):
    p = 2*b + a
    q = a + b
    if len(str(p)) > len(str(q)):
        count = count + 1
    a = p
    b = q
print(count)
