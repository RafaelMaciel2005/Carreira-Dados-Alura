import pyautogui as posicaoMouse

posicaoMouse.sleep(1)
#print(posicaoMouse.position())

posicaoMouse.moveTo(x=23, y=1057)
posicaoMouse.click(x=23, y=1057)

posicaoMouse.sleep(1)

posicaoMouse.typewrite("calculadora")

posicaoMouse.sleep(2)

#print(posicaoMouse.position())

posicaoMouse.moveTo(x=169, y=511)
posicaoMouse.click(x=169, y=511)