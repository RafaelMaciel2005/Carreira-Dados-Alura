def adicionar(a, b):
    print(a+b)

def subtrair(a, b):
    print(a-b)

def multiplicar (a, b):
    print(a*b)

def dividir (a, b):
    print(a/b)

opcao = int(input("Digite 1 para somar.\nDigite 2 para subtrair.\nDigite 3 para multiplicar.\nDigite 4 para Dividir.\n"))

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

if opcao == 1:
    adicionar(n1, n2)

elif opcao == 2:
    subtrair(n1, n2)

elif opcao == 3:
    multiplicar(n1, n2)

elif opcao == 4:
    dividir(n1, n2) 

else:
    print("Opção inválida!") 
 
