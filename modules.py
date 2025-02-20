import json
from os import listdir
from os.path import isfile, join
import sys
import csv

# Función para extraer datos del archivo JSON
def info_Json():
    infoFile="info.json"

    # Asegurar ruta al archivo JSON
    if getattr(sys, 'frozen', False):
        ruta_info_json = join(sys._MEIPASS, infoFile)
    else:
        ruta_info_json = infoFile

    # Extraemos datos del JSON
    try:
        with open(ruta_info_json,"r") as file:
            info = json.load(file)
        return info
    except Exception as e:
        print(f"Error al leer JSON: ", e)

# Función para devolver una lista con el nombre de los archivos de una carpeta
# Funciona únicamente colocando el .exe dentro de la carpeta con los xml
def get_xml_files(directory="./"):
    try: 
        onlyxmlFiles = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith('.xml')]
        return onlyxmlFiles
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return []
    
# Función que crea el archivo CSV con base a un diccionario de facturas XML ya extraídas.
def create_CSV_File(invoices_data):
    with open("datos_facturas.csv",mode="w", newline="") as file:
        # Header
        try:
            # Extraemos encabezado con base en los Keys del primer elemento de las facturas.
            fieldnames = list(invoices_data[0])
            # Colocamos encabezado
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
        except:
            print("Hubo un error al escribir el encabezado: ")
        
        # Rows
        try:
            writer.writerows(invoices_data)
        except:
            print(f"Hubo un error al insertar las filas: ")