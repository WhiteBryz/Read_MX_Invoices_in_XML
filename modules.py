import json
import os
import sys

def infoJson():
    infoFile="info.json"

    # Asegurar ruta al archivo JSON
    if getattr(sys, 'frozen', False):
        ruta_info_json = os.path.join(sys._MEIPASS, infoFile)
    else:
        ruta_info_json = infoFile

    try:
        with open(ruta_info_json,"r") as file:
            info = json.load(file)
        return info
    except Exception as e:
        print(f"Error al leer JSON: ", e)