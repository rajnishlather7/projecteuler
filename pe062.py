def sorted_numb(numb):
    numb = [i for i in list(str(numb))]
    numb.sort()
    return "".join(numb)


a = [sorted_numb(i ** 3) for i in range(10000)]
for i in range(len(a)):
    if a.count(a[i]) == 5:
        print(i ** 3)
        break
