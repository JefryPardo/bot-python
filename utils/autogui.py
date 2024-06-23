import pyautogui
import time

def buscar_imagen_referencia(imagen_referencia, region, confidence = 0.6):
    try:

        ruta_img = 'imagenes/'+imagen_referencia+'.png'

        print(ruta_img)
       
        elemento = pyautogui.locateOnScreen(ruta_img, region=region, confidence=confidence)
        print(elemento)
        return elemento
    
    except pyautogui.ImageNotFoundException:
        print("La imagen "+imagen_referencia+ " no se encontró en la pantalla.")
        return None
   

def click_centrado(elemento):

    try:
        centro_x = elemento.left + elemento.width / 2
        centro_y = elemento.top + elemento.height / 2
        
        pyautogui.moveTo(centro_x, centro_y, duration=0.4, tween=pyautogui.easeOutQuad)
        time.sleep(1)
        pyautogui.click(centro_x, centro_y)

    except pyautogui.ImageNotFoundException:
        print("Error al generar el click centrado.")
        return None
    
def doble_click_centrado(elemento):

    try:
        centro_x = elemento.left + elemento.width / 2
        centro_y = elemento.top + elemento.height / 2

        pyautogui.moveTo(centro_x, centro_y, duration=0.4, tween=pyautogui.easeOutQuad)
        time.sleep(3)
        pyautogui.click(centro_x, centro_y-40)
        pyautogui.click(centro_x, centro_y-40)

    except pyautogui.ImageNotFoundException:
        print("Error al generar el click centrado.")
        return None

def mover_mause_al_centro(elemento):

    try:
        centro_x = elemento.left + elemento.width / 2
        centro_y = elemento.top + elemento.height / 2
        
        pyautogui.moveTo(centro_x, centro_y, duration=0.4, tween=pyautogui.easeOutQuad)

    except pyautogui.ImageNotFoundException:
        print("Error al generar el click centrado.")
        return None
    
