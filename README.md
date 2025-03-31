# AutoSort 📂  

AutoSort es un script en Python que monitorea la carpeta de Descargas y organiza automáticamente los archivos en subcarpetas según su tipo (imágenes, documentos, videos, música, etc.).


## 🚀 Instalación  

1️⃣ **Clonar repositorio:**  
```sh
git clone https://github.com/tu-usuario/AutoSort.git
```

2️⃣ **Ve al directorio del proyecto:**  
```sh
cd AutoSort
```

3️⃣ **Crea y activa un entorno virtual (opcional, recomendado):**  
```sh
python -m venv venv  # Crear entorno virtual
venv\Scripts\activate  # Activar en Windows
source venv/bin/activate  # Activar en macOS/Linux
```

4️⃣ **Instala las dependencias:**  
```sh
pip install -r requirements.txt
```

---

## 🛠️ Configuración  

Puedes modificar la carpeta que deseas monitorear y el destino de los archivos en `config.py`:

```python
WATCH_FOLDER = r"C:\Users\Usuario\Downloads"
DESTINATION_FOLDER = r"C:\Users\Usuario\Documents\AutoSort"
```

También puedes personalizar las categorías de archivos:

```python
FILE_TYPES = {
    "Imágenes": [".jpg", ".png", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi"],
    "Música": [".mp3", ".wav"],
    "Otros": []
}
```

---

## 📂 Uso  

Para iniciar el organizador de archivos, ejecuta:
```sh
python src/watcher.py
```

El script empezará a monitorear la carpeta de descargas y moverá automáticamente los archivos a las carpetas correspondientes.

---

## 📂 Estructura del Proyecto  

```
📂 AutoSort  
│── 📜 src/  
│   ├── 📜 watcher.py   # Detecta archivos nuevos y los organiza  
│   ├── 📜 organizer.py # Mueve archivos a carpetas correspondientes  
│   ├── 📜 config.py    # Configuración del script  
│── 📜 requirements.txt  # Dependencias  
│── 📜 README.md         # Documentación  

