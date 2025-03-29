import shutil
import os
import time
import config

def wait_for_file(file_path, timeout=10):
    """Espera hasta que el archivo esté completamente descargado."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            return True
        time.sleep(1)
    return False

def organize_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    # Esperar hasta que el archivo esté completamente descargado
    if not wait_for_file(file_path):
        print(f"⚠️ Archivo {file_path} no está listo. Puede que aún se esté descargando.")
        return

    for folder, extensions in config.FILE_TYPES.items():
        if ext in extensions:
            dest_folder = os.path.join(config.DESTINATION_FOLDER, folder)
            os.makedirs(dest_folder, exist_ok=True)

            # Mover el archivo
            try:
                shutil.move(file_path, os.path.join(dest_folder, os.path.basename(file_path)))
                print(f"✅ {file_path} movido a {dest_folder}")
            except Exception as e:
                print(f"⚠️ Error moviendo {file_path}: {e}")
