def check_pan(s):
    l = list(s)
    l = set(l)
    if len(l) == 9 and "0" not in s:
        return s
    return False
ma = 0
for i in range(1,10000):
    s = ""
    r = 0
    a = 1
    while len(s)<9:
        s +=str(i*a)
        a=a+1
        
    if len(s)>9:
        s = "0"
    else:
        if check_pan(s):
            if int(s) > ma:
                ma = int(s)
print(ma)