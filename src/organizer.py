import shutil
import os
import time
import config

def organize_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    # Esperar un momento para asegurar que el archivo existe
    time.sleep(2)

    if not os.path.exists(file_path):
        print(f"⚠️ Archivo {file_path} no encontrado. Puede que aún se esté descargando.")
        return

    for folder, extensions in config.FILE_TYPES.items():
        if ext in extensions:
            dest_folder = os.path.join(config.DESTINATION_FOLDER, folder)
            os.makedirs(dest_folder, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(dest_folder, os.path.basename(file_path)))
                print(f"✅ {file_path} movido a {dest_folder}")
            except Exception as e:
                print(f"⚠️ Error moviendo {file_path}: {e}")
