import xml.etree.ElementTree as ET
from datetime import datetime as dt

def readFiles(xml_files):
    invoces_data = []
    counter = 0
    
    for file in xml_files:
        try:
            # Raíz
            tree = ET.parse(file)
            root = tree.getroot()

            # Datos generales factura
            File = f"{file[:10]}...xml"
            Rfc = root[0].get("Rfc")
            Nombre = root[0].get("Nombre")
            Serie = root.get("Serie")
            Folio = root.get("Folio")
            serieFolio = concat(Serie,Folio)
            Fecha = dt.strptime(root.get("Fecha"),"%Y-%m-%dT%H:%M:%S")
            Fecha = Fecha.strftime("%d/%m/%Y")

            # Importe e impuestos
            Base = root[3][0][0].get("Base")
            Importe = root[3][0][0].get("Importe")

            # Complemento
            Uuid = root[4][0].get("UUID")

            invoce = {
                "File": File,
                "Rfc": Rfc,
                "Nombre": Nombre,
                "Serie": Serie,
                "Folio": Folio,
                "SerieFolio": serieFolio,
                "Fecha": Fecha,
                "Base": Base,
                "Importe": Importe,
                "Uuid": Uuid
            }
            invoces_data.append(invoce)
            counter = counter + 1
            # print(f"{File}...xml, {Rfc}, {Nombre}, {Serie}, {Folio}, {serieFolio}, {Fecha}, {Base}, {Importe}, {Uuid}")
            # print(len(root[0]))
        except:
            print(f"No se pudo leer el archivo: {file}")
    
    print(f"En total se leyeron {counter} de {len(xml_files)} archivos XML.")
    return invoces_data

## Función para concatenar los strings de la serie y el folio
def concat(serie,folio):
    if(serie != None):
        return f"{serie} {folio}"
    else:
        return f"{folio}"