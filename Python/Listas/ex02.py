numeros = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]

numeros.sort()
print("Lista ordenado {}".format(numeros))

print("\n")

numeros.reverse()
print("Lista invertida {}".format(numeros))

print("\n")

ocorrencias = numeros.count(11)
print("Quantidade de ocorrências {}".format(ocorrencias))

print("\n")

ocorrencias_num = numeros.index(78)
print("O Índice do 78 é {}.".format(ocorrencias_num))
