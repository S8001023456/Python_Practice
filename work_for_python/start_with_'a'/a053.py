problem_solve = int(input())
getpoint = 0
if problem_solve >= 40:
    getpoint = 100
elif problem_solve > 20:
    getpoint = 100 - (40 - problem_solve)*1
elif problem_solve > 10:
    getpoint = (problem_solve - 10) * 2 + 60
else:
    getpoint = problem_solve * 6
print(getpoint)
