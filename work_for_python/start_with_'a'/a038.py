while True:
    try:
        number = int(input())
        numlist = []
        all_zero = True
        while number > 0:
            restnum = number % 10
            numlist.append(restnum)
            number //= 10
        for i in numlist:
            if i != 0:
                all_zero = False
        if all_zero == True:
            print("0")
        while numlist[0] == 0:
            numlist.pop(0)
        for i in numlist:
            print(i, end = "", sep = "")
        print()
    except:
        break
