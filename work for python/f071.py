a,b,c = map(int, input().split())
lucky = [a, b, c]
A1,A2,A3,A4,A5 = map(int, input().split())
NumberArea = [A1,A2,A3,A4,A5]
B1,B2,B3,B4,B5 = map(int, input().split())
Money = [B1,B2,B3,B4,B5]
getmoney = 0
comparator = True
for i in range(len(lucky)):
    for j in range(len(NumberArea)):
        if lucky[i] == NumberArea[j]:
            if i == 2:
                getmoney -= Money[j]
            else:
                getmoney += Money[j]

for k in NumberArea:
    if k == lucky[2]:
        comparator = False

if comparator == True:
    getmoney *= 2

if getmoney < 0:
    getmoney = 0
print(getmoney)
