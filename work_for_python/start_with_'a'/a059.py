cases = int(input())
perfect_square_list = []
for times in range(cases):
    lower_bound = int(input())
    upper_bound = int(input())
    perfect_square = 0
    for accumulate in range(lower_bound, upper_bound + 1):
        if (accumulate ** 0.5 // 1) ** 2 == accumulate:
            perfect_square += accumulate
    perfect_square_list.append(perfect_square)
for i in range(len(perfect_square_list)):
    print('Case ', i + 1, ': ', sep = '', end = '')
    print(perfect_square_list[i])
