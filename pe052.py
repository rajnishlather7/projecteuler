def to_str(numb):
    z = list(str(numb))
    z.sort()
    return "".join(z)


i = 11
while True:
    if to_str(i) == to_str(2*i) == to_str(3*i) == to_str(4*i) == to_str(5*i) == to_str(6*i):
        print(i)
        break
    else:
        i += 1
