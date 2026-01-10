artista = {
    "nome": "Ludwig van Beethoven",
    "nascimento": 1770,
    "falecimento": 1827,
    "nacionalidade": "Alemã",
    "estilo": "Clássico"
}

print(artista["nome"])

print(artista.get("nacionalidade"))

print(artista.get("profissao", "Informação não disponível"))

if "estilo" in artista:

    print(artista.get("estilo"))

else:
    print("Informação não disponível.")

if "instrumento principal" in artista:
    print(artista.get("instrumento principal"))

else:
    print("Informação não disponível")