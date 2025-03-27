import time
from watchdog.observers import Observer             #observador
from watchdog.events import FileSystemEventHandler  #manejador de eventos

class MyEvent(FileSystemEventHandler):
 #método que serpa invocado, cada que un archivo se modifique dentro del directorio   
    def on_modified(self, event):
        return (f"modificado: {event.src_path}")
    

#se crea la instancia del observador
observer = Observer()
#con el método schedule(), se le asigna una manejador para que responda a los eventos en la carpeta
observer.schedule(MyEvent(), ".",
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
    
