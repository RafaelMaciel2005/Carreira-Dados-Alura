num_cubo = [x**3 for x in range(10)]
print(num_cubo)

div_tres = [x for x in range(21) if x % 3 == 0]
print(div_tres)

frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"]

mais_de_cinco_caracteres = [x for x in frutas if len(frutas) > 5]
print(mais_de_cinco_caracteres)

notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]

notas_acima = [nota for nota in notas if nota > 75]
print(notas_acima)