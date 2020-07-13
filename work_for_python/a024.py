def math_GCD(former, latter):
    while former != 0 and latter != 0:
        if former >= latter:
            former %= latter
        else:
            latter %= former
    if former == 0:
        print(latter)
    else:
        print(former)
while True:
    try:
        a, b = map(int, input().split())
        math_GCD(a, b)
    except:
        break
