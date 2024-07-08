from os import listdir
from os.path import isfile, join

def get_xml_files(directory="./"):
    try: 
        onlyxmlFiles = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith('.xml')]
        return onlyxmlFiles
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return []