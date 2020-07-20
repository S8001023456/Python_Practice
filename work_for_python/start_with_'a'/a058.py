times = int(input())
num_list = []
three_k = 0
three_k_plus_1 = 0
three_k_plus_2 = 0
for input_num in range(times):
    num_list.append(int(input()))
for i in num_list:
    if i % 3 == 0:
        three_k += 1
    if i % 3 == 1:
        three_k_plus_1 += 1
    if i % 3 == 2:
        three_k_plus_2 += 1
print(three_k, three_k_plus_1, three_k_plus_2)
