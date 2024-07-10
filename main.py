from readXMLFiles import readFiles
from modules import info_Json, get_xml_files, create_CSV_File

# Extraer datos del JSON
app_info = info_Json()

print("=========================================================")
print(f"{app_info['name']} {app_info['version']}")
print(f"Creador: {app_info['creator']}")
print(f"Versión de facturación: {app_info['invoiceVersion']}")
print(f"Repositorio: {app_info['github']}")
print("=========================================================\n")

# Traer lista de los archivos a leer
xml_files = get_xml_files()
totalReadFiles = len(xml_files)

if totalReadFiles > 0:
    print(f"Numero de XML a extraer: {totalReadFiles}")
    continueProgram = input("¿Desea continuar? (y/n):")
    print("\n")

    if continueProgram.lower() == "y":
        # Leemos las facturas en formato XML
        invoces_data = readFiles(xml_files)

        # Creamos archivo CSV
        create_CSV_File(invoces_data)

        input(f"Proceso finalizado")
    else:
        print("Proceso cancelado, se finaliza programa.")
else:
    input("No se detectó ningún archivo XML.")
