import time
from watchdog.observers import Observer             #observador
from watchdog.events import FileSystemEventHandler  #manejador de eventos

class MyEvent(FileSystemEventHandler):
 #método que serpa invocado, cada que un archivo se modifique dentro del directorio   
    def on_modified(self, event):
        print (f"📁Archivo modificado: {event.src_path}")

    def on_deleted(self, event):
        print (f"Se eliminó: {event.src_path}")

    def on_created(self, event):  
        #evita archivos temporales
        if not event.is_directory:
            if not event.src_path.endswith((".tmp", ".crdownload", ".opdownload")):
                print(f"Se creó: {event.src_path}")

    def on_moved(self, event):
        print(f"Se movió: {event.src_path}->{event.dest_path}")
    

#se crea la instancia del observador
observer = Observer()
#con el método schedule(), se le asigna una manejador para que responda a los eventos en la carpeta
observer.schedule(MyEvent(), "C:\\Users\\Usuario\\Downloads",
#sin considerar las subcarpetas
recursive=False)
#inicia el observador
observer.start()

try:
    while observer.is_alive():
        print("Observando cambios en la carpeta")
        time.sleep(5)
        observer.join(1)

#detener observador con ctrl + c
except KeyboardInterrupt:
    observer.stop()

observer.join()
    
