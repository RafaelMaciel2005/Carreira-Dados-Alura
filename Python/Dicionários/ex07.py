def registrar_livro(titulo, autor, ano):

    return{
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

livro = registrar_livro("Pinóquio", "Disney", 1940)

print(livro)
