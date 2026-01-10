n = int(input("Digite o número a calcular a soma dos quadrados:"))
soma = 0

for i in range (1, n+1):
    quad = i*i
    soma += quad
    print("O quadrado de {} é {}.".format(i, quad))
print("A soma total dos quadrados é {}.".format(soma)) 