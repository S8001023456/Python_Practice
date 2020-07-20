while True:
    try:
        row, col = map(int, input().split())
        matrix = []
        for i in range(row):
            row_list = list(map(int, input().split()))
            matrix.append(row_list)
        for j in range(col):
            for i in range(row):
                print(matrix[i][j], end = " ")
            print()
    except:
        break
