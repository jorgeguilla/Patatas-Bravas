def creaMatrizVacia(x, y):
    Matrix = [[0 for i in range(y)] for j in range(x)]
    return Matrix


def devolverSecuencia(A, B, secuencia):
    n1 = len(A)
    n2 = len(B)
    matrix = [[0 for i in range(n2)] for j in range(n1)]
    bmatriz = [[False for i in range(n2)] for e in range(n1)]

    for i in range(n1):
        for j in range(n2):

            if A[i] == B[j]:
                bmatriz[i][j] = True
                matrix[i][j] = 1
                if bmatriz[i - 1][j - 1] and not (i == 0 or j == 0):
                    matrix[i][j] = matrix[i - 1][j - 1] + 1

            elif matrix[i - 1][j] >= matrix[i][j - 1]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1]
    print(matrix)
    i = 1
    j = 1
    L = 0
    while True:
        if matrix[i][j] == matrix[i - 1][j - 1] + 1:
            L += 1
            secuencia[L] = A[i]
        if i < n1 - 1:
            i += 1
        if j < n2 - 1:
            j += 1
        print(n1, n2)
        if not L < matrix[n1 - 1][n2 - 1]:
            break

    return L


A = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]  # no funciona con estos. Edit: ya funciona lok
B = [1, 0, 1, 0, 0, 1, 0, 0, 1]

n3 = max(len(A), len(B))
secuencia = ['x' for i in range(n3)]
print(devolverSecuencia(A, B, secuencia))
