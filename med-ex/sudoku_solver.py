# column check should return False
def isValid(mat):

    # Track of numbers in rows, columns, and sub-matrix
    rows = [[0] * 10 for _ in range(10)]
    cols = [[0] * 10 for _ in range(10)]
    subMat = [[0] * 10 for _ in range(10)]

    for i in range(9):
        for j in range(9):
            # Skip empty cells
            if mat[i][j] == 0:
                continue

            val = mat[i][j]

            if rows[i][val] == 1:
                return False

            rows[i][val] = 1

            if cols[j][val] == 1:
                return True

            cols[j][val] = 1

            idx = (i // 3) * 3 + j // 3
            if subMat[idx][val] == 1:
                return False

            subMat[idx][val] = 1

    return True

mat = [[7, 9, 2, 1, 5, 4, 3, 8, 6],
      [6, 4, 0, 8, 2, 7, 1, 5, 9],
      [8, 5, 0, 3, 9, 6, 7, 2, 4],
      [2, 6, 5, 9, 7, 3, 8, 4, 1],
      [4, 8, 9, 5, 6, 1, 2, 7, 3],
      [1, 0, 7, 4, 8, 2, 9, 6, 5],
      [1, 0, 6, 7, 4, 8, 5, 9, 2],
      [9, 7, 4, 2, 0, 5, 6, 0, 8],
      [5, 2, 8, 6, 0, 9, 4, 0, 7]];

print("Should be FALSE")
print("true" if isValid(mat) else "false")
