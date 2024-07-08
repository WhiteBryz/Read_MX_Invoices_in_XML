import xml.etree.ElementTree as ET
import listAllFiles as LAF
from datetime import datetime as dt

def concatFolio(serie,folio):
    if(serie != None):
        return f"{serie} {folio}"
    else:
        return f"{folio}"

xml_files = LAF.get_xml_files()
print(f"Total de facturas: ",len(xml_files))

# print(xml_files)

for file in xml_files:
    # Raíz
    tree = ET.parse(file)
    root = tree.getroot()

    # Datos generales factura
    File = file[:10]
    Rfc = root[0].get("Rfc")
    Nombre = root[0].get("Nombre")
    Serie = root.get("Serie")
    Folio = root.get("Folio")
    serieFolio = concatFolio(Serie,Folio)
    Fecha = dt.strptime(root.get("Fecha"),"%Y-%m-%dT%H:%M:%S")
    Fecha = Fecha.strftime("%d/%m/%Y")

    # Importe e impuestos
    Base = root[3][0][0].get("Base")
    Importe = root[3][0][0].get("Importe")

    # Complemento
    Uuid = root[4][0].get("UUID")

    print(f"{File}...xml, {Rfc}, {Nombre}, {Serie}, {Folio}, {serieFolio}, {Fecha}, {Base}, {Importe}, {Uuid}")
    # print(len(root[0]))