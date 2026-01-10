matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

soma = 0

for i in range (4):
    for j in range (4):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]

print("O valor total da soma dos números pares da matriz é : {}".format(soma))
