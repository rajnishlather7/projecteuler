i = 1
string = "."
while len(string) < 1000001:
    string = string + str(i)
    i = i +1
print(int(string[1])*int(string[10])*int(string[100])*int(string[1000])*int(string[10000])*int(string[100000])*int(string[1000000]))