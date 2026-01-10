import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm("Clique no botão desejado", buttons = ["Excel", "Word", "Notepad"])

if opcao == "Excel":

    escolha_opcao.hotkey("win", "r")
    escolha_opcao.sleep(1)
    escolha_opcao.typewrite("Excel")
    escolha_opcao.press("enter")
   
elif opcao == "Word":

    escolha_opcao.hotkey("win", "r")
    escolha_opcao.sleep(1)
    escolha_opcao.typewrite("Word")
    escolha_opcao.press("enter")

elif opcao == "Notepad":

    escolha_opcao.hotkey("win", "r")
    escolha_opcao.sleep(1)
    escolha_opcao.typewrite("Notepad")
    escolha_opcao.press("enter")