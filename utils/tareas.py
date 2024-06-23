import utils.autogui as autogui
import pyautogui
import utils.regiones as regiones
import time
from PIL import Image, ImageOps
import pytesseract

def limpiar_input_store():

    elemento_boton_limpiar_input_tienda = autogui.buscar_imagen_referencia(
        regiones.limpiar_input_tienda['nombre'], 
        regiones.limpiar_input_tienda['region'],
        0.8
    )
    
    
    autogui.click_centrado(elemento_boton_limpiar_input_tienda)


def escribir_texto(texto):
    pyautogui.typewrite(texto, interval=0.1)

def buscar_item():

    elemento_boton_buscar = autogui.buscar_imagen_referencia(
        regiones.buscar_boton_tienda['nombre'],
        regiones.buscar_boton_tienda['region']
    )

    autogui.click_centrado(elemento_boton_buscar)
    time.sleep(4)

def cerrar_tienda():

    elemento_boton_buscar = autogui.buscar_imagen_referencia(
        regiones.cerrar_tienda['nombre'],
        regiones.cerrar_tienda['region'],
        0.6
    )

    autogui.click_centrado(elemento_boton_buscar)
    time.sleep(3)
    pyautogui.rightClick()


def get_unidades_en_venta_slot1():

    region = regiones.unidades_en_venta_slot1
    screenshot = pyautogui.screenshot(region=region)

    ruta_name = "imagenes/venta_slot1.png"

    screenshot.save(ruta_name)
    imagen = Image.open(ruta_name)
    configuracion = pytesseractConfigNumber()

    return pytesseract.image_to_string(imagen, config=configuracion) 

def get_precio_slot1():

    region = regiones.precio_slot1
    screenshot = pyautogui.screenshot(region=region)

    ruta_name = "imagenes/precio_slot1.png"

    screenshot.save(ruta_name)
    imagen = Image.open(ruta_name)
    imagen_gris = ImageOps.grayscale(imagen)

    configuracion = pytesseractConfigNumber()

    return pytesseract.image_to_string(imagen_gris, config=configuracion) 


def pytesseractConfigNumber():
    return '--psm 6 -c tessedit_char_whitelist=0123456789'