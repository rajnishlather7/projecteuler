file1 = open("triangle.txt", "r")
z = file1.readlines()
l = list()
for i in z:
    a = list(map(int, i.rstrip().split(" ")))
    l.append(a)

n = len(l)
s = [[0] * i for i in range(1, n + 1)]

s[0][0] = l[0][0]
for i in range(1, n):
    s[i][0] = s[i - 1][0] + l[i][0]

for i in range(1, n):
    for j in range(1, i + 1):
        if j == i:
            s[i][j] = s[i - 1][j - 1] + l[i][j]
        else:
            s[i][j] = max(s[i - 1][j - 1], s[i - 1][j]) + l[i][j]

print(max(s[n - 1]))
