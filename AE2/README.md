# Evidencia de Aprendizaje 2 - Manejo de archivos y clases

## Descripción
En esta actividad descargué un CSV y un JSON de Hugging Face, los importé con clases de Python, les hice modificaciones, guardé archivos nuevos y generé un `resumen.txt` con una tercera clase.

## Origen de los datos
- CSV: (https://huggingface.co/datasets/scikit-learn/iris/blob/main/Iris.csv)
- JSON: https://huggingface.co/datasets/geekyfreak/json_dump/blob/main/data.json

## Estructura
- `datos_originales/`: archivos descargados, sin modificar.
- `datos_modificados/`: archivos nuevos que guardó el código.
- `manejador_csv.py`: clase que importa, modifica y guarda el CSV.
- `manejador_json.py`: clase que importa, modifica y guarda el JSON.
- `generador_resumen_txt.py`: clase que crea el `resumen.txt`.
- `flujo_ae2.ipynb`: notebook que coordina todo.
- `resumen.txt`: resumen generado al ejecutar el notebook.

## Pasos para ejecutarlo
1. Activo el entorno: `source .venv/bin/activate`
2. Abro `AE2/flujo_ae2.ipynb` y selecciono el kernel `.venv`.
3. Uso **Ejecutar todo**.
4. Reviso los archivos nuevos en `datos_modificados/` y el `resumen.txt`.