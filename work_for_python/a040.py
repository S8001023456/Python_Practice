lower, upper = map(int, input().split())
accumulate_lower = lower
four_power_sum = 0
for times in range(lower, upper, 1):
    for i in range(len(str(accumulate_lower))):
        four_power_sum += int(str(accumulate_lower)[i]) ** 4
    if four_power_sum == accumulate_lower:
        print(four_power_sum, end = " ")
    accumulate_lower += 1
    four_power_sum = 0
