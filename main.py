import listAllFiles as LAF
from createCSV import createCSVFile
from readXMLFiles import readFiles


xml_files = LAF.get_xml_files()
number_XML_files = len(xml_files)

print(f"Numero de XML a extraer: {number_XML_files}")
# print(xml_files)
continueProgram = input("¿Desea continuar? (y/n): ")

if continueProgram.lower() == "y":

    invoces_data = readFiles(xml_files)
    createCSVFile(invoces_data)
    # print(invoces_data)
else:
    print("Programa terminado")
