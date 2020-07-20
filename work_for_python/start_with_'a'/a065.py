while True:
    try:
        password_str = input()
        for i in range(len(password_str) - 1):
            print(abs(ord(password_str[i]) - ord(password_str[i + 1])), end = '')
        print()
    except:
        break
