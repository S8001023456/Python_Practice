while True:
    try:
        k = int(input())
        print(int(k * (k**2 + 5) / 6 + 1))
    except:
        break
