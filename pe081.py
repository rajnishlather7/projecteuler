file1 = open("inp.txt", "r")
z = file1.readlines()
l = []
for i in z:
    a = list(map(int, i.rstrip().split(",")))
    l.append(a)

n = len(l)
s = [[0] * n for i in range(n)]
s[0][0] = l[0][0]
for i in range(1, n):
    s[i][0] = s[i - 1][0] + l[i][0]
    s[0][i] = s[0][i - 1] + l[0][i]

for i in range(1, n):
    for j in range(1, n):
        s[i][j] = min(s[i][j - 1], s[i - 1][j]) + l[i][j]
print(s[79][79])