while True:
    try:
        dividend, divisor, remainder_digits = map(int, input().split())
        rem_list = []
        remainder = dividend % divisor
        integer = dividend // divisor
        for i in range(remainder_digits):
            quotient = remainder * 10 // divisor
            rem_list.append(quotient)
            remainder = remainder * 10 % divisor
        print(integer, ".", sep = "", end = "")
        for j in rem_list:
            print(j, sep = "", end = "")
        print()
    except:
        break
