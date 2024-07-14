# XMLScrapping

Aplicación creada en Python v.12 para leer facturas expedidas en México en formato XML y extraer datos de mi propio interés.

Funciona con las facturas versión 4.0.

Los datos a extraer del XML son:
 - RFC
 - Nombre
 - Código de Régimen Fiscal
 - Serie
 - Folio
 - Fecha de timbrado (dd/mm/aaaa)
 - Total de Impuestos Retenidos (Si hubiera)
 - Total de Impuestos Trasladados (Si hubiera)
 - SubTotal
 - Descuento (Si hubiera)
 - Total
 - UUID

## Pasos para leer los archivos XML
  1. Crear una carpeta que va a contener todas las facturas XML.
  2. Colocar todas las facturas a leer en formato XML. La carpeta puede contener otro tipo de archivos, pero solamente se leerán los de tipo XML.
  3. Posicionar el ejecutable **XMLScrapping.exe** dentro de la carpeta que contiene los XML a leer y ejecutarlo con doble clic.
  4. La aplicación leerá la cantidad de XML que se encuentran en la carpeta. 
     1. Si la aplicación no detecta ningún archivo XML mostrará un mensaje de no haber encontrado ningún archivo y se puede proceder a cerrar la aplicación.
     2. En caso de encontrar archivos XML preguntará si se desea continuar. Colocar con el teclado la letra **y** si se desea continuar o **n** si se desea abortar la ejecucución.
  5. En caso de que se haya colocado la letra **y**, la aplicación leerá todos los archivos XML dentro de la carpeta, extraerá la información y enseguida creará un archivo CSV llamado **datos_factura.csv**.
  6. En caso de que no se haya podido leer uno o más archivos XML, los enlistará para que posteriormente se valide que el formato tiene la estructura correcta (por parte del usuario).
  7. Al final se mostrará un mensaje de éxito y para salir de la aplicación basta con darle **Enter** con el teclado o cerrar la pestaña. Ningún funcionamiento adicional se ejecutará.
  8. El usuario deberá abrir el archivo **datos_factura.csv** con la herramienta de su preferencia para darle el formato que requiera o recoja los datos de su interés. Algunos ejemplos de las herramientas que se pueden utilizar son: Excel, Google Sheets o alguna Base de Datos que acepte el formato.

## Formato del CSV 
El documento CSV tiene la siguiente estructura basado en los encabezados:
 - File
 - RFC
 - Nombre
 - Código de Régimen Fiscal
 - Nombre del Régimen Fiscal
 - Serie (Si hubiera)
 - Folio (Si hubiera)
 - SerieFolio (Concatenación de los datos Serie y Folio. Si la factura no tiene ni Serie ni Folio se coloca la primera sección del UUID)
 - Fecha (dd/mm/aaaa)
 - Total de Impuestos Retenidos (Si hubiera)
 - Total de Impuestos Trasladados (Si hubiera)
 - SubTotal
 - Descuento (Si hubiera)
 - Total
 - UUID

## Librerías usadas 📖
Para poder funcionar, se hacen uso de las siguientes librerías de python (el orden no importa):
- __JSON__ → Para leer los archivos de tipo JSON.
- __os__ → Para leer los archivos dentro de una carpeta.
- __sys__ → Para asegurarnos si el el programa está siendo ejecutado como un ejecutable empaquetado. Se usa para poder definir la ruta de nuestro archivo JSON y poder leer los datos de información.
- __csv__ → Se emplea para crear el documento CSV.
- __xml.etree.ElementTree__ → Se utiliza para leer los XML y poder acceder a sus datos.
- __datetime__ → Empleado para darle formato a las fechas.

## Archivo .bat ⚠️
El archivo build contiene comandos para Windows que automatiza el proceso de crear el ejecutable en caso de realizar cambios en el código.
Para que funcione adecuadamente es necesario tener instalado Python y Pyinstaller. Este último es una herramienta que empaqueta el código python y crea el ejecutable (_.exe_). Además, es necesario añadir la ruta de la carpeta de scripts de python a nuestras variables de entorno, de lo contrario no se podrá ejecutar. *Esto en caso de querer crear nuestro propio ejecutable.* Dentro de la carpeta *dist* se encuentra el ejecutable con la última versión disponible.