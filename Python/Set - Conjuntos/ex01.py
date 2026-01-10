animais = {"gato", "cachorro", "pássaro"}

animais.add("peixe")

print(animais)

animais.remove("pássaro")
print("Conjunto atualizado: {}".format(animais))

try:
    animais.remove("lagarto")
except KeyError as e:
    print("ERRO {}".format(e))

animais.discard("lagarto")  

animais.pop()
print(animais)

animais.clear()
print(animais)