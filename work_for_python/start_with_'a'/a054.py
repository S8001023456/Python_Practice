iden_dic = {'A': 10 ,'B': 11, 'C': 12, 'D': 13,'E': 14,'F': 15,'G': 16,'H': 17,'I': 34,'J': 18,'K': 19,'L': 20,'M': 21,
            'N': 22 ,'O': 35, 'P': 23, 'Q': 24,'R': 25,'S': 26,'T': 27,'U': 28,'V': 29,'W': 32,'X': 30,'Y': 31,'Z': 33}
identity = input()
def check_iden(_identity, eng_num):
    bits_sum = 0
    iden_eng_num_sum = iden_dic[eng_num] // 10 + iden_dic[eng_num] % 10 * 9
    for iden_num in range(len(_identity) - 1):
        bits_sum += int(_identity[iden_num]) * (8 - iden_num)
    bits_sum += iden_eng_num_sum
    return 10 - (bits_sum % 10)
for i, j in iden_dic.items():
    if check_iden(identity, i) % 10 == int(identity[8]):
        print(i, end = "")
print()
