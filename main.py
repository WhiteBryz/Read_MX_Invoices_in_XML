import listAllFiles as LAF
from createCSV import createCSVFile
from readXMLFiles import readFiles
from modules import infoJson


app_info = infoJson()

print("=========================================================")
print(f"{app_info['name']} {app_info['version']}")
print(f"Creador: {app_info['creator']}")
print(f"Versión de facturación: {app_info['invoiceVersion']}")
print(f"Repositorio: {app_info['github']}")
print("=========================================================")

xml_files = LAF.get_xml_files()
number_XML_files = len(xml_files)

print(f"Numero de XML a extraer: {number_XML_files}")
# print(xml_files)
continueProgram = input("¿Desea continuar? (y/n): ")

if continueProgram.lower() == "y":

    invoces_data = readFiles(xml_files)
    createCSVFile(invoces_data)
    # print(invoces_data)

    input(f"Proceso finalizado")
else:
    print("Programa terminado")

