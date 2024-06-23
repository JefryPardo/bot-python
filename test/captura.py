import pyautogui
import time

# region = (500, -35, 550, 400)
region = (650, 650, 100, 100)
screenshot = pyautogui.screenshot(region=region)

screenshot.save("resultados.png")
print("Captura de pantalla guardada como resultados.png")