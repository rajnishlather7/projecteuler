"""Sum square difference"""


number = 10
sum_of_square = sum([i*i for i in range(1, number + 1)])
square_of_sum = sum([j for j in range(1, number + 1)])**2

print(square_of_sum - sum_of_square)
