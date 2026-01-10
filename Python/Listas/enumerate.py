nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"]

for i in nomes:
    print(i)

print()

for indice, i in enumerate(nomes):
    print("O nome {} está no indice {}.".format(i, indice))

print()

notas = [85, 90, 78, 92, 88]

for indice, i in enumerate(nomes):
    print("O {} obteve a nota {}.".format(i, notas[indice]))