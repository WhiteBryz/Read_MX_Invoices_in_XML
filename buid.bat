@echo off
del /s /q build
del /s /q dist
del /q main.spec
C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\pyinstaller --onefile --name read_XML_invoices main.py