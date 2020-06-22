def check_pent(num):
    test = (((1+24*num)**0.5)+1)/6
    if test%1:
        return False
    return True

def check_hex(num):
    test = (((1+8*num)**0.5)+1)/4
    if test%1:
        return False
    return True


i = 286
while True:
    num = i*(i+1)/2
    if check_hex(num) and check_pent(num):
        break
    i+=1
print(num)