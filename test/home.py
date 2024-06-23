import pytesseract
from PIL import Image, ImageOps

def pytesseractConfigNumber():
    return '--psm 6 -c tessedit_char_whitelist=0123456789'

ruta_name = "captura.png"

# Abrir la imagen
imagen = Image.open(ruta_name)

imagen_gris = ImageOps.grayscale(imagen)

configuracion = pytesseractConfigNumber()

unidades = pytesseract.image_to_string(imagen_gris, config=configuracion) 

print(unidades)
