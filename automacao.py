import pyautogui
import time

# pegar posições do mouse e da data
print(pyautogui.position())
print(pyautogui.size())

# funçoes do mouse

time.sleep(5)
#pyautogui.click(x=1561, y=223) # clica em um lugar
pyautogui.moveTo(x=1351, y=152, duration=1) #arrasta o mouse até a posicao 
pyautogui.click(x=1230, y=328)
pyautogui.scroll(-100) # numero negativo = scroll para baixo

# funções do teclado
pyautogui.write("Se inscreve no canal")
pyautogui.hotkey("ctrl", "c")
pyautogui.press("enter")