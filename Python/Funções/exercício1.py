""""Receber uma lista de numeros do usario, encontrar o maior, menor e calcular a média."""

def estatisticas (*args):

    return sum(args) / len(args), max(args), min(args)

entrada = list(map(float, input("Digite uma sequencia de números:").split()))

media, maior, menor = estatisticas(*entrada)

print("A média dos números é {}.".format(media))
print("O maior dos números é {}.".format(maior))
print("O menor dos números é {}.".format(menor))
