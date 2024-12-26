# wap in python to transpose a square matrix 

def trans(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in mat:
    print(row)

trans(mat)

for row in mat:
    print(row)
