vendas = {
    "Janeiro": 120,
    "Fevereiro": 150,
    "Março": 80,
    "Abril": 190,
    "Maio": 210
}

for meses in vendas:
    print("Mês: {}".format(meses))

total = 0
for valor in vendas.values():
    total += valor
print("O total de vendas foi: {}".format(total))

       