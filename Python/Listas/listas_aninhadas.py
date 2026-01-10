matriz = [[1, 2, 3],  
          [4, 5, 6],
          [7, 8, 9]]

valor = matriz [1][2]
print(valor)

soma = 0

for linha in matriz:

    for numero in linha:

        soma += numero

print("A soma dos valores da matriz é {}.".format(soma))

for linha in matriz:
    for numero in linha:

        print(numero, end="\t")

    print()    