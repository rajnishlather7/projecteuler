def num_to_digit(num):
    l = [int(i) for i in str(num)]
    return l
def check_bouncy(num):
    l = num_to_digit(num)
    going_down = False
    going_up = False
    for i in range(1,len(l)):

        if l[i-1] > l[i]:
            going_down = True
        elif l[i-1] < l[i] :
            going_up = True
        if going_up and going_down:
            return True
    return False

c = 0
i = 1
while True:
    if check_bouncy(i):
        c+=1
    if c/i == 0.99:
        print(i)
        break
    i +=1