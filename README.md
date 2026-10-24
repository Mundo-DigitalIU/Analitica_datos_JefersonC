# Analítica de datos - Actividad 1

## Descripción
En esta actividad cargué un dataset de Hugging Face (`scikit-learn/iris`) y lo convertí en un DataFrame de pandas. Después le hice una transformación mínima (filtré las filas donde `SepalLengthCm` es mayor a 5) y generé un resumen del resultado en un archivo `.txt`.

## Tecnologías que usé
- Python
- pandas
- Hugging Face Datasets
- Jupyter Notebook
- Git y GitHub

## Estructura del proyecto
- `src/clases_po/hf_dataset_loader.py`: clase que carga el dataset y lo devuelve como DataFrame.
- `src/clases_po/dataset_summarizer.py`: clase que recibe un DataFrame y genera el resumen en un `.txt`.
- `src/clases_po/flujo_principal.ipynb`: notebook que usa las dos clases y hace la transformación.
- `src/clases_po/resumen_iris_transformado.txt`: resumen generado al ejecutar el notebook.
- `requirements.txt`: librerías necesarias.

## Paso 1: crear el entorno virtual
Verifico la versión de Python:
```bash
python --version
```
Creo el entorno:
```bash
python -m venv .venv
```

## Paso 2: activar el entorno
```bash
source .venv/bin/activate
```

## Paso 3: instalar las librerías
```bash
pip install -r requirements.txt
```

## Paso 4: ejecutar el flujo
Abro `src/clases_po/flujo_principal.ipynb`, selecciono el kernel `.venv` y uso **Ejecutar todo**. Al terminar se genera el archivo `resumen_iris_transformado.txt`.
 