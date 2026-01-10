aluno = {
    "matricula": "A12345",
    "nome": "João Silva",
    "curso": "Engenharia de Software",
    "semestre": 5,
    "cr": 8.5
}

aluno["hobbies"] = "Leitura", "Corrida", "Xadrez"
aluno["idade"] = 22
print("Lista atualizada:", aluno)

aluno["semestre"] = 6
aluno["cr"] = 8.7
print("Lista atualizada:", aluno)

del aluno["idade"]
item_removido = aluno.pop("hobbies")
print("Item removido:", item_removido)

item_removido_2 = aluno.popitem()
print("O ultimo item da lista foi removido :", item_removido_2)

copia_1 = aluno.copy()
copia_2 = dict(aluno)
print(copia_1)
print(copia_2)