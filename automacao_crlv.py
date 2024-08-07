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
pyautogui.write("https://transito.mg.gov.br/veiculos/documentos-de-veiculos/imprimir-crlv")
print("Pressiona a tecla ENTER...")
pyautogui.press("enter")
time.sleep(3)

pyautogui.scroll(-1000)
time.sleep(1)
pyautogui.click(x=605, y=266)
time.sleep(1)
pyautogui.write("ABC1D20")
pyautogui.click(x=571, y=387)
time.sleep(1)
pyautogui.write("61384687652")
pyautogui.click(x=725, y=486)
time.sleep(1)
pyautogui.write("21544548778")
pyautogui.click(x=601, y=588)
time.sleep(1)
pyautogui.write("215421876414")
pyautogui.click(x=562, y=674)
time.sleep(1)
pyautogui.click(x=692, y=761)
time.sleep(1)

pyautogui.hotkey("ctrl", "p")
pyautogui.press("enter")













