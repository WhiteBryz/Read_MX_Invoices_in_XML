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
  3. Posicionar el ejecutable **XMLScrapping.exe** dentro de la carpeta que contiene los XML a leer y ejecutarlo con doble clic.
  4. La aplicación leerá la cantidad de XML a analizar y preguntará si se desea continuar. Colocar con el teclado la letra **y** si se desea continuar o **n** si se desea abortar la ejecucución.
  5. En caso de que se haya colocado **y**, la aplicación leerá todos los archivos XML, estraerá la información y creará un archivo CSV llamado **datos_factura**.
  6. En caso de que no se haya podido leer uno o más archivos XML, los enlistará para su posterior validación del formato (por parte del usuario).
  7. Para finalizar y cerrar la aplicación, basta con darle **Enter** con el teclado.
  8. El usuario deberá abrir el archivo CSV con la herramienta de su preferencia para darle formato y proceder con el análisis.