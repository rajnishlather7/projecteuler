c = [i for i in range(999)]
all_in = []
for z in range(1, 999):
    for y in range(z + 1, 998 - z):
        v = (z*z + y*y)**0.5
        if z != y and v in c and z < y and v + y + z == 1000:
            all_in.append(z)
            all_in.append(y)
            all_in.append(v)
print(all_in[0] * all_in[1] * all_in[2])
