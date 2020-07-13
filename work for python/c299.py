while True:
    try:
        numberlist = list(map(int, input().split()))
        numberlist.pop(0)
        numberlist.sort()
        comparator = True
        for i in range(len(numberlist) - 1):
            if numberlist[i] + 1 != numberlist[i+1]:
                comparator = False
        if comparator == True:
            print(numberlist[0],numberlist[len(numberlist) - 1],"yes")
        else:
            print(numberlist[0],numberlist[len(numberlist) - 1],"no")
    except:
        break
