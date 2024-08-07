import pyautogui
import time

pyautogui.PAUSE = 0.3
print("Abrindo o windows...")
pyautogui.press("win")
print("Digita chrome na busca...")
pyautogui.write("chrome")
print("Pressiona a tecla ENTER...")
pyautogui.press("enter")
print("Clica no perfil do Google Chrome...")
pyautogui.click(x=1277, y=460)
print("Abre uma nova aba...")
pyautogui.hotkey("ctrl", "t")

time.sleep(1)
print("Digita o site...")
pyautogui.write("https://www.axialmg.com.br/")
print("Pressiona a tecla ENTER...")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=1618, y=156)
time.sleep(2)
pyautogui.click(x=1617, y=202)
time.sleep(3)
pyautogui.write("00000000000")
time.sleep(3)
pyautogui.click(x=957, y=747)
pyautogui.write("1234567")
pyautogui.click(x=946, y=584)
time.sleep(2)

pyautogui.click(x=688, y=522)
time.sleep(2)
pyautogui.click(x=1446, y=530)
time.sleep(2)

pyautogui.hotkey("ctrl", "p")
pyautogui.press("enter")








