l1 = [i for i in range(201) if not i%1]
l2 = [i for i in range(201) if not i%2]
l3 = [i for i in range(201) if not i%5]
l4 = [i for i in range(201) if not i%10]
l5 = [i for i in range(201) if not i%20]
l6 = [i for i in range(201) if not i%50]
l7 = [i for i in range(201) if not i%100]
l8 = [i for i in range(201) if not i%200]
t = 0
for a in l8:
    print(t)
    for b in l7:
        for c in l6:
            for d in l5:
                for e in l4:
                    for f in l3:
                        for g in l2:
                            for h in l1:
                                if a+b+c+d+e+f+g+h == 200:
                                    t+=1
                                elif a+b+c+d+e+f+g+h >200:
                                    break
print(t)