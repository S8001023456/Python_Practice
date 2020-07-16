decimal_num = int(input())
binary_list = []
while decimal_num // 2 != 0:
    binary_list.append(decimal_num % 2)
    decimal_num //= 2
binary_list.append(decimal_num % 2)
binary_list.reverse()
for i in range(len(binary_list)):
    print(binary_list[i])
