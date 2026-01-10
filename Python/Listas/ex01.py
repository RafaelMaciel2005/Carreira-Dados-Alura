animais = []
animais.append("Gato")
animais.append("Cachorro")  
animais.append("Pássaro")     
print(animais)    
animais.insert(1, "Peixe")
print(animais)
animais.remove("Gato")
print(animais)
animal_removido = animais[-1]
print(animal_removido)
animais.pop(-1)
print(animais)
novos_animais = ["Tartaruga, Hamster"]
todos_animais = animais + novos_animais
print(todos_animais)
animais_duplicados = todos_animais * 2
print(animais_duplicados)
print("Cachorro" in todos_animais)
