def get_length(num):
    mu = {}
    for i in range(1, num):
        current_num = i
        count = 1
        while current_num > 1:
            if current_num in mu:
                count = count + mu[current_num]
                current_num = 1
            elif current_num % 2 == 0:
                current_num = current_num // 2
                count += 1
            elif current_num % 2 != 0:
                current_num = 3 * current_num + 1
                count += 1
        mu[i] = count

    return mu


z = get_length(1000000)
max(z, key=z.get)
