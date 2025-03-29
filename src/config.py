import os

#carpeta monitoreada en busca de archivos nuevos
WATCH_FOLDER = r"C:\Users\Usuario\Downloads"

#carpeta donde se moverán los archivos
DESTINATION_FOLDER = r"C:\Users\Usuario\Documents\AutoSort"


FILE_TYPES = {
    "Imágenes": [".jpg", ".png", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi"],
    "Música": [".mp3", ".wav"],
    "Otros": []
}

#Creación automática de carpetas si no existen
def create_folders():
    for folder in FILE_TYPES.keys():    #iterar cada carpeta
        path = os.path.join(DESTINATION_FOLDER, folder)
        os.makedirs(path, exist_ok=True)

create_folders()

