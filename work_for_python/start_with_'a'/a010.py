while True:
    try:
        number = int(input())
        prime_power = []
        power_times = 0
        if number % 2 == 0:
            prime_power.append(2)
            while number % 2 == 0:
                power_times += 1
                number //= 2
            prime_power.append(power_times)
            power_times = 0
        for i in range(3, number + 1, 2):
            if number % i == 0:
                prime_power.append(i)
                while number % i == 0:
                    power_times += 1
                    number //= i
                prime_power.append(power_times)
                power_times = 0
        for index in range(0, len(prime_power), 2):
            if index == len(prime_power) - 2:
                if prime_power[index + 1] == 1:
                    print(prime_power[index], sep = '', end = '')
                else:
                    print(prime_power[index], '^', prime_power[index + 1], sep = '', end = '')
            else:
                if prime_power[index + 1] == 1:
                    print(prime_power[index], ' * ', sep = '', end = '')
                else:
                    print(prime_power[index], '^', prime_power[index + 1], ' * ', sep = '', end = '')
        print()
    except:
        break
