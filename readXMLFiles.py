import xml.etree.ElementTree as ET
from datetime import datetime as dt
import dictionarys as dic

def readFiles(xml_files):
    invoces_data = []
    counter = 0
    
    for file in xml_files:
        try:
            # Raíz
            tree = ET.parse(file)
            root = tree.getroot()

            # Se obtiene el UUID del complemento (Timbre fiscal)
            ns = {'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
            timbre_fiscal = root.find('.//tfd:TimbreFiscalDigital', ns)

            if timbre_fiscal is not None:
                Uuid = timbre_fiscal.get('UUID')
            else:
                Uuid = 0

            # Se obtiene la fecha de timbrado y se formatea
            Fecha = dt.strptime(timbre_fiscal.get("FechaTimbrado"),"%Y-%m-%dT%H:%M:%S")
            Fecha = Fecha.strftime("%d/%m/%Y")

            # Datos generales factura
            File = f"{file[:10]}...xml"
            Rfc = root[0].get("Rfc")
            Nombre = root[0].get("Nombre")
            CodigoRegimen = root[0].get("RegimenFiscal")
            NombreRegimen = dic.regimenes_fiscales[CodigoRegimen]["Nombre"]
            Serie = ifElementExists(root.get("Serie"))
            Folio = ifElementExists(root.get("Folio"))
            
            if len(Serie) > 0 or len(Folio) > 0:
                serieFolio = concat(Serie,Folio)
            else:
                serieFolio = Uuid.split("-")[0]         

            # Impuestos       
            TotalImpuestosRetenidos = ifAmountExits(root[3].get("TotalImpuestosRetenidos"))
            TotalImpuestosTrasladados = ifAmountExits(root[3].get("TotalImpuestosTrasladados"))
                
            # Total y subtotal
            SubTotal = ifAmountExits(root.get("SubTotal"))
            Descuento = ifAmountExits(root.get("Descuento"))
            SubTotal = SubTotal - Descuento
            Total = ifAmountExits(root.get("Total"))

            invoce = {
                "File": File,
                "Rfc": Rfc,
                "Nombre": Nombre,
                "CodigoRegimen": CodigoRegimen,
                "NombreRegimen": NombreRegimen,
                "Serie": Serie,
                "Folio": Folio,
                "SerieFolio": serieFolio,
                "Fecha": Fecha,
                "TotalImpuestosRetenidos": TotalImpuestosRetenidos,
                "TotalImpuestosTrasladados": TotalImpuestosTrasladados,
                "SubTotal": SubTotal,
                "Descuento": Descuento,
                "Total": Total,
                "Uuid": Uuid
            }

            invoces_data.append(invoce)
            counter = counter + 1
        except:
            print(f"    No se pudo leer el archivo: {file}")
    
    # Mensaje final
    print(f"\nEn total se leyeron {counter} de {len(xml_files)} archivos XML.")
    
    return invoces_data

## Función para concatenar los strings de la serie y el folio
def concat(serie,folio):
    if(serie != None):
        return f"{serie} {folio}"
    else:
        return f"{folio}"


# Función para validar que el elemento en cuestión exista (Se utiliza en la extracción de impuestos y descuentos)
def ifAmountExits(element):
    if element != None:
        return float(element)
    else:
        return 0
    
def ifElementExists(element):
    if element != None:
        return element
    else:
        return ""