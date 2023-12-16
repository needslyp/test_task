def minimum(matrix: list) -> list:
    row_sum = {}
    for row in range(len(matrix)):
        sum = 0
        for col in range(len(matrix[0])):
            sum += matrix[row][col]
        row_sum[row] = sum

    col_sum = {}
    for col in range(len(matrix[0])):
        sum = 0
        for row in range(len(matrix)):
            sum += matrix[row][col]
        col_sum[col] = sum

    return [min([(value, key) for key, value in row_sum.items()])[1], min([(value, key) for key, value in col_sum.items()])[1]]

print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))

print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))
