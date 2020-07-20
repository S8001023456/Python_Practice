while True:
    try:
        lower, upper = map(int, input().split())
        four_power_sum = 0
        bool = False
        for times in range(lower, upper):
            str_times_len = len(str(times))
            str_times = str(times)
            for i in range(len(str(times))):
                four_power_sum += int(str_times[i]) ** str_times_len
            if four_power_sum == times:
                print(four_power_sum, end = ' ')
                bool = True
            four_power_sum = 0
        if bool == False:
            print('none', end = '')
        print()
    except:
        break
