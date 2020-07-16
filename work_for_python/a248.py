while True:
    try:
        dividend, divisor, remainder_digits = map(int, input().split())
        rem_list = []
        remainder = dividend % divisor
        integer = dividend // divisor
        count_rem_dig = remainder_digits % 6
        remainder_digits //= 6
        for i in range(remainder_digits):
            quotient = remainder * 1000000 // divisor
            if len(str(quotient)) < 6:
                for plus_zero in range(6 - len(str(quotient))):
                    rem_list.append(0)
            rem_list.append(quotient)
            remainder = remainder * 1000000 % divisor
        for k in range(count_rem_dig):
            quotient = remainder * 10 // divisor
            rem_list.append(quotient)
            remainder = remainder * 10 % divisor
        print(integer, ".", sep = "", end = "")
        for j in rem_list:
            print(j, sep = "", end = "")
        print()
    except:
        break
