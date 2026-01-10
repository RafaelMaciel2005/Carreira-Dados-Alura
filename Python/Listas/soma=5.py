a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

combinacoes = [(x, y) for x in a for y in b if x + y == 5]
print(combinacoes)

