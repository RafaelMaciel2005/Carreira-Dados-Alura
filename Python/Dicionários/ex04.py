filme = {
    "titulo": "Inception",
    "diretor": "Christopher Nolan",
    "ano": 2010,
    "genero": "Ficção científica"
}
print("As chaves do diconários são:{}".format(list(filme.keys())))

print("Os valores do diconários são:{}".format(list(filme.values())))

print("Todos os itens do diconários são:{}".format(list(filme.items())))

apagado = filme.clear()
print(apagado)

ator = filme.setdefault["Leonardo DiCaprio", "Ellen Page"]
print(filme)

