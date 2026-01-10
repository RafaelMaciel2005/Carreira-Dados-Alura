numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

numeros_impares = list(filter(lambda impar: impar %2 != 0, numeros))

num_quad = list(map(lambda quad: quad**2, numeros_impares))

print(numeros_impares)
print(num_quad)