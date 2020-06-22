"""Even Fibonacci numbers"""


fib_list = [1, 1]
while fib_list[-1] < 4000000:
    fib_list.append(fib_list[-1]+fib_list[-2])
even_fib_list = [i for i in fib_list if i % 2 == 0]
print(sum(even_fib_list))
