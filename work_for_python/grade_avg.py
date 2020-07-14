cases = int(input())
sum_point = 0
sum_credits = 0
for i in range(cases):
    score, credits = map(int, input().split())
    sum_point += score * credits
    sum_credits += credits
point_avg = sum_point/sum_credits
print("my average score =", round(point_avg, 2))
