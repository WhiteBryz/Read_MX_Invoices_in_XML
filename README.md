# Read_MX_Invoces_in_XML

Aplicación creada en Python v.12 para leer facturas expedidas en México en formato XML y extraer datos de mi propio interés.
Los datos a extraer son:
 - RFC
 - Nombre
 - Serie
 - Folio
 - Serie + Folio
 - Fecha (dd/mm/aaaa)
 - Base (total)
 - Importe (del IVA)
 - UUID

## Pasos para leer los archivos XML
  1. Crear una carpeta que va a contener todas las facturas XML.
  2. Colocar todas las facturas a leer en formato XML. La carpeta puede contener otro tipo de archivos, pero solamente se leerán los de tipo XML.
  3. Posicionar el ejecutable [nombre_ejecutable.exe] dentro de la carpeta y ejecutarlo.
  4. La aplicación leerá todos los archivos XML, extraerá los datos y creará un archivo de tipo CSV [nombre_archivo.csv] con la información extraída.
  5. Leer la información con la herramienta de preferencia para darle formato y proceder al análisis.
