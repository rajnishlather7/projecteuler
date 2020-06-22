
n1 = 1010101010
n2 = 1389026623
i = n1
while i < n2:
    z = i**2
    z = str(z)
    if z[0] == "1" and z[2] == "2" and z[4] == "3" and z[6] == "4" and z[8] == "5" and z[10] == "6" and z[12] == "7" and z[14] == "8" and z[16] == "9":
        print(i)
        break
    if i%100 == 30:
        i = i+40
    else:
        i=i+60