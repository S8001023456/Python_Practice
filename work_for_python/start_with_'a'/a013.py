while True:
    try:
        rome_dic = {'M':1000,   'CM':900,  'D':500,  'CD':400,
                    'C':100,  'XC':90, 'L':50, 'XL':40,
                    'X':10, 'IX':9,'V':5,'IV':4, 'I':1}

        str1, str2 = input().split()
        def rome_to_int(str):
            i = 0
            decimal_num = 0
            while(i < len(str)):
                if i == len(str) - 1:
                    decimal_num += rome_dic[str[i]]
                    i += 1
                else:
                    if str[i] + str[i + 1] == 'IV' or str[i] + str[i + 1] == 'IX' \
                    or str[i] + str[i + 1] == 'XL' or str[i] + str[i + 1] == 'XC' \
                    or str[i] + str[i + 1] == 'CD' or str[i] + str[i + 1] == 'CM' :
                        decimal_num += rome_dic[str[i] + str[i + 1]]
                        i += 2
                    else:
                        decimal_num += rome_dic[str[i]]
                        i += 1
            return decimal_num
        int1 = rome_to_int(str1)
        int2 = rome_to_int(str2)
        rome_int = abs(int1 - int2)
        if rome_int == 0:
            print('ZERO')
        else:
            for i, j in rome_dic.items():
                if rome_int // j != 0:
                    for times in range(rome_int // j):
                        print(i, sep = '', end = '')
                    rome_int = rome_int % j
            print()
    except:
        break
