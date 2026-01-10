estacionamento = {
    "A1": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sr. Silva"
    },
    "B2":{
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"
    },
    "C3":{
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. Jorge"
    }
}

modelo_b2 = estacionamento["B2"]["modelo"]
print("O carro da vaga B2 é um {}".format(modelo_b2))

estacionamento["A1"]["dono"] = "Sra. Lúcia"
print(estacionamento["A1"])

estacionamento["D4"] = {
    "marca": "Chevrolet",
    "modelo": "Onix",
    "dono": "Sr. Roberto"
}
print("Exibindo a vaga D4: {}".format(estacionamento["D4"]))