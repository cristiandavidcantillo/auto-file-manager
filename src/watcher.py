from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer import organize_file
import time
import config

class MyEvent(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"📂 Detectado nuevo archivo: {event.src_path}")  # 👀 Ver si detecta algo
            organize_file(event.src_path)

def start_watcher():
    print("👀 Iniciando watcher...")  # 👀 Ver si el script arranca
    observer = Observer()
    observer.schedule(MyEvent(), config.WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Deteniendo watcher...")
        observer.stop()

    observer.join()

if __name__ == "__main__":
    start_watcher()
