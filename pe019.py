s = 2
c = 2
for i in range(1,2):
    if s >=7:
        s = s - 7
    if s == 1:
        c = c +2
        if i%4:
            s=s+1
        else:
            s=s+2
    elif s ==2:
        if i%4:
            s = s+1
            c = c + 2
        else:
            c=c+1
            s=s+2
    elif s ==3:
        if i%4:
            s = s+1
            c = c + 1
        else:
            c=c+2
            s=s+2
    elif s ==4:
        if i%4:
            s = s+1
            c = c + 3
        else:
            c=c+1
            s=s+2
    elif s ==5:
        if i%4:
            s = s+1
            c = c + 1
        else:
            c=c+1
            s=s+2
    elif s ==6:
        if i%4:
            s = s+1
            c = c + 1
        else:
            c=c+1
            s=s+2
    elif s ==0:
        if i%4:
            s = s+1
            c = c + 2
        else:
            c=c+3
            s=s+2
print(c)