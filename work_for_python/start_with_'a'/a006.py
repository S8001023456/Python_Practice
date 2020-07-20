a, b, c = map(int, input().split())
determinant = b*b - 4*a*c
solution_pos = (-b + (b*b - 4*a*c) ** 0.5)/(2 * a)
solution_minus = (-b - (b*b - 4*a*c) ** 0.5)/(2 * a)
if determinant >= 0:
    solution_pos = int(solution_pos)
    solution_minus = int(solution_minus)
if determinant > 0:
    print("Two different roots x1=", solution_pos, " , x2=", solution_minus, sep = "")
elif determinant == 0:
    print("Two same roots x=", solution_pos, sep = "")
else:
    print("No real root")
