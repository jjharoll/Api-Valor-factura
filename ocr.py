import pytesseract
import asyncio
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jharol.perez\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        # Convierte el texto en una lista de líneas separadas por \n
        lines = text.split("\n")
        
        keyword = "Total a Pagar"
        for i, line in enumerate(lines):
            if keyword in line:
                print("Se encontró la palabra clave '{}' en la línea {}:".format(keyword, i))
                print(lines[i])
                print("Contenido de la línea siguiente:")
                valor = f'Valor Factura es de: {lines[i + 2]}'
                break
            else:
                print("No se encontró la palabra clave '{}'.".format(keyword))
        await asyncio.sleep(2)
        return valor
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)
