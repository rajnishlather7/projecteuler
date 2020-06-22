# re-do sol
deno = 1
for i in range(12, 99):
    for j in range(i + 1, 99):

        try:
            if i % 10 != 0 and j % 10 != 0 and i % 11 != 0 and j % 11 != 0:
                x, y = check(i, j)
                if i / j == int(x) / int(y):
                    print(i, j)
                    deno = deno * y
        except:
            pass
