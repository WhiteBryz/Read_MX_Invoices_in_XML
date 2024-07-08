import csv

def createCSVFile(invoces_data):
    with open("datos_facturas.csv",mode="w", newline="") as file:
        fieldnames = ["File", "Rfc", "Nombre", "Serie", "Folio", "SerieFolio", "Fecha", "Base", "Importe", "Uuid"]
        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        try:
            writer.writerows(invoces_data)
        except Exception as e:
            print(f"Hubo un error al crear el CSV: ",e)