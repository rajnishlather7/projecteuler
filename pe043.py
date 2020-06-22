import itertools

iterable = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
l = list(itertools.permutations(iterable))
s = 0
for i in l:
    i = list(i)
    if not int("".join(i[1:4])) % 2 and not int("".join(i[2:5])) % 3 and not int("".join(i[3:6])) % 5 and not int(
            "".join(i[4:7])) % 7 and not int("".join(i[5:8])) % 11 and not int("".join(i[6:9])) % 13 and not int(
            "".join(i[7:10])) % 17 and not int("".join(i[1:4])) % 2:
        s += int("".join(i))

print(s)