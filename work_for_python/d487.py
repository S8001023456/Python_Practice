while True:
    try:
        def factorial(number):
            if number == 0:
                print("0! = 1 = ",sep = "", end = "")
            sum = 1
            if number != 0:
                print(number,"! = ",sep = "", end = "")
                for i in range(number, 1, -1):
                    sum *= i
                    print(i, " * ",sep = "", end = "")
                print("1 = ",sep = "", end = "")
            print(sum)
        a = int(input())
        factorial(a)
    except:
        break
