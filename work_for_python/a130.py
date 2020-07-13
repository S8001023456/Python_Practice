cases = int(input())
web_popularity = []
numeral_cases = []
for j in range(cases):
    for i in range(3):
        reg = list(map(str, input().split()))
        reg[1] = int(reg[1])
        web_popularity.append(reg)
    sources = sorted(web_popularity, key = lambda cmp:cmp[1])
    numeral_cases.append(sources)
for numeral_case in range(len(numeral_cases)):
    print("Case #", numeral_case + 1,sep = "")
    for source in range(len(sources)):
        max = numeral_cases[numeral_case][len(sources)-1][1]
        if numeral_cases[numeral_case][source][1] == max:
            print(numeral_cases[numeral_case][source][0])
